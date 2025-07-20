#!/usr/bin/env python3
"""
Visualize and summarize extracted PDF fields
"""

import json
import argparse
from pathlib import Path
from collections import defaultdict


def load_field_data(json_path: str) -> list:
    """Load field data from JSON file"""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def categorize_fields(fields: list) -> dict:
    """Categorize fields by their type and purpose"""
    categories = defaultdict(list)
    
    for field in fields:
        name = field['field_name'].lower()
        
        # Categorize based on field name patterns
        if any(x in name for x in ['client', 'buyer', 'tenant']):
            categories['Client Information'].append(field)
        elif any(x in name for x in ['broker', 'agent']):
            categories['Broker Information'].append(field)
        elif any(x in name for x in ['address', 'city', 'state', 'zip', 'property']):
            categories['Address/Property Information'].append(field)
        elif any(x in name for x in ['phone', 'email', 'fax']):
            categories['Contact Information'].append(field)
        elif any(x in name for x in ['signature', 'initial']):
            categories['Signatures/Initials'].append(field)
        elif any(x in name for x in ['date', 'term', 'begin', 'end']):
            categories['Dates/Terms'].append(field)
        elif any(x in name for x in ['fee', 'price', 'compensation', 'purchase', 'lease', 'rent']):
            categories['Financial Terms'].append(field)
        else:
            categories['Other'].append(field)
    
    return categories


def print_summary(fields: list):
    """Print a summary of the extracted fields"""
    print("\n" + "="*80)
    print("PDF FIELD EXTRACTION SUMMARY")
    print("="*80)
    
    # Basic stats
    print(f"\nTotal fields found: {len(fields)}")
    
    # Field types
    field_types = defaultdict(int)
    for field in fields:
        field_types[field['field_type']] += 1
    
    print("\nField types:")
    for ftype, count in field_types.items():
        print(f"  - {ftype}: {count}")
    
    # Pages with fields
    pages = set()
    for field in fields:
        if field['page'] is not None:
            pages.add(field['page'])
    
    print(f"\nPages containing fields: {sorted(pages) if pages else 'Unknown'}")
    
    # Categorized fields
    categories = categorize_fields(fields)
    
    print("\n" + "-"*60)
    print("FIELDS BY CATEGORY")
    print("-"*60)
    
    for category, cat_fields in categories.items():
        print(f"\n{category} ({len(cat_fields)} fields):")
        for field in cat_fields:
            value_status = "has value" if field['current_value'] else "empty"
            context = field.get('label', '') or field.get('surrounding_context', '')[:50]
            # Get directional context
            contexts = []
            if field.get('context_left'):
                contexts.append(f"Left: {field['context_left'][:30]}...")
            elif field.get('context_above'):
                contexts.append(f"Above: {field['context_above'][:30]}...")
            elif context:
                contexts.append(f"Context: {context[:30]}...")
            
            context_str = f" | {contexts[0]}" if contexts else ""
            
            print(f"  - {field['field_name']} ({value_status}){context_str}")


def export_simplified_json(fields: list, output_path: str):
    """Export a simplified version of the field data"""
    simplified = []
    
    for field in fields:
        simplified.append({
            'name': field['field_name'],
            'type': field['field_type'],
            'value': field['current_value'],
            'page': field['page'],
            'context': field.get('label', '') or field.get('surrounding_context', '')[:100]
        })
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(simplified, f, indent=2, ensure_ascii=False)
    
    print(f"\nSimplified data exported to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description='Visualize and summarize extracted PDF fields')
    parser.add_argument('json_file', help='Path to the JSON file with extracted fields')
    parser.add_argument('-s', '--simplify', help='Export simplified JSON to specified path')
    
    args = parser.parse_args()
    
    # Check if file exists
    if not Path(args.json_file).exists():
        print(f"Error: File '{args.json_file}' not found")
        return
    
    # Load field data
    fields = load_field_data(args.json_file)
    
    # Print summary
    print_summary(fields)
    
    # Export simplified version if requested
    if args.simplify:
        export_simplified_json(fields, args.simplify)


if __name__ == "__main__":
    main()