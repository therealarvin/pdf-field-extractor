#!/usr/bin/env python3
import json
import sys

def extract_master_fields():
    """Extract only master suite related fields from the enhanced JSON file"""
    
    with open('residential_lease_inventory_and_condition_fields_enhanced.json', 'r') as f:
        all_fields = json.load(f)
    
    # Filter for master suite fields only
    master_fields = []
    for field in all_fields:
        field_name = field.get('field_name', '')
        if 'master' in field_name.lower():
            master_fields.append(field)
    
    # Save filtered fields
    with open('master_suite_fields.json', 'w') as f:
        json.dump(master_fields, f, indent=2)
    
    print(f"Found {len(master_fields)} master suite fields:")
    
    # Group by type
    bedroom_fields = []
    bathroom_fields = []
    
    for field in master_fields:
        field_name = field.get('field_name', '')
        if 'master_bath' in field_name:
            bathroom_fields.append(field_name)
        else:
            bedroom_fields.append(field_name)
    
    print(f"\nMaster Bedroom fields ({len(bedroom_fields)}):")
    for field in sorted(bedroom_fields):
        print(f"  - {field}")
    
    print(f"\nMaster Bathroom fields ({len(bathroom_fields)}):")
    for field in sorted(bathroom_fields):
        print(f"  - {field}")
    
    # Analyze field patterns
    print(f"\nField Pattern Analysis:")
    
    # Group by base feature (ceiling, paint, etc)
    features = {}
    for field in master_fields:
        field_name = field.get('field_name', '')
        
        # Extract feature name
        if 'master_bath_' in field_name:
            feature = field_name.replace('master_bath_', '').replace('_move_in_comments', '').replace('_landlords_move_out_comments', '')
        elif 'master_' in field_name:
            feature = field_name.replace('master_', '').replace('_move_in_comments', '').replace('_landlords_move_out_comments', '')
        else:
            continue
            
        if feature not in features:
            features[feature] = {'move_in': [], 'move_out': []}
        
        if '_move_in_comments' in field_name:
            features[feature]['move_in'].append(field_name)
        elif '_landlords_move_out_comments' in field_name:
            features[feature]['move_out'].append(field_name)
    
    print(f"\nFeatures with both move-in and move-out comments:")
    for feature, variants in features.items():
        if variants['move_in'] and variants['move_out']:
            print(f"  {feature}: {len(variants['move_in'])} move-in, {len(variants['move_out'])} move-out")

if __name__ == "__main__":
    extract_master_fields()