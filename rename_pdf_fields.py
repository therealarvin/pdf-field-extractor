#!/usr/bin/env python3
"""
Interactive PDF Field Renamer
Allows renaming PDF form fields based on their context
"""

import json
import sys
import os
from pathlib import Path
from typing import Dict, List, Optional
import fitz  # PyMuPDF
import shutil
from datetime import datetime


class PDFFieldRenamer:
    def __init__(self, json_path: str, pdf_path: str):
        self.json_path = json_path
        self.pdf_path = pdf_path
        self.fields_data = self.load_fields_data()
        self.renamed_fields = {}
        self.skipped_fields = set()
        
    def load_fields_data(self) -> List[Dict]:
        """Load the extracted fields data from JSON"""
        with open(self.json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def display_field_info(self, field: Dict, index: int, total: int):
        """Display field information in a clear format"""
        print("\n" + "="*80)
        print(f"FIELD {index + 1} of {total}")
        print("="*80)
        
        print(f"\nCurrent Name: {field['field_name']}")
        print(f"Type: {field['field_type']}")
        print(f"Page: {field.get('page', 'Unknown')}")
        
        if field.get('current_value'):
            print(f"Current Value: {field['current_value']}")
        
        print("\nContext:")
        if field.get('context_left'):
            print(f"  LEFT:  {field['context_left']}")
        if field.get('context_above'):
            print(f"  ABOVE: {field['context_above']}")
        if field.get('context_right'):
            print(f"  RIGHT: {field['context_right']}")
        if field.get('context_below'):
            print(f"  BELOW: {field['context_below']}")
        
        if not any([field.get(f'context_{dir}') for dir in ['left', 'right', 'above', 'below']]):
            print("  (No context found)")
    
    def get_user_input(self, field: Dict) -> Optional[str]:
        """Get new field name from user"""
        print("\n" + "-"*60)
        print("Options:")
        print("  - Enter new name for this field")
        print("  - Press ENTER to keep current name")
        print("  - Type 'skip' to skip remaining fields")
        print("  - Type 'quit' to exit without saving")
        print("-"*60)
        
        while True:
            user_input = input("\nNew name (or ENTER/skip/quit): ").strip()
            
            if user_input.lower() == 'quit':
                return 'QUIT'
            elif user_input.lower() == 'skip':
                return 'SKIP'
            elif user_input == '':
                return None  # Keep current name
            elif len(user_input) > 0:
                # Validate the name
                if '/' in user_input or '\\' in user_input:
                    print("Error: Field names cannot contain / or \\")
                    continue
                return user_input
    
    def rename_fields_interactive(self):
        """Interactive renaming process"""
        print("\n" + "="*80)
        print("PDF FIELD RENAMING TOOL")
        print("="*80)
        print(f"\nPDF: {self.pdf_path}")
        print(f"Total fields: {len(self.fields_data)}")
        
        for index, field in enumerate(self.fields_data):
            # Skip if already processed
            if field['field_name'] in self.skipped_fields:
                continue
            
            self.display_field_info(field, index, len(self.fields_data))
            
            new_name = self.get_user_input(field)
            
            if new_name == 'QUIT':
                print("\nExiting without saving changes.")
                return False
            elif new_name == 'SKIP':
                print("\nSkipping remaining fields.")
                break
            elif new_name:
                self.renamed_fields[field['field_name']] = new_name
                print(f"\n✓ Will rename '{field['field_name']}' to '{new_name}'")
            else:
                print(f"\n✓ Keeping original name: '{field['field_name']}'")
        
        return True
    
    def apply_renames_to_pdf(self, output_path: str = None):
        """Apply the field renames to the PDF"""
        if not self.renamed_fields:
            print("\nNo fields were renamed.")
            return False
        
        # Create output path if not specified
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = Path(self.pdf_path).stem + f"_renamed_{timestamp}.pdf"
        
        try:
            # Open PDF
            pdf_doc = fitz.open(self.pdf_path)
            
            # Track renamed fields
            renamed_count = 0
            
            # Iterate through pages and rename fields
            for page_num in range(len(pdf_doc)):
                page = pdf_doc[page_num]
                
                for widget in page.widgets():
                    if widget.field_name in self.renamed_fields:
                        new_name = self.renamed_fields[widget.field_name]
                        widget.field_name = new_name
                        widget.update()
                        renamed_count += 1
            
            # Save the modified PDF
            pdf_doc.save(output_path)
            pdf_doc.close()
            
            print(f"\n✓ Successfully renamed {renamed_count} fields")
            print(f"✓ Saved to: {output_path}")
            
            return True
            
        except Exception as e:
            print(f"\nError applying renames: {e}")
            return False
    
    def update_json_file(self, output_path: str = None):
        """Update the JSON file with new field names"""
        if not self.renamed_fields:
            return
        
        # Create output path if not specified
        if output_path is None:
            output_path = Path(self.json_path).stem + "_renamed.json"
        
        # Update field names in data
        updated_data = []
        for field in self.fields_data:
            field_copy = field.copy()
            if field['field_name'] in self.renamed_fields:
                field_copy['original_name'] = field['field_name']
                field_copy['field_name'] = self.renamed_fields[field['field_name']]
            updated_data.append(field_copy)
        
        # Save updated JSON
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(updated_data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Updated JSON saved to: {output_path}")
    
    def show_summary(self):
        """Show summary of changes"""
        if not self.renamed_fields:
            return
        
        print("\n" + "="*80)
        print("RENAMING SUMMARY")
        print("="*80)
        print(f"\nTotal fields renamed: {len(self.renamed_fields)}")
        print("\nChanges:")
        
        for old_name, new_name in self.renamed_fields.items():
            print(f"  '{old_name}' → '{new_name}'")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Interactive PDF field renaming tool')
    parser.add_argument('json_file', help='Path to the JSON file with extracted fields')
    parser.add_argument('pdf_file', help='Path to the original PDF file')
    parser.add_argument('-o', '--output', help='Output PDF file path')
    parser.add_argument('-j', '--json-output', help='Output JSON file path')
    parser.add_argument('--no-pdf', action='store_true', help='Only update JSON, do not modify PDF')
    
    args = parser.parse_args()
    
    # Validate files exist
    if not Path(args.json_file).exists():
        print(f"Error: JSON file '{args.json_file}' not found")
        sys.exit(1)
    
    if not Path(args.pdf_file).exists():
        print(f"Error: PDF file '{args.pdf_file}' not found")
        sys.exit(1)
    
    # Create renamer instance
    renamer = PDFFieldRenamer(args.json_file, args.pdf_file)
    
    # Run interactive renaming
    if renamer.rename_fields_interactive():
        # Show summary
        renamer.show_summary()
        
        if renamer.renamed_fields:
            # Ask for confirmation
            print("\n" + "-"*60)
            confirm = input("Apply these changes? (y/n): ").strip().lower()
            
            if confirm == 'y':
                # Update JSON
                renamer.update_json_file(args.json_output)
                
                # Update PDF unless --no-pdf flag is set
                if not args.no_pdf:
                    renamer.apply_renames_to_pdf(args.output)
                
                print("\n✓ All changes applied successfully!")
            else:
                print("\nChanges discarded.")


if __name__ == "__main__":
    main()