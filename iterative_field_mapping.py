#!/usr/bin/env python3
"""
Automated iterative field mapping for PDF forms.
Maps PDF fields to iterative names: form_name_textfield_N, form_name_checkbox_N, etc.
"""

import json
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path


def extract_form_name(pdf_path):
    """Extract form name from PDF filename."""
    filename = Path(pdf_path).stem
    # Convert to lowercase and replace spaces/special chars with underscores
    form_name = filename.lower().replace(' ', '_').replace('-', '_').replace('(', '').replace(')', '')
    return form_name


def run_field_extraction(pdf_path):
    """Run the field extraction script and return the output JSON filename."""
    print(f"Extracting fields from {pdf_path}...")
    
    try:
        result = subprocess.run(
            ['python3', 'extract_pdf_fields_enhanced.py', pdf_path],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse output to find JSON filename
        for line in result.stdout.split('\n'):
            if 'Saved extracted fields to' in line:
                json_file = line.split('Saved extracted fields to')[1].strip()
                print(f"Fields extracted to: {json_file}")
                return json_file
        
        # If not found in stdout, construct expected filename
        base_name = Path(pdf_path).stem
        json_file = f"{base_name}_fields_enhanced.json"
        if os.path.exists(json_file):
            print(f"Fields extracted to: {json_file}")
            return json_file
        
        raise Exception("Could not find extracted fields JSON file")
        
    except subprocess.CalledProcessError as e:
        print(f"Error extracting fields: {e}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)


def create_iterative_mapping(extracted_json_path, form_name):
    """Create iterative field mapping from extracted fields."""
    print(f"\nCreating iterative mapping for form: {form_name}")
    
    # Load extracted fields
    with open(extracted_json_path, 'r') as f:
        data = json.load(f)
    
    # Handle both list format and dictionary format
    if isinstance(data, list):
        fields = data
    else:
        fields = data.get('fields', [])
    
    # Separate fields by type and create mappings
    field_mappings = {}
    text_counter = 1
    checkbox_counter = 1
    radio_counter = 1
    button_counter = 1
    
    for field in fields:
        # Handle different field formats
        field_type = field.get('field_type', field.get('type', '')).lower()
        field_name = field.get('field_name', field.get('name', ''))
        
        if not field_name:
            continue
        
        # Assign iterative name based on field type
        if field_type == 'text':
            new_name = f"{form_name}_textfield_{text_counter}"
            text_counter += 1
        elif field_type == 'checkbox':
            new_name = f"{form_name}_checkbox_{checkbox_counter}"
            checkbox_counter += 1
        elif field_type == 'radio':
            new_name = f"{form_name}_radio_{radio_counter}"
            radio_counter += 1
        elif field_type == 'button':
            new_name = f"{form_name}_button_{button_counter}"
            button_counter += 1
        else:
            # Default to textfield for unknown types
            new_name = f"{form_name}_textfield_{text_counter}"
            text_counter += 1
        
        field_mappings[field_name] = new_name
    
    # Create mapping file structure
    mapping_data = {
        "field_mappings": field_mappings,
        "metadata": {
            "total_fields": len(field_mappings),
            "mapped_fields": len(field_mappings),
            "created_date": datetime.now().strftime("%Y-%m-%d"),
            "pdf_file": os.path.basename(extracted_json_path.replace('_fields_enhanced.json', '.pdf')),
            "form_name": form_name,
            "field_counts": {
                "text": text_counter - 1,
                "checkbox": checkbox_counter - 1,
                "radio": radio_counter - 1,
                "button": button_counter - 1
            }
        }
    }
    
    # Save mapping file
    mapping_filename = f"field_mapping_{form_name}.json"
    with open(mapping_filename, 'w') as f:
        json.dump(mapping_data, f, indent=2)
    
    print(f"Created mapping file: {mapping_filename}")
    print(f"Mapped {len(field_mappings)} fields:")
    print(f"  - Text fields: {text_counter - 1}")
    print(f"  - Checkboxes: {checkbox_counter - 1}")
    print(f"  - Radio buttons: {radio_counter - 1}")
    print(f"  - Buttons: {button_counter - 1}")
    
    return mapping_filename


def apply_mapping(mapping_file, pdf_path, extracted_json_path, form_name, output_dir=None):
    """Apply the field mapping to create renamed PDF."""
    print(f"\nApplying field mapping...")
    
    try:
        result = subprocess.run(
            ['python3', 'apply_field_mapping_fitz.py', mapping_file, pdf_path, extracted_json_path],
            capture_output=True,
            text=True,
            check=True
        )
        
        print(result.stdout)
        
        # Find the output file and rename it to desired format
        pdf_dir = os.path.dirname(pdf_path)
        output_base_dir = output_dir if output_dir else pdf_dir
        
        for line in result.stdout.split('\n'):
            if 'Saved renamed PDF to:' in line:
                output_file = line.split('Saved renamed PDF to:')[1].strip()
                # Rename to desired format and move to output directory
                final_name = os.path.join(output_base_dir, f"{form_name}_Fillable.pdf")
                if os.path.exists(output_file):
                    # Create output directory if it doesn't exist
                    os.makedirs(output_base_dir, exist_ok=True)
                    # Move and rename
                    if output_file != final_name:
                        os.rename(output_file, final_name)
                    print(f"\nFinal output: {final_name}")
                    return final_name
        
        # If not found, look for the file with mapped timestamp
        import glob
        pattern = os.path.join(pdf_dir, f"*_mapped_*.pdf")
        mapped_files = glob.glob(pattern)
        if mapped_files:
            # Get the most recent one
            latest = max(mapped_files, key=os.path.getctime)
            final_name = os.path.join(output_base_dir, f"{form_name}_Fillable.pdf")
            # Create output directory if it doesn't exist
            os.makedirs(output_base_dir, exist_ok=True)
            os.rename(latest, final_name)
            print(f"\nFinal output: {final_name}")
            return final_name
        
    except subprocess.CalledProcessError as e:
        print(f"Error applying mapping: {e}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python3 iterative_field_mapping.py <pdf_file> [output_directory]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) == 3 else None
    
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)
    
    # Extract form name
    form_name = extract_form_name(pdf_path)
    print(f"Processing PDF: {pdf_path}")
    print(f"Form name: {form_name}")
    
    # Step 1: Extract fields
    extracted_json = run_field_extraction(pdf_path)
    
    # Step 2: Create iterative mapping
    mapping_file = create_iterative_mapping(extracted_json, form_name)
    
    # Step 3: Apply mapping
    output_pdf = apply_mapping(mapping_file, pdf_path, extracted_json, form_name, output_dir)
    
    print("\nWorkflow completed successfully!")
    print(f"Output files:")
    print(f"  - Renamed PDF: {output_pdf}")
    print(f"  - Field mapping: {mapping_file}")
    print(f"  - Field metadata: {extracted_json}_mapped.json")


if __name__ == "__main__":
    main()