#!/usr/bin/env python3
import json
from collections import defaultdict

# Load the extracted fields
with open('new_home_contract_completed_construction_Fillable_fields_enhanced.json', 'r') as f:
    fields = json.load(f)

# Group fields by page and type
pages = defaultdict(list)
for field in fields:
    pages[field['page']].append(field)

# Analyze fields by context patterns
field_analysis = []

for field in fields:
    context_all = (
        field.get('context_left', '').lower() + ' ' +
        field.get('context_right', '').lower() + ' ' +
        field.get('context_above', '').lower() + ' ' +
        field.get('context_below', '').lower()
    )
    
    # Determine field purpose based on context
    field_info = {
        'field_name': field['field_name'],
        'field_type': field['field_type'],
        'page': field['page'],
        'purpose': '',
        'unique_id': ''
    }
    
    # Party names
    if 'buyer' in context_all and ('name' in context_all or field['field_name'].endswith('_1') or field['field_name'].endswith('_2')):
        field_info['purpose'] = 'Buyer Name'
        field_info['unique_id'] = 'buyer_name'
    elif 'seller' in context_all and ('name' in context_all or field['field_name'].endswith('_1') or field['field_name'].endswith('_2')):
        field_info['purpose'] = 'Seller Name'
        field_info['unique_id'] = 'seller_name'
    
    # Property information
    elif 'property' in context_all and 'lot' in context_all:
        field_info['purpose'] = 'Lot Number'
        field_info['unique_id'] = 'property_lot'
    elif 'block' in context_all:
        field_info['purpose'] = 'Block Number'
        field_info['unique_id'] = 'property_block'
    elif 'addition' in context_all:
        field_info['purpose'] = 'Addition Name'
        field_info['unique_id'] = 'property_addition'
    elif 'county' in context_all:
        field_info['purpose'] = 'County'
        field_info['unique_id'] = 'property_county'
    elif 'city' in context_all:
        field_info['purpose'] = 'City'
        field_info['unique_id'] = 'property_city'
    elif 'address' in context_all or 'zip' in context_all:
        field_info['purpose'] = 'Property Address'
        field_info['unique_id'] = 'property_address'
    
    # Financial
    elif '$' in context_all or 'price' in context_all:
        if 'sales price' in context_all:
            field_info['purpose'] = 'Sales Price'
            field_info['unique_id'] = 'sales_price'
        elif 'down payment' in context_all:
            field_info['purpose'] = 'Down Payment'
            field_info['unique_id'] = 'down_payment'
        elif 'earnest money' in context_all:
            field_info['purpose'] = 'Earnest Money'
            field_info['unique_id'] = 'earnest_money'
        elif 'financing' in context_all:
            field_info['purpose'] = 'Financing Amount'
            field_info['unique_id'] = 'financing_amount'
    
    # Dates
    elif 'date' in context_all or 'day' in context_all or 'month' in context_all or 'year' in context_all:
        if 'closing' in context_all:
            field_info['purpose'] = 'Closing Date'
            field_info['unique_id'] = 'closing_date'
        elif 'effective' in context_all:
            field_info['purpose'] = 'Effective Date'
            field_info['unique_id'] = 'effective_date'
        elif 'signature' in context_all:
            field_info['purpose'] = 'Signature Date'
            field_info['unique_id'] = 'signature_date'
    
    # Signatures
    elif 'signature' in context_all:
        if 'buyer' in context_all:
            field_info['purpose'] = 'Buyer Signature'
            field_info['unique_id'] = 'buyer_signature'
        elif 'seller' in context_all:
            field_info['purpose'] = 'Seller Signature'
            field_info['unique_id'] = 'seller_signature'
    
    # Checkboxes
    elif field['field_type'] == 'CheckBox':
        if 'financing' in context_all:
            field_info['purpose'] = 'Financing Type'
            field_info['unique_id'] = 'financing_type'
        elif 'va' in context_all:
            field_info['purpose'] = 'VA Financing'
            field_info['unique_id'] = 'financing_va'
        elif 'fha' in context_all:
            field_info['purpose'] = 'FHA Financing'
            field_info['unique_id'] = 'financing_fha'
        elif 'conventional' in context_all:
            field_info['purpose'] = 'Conventional Financing'
            field_info['unique_id'] = 'financing_conventional'
    
    field_analysis.append(field_info)

# Print summary
print(f"Total fields analyzed: {len(fields)}")
print(f"\nFields by page:")
for page, page_fields in sorted(pages.items()):
    print(f"  Page {page}: {len(page_fields)} fields")

# Show first 30 analyzed fields
print("\nFirst 30 fields with analyzed purpose:")
for i, field in enumerate(field_analysis[:30]):
    print(f"{i+1}. {field['field_name']} ({field['field_type']}) - Purpose: {field['purpose'] or 'Unknown'}")

# Save full analysis
with open('new_home_contract_field_analysis.json', 'w') as f:
    json.dump(field_analysis, f, indent=2)
print("\nFull analysis saved to new_home_contract_field_analysis.json")