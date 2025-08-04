#!/usr/bin/env python3
import json
import re
from collections import defaultdict

def analyze_field_context(field):
    """Analyze field context to determine its purpose and unique_id"""
    context_all = (
        field.get('context_left', '').lower() + ' ' +
        field.get('context_right', '').lower() + ' ' +
        field.get('context_above', '').lower() + ' ' +
        field.get('context_below', '').lower()
    ).strip()
    
    # Clean up context
    context_all = ' '.join(context_all.split())
    
    # Get specific contexts
    context_left = field.get('context_left', '').strip()
    context_right = field.get('context_right', '').strip() 
    context_above = field.get('context_above', '').strip()
    context_below = field.get('context_below', '').strip()
    
    field_type = field['field_type']
    page = field['page']
    
    # Detailed context analysis
    purpose = ''
    unique_id = ''
    display_name = ''
    
    # === PARTY INFORMATION ===
    if 'buyer' in context_all:
        if 'name' in context_all or (page == 0 and field['field_name'].endswith('_1')):
            purpose = 'Buyer Name'
            unique_id = 'buyer_name'
            display_name = 'Buyer Name'
        elif 'phone' in context_all:
            purpose = 'Buyer Phone'
            unique_id = 'buyer_phone'
            display_name = 'Buyer Phone Number'
        elif 'email' in context_all:
            purpose = 'Buyer Email'
            unique_id = 'buyer_email'
            display_name = 'Buyer Email Address'
        elif 'signature' in context_all:
            purpose = 'Buyer Signature'
            unique_id = 'buyer_signature'
            display_name = 'Buyer Signature'
            
    elif 'seller' in context_all:
        if 'name' in context_all or (page == 0 and field['field_name'].endswith('_2')):
            purpose = 'Seller Name'
            unique_id = 'seller_name'
            display_name = 'Seller Name'
        elif 'phone' in context_all:
            purpose = 'Seller Phone'
            unique_id = 'seller_phone'
            display_name = 'Seller Phone Number'
        elif 'email' in context_all:
            purpose = 'Seller Email'
            unique_id = 'seller_email'
            display_name = 'Seller Email Address'
        elif 'signature' in context_all:
            purpose = 'Seller Signature'
            unique_id = 'seller_signature'
            display_name = 'Seller Signature'
    
    # === PROPERTY INFORMATION ===
    elif 'lot' in context_all and 'property' in context_all:
        purpose = 'Lot Number'
        unique_id = 'property_lot'
        display_name = 'Lot Number'
    elif 'block' in context_all:
        purpose = 'Block Number'
        unique_id = 'property_block'
        display_name = 'Block Number'
    elif 'addition' in context_all:
        purpose = 'Addition Name'
        unique_id = 'property_addition'
        display_name = 'Addition Name'
    elif 'subdivision' in context_all:
        purpose = 'Subdivision'
        unique_id = 'property_subdivision'
        display_name = 'Subdivision'
    elif 'county' in context_all and 'of' in context_all:
        purpose = 'County'
        unique_id = 'property_county'
        display_name = 'County'
    elif 'city' in context_all and 'of' in context_all:
        purpose = 'City'
        unique_id = 'property_city'
        display_name = 'City'
    elif 'address' in context_all or 'zip' in context_all:
        if 'zip' in context_all:
            purpose = 'Property Address/ZIP'
            unique_id = 'property_address_zip'
            display_name = 'Property Address/ZIP Code'
        else:
            purpose = 'Property Address'
            unique_id = 'property_address'
            display_name = 'Property Address'
    
    # === FINANCIAL INFORMATION ===
    elif '$' in context_left or '$' in context_right:
        if 'sales price' in context_all:
            purpose = 'Sales Price'
            unique_id = 'sales_price'
            display_name = 'Sales Price'
        elif 'down payment' in context_all:
            purpose = 'Down Payment'
            unique_id = 'down_payment'
            display_name = 'Down Payment'
        elif 'earnest money' in context_all:
            purpose = 'Earnest Money'
            unique_id = 'earnest_money'
            display_name = 'Earnest Money'
        elif 'financing' in context_all:
            purpose = 'Financing Amount'
            unique_id = 'financing_amount'
            display_name = 'Financing Amount'
        elif 'cash' in context_all:
            purpose = 'Cash Amount'
            unique_id = 'cash_amount'
            display_name = 'Cash Amount'
    
    # === DATES ===
    elif 'date' in context_all or 'days' in context_all:
        if 'closing' in context_all:
            purpose = 'Closing Date'
            unique_id = 'closing_date'
            display_name = 'Closing Date'
        elif 'effective' in context_all:
            purpose = 'Effective Date'
            unique_id = 'effective_date'
            display_name = 'Effective Date'
        elif 'possession' in context_all:
            purpose = 'Possession Date'
            unique_id = 'possession_date'
            display_name = 'Possession Date'
    
    # === FINANCING CHECKBOXES ===
    elif field_type == 'CheckBox':
        if 'third party financing' in context_all:
            purpose = 'Third Party Financing'
            unique_id = 'financing_third_party'
            display_name = 'Third Party Financing'
        elif 'loan assumption' in context_all:
            purpose = 'Loan Assumption'
            unique_id = 'financing_loan_assumption'
            display_name = 'Loan Assumption'
        elif 'seller financing' in context_all:
            purpose = 'Seller Financing'
            unique_id = 'financing_seller'
            display_name = 'Seller Financing'
        elif 'va' in context_all:
            purpose = 'VA Financing'
            unique_id = 'financing_va'
            display_name = 'VA Financing'
        elif 'fha' in context_all:
            purpose = 'FHA Financing'
            unique_id = 'financing_fha'
            display_name = 'FHA Financing'
        elif 'conventional' in context_all:
            purpose = 'Conventional Financing'
            unique_id = 'financing_conventional'
            display_name = 'Conventional Financing'
    
    # === ESCROW/TITLE ===
    elif 'escrow' in context_all:
        if 'agent' in context_all:
            purpose = 'Escrow Agent'
            unique_id = 'escrow_agent'
            display_name = 'Escrow Agent'
        elif 'address' in context_all:
            purpose = 'Escrow Address'
            unique_id = 'escrow_address'
            display_name = 'Escrow Agent Address'
    elif 'title company' in context_all:
        purpose = 'Title Company'
        unique_id = 'title_company'
        display_name = 'Title Company'
    
    # === BROKER/AGENT INFORMATION ===
    elif 'broker' in context_all or 'agent' in context_all:
        if 'listing' in context_all:
            if 'name' in context_all:
                purpose = 'Listing Broker Name'
                unique_id = 'listing_broker_name'
                display_name = 'Listing Broker Name'
            elif 'license' in context_all:
                purpose = 'Listing Broker License'
                unique_id = 'listing_broker_license'
                display_name = 'Listing Broker License #'
        elif 'selling' in context_all or 'other' in context_all:
            if 'name' in context_all:
                purpose = 'Selling Broker Name'
                unique_id = 'selling_broker_name'
                display_name = 'Selling Broker Name'
            elif 'license' in context_all:
                purpose = 'Selling Broker License'
                unique_id = 'selling_broker_license'
                display_name = 'Selling Broker License #'
    
    # === SIGNATURES AND INITIALS ===
    elif 'signature' in context_all:
        purpose = 'Signature'
        unique_id = 'signature'
        display_name = 'Signature'
    elif 'initial' in context_all:
        purpose = 'Initial'
        unique_id = 'initial'
        display_name = 'Initial'
    
    # === TIME/DAYS ===
    elif 'time' in context_all:
        purpose = 'Time'
        unique_id = 'time'
        display_name = 'Time'
    elif 'days' in context_all and field_type == 'Text':
        purpose = 'Number of Days'
        unique_id = 'days'
        display_name = 'Days'
    
    return purpose, unique_id, display_name, context_all

