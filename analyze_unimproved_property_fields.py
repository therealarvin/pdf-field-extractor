#!/usr/bin/env python3
"""Analyze and organize unimproved property contract fields"""

import json
from collections import defaultdict

def analyze_fields(filename):
    with open(filename, 'r') as f:
        fields = json.load(f)
    
    # Group by page and type
    by_page = defaultdict(list)
    by_type = defaultdict(list)
    
    # Context patterns
    party_fields = []
    property_fields = []
    financial_fields = []
    date_fields = []
    signature_fields = []
    checkbox_groups = defaultdict(list)
    
    print(f"Total fields: {len(fields)}")
    print("\nField distribution by type:")
    
    for field in fields:
        page = field['page']
        field_type = field['field_type']
        field_name = field['field_name']
        
        by_page[page].append(field)
        by_type[field_type].append(field)
        
        # Analyze context
        context = ' '.join([
            field.get('context_left', ''),
            field.get('context_right', ''),
            field.get('context_above', ''),
            field.get('context_below', '')
        ]).lower()
        
        # Categorize based on context
        if any(word in context for word in ['seller', 'buyer', 'name', 'agent', 'broker', 'escrow']):
            party_fields.append((field_name, context, page))
        
        if any(word in context for word in ['property', 'address', 'lot', 'block', 'city', 'county', 'zip']):
            property_fields.append((field_name, context, page))
            
        if any(word in context for word in ['$', 'price', 'amount', 'dollar', 'payment', 'earnest', 'money', 'fee']):
            financial_fields.append((field_name, context, page))
            
        if 'date' in context or 'day' in context:
            date_fields.append((field_name, context, page))
            
        if 'signature' in context or 'sign' in context or 'initial' in context:
            signature_fields.append((field_name, context, page))
    
    # Print type distribution
    for field_type, fields_list in by_type.items():
        print(f"  {field_type}: {len(fields_list)}")
    
    print(f"\nPages: {min(by_page.keys())} to {max(by_page.keys())}")
    
    print("\n=== CATEGORIZED FIELDS ===")
    print(f"\nParty-related fields: {len(party_fields)}")
    for name, context, page in party_fields[:10]:
        print(f"  {name} (p{page}): {context[:80]}...")
        
    print(f"\nProperty-related fields: {len(property_fields)}")
    for name, context, page in property_fields[:10]:
        print(f"  {name} (p{page}): {context[:80]}...")
        
    print(f"\nFinancial fields: {len(financial_fields)}")
    for name, context, page in financial_fields[:10]:
        print(f"  {name} (p{page}): {context[:80]}...")
        
    print(f"\nDate fields: {len(date_fields)}")
    for name, context, page in date_fields[:10]:
        print(f"  {name} (p{page}): {context[:80]}...")
        
    print(f"\nSignature fields: {len(signature_fields)}")
    for name, context, page in signature_fields[:10]:
        print(f"  {name} (p{page}): {context[:80]}...")
    
    # Look for potential same-value fields
    print("\n=== POTENTIAL SAME-VALUE FIELDS ===")
    context_map = defaultdict(list)
    for field in fields:
        # Create a normalized context key
        key_parts = []
        for ctx_type in ['context_left', 'context_right', 'context_above', 'context_below']:
            if field.get(ctx_type):
                key_parts.append(field[ctx_type].lower().strip())
        if key_parts:
            context_key = '|'.join(sorted(key_parts))
            context_map[context_key].append({
                'name': field['field_name'],
                'page': field['page'],
                'type': field['field_type']
            })
    
    # Show fields with similar context (potential same-value fields)
    for context_key, field_list in context_map.items():
        if len(field_list) > 1:
            print(f"\nSimilar context fields ({len(field_list)} occurrences):")
            print(f"  Context: {context_key[:100]}...")
            for f in field_list:
                print(f"    - {f['name']} (page {f['page']}, {f['type']})")

if __name__ == "__main__":
    analyze_fields("unimproved_property_contract_Fillable_fields_enhanced.json")