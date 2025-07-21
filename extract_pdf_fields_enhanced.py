#!/usr/bin/env python3
"""
Enhanced PDF Field Extractor
Extracts fillable text fields from PDFs along with surrounding context
Uses multiple methods to find field positions and context
"""

import PyPDF2
import pdfplumber
from typing import Dict, List, Tuple, Optional
import argparse
import json
import re
from pathlib import Path
import fitz  # PyMuPDF


class EnhancedPDFFieldExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.fields_data = []
        
    def extract_form_fields_with_pymupdf(self) -> Dict[str, any]:
        """Extract form fields using PyMuPDF for better position detection"""
        fields = {}
        radio_groups = {}
        
        try:
            pdf_document = fitz.open(self.pdf_path)
            
            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]
                
                # Get form fields on this page
                for widget in page.widgets():
                    field_name = widget.field_name
                    field_value = widget.field_value
                    field_type = widget.field_type_string
                    rect = widget.rect
                    
                    # Handle radio buttons specially to group them
                    if field_type == 'RadioButton':
                        button_states = widget.button_states() if hasattr(widget, 'button_states') else {}
                        
                        # Extract option names from button states
                        options = []
                        if 'normal' in button_states:
                            for state in button_states['normal']:
                                if state != 'Off':  # 'Off' is the default unselected state
                                    options.append(state)
                        
                        if field_name not in radio_groups:
                            radio_groups[field_name] = {
                                'name': field_name,
                                'type': field_type,
                                'value': field_value or '',
                                'page': page_num,
                                'rect': [rect.x0, rect.y0, rect.x1, rect.y1],
                                'widget': widget,
                                'options': set(options),
                                'individual_buttons': []
                            }
                        else:
                            # Merge options and update rect to encompass all buttons
                            radio_groups[field_name]['options'].update(options)
                            # Expand bounding rect to include this button
                            existing_rect = radio_groups[field_name]['rect']
                            new_rect = [rect.x0, rect.y0, rect.x1, rect.y1]
                            radio_groups[field_name]['rect'] = [
                                min(existing_rect[0], new_rect[0]),  # min x0
                                min(existing_rect[1], new_rect[1]),  # min y0
                                max(existing_rect[2], new_rect[2]),  # max x1
                                max(existing_rect[3], new_rect[3])   # max y1
                            ]
                        
                        # Add individual button info
                        radio_groups[field_name]['individual_buttons'].append({
                            'rect': [rect.x0, rect.y0, rect.x1, rect.y1],
                            'options': options
                        })
                        
                    else:
                        # Handle non-radio fields normally
                        fields[field_name] = {
                            'name': field_name,
                            'type': field_type,
                            'value': field_value or '',
                            'page': page_num,
                            'rect': [rect.x0, rect.y0, rect.x1, rect.y1],
                            'widget': widget
                        }
            
            # Convert radio groups to proper format and add to fields
            for group_name, group_data in radio_groups.items():
                group_data['options'] = list(group_data['options'])  # Convert set to list
                fields[group_name] = group_data
            
            pdf_document.close()
            return fields
            
        except Exception as e:
            print(f"Error with PyMuPDF extraction: {e}")
            return {}
    
    def extract_page_text_with_positions(self, page_num: int) -> List[Dict]:
        """Extract all text from a page with position information"""
        text_elements = []
        
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                if page_num < len(pdf.pages):
                    page = pdf.pages[page_num]
                    
                    # Extract words with positions
                    words = page.extract_words(
                        keep_blank_chars=True,
                        x_tolerance=3,
                        y_tolerance=3,
                        extra_attrs=['fontname', 'size']
                    )
                    
                    for word in words:
                        text_elements.append({
                            'text': word['text'],
                            'x0': word['x0'],
                            'y0': word['top'],
                            'x1': word['x1'],
                            'y1': word['bottom'],
                            'fontname': word.get('fontname', ''),
                            'size': word.get('size', 0)
                        })
                    
            return text_elements
            
        except Exception as e:
            print(f"Error extracting text with positions: {e}")
            return []
    
    def extract_directional_context(self, field_rect: List[float], page_text: List[Dict]) -> Dict[str, str]:
        """Extract text context from all four directions around a field"""
        if not field_rect or not page_text:
            return {"left": "", "right": "", "above": "", "below": ""}
        
        field_x0, field_y0, field_x1, field_y1 = field_rect
        field_center_x = (field_x0 + field_x1) / 2
        field_center_y = (field_y0 + field_y1) / 2
        
        # Collections for each direction
        left_texts = []
        right_texts = []
        above_texts = []
        below_texts = []
        
        for text_elem in page_text:
            text_x0 = text_elem['x0']
            text_y0 = text_elem['y0']
            text_x1 = text_elem['x1']
            text_y1 = text_elem['y1']
            text_center_x = (text_x0 + text_x1) / 2
            text_center_y = (text_y0 + text_y1) / 2
            
            # LEFT: Text to the left of the field
            if text_x1 < field_x0 and abs(text_center_y - field_center_y) < 15:
                distance = field_x0 - text_x1
                if distance < 80:  # Within 80 pixels
                    left_texts.append({
                        'text': text_elem['text'],
                        'distance': distance,
                        'y': text_center_y
                    })
            
            # RIGHT: Text to the right of the field
            elif text_x0 > field_x1 and abs(text_center_y - field_center_y) < 15:
                distance = text_x0 - field_x1
                if distance < 80:
                    right_texts.append({
                        'text': text_elem['text'],
                        'distance': distance,
                        'y': text_center_y
                    })
            
            # ABOVE: Text above the field
            elif text_y1 < field_y0 and abs(text_center_x - field_center_x) < 100:
                distance = field_y0 - text_y1
                if distance < 40:
                    above_texts.append({
                        'text': text_elem['text'],
                        'distance': distance,
                        'x': text_center_x
                    })
            
            # BELOW: Text below the field
            elif text_y0 > field_y1 and abs(text_center_x - field_center_x) < 100:
                distance = text_y0 - field_y1
                if distance < 40:
                    below_texts.append({
                        'text': text_elem['text'],
                        'distance': distance,
                        'x': text_center_x
                    })
        
        # Sort each direction by distance and take closest items
        def process_direction_texts(texts, max_words=5):
            texts.sort(key=lambda x: x['distance'])
            words = []
            for t in texts[:max_words]:
                words.append(t['text'])
            return ' '.join(words).strip()
        
        return {
            "left": process_direction_texts(left_texts, 8),
            "right": process_direction_texts(right_texts, 5),
            "above": process_direction_texts(above_texts, 10),
            "below": process_direction_texts(below_texts, 5)
        }
    
    def extract_all_fields_with_enhanced_context(self) -> List[Dict]:
        """Extract all fields with enhanced context detection"""
        print("Extracting form fields with enhanced methods...")
        
        # Try PyMuPDF first for better position detection
        fields = self.extract_form_fields_with_pymupdf()
        
        if not fields:
            print("No form fields found using PyMuPDF, trying PyPDF2...")
            # Fall back to PyPDF2
            fields = self.extract_form_fields_pypdf2()
        
        if not fields:
            print("No form fields found in the PDF")
            return []
        
        print(f"Found {len(fields)} form fields")
        
        # Cache page text to avoid re-extraction
        page_text_cache = {}
        
        results = []
        for field_name, field_info in fields.items():
            print(f"Processing field: {field_name}")
            
            # Get page text if not cached
            page_num = field_info.get('page')
            if page_num is not None and page_num not in page_text_cache:
                page_text_cache[page_num] = self.extract_page_text_with_positions(page_num)
            
            # Find directional context
            directional_context = {"left": "", "right": "", "above": "", "below": ""}
            
            if page_num is not None and field_info.get('rect'):
                page_text = page_text_cache.get(page_num, [])
                directional_context = self.extract_directional_context(field_info['rect'], page_text)
            
            result = {
                'field_name': field_name,
                'field_type': field_info.get('type', 'Unknown'),
                'current_value': field_info.get('value', ''),
                'page': page_num,
                'position': field_info.get('rect'),
                'context_left': directional_context['left'],
                'context_right': directional_context['right'],
                'context_above': directional_context['above'],
                'context_below': directional_context['below']
            }
            
            # Add radio button options if this is a radio button group
            if field_info.get('type') == 'RadioButton' and 'options' in field_info:
                result['radio_options'] = field_info['options']
            
            results.append(result)
        
        return results
    
    def extract_form_fields_pypdf2(self) -> Dict[str, any]:
        """Fallback method using PyPDF2"""
        fields = {}
        
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                if '/AcroForm' in pdf_reader.trailer['/Root']:
                    fields_dict = pdf_reader.get_fields()
                    
                    if fields_dict:
                        for field_name, field_data in fields_dict.items():
                            fields[field_name] = {
                                'name': field_name,
                                'type': field_data.get('/FT', 'Unknown'),
                                'value': field_data.get('/V', ''),
                                'page': None,
                                'rect': field_data.get('/Rect')
                            }
                
                return fields
                
        except Exception as e:
            print(f"Error with PyPDF2 extraction: {e}")
            return {}
    
    def save_results(self, results: List[Dict], output_path: str = None):
        """Save extraction results to file"""
        if output_path is None:
            output_path = Path(self.pdf_path).stem + '_fields_enhanced.json'
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"Results saved to: {output_path}")
    
    def print_results(self, results: List[Dict]):
        """Print results in a readable format"""
        print("\n" + "="*80)
        print("EXTRACTED FORM FIELDS WITH DIRECTIONAL CONTEXT")
        print("="*80 + "\n")
        
        for i, field in enumerate(results, 1):
            print(f"Field #{i}")
            print("-" * 40)
            print(f"Name: {field['field_name']}")
            print(f"Type: {field['field_type']}")
            print(f"Current Value: {field['current_value'] or '(empty)'}")
            print(f"Page: {field['page'] if field['page'] is not None else 'Unknown'}")
            
            if field['position']:
                print(f"Position: {field['position']}")
            
            # Print directional context
            print(f"Context:")
            if field.get('context_left'):
                print(f"  Left: {field['context_left']}")
            if field.get('context_above'):
                print(f"  Above: {field['context_above']}")
            if field.get('context_right'):
                print(f"  Right: {field['context_right']}")
            if field.get('context_below'):
                print(f"  Below: {field['context_below']}")
            
            if not any([field.get('context_left'), field.get('context_right'), 
                       field.get('context_above'), field.get('context_below')]):
                print("  (no context found)")
            
            print()


def main():
    parser = argparse.ArgumentParser(description='Enhanced PDF field extraction with context')
    parser.add_argument('pdf_file', help='Path to the PDF file')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('-p', '--print', action='store_true', help='Print results to console')
    
    args = parser.parse_args()
    
    # Check if file exists
    if not Path(args.pdf_file).exists():
        print(f"Error: File '{args.pdf_file}' not found")
        return
    
    # Create extractor
    extractor = EnhancedPDFFieldExtractor(args.pdf_file)
    
    # Extract fields with context
    results = extractor.extract_all_fields_with_enhanced_context()
    
    if results:
        # Save results
        extractor.save_results(results, args.output)
        
        # Print if requested
        if args.print:
            extractor.print_results(results)
    else:
        print("No fields extracted")


if __name__ == "__main__":
    main()