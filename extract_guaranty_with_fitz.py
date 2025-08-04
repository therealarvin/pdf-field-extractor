#!/usr/bin/env python3

import fitz  # PyMuPDF
import json
import sys
from pathlib import Path

def extract_form_fields_fitz(pdf_path):
    """Extract form fields using PyMuPDF."""
    fields = []
    
    try:
        doc = fitz.open(pdf_path)
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # Get widgets (form fields) on the page
            for widget in page.widgets():
                field_info = {
                    'page': page_num + 1,
                    'field_name': widget.field_name,
                    'field_type': widget.field_type,
                    'field_type_string': widget.field_type_string,
                    'field_value': widget.field_value,
                    'field_display': widget.field_display,
                    'field_flags': widget.field_flags,
                    'rect': list(widget.rect),  # Position on page
                    'text_maxlen': widget.text_maxlen if hasattr(widget, 'text_maxlen') else None,
                    'choice_values': widget.choice_values if hasattr(widget, 'choice_values') else None,
                }
                
                # Try to get additional properties
                try:
                    field_info['border_width'] = widget.border_width
                    field_info['border_style'] = widget.border_style
                    field_info['border_dashes'] = widget.border_dashes
                except:
                    pass
                
                fields.append(field_info)
        
        doc.close()
        
    except Exception as e:
        print(f"Error extracting fields with PyMuPDF: {e}")
        return []
    
    return fields

def analyze_field_context(fields):
    """Analyze fields and try to determine their purpose from position and context."""
    # Sort fields by page and vertical position
    sorted_fields = sorted(fields, key=lambda f: (f['page'], f['rect'][1]))
    
    enhanced_fields = []
    
    for i, field in enumerate(sorted_fields):
        enhanced_field = field.copy()
        
        # Look for fields that are close together vertically (likely on same line)
        same_line_fields = []
        for j, other in enumerate(sorted_fields):
            if (other['page'] == field['page'] and 
                abs(other['rect'][1] - field['rect'][1]) < 5 and 
                i != j):
                same_line_fields.append(other)
        
        enhanced_field['same_line_fields'] = [f['field_name'] for f in same_line_fields]
        enhanced_field['horizontal_position'] = field['rect'][0]
        enhanced_field['vertical_position'] = field['rect'][1]
        
        enhanced_fields.append(enhanced_field)
    
    return enhanced_fields

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_guaranty_with_fitz.py <pdf_path>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    if not Path(pdf_path).exists():
        print(f"File not found: {pdf_path}")
        sys.exit(1)
    
    print(f"Extracting form fields from {pdf_path}...")
    fields = extract_form_fields_fitz(pdf_path)
    
    if fields:
        print(f"\nFound {len(fields)} form fields:")
        
        # Group by page
        pages = {}
        for field in fields:
            page = field['page']
            if page not in pages:
                pages[page] = []
            pages[page].append(field)
        
        for page, page_fields in sorted(pages.items()):
            print(f"\n=== PAGE {page} ===")
            # Sort by vertical position
            page_fields.sort(key=lambda f: (f['rect'][1], f['rect'][0]))
            
            for field in page_fields:
                print(f"\nField: {field['field_name']}")
                print(f"  Type: {field['field_type_string']} ({field['field_type']})")
                print(f"  Position: x={field['rect'][0]:.1f}, y={field['rect'][1]:.1f}")
                print(f"  Size: {field['rect'][2]-field['rect'][0]:.1f} x {field['rect'][3]-field['rect'][1]:.1f}")
                if field['field_value']:
                    print(f"  Value: {field['field_value']}")
                if field.get('text_maxlen'):
                    print(f"  Max Length: {field['text_maxlen']}")
        
        # Analyze context
        enhanced_fields = analyze_field_context(fields)
        
        # Save results
        with open('residential_lease_guaranty_fields_fitz.json', 'w') as f:
            json.dump(enhanced_fields, f, indent=2)
        print(f"\nEnhanced fields saved to residential_lease_guaranty_fields_fitz.json")
    else:
        print("No form fields found in the PDF.")

if __name__ == "__main__":
    main()