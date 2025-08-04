#!/usr/bin/env python3

import pdfplumber
import json
import sys
import re
from pathlib import Path

def extract_text_and_structure(pdf_path):
    """Extract text and identify potential form fields from PDF."""
    all_text = []
    potential_fields = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                # Extract text
                text = page.extract_text()
                if text:
                    all_text.append(f"=== PAGE {page_num + 1} ===\n{text}")
                
                # Look for common patterns that indicate form fields
                if text:
                    # Pattern for blank lines (underscores)
                    blank_lines = re.findall(r'_{5,}', text)
                    
                    # Pattern for field labels followed by blanks or colons
                    field_patterns = [
                        r'([A-Za-z\s]+):\s*_{3,}',  # Label: _____
                        r'([A-Za-z\s]+):\s*$',       # Label: (at end of line)
                        r'([A-Za-z\s]+)\s+_{3,}',    # Label _____
                        r'\[\s*\]\s*([A-Za-z\s]+)',  # [ ] Checkbox label
                        r'([A-Za-z\s]+)\s*\(\s*\)',  # Label ( )
                    ]
                    
                    for pattern in field_patterns:
                        matches = re.findall(pattern, text)
                        for match in matches:
                            potential_fields.append({
                                'page': page_num + 1,
                                'label': match.strip(),
                                'pattern': pattern
                            })
    
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return None, None
    
    return all_text, potential_fields

def main():
    if len(sys.argv) != 2:
        print("Usage: python analyze_guaranty_pdf.py <pdf_path>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    if not Path(pdf_path).exists():
        print(f"File not found: {pdf_path}")
        sys.exit(1)
    
    print(f"Analyzing {pdf_path}...")
    text_content, fields = extract_text_and_structure(pdf_path)
    
    if text_content:
        # Save text content
        with open('residential_lease_guaranty_text.txt', 'w') as f:
            f.write('\n\n'.join(text_content))
        print(f"Text content saved to residential_lease_guaranty_text.txt")
        
        # Print first 2000 characters to see structure
        full_text = '\n\n'.join(text_content)
        print("\n=== DOCUMENT PREVIEW (first 2000 chars) ===")
        print(full_text[:2000])
        print("\n=== END PREVIEW ===\n")
    
    if fields:
        print(f"\nFound {len(fields)} potential fields:")
        unique_labels = list(set(f['label'] for f in fields))
        for label in sorted(unique_labels):
            print(f"  - {label}")
        
        # Save fields
        with open('residential_lease_guaranty_potential_fields.json', 'w') as f:
            json.dump(fields, f, indent=2)

if __name__ == "__main__":
    main()