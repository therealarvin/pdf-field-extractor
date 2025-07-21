#!/usr/bin/env python3
"""
Apply Field Mapping Script
Applies a pre-defined field name mapping to rename PDF form fields.
This script does not perform any automatic renaming - it only applies the exact mapping provided.
"""

import json
import sys
import os
from datetime import datetime
from typing import Dict, List
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter

def load_mapping(mapping_file: str) -> Dict[str, str]:
    """Load the field name mapping from JSON file"""
    try:
        with open(mapping_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('field_mappings', {})
    except Exception as e:
        print(f"Error loading mapping file: {e}")
        sys.exit(1)

def apply_mapping_to_pdf(pdf_path: str, mapping: Dict[str, str], output_path: str = None) -> str:
    """Apply the field mapping to the PDF"""
    if not output_path:
        base_name = os.path.splitext(pdf_path)[0]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"{base_name}_mapped_{timestamp}.pdf"
    
    try:
        # Read the PDF
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        # Clone the reader into the writer
        writer.clone_reader_document_root(reader)
        
        # Track renaming
        renamed_count = 0
        skipped_count = 0
        not_found_count = 0
        
        # Update form field names
        if writer.get_form_fields():
            for field_name in list(writer.get_form_fields().keys()):
                if field_name in mapping:
                    new_name = mapping[field_name]
                    try:
                        writer.update_page_form_field_values(
                            writer.pages[0], 
                            {field_name: writer.get_form_fields()[field_name].value}, 
                            auto_regenerate=False
                        )
                        # Rename the field
                        for page in writer.pages:
                            if '/Annots' in page:
                                for annot_ref in page['/Annots']:
                                    annot = annot_ref.get_object()
                                    if '/T' in annot and annot['/T'] == field_name:
                                        annot.update({
                                            PyPDF2.generic.NameObject('/T'): PyPDF2.generic.TextStringObject(new_name)
                                        })
                        print(f"✓ Renamed: '{field_name}' → '{new_name}'")
                        renamed_count += 1
                    except Exception as e:
                        print(f"⚠ Failed to rename '{field_name}': {e}")
                        not_found_count += 1
                else:
                    skipped_count += 1
        
        # Alternative approach using lower-level access
        if renamed_count == 0:
            print("\nTrying alternative renaming approach...")
            if '/AcroForm' in writer._root_object and '/Fields' in writer._root_object['/AcroForm']:
                fields = writer._root_object['/AcroForm']['/Fields']
                
                for field_ref in fields:
                    field = field_ref.get_object()
                    if '/T' in field:
                        current_name = str(field['/T'])
                        
                        # Apply mapping if exists
                        if current_name in mapping:
                            new_name = mapping[current_name]
                            field[PyPDF2.generic.NameObject('/T')] = PyPDF2.generic.TextStringObject(new_name)
                            print(f"✓ Renamed: '{current_name}' → '{new_name}'")
                            renamed_count += 1
                        else:
                            print(f"- Skipped: '{current_name}' (no mapping found)")
                            skipped_count += 1
        
        # Write the output PDF
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        print(f"\n{'='*80}")
        print(f"✓ Successfully processed PDF")
        print(f"✓ Renamed {renamed_count} fields")
        print(f"- Skipped {skipped_count} fields (no mapping)")
        if not_found_count > 0:
            print(f"⚠ Failed to rename {not_found_count} fields")
        print(f"✓ Output saved to: {output_path}")
        
        return output_path
        
    except Exception as e:
        print(f"Error processing PDF: {e}")
        import traceback
        traceback.print_exc()
        return None

def apply_mapping_to_json(json_path: str, mapping: Dict[str, str], output_path: str = None) -> str:
    """Apply the field mapping to the extracted fields JSON"""
    if not output_path:
        base_name = os.path.splitext(json_path)[0]
        output_path = f"{base_name}_mapped.json"
    
    try:
        # Load the extracted fields
        with open(json_path, 'r', encoding='utf-8') as f:
            fields = json.load(f)
        
        # Apply mapping
        renamed_count = 0
        skipped_count = 0
        
        for field in fields:
            current_name = field.get('field_name', '')
            if current_name in mapping:
                field['original_name'] = current_name
                field['field_name'] = mapping[current_name]
                renamed_count += 1
            else:
                skipped_count += 1
        
        # Save the updated JSON
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(fields, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Updated JSON with {renamed_count} renamed fields")
        print(f"✓ Saved to: {output_path}")
        
        return output_path
        
    except Exception as e:
        print(f"Error processing JSON: {e}")
        return None

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 apply_field_mapping.py <mapping_file.json> <input.pdf> <extracted_fields.json> [output.pdf] [output.json]")
        print("\nExample:")
        print("  python3 apply_field_mapping.py field_mapping.json document.pdf document_fields.json")
        print("\nThis will create:")
        print("  - document_mapped_[timestamp].pdf (PDF with renamed fields)")
        print("  - document_fields_mapped.json (Updated field metadata)")
        sys.exit(1)
    
    mapping_file = sys.argv[1]
    pdf_file = sys.argv[2]
    json_file = sys.argv[3]
    output_pdf = sys.argv[4] if len(sys.argv) > 4 else None
    output_json = sys.argv[5] if len(sys.argv) > 5 else None
    
    # Validate inputs
    if not os.path.exists(mapping_file):
        print(f"Error: Mapping file not found: {mapping_file}")
        sys.exit(1)
    
    if not os.path.exists(pdf_file):
        print(f"Error: PDF file not found: {pdf_file}")
        sys.exit(1)
    
    if not os.path.exists(json_file):
        print(f"Error: JSON file not found: {json_file}")
        sys.exit(1)
    
    print(f"Loading field mapping from: {mapping_file}")
    mapping = load_mapping(mapping_file)
    print(f"Loaded {len(mapping)} field mappings")
    
    print(f"\nApplying mapping to PDF: {pdf_file}")
    pdf_result = apply_mapping_to_pdf(pdf_file, mapping, output_pdf)
    
    print(f"\nApplying mapping to JSON: {json_file}")
    json_result = apply_mapping_to_json(json_file, mapping, output_json)
    
    if pdf_result and json_result:
        print("\n✓ All mappings applied successfully!")
    else:
        print("\n⚠ Some errors occurred during processing")
        sys.exit(1)

if __name__ == "__main__":
    main()