# Load the extracted fields
with open('new_home_contract_completed_construction_Fillable_fields_enhanced.json', 'r') as f:
    fields = json.load(f)

# Analyze all fields
analyzed_fields = []
unique_id_counts = defaultdict(int)

for field in fields:
    purpose, unique_id, display_name, context_all = analyze_field_context(field)
    
    # If we identified a unique_id, handle duplicates
    if unique_id:
        count = unique_id_counts[unique_id]
        if count > 0:
            # This is a duplicate - likely a same-value field on another page
            unique_id = f"{unique_id}_page_{field['page']}"
        unique_id_counts[unique_id] += 1
    
    analyzed_fields.append({
        'field_name': field['field_name'],
        'field_type': field['field_type'],
        'page': field['page'],
        'purpose': purpose,
        'unique_id': unique_id,
        'display_name': display_name,
        'context': context_all,
        'position': field.get('position', [])
    })

# Print detailed analysis
print(f"Total fields analyzed: {len(fields)}")
print(f"\nFields with identified purpose: {sum(1 for f in analyzed_fields if f['purpose'])}")
print(f"Fields without identified purpose: {sum(1 for f in analyzed_fields if not f['purpose'])}")

# Show fields by page
print("\n=== FIELDS BY PAGE ===")
for page in range(11):
    page_fields = [f for f in analyzed_fields if f['page'] == page]
    print(f"\nPage {page} ({len(page_fields)} fields):")
    for f in page_fields[:10]:  # Show first 10 fields per page
        print(f"  {f['field_name']} - {f['purpose'] or 'Unknown'}")
    if len(page_fields) > 10:
        print(f"  ... and {len(page_fields) - 10} more fields")

# Save full analysis
with open('new_home_contract_detailed_analysis.json', 'w') as f:
    json.dump(analyzed_fields, f, indent=2)

print("\nFull analysis saved to new_home_contract_detailed_analysis.json")