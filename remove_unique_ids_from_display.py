#!/usr/bin/env python3
"""
Script to remove unique_id from display_attributes in schema files.
Keeps unique_id only at the base object level alongside pdf_attributes.
"""

import re
import sys
from pathlib import Path


def process_schema_file(file_path):
    """Process a TypeScript schema file to remove unique_id from display_attributes."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match unique_id within display_attributes blocks
    # This pattern looks for unique_id lines within display_attributes objects
    pattern = r'("display_attributes"\s*:\s*\{[^}]*?)(\s*"unique_id"\s*:\s*"[^"]+"\s*,?)([^}]*?\})'
    
    def remove_unique_id(match):
        before = match.group(1)
        unique_id_line = match.group(2)
        after = match.group(3)
        
        # Remove the unique_id line and any trailing comma issues
        result = before + after
        
        # Clean up any double commas or leading commas
        result = re.sub(r',\s*,', ',', result)
        result = re.sub(r'\{\s*,', '{', result)
        result = re.sub(r',\s*\}', '}', result)
        
        return result
    
    # Process the content
    modified_content = content
    
    # Keep replacing until no more matches (handles nested cases)
    while True:
        new_content = re.sub(pattern, remove_unique_id, modified_content, flags=re.DOTALL)
        if new_content == modified_content:
            break
        modified_content = new_content
    
    # Write the modified content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    return modified_content


def main():
    """Main function to process schema files."""
    
    # Default file to process
    default_file = "residential_real_estate_listing_agreement_exclusive_right_to_lease_schema_reorganized.ts"
    
    # Get file path from command line or use default
    if len(sys.argv) > 1:
        file_path = Path(sys.argv[1])
    else:
        file_path = Path(default_file)
    
    if not file_path.exists():
        print(f"Error: File '{file_path}' not found!")
        sys.exit(1)
    
    print(f"Processing file: {file_path}")
    
    try:
        # Process the file
        process_schema_file(file_path)
        print(f"Successfully removed unique_ids from display_attributes in {file_path}")
        
        # Count remaining unique_ids to verify
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Count unique_ids at base level (not in display_attributes)
        base_unique_ids = len(re.findall(r'^\s*"unique_id"\s*:', content, re.MULTILINE))
        display_unique_ids = len(re.findall(r'"display_attributes"\s*:\s*\{[^}]*"unique_id"', content, re.DOTALL))
        
        print(f"\nStats:")
        print(f"- Total unique_id occurrences: {base_unique_ids}")
        print(f"- unique_ids in display_attributes: {display_unique_ids}")
        print(f"- unique_ids at base level: {base_unique_ids - display_unique_ids}")
        
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()