#!/usr/bin/env python3

import json
import PyPDF2
import sys
from pathlib import Path

def extract_pdf_fields(pdf_path):
    """Extract all form fields from a PDF file."""
    fields = []
    
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            if '/AcroForm' in pdf_reader.trailer['/Root']:
                form = pdf_reader.trailer['/Root']['/AcroForm']
                if '/Fields' in form:
                    for field_ref in form['/Fields']:
                        field = field_ref.get_object()
                        extract_field_info(field, fields)
    except Exception as e:
        print(f"Error extracting fields: {e}")
    
    return fields

def extract_field_info(field, fields_list, parent_name=''):
    """Recursively extract field information."""
    if '/T' in field:
        field_name = field['/T']
        if parent_name:
            field_name = f"{parent_name}.{field_name}"
        
        field_info = {
            'name': field_name,
            'type': field.get('/FT', 'Unknown'),
            'flags': field.get('/Ff', 0),
            'default_value': field.get('/DV', ''),
            'value': field.get('/V', ''),
            'options': []
        }
        
        # For choice fields, extract options
        if field_info['type'] == '/Ch' and '/Opt' in field:
            options = field['/Opt']
            if isinstance(options, list):
                field_info['options'] = [str(opt) for opt in options]
        
        fields_list.append(field_info)
    
    # Process child fields
    if '/Kids' in field:
        for kid_ref in field['/Kids']:
            kid = kid_ref.get_object()
            extract_field_info(kid, fields_list, field_name if '/T' in field else parent_name)

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_guaranty_fields.py <pdf_path>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    if not Path(pdf_path).exists():
        print(f"File not found: {pdf_path}")
        sys.exit(1)
    
    fields = extract_pdf_fields(pdf_path)
    
    # Print results
    print(f"Found {len(fields)} fields in {pdf_path}")
    print("\nFields:")
    for i, field in enumerate(fields):
        print(f"\n{i+1}. {field['name']}")
        print(f"   Type: {field['type']}")
        if field['default_value']:
            print(f"   Default: {field['default_value']}")
        if field['value']:
            print(f"   Value: {field['value']}")
        if field['options']:
            print(f"   Options: {field['options']}")
    
    # Save to JSON
    output_file = 'residential_lease_guaranty_raw_fields.json'
    with open(output_file, 'w') as f:
        json.dump(fields, f, indent=2)
    print(f"\nFields saved to {output_file}")

if __name__ == "__main__":
    main()