#!/usr/bin/env python3
"""
PDF Field Extractor
Extracts fillable text fields from PDFs along with surrounding context
"""

import PyPDF2
import pdfplumber
from typing import Dict, List, Tuple, Optional
import argparse
import json
import re
from pathlib import Path


class PDFFieldExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.fields_data = []
        
    def extract_form_fields(self) -> Dict[str, any]:
        """Extract form fields using PyPDF2"""
        fields = {}
        
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                # Check if PDF has form fields
                if '/AcroForm' in pdf_reader.trailer['/Root']:
                    fields_dict = pdf_reader.get_fields()
                    
                    if fields_dict:
                        for field_name, field_data in fields_dict.items():
                            field_info = {
                                'name': field_name,
                                'type': field_data.get('/FT', 'Unknown'),
                                'value': field_data.get('/V', ''),
                                'default_value': field_data.get('/DV', ''),
                                'flags': field_data.get('/Ff', 0),
                                'page': None,
                                'rect': None
                            }
                            
                            # Try to get field position
                            if '/Rect' in field_data:
                                field_info['rect'] = field_data['/Rect']
                            
                            # Try to determine page number
                            if '/P' in field_data:
                                page_ref = field_data['/P']
                                for i, page in enumerate(pdf_reader.pages):
                                    if page.indirect_ref == page_ref:
                                        field_info['page'] = i
                                        break
                            
                            fields[field_name] = field_info
                
                return fields
                
        except Exception as e:
            print(f"Error extracting form fields: {e}")
            return {}
    
    def extract_text_around_position(self, page_num: int, x: float, y: float, 
                                   radius: int = 100) -> str:
        """Extract text around a specific position on a page"""
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                if page_num < len(pdf.pages):
                    page = pdf.pages[page_num]
                    
                    # Get all words on the page with their positions
                    words = page.extract_words()
                    
                    nearby_text = []
                    for word in words:
                        word_x = (word['x0'] + word['x1']) / 2
                        word_y = (word['top'] + word['bottom']) / 2
                        
                        # Check if word is within radius of the field
                        if (abs(word_x - x) <= radius and 
                            abs(word_y - y) <= radius):
                            nearby_text.append({
                                'text': word['text'],
                                'distance': ((word_x - x)**2 + (word_y - y)**2) ** 0.5,
                                'x': word_x,
                                'y': word_y
                            })
                    
                    # Sort by distance and combine text
                    nearby_text.sort(key=lambda w: w['distance'])
                    context = ' '.join([w['text'] for w in nearby_text[:20]])  # Get 20 nearest words
                    
                    return context
                    
        except Exception as e:
            print(f"Error extracting text context: {e}")
            
        return ""
    
    def get_page_text_blocks(self, page_num: int) -> List[Dict]:
        """Get text blocks from a page for context analysis"""
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                if page_num < len(pdf.pages):
                    page = pdf.pages[page_num]
                    
                    # Extract text with position information
                    chars = page.chars
                    
                    # Group characters into lines and blocks
                    lines = []
                    current_line = []
                    last_y = None
                    
                    for char in sorted(chars, key=lambda c: (c['top'], c['x0'])):
                        if last_y is None or abs(char['top'] - last_y) < 2:
                            current_line.append(char)
                        else:
                            if current_line:
                                lines.append(current_line)
                            current_line = [char]
                        last_y = char['top']
                    
                    if current_line:
                        lines.append(current_line)
                    
                    # Convert lines to text blocks
                    text_blocks = []
                    for line in lines:
                        if line:
                            text = ''.join([c['text'] for c in line])
                            x0 = min(c['x0'] for c in line)
                            x1 = max(c['x1'] for c in line)
                            y0 = min(c['top'] for c in line)
                            y1 = max(c['bottom'] for c in line)
                            
                            text_blocks.append({
                                'text': text.strip(),
                                'bbox': [x0, y0, x1, y1],
                                'center': [(x0 + x1) / 2, (y0 + y1) / 2]
                            })
                    
                    return text_blocks
                    
        except Exception as e:
            print(f"Error getting text blocks: {e}")
            
        return []
    
    def find_field_context(self, field_info: Dict) -> str:
        """Find context for a specific field"""
        if field_info['page'] is not None and field_info['rect'] is not None:
            # Calculate field center position
            rect = field_info['rect']
            field_x = (rect[0] + rect[2]) / 2
            field_y = (rect[1] + rect[3]) / 2
            
            # Extract surrounding text
            context = self.extract_text_around_position(
                field_info['page'], 
                field_x, 
                field_y,
                radius=150
            )
            
            # If no immediate context, try to find labels above or to the left
            if not context or len(context) < 10:
                text_blocks = self.get_page_text_blocks(field_info['page'])
                
                # Look for text blocks near the field
                nearby_blocks = []
                for block in text_blocks:
                    block_x, block_y = block['center']
                    
                    # Check if block is to the left or above the field
                    if (block_x < field_x and abs(block_y - field_y) < 20) or \
                       (block_y < field_y and abs(block_x - field_x) < 100):
                        distance = ((block_x - field_x)**2 + (block_y - field_y)**2) ** 0.5
                        nearby_blocks.append((distance, block['text']))
                
                # Sort by distance and combine
                nearby_blocks.sort()
                additional_context = ' '.join([text for _, text in nearby_blocks[:5]])
                context = f"{additional_context} {context}".strip()
            
            return context
        
        return ""
    
    def extract_all_fields_with_context(self) -> List[Dict]:
        """Extract all fields with their surrounding context"""
        print("Extracting form fields...")
        fields = self.extract_form_fields()
        
        if not fields:
            print("No form fields found in the PDF")
            return []
        
        print(f"Found {len(fields)} form fields")
        
        results = []
        for field_name, field_info in fields.items():
            print(f"Processing field: {field_name}")
            
            # Get surrounding context
            context = self.find_field_context(field_info)
            
            result = {
                'field_name': field_name,
                'field_type': field_info['type'],
                'current_value': field_info['value'],
                'default_value': field_info['default_value'],
                'page': field_info['page'],
                'position': field_info['rect'],
                'surrounding_context': context,
                'flags': field_info['flags']
            }
            
            results.append(result)
        
        return results
    
    def save_results(self, results: List[Dict], output_path: str = None):
        """Save extraction results to file"""
        if output_path is None:
            output_path = Path(self.pdf_path).stem + '_fields.json'
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"Results saved to: {output_path}")
    
    def print_results(self, results: List[Dict]):
        """Print results in a readable format"""
        print("\n" + "="*80)
        print("EXTRACTED FORM FIELDS AND CONTEXT")
        print("="*80 + "\n")
        
        for i, field in enumerate(results, 1):
            print(f"Field #{i}")
            print("-" * 40)
            print(f"Name: {field['field_name']}")
            print(f"Type: {field['field_type']}")
            print(f"Current Value: {field['current_value'] or '(empty)'}")
            print(f"Default Value: {field['default_value'] or '(none)'}")
            print(f"Page: {field['page'] if field['page'] is not None else 'Unknown'}")
            
            if field['position']:
                print(f"Position: {field['position']}")
            
            print(f"Context: {field['surrounding_context'] or '(no context found)'}")
            print()


def main():
    parser = argparse.ArgumentParser(description='Extract form fields from PDF with surrounding context')
    parser.add_argument('pdf_file', help='Path to the PDF file')
    parser.add_argument('-o', '--output', help='Output file path (default: <pdf_name>_fields.json)')
    parser.add_argument('-p', '--print', action='store_true', help='Print results to console')
    
    args = parser.parse_args()
    
    # Check if file exists
    if not Path(args.pdf_file).exists():
        print(f"Error: File '{args.pdf_file}' not found")
        return
    
    # Create extractor
    extractor = PDFFieldExtractor(args.pdf_file)
    
    # Extract fields with context
    results = extractor.extract_all_fields_with_context()
    
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