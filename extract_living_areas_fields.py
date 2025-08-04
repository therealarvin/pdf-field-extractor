#!/usr/bin/env python3
import json
import sys

def extract_living_areas_fields(input_file, output_file):
    """Extract only living areas fields from the enhanced JSON file."""
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            all_fields = json.load(f)
        
        # Filter for living areas fields
        living_areas_fields = []
        for field in all_fields:
            field_name = field.get('field_name', '')
            if any(area in field_name for area in ['living', 'dining', 'family']):
                living_areas_fields.append(field)
        
        # Write filtered fields to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(living_areas_fields, f, indent=2)
        
        print(f"Extracted {len(living_areas_fields)} living areas fields to {output_file}")
        
        # Print field categories summary
        living_count = sum(1 for field in living_areas_fields if 'living' in field['field_name'])
        dining_count = sum(1 for field in living_areas_fields if 'dining' in field['field_name'])
        family_count = sum(1 for field in living_areas_fields if 'family' in field['field_name'])
        
        print(f"Field breakdown:")
        print(f"  Living room: {living_count} fields")
        print(f"  Dining room: {dining_count} fields")
        print(f"  Family room: {family_count} fields")
        print(f"  Total: {len(living_areas_fields)} fields")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_file = "/Users/arvin/WebDev/field_extraction/residential_lease_inventory_and_condition_fields_enhanced.json"
    output_file = "/Users/arvin/WebDev/field_extraction/living_areas_fields_only.json"
    
    extract_living_areas_fields(input_file, output_file)