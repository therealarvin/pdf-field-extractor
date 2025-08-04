#!/usr/bin/env python3
"""
Script to:
1. Remove unique_id from display_attributes in schema files
2. Update base-level unique_id to match the formfield value from pdf_attributes
"""

import re
import json
import sys
from pathlib import Path


def extract_formfield(pdf_attributes_str):
    """Extract the formfield value from a pdf_attributes string."""
    # Match the formfield value
    match = re.search(r'"formfield"\s*:\s*"([^"]+)"', pdf_attributes_str)
    if match:
        return match.group(1)
    return None


def process_schema_file(file_path):
    """Process a TypeScript schema file to fix unique_ids."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # First, remove unique_id from display_attributes
    pattern_display = r'("display_attributes"\s*:\s*\{[^}]*?)(\s*"unique_id"\s*:\s*"[^"]+"\s*,?)([^}]*?\})'
    
    def remove_unique_id_from_display(match):
        before = match.group(1)
        unique_id_line = match.group(2)
        after = match.group(3)
        
        # Remove the unique_id line
        result = before + after
        
        # Clean up any double commas or leading commas
        result = re.sub(r',\s*,', ',', result)
        result = re.sub(r'\{\s*,', '{', result)
        result = re.sub(r',\s*\}', '}', result)
        
        return result
    
    # Remove unique_ids from display_attributes
    while True:
        new_content = re.sub(pattern_display, remove_unique_id_from_display, content, flags=re.DOTALL)
        if new_content == content:
            break
        content = new_content
    
    # Now update base-level unique_ids to match formfields
    # Pattern to match entire schema items
    pattern_item = r'(\{\s*"unique_id"\s*:\s*"[^"]+"\s*,\s*"pdf_attributes"\s*:\s*\[[^\]]+\][^}]*\})'
    
    def update_unique_id_to_formfield(match):
        item_str = match.group(0)
        
        # Extract the formfield value
        formfield = extract_formfield(item_str)
        
        if formfield:
            # Replace the unique_id value with the formfield value
            updated = re.sub(
                r'"unique_id"\s*:\s*"[^"]+"',
                f'"unique_id": "{formfield}"',
                item_str,
                count=1
            )
            return updated
        
        return item_str
    
    # Update all base-level unique_ids
    content = re.sub(pattern_item, update_unique_id_to_formfield, content, flags=re.DOTALL)
    
    # Write the modified content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return content


def verify_changes(file_path):
    """Verify the changes made to the file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Count stats
    total_unique_ids = len(re.findall(r'"unique_id"\s*:', content))
    display_unique_ids = len(re.findall(r'"display_attributes"\s*:\s*\{[^}]*"unique_id"', content, re.DOTALL))
    
    # Find some examples of unique_id and formfield pairs
    examples = []
    pattern = r'"unique_id"\s*:\s*"([^"]+)"[^{]*"pdf_attributes"[^{]*"formfield"\s*:\s*"([^"]+)"'
    matches = re.finditer(pattern, content, re.DOTALL)
    
    for i, match in enumerate(matches):
        if i < 5:  # Show first 5 examples
            unique_id = match.group(1)
            formfield = match.group(2)
            examples.append((unique_id, formfield))
    
    return total_unique_ids, display_unique_ids, examples


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
        print(f"Successfully processed {file_path}")
        
        # Verify changes
        total, display, examples = verify_changes(file_path)
        
        print(f"\nStats:")
        print(f"- Total unique_id occurrences: {total}")
        print(f"- unique_ids in display_attributes: {display}")
        print(f"- unique_ids at base level: {total - display}")
        
        print(f"\nFirst few unique_id -> formfield mappings:")
        for unique_id, formfield in examples:
            match_status = "✓" if unique_id == formfield else "✗"
            print(f"  {match_status} {unique_id} -> {formfield}")
        
    except Exception as e:
        print(f"Error processing file: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()