#!/usr/bin/env python3
"""
Final comprehensive schema generator for residential lease multi-family property unit form.
This script analyzes all 296 fields and generates a complete TypeScript schema.
"""

import json
import re
from collections import defaultdict, OrderedDict

def clean_text(text):
    """Clean and normalize text for analysis"""
    if not text:
        return ""
    # Add spaces between camelCase words
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters but keep essential ones
    text = re.sub(r'[^\w\s$%@\-./]', ' ', text)
    return text.strip()

def analyze_comprehensive_context(field):
    """Comprehensive field analysis with all context"""
    # Get all context
    left = clean_text(field.get('context_left', ''))
    right = clean_text(field.get('context_right', ''))
    above = clean_text(field.get('context_above', ''))
    below = clean_text(field.get('context_below', ''))
    
    all_context = f"{left} {right} {above} {below}".lower()
    field_name = field['field_name']
    field_type = field['field_type']
    page = field['page']
    
    # Extract field number
    field_num = field_name.split('_')[-1]
    
    # Analysis results
    result = {
        'field': field,
        'field_name': field_name,
        'field_type': field_type,
        'page': page,
        'field_num': field_num,
        'all_context': all_context,
        'left': left,
        'right': right,
        'above': above,
        'below': below
    }
    
    # Determine semantic purpose based on comprehensive context analysis
    
    # === PROPERTY INFORMATION ===
    if 'address' in all_context and ('property' in all_context or 'unit' in all_context or 'in' in left.lower()):
        result['purpose'] = 'property_address'
        result['unique_id'] = 'property_address'
        result['display_name'] = 'Property Address'
        result['block'] = 'property_information'
    
    elif 'unit' in all_context and ('number' in all_context or 'no' in all_context):
        result['purpose'] = 'unit_number'
        result['unique_id'] = 'unit_number'
        result['display_name'] = 'Unit Number'
        result['block'] = 'property_information'
    
    elif 'county' in all_context and 'texas' in all_context:
        result['purpose'] = 'property_county'
        result['unique_id'] = 'property_county'
        result['display_name'] = 'County'
        result['block'] = 'property_information'
    
    elif 'city' in all_context and page < 3:
        result['purpose'] = 'property_city'
        result['unique_id'] = 'property_city'
        result['display_name'] = 'City'
        result['block'] = 'property_information'
    
    elif 'state' in all_context and 'texas' not in all_context and page < 3:
        result['purpose'] = 'property_state'
        result['unique_id'] = 'property_state'
        result['display_name'] = 'State'
        result['block'] = 'property_information'
    
    elif 'zip' in all_context or 'postal' in all_context:
        result['purpose'] = 'property_zip'
        result['unique_id'] = 'property_zip'
        result['display_name'] = 'ZIP Code'
        result['block'] = 'property_information'
    
    # === LANDLORD INFORMATION ===
    elif 'landlord' in all_context or 'owner' in all_context or ('land' in all_context and 'lord' in all_context):
        if 'name' in all_context or (page == 0 and field_num in ['1', '2']):
            result['purpose'] = 'landlord_name'
            result['unique_id'] = 'landlord_name'
            result['display_name'] = 'Landlord Name'
            result['block'] = 'landlord_information'
        elif 'phone' in all_context:
            result['purpose'] = 'landlord_phone'
            result['unique_id'] = 'landlord_phone'
            result['display_name'] = 'Landlord Phone'
            result['block'] = 'landlord_information'
        elif 'email' in all_context or 'e mail' in all_context:
            result['purpose'] = 'landlord_email'
            result['unique_id'] = 'landlord_email'
            result['display_name'] = 'Landlord Email'
            result['block'] = 'landlord_information'
        elif 'fax' in all_context:
            result['purpose'] = 'landlord_fax'
            result['unique_id'] = 'landlord_fax'
            result['display_name'] = 'Landlord Fax'
            result['block'] = 'landlord_information'
        elif 'address' in all_context:
            result['purpose'] = 'landlord_address'
            result['unique_id'] = 'landlord_address'
            result['display_name'] = 'Landlord Address'
            result['block'] = 'landlord_information'
        elif 'signature' in all_context:
            result['purpose'] = 'landlord_signature'
            result['unique_id'] = f'landlord_signature_page_{page}'
            result['display_name'] = 'Landlord Signature'
            result['block'] = 'signatures'
        elif 'initial' in all_context:
            result['purpose'] = 'landlord_initial'
            result['unique_id'] = f'landlord_initial_page_{page}'
            result['display_name'] = 'Landlord Initial'
            result['block'] = 'signatures'
        else:
            result['purpose'] = 'landlord_field'
            result['unique_id'] = f'landlord_field_{field_num}_page_{page}'
            result['display_name'] = 'Landlord Information'
            result['block'] = 'landlord_information'
    
    # === TENANT INFORMATION ===
    elif 'tenant' in all_context or 'lessee' in all_context:
        if 'name' in all_context or (page == 0 and field_num == '3'):
            result['purpose'] = 'tenant_name'
            result['unique_id'] = 'tenant_1_name' if field_num == '3' else f'tenant_name_{field_num}'
            result['display_name'] = 'Tenant Name'
            result['block'] = 'tenant_information'
        elif 'phone' in all_context:
            result['purpose'] = 'tenant_phone'
            result['unique_id'] = 'tenant_phone'
            result['display_name'] = 'Tenant Phone'
            result['block'] = 'tenant_information'
        elif 'email' in all_context:
            result['purpose'] = 'tenant_email'
            result['unique_id'] = 'tenant_email'
            result['display_name'] = 'Tenant Email'
            result['block'] = 'tenant_information'
        elif 'signature' in all_context:
            result['purpose'] = 'tenant_signature'
            result['unique_id'] = f'tenant_signature_page_{page}'
            result['display_name'] = 'Tenant Signature'
            result['block'] = 'signatures'
        elif 'initial' in all_context:
            result['purpose'] = 'tenant_initial'
            result['unique_id'] = f'tenant_initial_page_{page}'
            result['display_name'] = 'Tenant Initial'
            result['block'] = 'signatures'
        else:
            result['purpose'] = 'tenant_field'
            result['unique_id'] = f'tenant_field_{field_num}_page_{page}'
            result['display_name'] = 'Tenant Information'
            result['block'] = 'tenant_information'
    
    # === LEASE TERMS ===
    elif 'commencement' in all_context and 'date' in all_context:
        result['purpose'] = 'lease_start_date'
        result['unique_id'] = 'lease_start_date'
        result['display_name'] = 'Lease Start Date'
        result['block'] = 'lease_terms'
    
    elif 'expiration' in all_context and 'date' in all_context:
        result['purpose'] = 'lease_end_date'
        result['unique_id'] = 'lease_end_date'
        result['display_name'] = 'Lease End Date'
        result['block'] = 'lease_terms'
    
    elif 'term' in all_context and 'lease' in all_context:
        result['purpose'] = 'lease_term'
        result['unique_id'] = 'lease_term'
        result['display_name'] = 'Lease Term'
        result['block'] = 'lease_terms'
    
    elif 'notice' in all_context and ('days' in all_context or 'day' in all_context):
        result['purpose'] = 'notice_days'
        result['unique_id'] = 'notice_days'
        result['display_name'] = 'Notice Period (Days)'
        result['block'] = 'lease_terms'
    
    # === FINANCIAL INFORMATION ===
    elif 'rent' in all_context:
        if 'monthly' in all_context or 'month' in all_context:
            result['purpose'] = 'monthly_rent'
            result['unique_id'] = 'monthly_rent'
            result['display_name'] = 'Monthly Rent'
            result['block'] = 'financial_information'
        elif 'late' in all_context and 'initial' in all_context:
            result['purpose'] = 'initial_late_fee'
            result['unique_id'] = 'initial_late_fee'
            result['display_name'] = 'Initial Late Fee'
            result['block'] = 'financial_information'
        elif 'late' in all_context and 'daily' in all_context:
            result['purpose'] = 'daily_late_fee'
            result['unique_id'] = 'daily_late_fee'
            result['display_name'] = 'Daily Late Fee'
            result['block'] = 'financial_information'
        elif 'late' in all_context:
            result['purpose'] = 'late_fee'
            result['unique_id'] = f'late_fee_{field_num}'
            result['display_name'] = 'Late Fee'
            result['block'] = 'financial_information'
        else:
            result['purpose'] = 'rent_amount'
            result['unique_id'] = f'rent_amount_{field_num}'
            result['display_name'] = 'Rent Amount'
            result['block'] = 'financial_information'
    
    elif 'security' in all_context and 'deposit' in all_context:
        result['purpose'] = 'security_deposit'
        result['unique_id'] = 'security_deposit'
        result['display_name'] = 'Security Deposit'
        result['block'] = 'financial_information'
    
    elif 'deposit' in all_context:
        if 'pet' in all_context:
            result['purpose'] = 'pet_deposit'
            result['unique_id'] = 'pet_deposit'
            result['display_name'] = 'Pet Deposit'
            result['block'] = 'financial_information'
        else:
            result['purpose'] = 'deposit'
            result['unique_id'] = f'deposit_{field_num}'
            result['display_name'] = 'Deposit'
            result['block'] = 'financial_information'
    
    elif '$' in all_context or 'amount' in all_context or 'fee' in all_context:
        result['purpose'] = 'monetary_amount'
        result['unique_id'] = f'amount_{field_num}_page_{page}'
        result['display_name'] = 'Amount'
        result['block'] = 'financial_information'
    
    # === DATES ===
    elif 'date' in all_context:
        if 'signature' in all_context:
            result['purpose'] = 'signature_date'
            result['unique_id'] = f'signature_date_page_{page}'
            result['display_name'] = 'Date'
            result['block'] = 'signatures'
        else:
            result['purpose'] = 'date_field'
            result['unique_id'] = f'date_{field_num}_page_{page}'
            result['display_name'] = 'Date'
            result['block'] = 'dates'
    
    # === CHECKBOXES ===
    elif field_type == 'CheckBox':
        if 'automatic' in all_context and 'renew' in all_context:
            result['purpose'] = 'automatic_renewal'
            result['unique_id'] = 'automatic_renewal'
            result['display_name'] = 'Automatic Renewal'
            result['block'] = 'lease_terms'
        elif 'month to month' in all_context or 'month-to-month' in all_context:
            result['purpose'] = 'month_to_month'
            result['unique_id'] = 'month_to_month'
            result['display_name'] = 'Month-to-Month'
            result['block'] = 'lease_terms'
        elif 'hoa' in all_context:
            result['purpose'] = 'hoa_property'
            result['unique_id'] = 'is_hoa_property'
            result['display_name'] = 'HOA Property'
            result['block'] = 'property_features'
        elif 'furnished' in all_context:
            result['purpose'] = 'furnished'
            result['unique_id'] = 'is_furnished'
            result['display_name'] = 'Furnished'
            result['block'] = 'property_features'
        elif 'pet' in all_context:
            result['purpose'] = 'pets_allowed'
            result['unique_id'] = 'pets_allowed'
            result['display_name'] = 'Pets Allowed'
            result['block'] = 'property_features'
        else:
            result['purpose'] = 'checkbox_option'
            result['unique_id'] = f'checkbox_{field_num}_page_{page}'
            result['display_name'] = 'Option'
            result['block'] = 'options'
    
    # === PROPERTY FEATURES ===
    elif 'parking' in all_context:
        result['purpose'] = 'parking_spaces'
        result['unique_id'] = 'parking_spaces'
        result['display_name'] = 'Parking Spaces'
        result['block'] = 'property_features'
    
    elif 'occupant' in all_context:
        result['purpose'] = 'occupant'
        result['unique_id'] = f'occupant_{field_num}'
        result['display_name'] = 'Occupant Name'
        result['block'] = 'occupants'
    
    # === CONTACT INFORMATION ===
    elif 'phone' in all_context and 'tenant' not in all_context and 'landlord' not in all_context:
        result['purpose'] = 'phone_number'
        result['unique_id'] = f'phone_{field_num}_page_{page}'
        result['display_name'] = 'Phone Number'
        result['block'] = 'contact_information'
    
    elif 'fax' in all_context and 'landlord' not in all_context:
        result['purpose'] = 'fax_number'
        result['unique_id'] = f'fax_{field_num}_page_{page}'
        result['display_name'] = 'Fax Number'
        result['block'] = 'contact_information'
    
    elif 'email' in all_context or 'e mail' in all_context:
        result['purpose'] = 'email_address'
        result['unique_id'] = f'email_{field_num}_page_{page}'
        result['display_name'] = 'Email Address'
        result['block'] = 'contact_information'
    
    # === SIGNATURES AND INITIALS ===
    elif 'signature' in all_context:
        result['purpose'] = 'signature'
        result['unique_id'] = f'signature_{field_num}_page_{page}'
        result['display_name'] = 'Signature'
        result['block'] = 'signatures'
    
    elif 'initial' in all_context:
        result['purpose'] = 'initial'
        result['unique_id'] = f'initial_{field_num}_page_{page}'
        result['display_name'] = 'Initial'
        result['block'] = 'signatures'
    
    # === DEFAULT ===
    else:
        result['purpose'] = 'unknown'
        result['unique_id'] = f'field_{field_num}_page_{page}'
        result['display_name'] = f'Field {field_num}'
        result['block'] = 'other'
    
    return result

def consolidate_fields(analyzed_fields):
    """Consolidate fields that represent the same data"""
    consolidated = defaultdict(list)
    
    # Group by unique_id
    for field_info in analyzed_fields:
        consolidated[field_info['unique_id']].append(field_info)
    
    return consolidated

def generate_final_schema():
    """Generate the final comprehensive TypeScript schema"""
    # Load fields
    with open('residential_lease_for_a_multi_family_property_unit___722_ts04618_unlocked_Fillable_fields_enhanced.json', 'r') as f:
        fields = json.load(f)
    
    print(f"Analyzing {len(fields)} fields...")
    
    # Analyze all fields
    analyzed_fields = []
    for field in fields:
        analysis = analyze_comprehensive_context(field)
        analyzed_fields.append(analysis)
    
    # Group by purpose for summary
    purpose_summary = defaultdict(int)
    for field in analyzed_fields:
        purpose_summary[field['purpose']] += 1
    
    print("\nField distribution by purpose:")
    for purpose, count in sorted(purpose_summary.items(), key=lambda x: x[1], reverse=True):
        print(f"  {purpose}: {count}")
    
    # Consolidate fields
    consolidated = consolidate_fields(analyzed_fields)
    
    print(f"\nConsolidated to {len(consolidated)} unique field groups")
    
    # Generate schema items
    schema_items = []
    order = 1
    
    # Define the order of blocks and fields
    field_order = [
        # Property Information
        ('property_address', 'property_information'),
        ('unit_number', 'property_information'),
        ('property_city', 'property_information'),
        ('property_county', 'property_information'),
        ('property_state', 'property_information'),
        ('property_zip', 'property_information'),
        
        # Landlord Information
        ('landlord_name', 'landlord_information'),
        ('landlord_phone', 'landlord_information'),
        ('landlord_email', 'landlord_information'),
        ('landlord_fax', 'landlord_information'),
        ('landlord_address', 'landlord_information'),
        
        # Tenant Information
        ('tenant_1_name', 'tenant_information'),
        ('tenant_phone', 'tenant_information'),
        ('tenant_email', 'tenant_information'),
        
        # Lease Terms
        ('lease_start_date', 'lease_terms'),
        ('lease_end_date', 'lease_terms'),
        ('automatic_renewal', 'lease_terms'),
        ('month_to_month', 'lease_terms'),
        ('notice_days', 'lease_terms'),
        
        # Financial Information
        ('monthly_rent', 'financial_information'),
        ('security_deposit', 'financial_information'),
        ('pet_deposit', 'financial_information'),
        ('initial_late_fee', 'financial_information'),
        ('daily_late_fee', 'financial_information'),
        
        # Property Features
        ('is_hoa_property', 'property_features'),
        ('is_furnished', 'property_features'),
        ('pets_allowed', 'property_features'),
        ('parking_spaces', 'property_features'),
    ]
    
    # Block styles
    block_styles = {
        'property_information': {
            'title': 'Property Information',
            'icon': 'home',
            'color_theme': 'blue'
        },
        'landlord_information': {
            'title': 'Landlord Information',
            'icon': 'user',
            'color_theme': 'green'
        },
        'tenant_information': {
            'title': 'Tenant Information',
            'icon': 'users',
            'color_theme': 'green'
        },
        'lease_terms': {
            'title': 'Lease Terms',
            'icon': 'calendar',
            'color_theme': 'purple'
        },
        'financial_information': {
            'title': 'Financial Information',
            'icon': 'dollar-sign',
            'color_theme': 'orange'
        },
        'property_features': {
            'title': 'Property Features',
            'icon': 'home',
            'color_theme': 'blue'
        },
        'signatures': {
            'title': 'Signatures',
            'icon': 'pen-tool',
            'color_theme': 'gray'
        }
    }
    
    # Track which block styles have been added
    blocks_added = set()
    
    # Process fields in order
    for field_id, expected_block in field_order:
        if field_id in consolidated:
            field_group = consolidated[field_id]
            first_field = field_group[0]
            
            # Create schema item
            schema_item = {
                "unique_id": field_id,
                "pdf_attributes": [],
                "display_attributes": {
                    "display_name": first_field['display_name'],
                    "input_type": "text",  # Default
                    "order": order,
                    "block": expected_block,
                    "value": {"type": "manual"}
                }
            }
            
            # Add all PDF field mappings
            for field_info in field_group:
                schema_item["pdf_attributes"].append({
                    "formType": "residential_lease_for_a_multi_family_property_unit",
                    "formfield": field_info['field_name']
                })
            
            # Add block style for first item in each block
            if expected_block not in blocks_added and expected_block in block_styles:
                schema_item["display_attributes"]["block_style"] = block_styles[expected_block]
                blocks_added.add(expected_block)
            
            # Set field-specific properties
            if field_id == 'property_address':
                schema_item["display_attributes"]["width"] = 9
                schema_item["display_attributes"]["placeholder"] = "123 Main Street"
            
            elif field_id == 'unit_number':
                schema_item["display_attributes"]["width"] = 3
                schema_item["display_attributes"]["placeholder"] = "Unit 101"
            
            elif field_id == 'property_city':
                schema_item["display_attributes"]["width"] = 6
                schema_item["display_attributes"]["placeholder"] = "Houston"
            
            elif field_id == 'property_county':
                schema_item["display_attributes"]["width"] = 4
                schema_item["display_attributes"]["placeholder"] = "Harris"
            
            elif field_id == 'property_state':
                schema_item["display_attributes"]["width"] = 2
                schema_item["display_attributes"]["placeholder"] = "TX"
            
            elif field_id == 'property_zip':
                schema_item["display_attributes"]["width"] = 4
                schema_item["display_attributes"]["placeholder"] = "77001"
            
            elif field_id in ['landlord_name', 'tenant_1_name']:
                schema_item["display_attributes"]["width"] = 6
                schema_item["display_attributes"]["placeholder"] = "John Doe"
            
            elif field_id in ['landlord_phone', 'tenant_phone']:
                schema_item["display_attributes"]["width"] = 4
                schema_item["display_attributes"]["placeholder"] = "(555) 123-4567"
                schema_item["display_attributes"]["validation"] = {
                    "loopback": [{
                        "regex": "^[-()\\s\\d]{10,}$",
                        "message": "Must be a valid phone number"
                    }]
                }
                schema_item["display_attributes"]["special_input"] = {
                    "text": {"phone": True}
                }
            
            elif field_id in ['landlord_email', 'tenant_email']:
                schema_item["display_attributes"]["width"] = 6
                schema_item["display_attributes"]["placeholder"] = "email@example.com"
                schema_item["display_attributes"]["validation"] = {
                    "loopback": [{
                        "regex": "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$",
                        "message": "Must be a valid email address"
                    }]
                }
                schema_item["display_attributes"]["special_input"] = {
                    "text": {"email": True}
                }
            
            elif field_id == 'landlord_fax':
                schema_item["display_attributes"]["width"] = 4
                schema_item["display_attributes"]["placeholder"] = "(555) 123-4568"
                schema_item["display_attributes"]["validation"] = {
                    "loopback": [{
                        "regex": "^[-()\\s\\d]{10,}$",
                        "message": "Must be a valid fax number"
                    }]
                }
                schema_item["display_attributes"]["special_input"] = {
                    "text": {"phone": True}
                }
            
            elif field_id == 'landlord_address':
                schema_item["display_attributes"]["width"] = 12
                schema_item["display_attributes"]["placeholder"] = "456 Oak Avenue, Houston, TX 77001"
            
            elif field_id in ['lease_start_date', 'lease_end_date']:
                schema_item["display_attributes"]["width"] = 4
                schema_item["display_attributes"]["placeholder"] = "01/01/2024"
                schema_item["display_attributes"]["validation"] = {
                    "loopback": [{
                        "regex": "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
                        "message": "Must be a valid date (MM/DD/YYYY)"
                    }]
                }
                schema_item["display_attributes"]["special_input"] = {
                    "text": {"date": True}
                }
                
                if field_id == 'lease_end_date':
                    schema_item["display_attributes"]["validation"]["crossField"] = [{
                        "rule": ">",
                        "unique_id": "lease_start_date",
                        "message": "End date must be after start date"
                    }]
            
            elif field_id in ['automatic_renewal', 'month_to_month']:
                # Handle as combined checkbox for lease renewal
                if field_id == 'automatic_renewal':
                    schema_item["unique_id"] = "lease_renewal_type"
                    schema_item["display_attributes"]["display_name"] = "Lease Renewal Type"
                    schema_item["display_attributes"]["input_type"] = "checkbox"
                    schema_item["display_attributes"]["width"] = 12
                    schema_item["display_attributes"]["checkbox_options"] = {
                        "options": [
                            {"display_name": "Automatic Renewal", "databaseStored": "AUTOMATIC_RENEWAL"},
                            {"display_name": "Month-to-Month", "databaseStored": "MONTH_TO_MONTH"}
                        ],
                        "maxSelected": 1,
                        "minSelected": 1
                    }
                    
                    # Add month-to-month fields to pdf_attributes
                    if 'month_to_month' in consolidated:
                        for field_info in consolidated['month_to_month']:
                            schema_item["pdf_attributes"].append({
                                "formType": "residential_lease_for_a_multi_family_property_unit",
                                "formfield": field_info['field_name']
                            })
                else:
                    continue  # Skip month_to_month as it's included above
            
            elif field_id == 'notice_days':
                schema_item["display_attributes"]["width"] = 4
                schema_item["display_attributes"]["placeholder"] = "30"
                schema_item["display_attributes"]["validation"] = {
                    "loopback": [{
                        "regex": "^\\d+$",
                        "message": "Must be a number"
                    }]
                }
                schema_item["display_attributes"]["special_input"] = {
                    "text": {"number": True}
                }
            
            elif field_id in ['monthly_rent', 'security_deposit', 'pet_deposit', 'initial_late_fee', 'daily_late_fee']:
                schema_item["display_attributes"]["width"] = 4
                schema_item["display_attributes"]["placeholder"] = "$0.00"
                schema_item["display_attributes"]["validation"] = {
                    "loopback": [{
                        "regex": "^[\\d.,$]+$",
                        "message": "Must be a valid monetary amount"
                    }]
                }
                schema_item["display_attributes"]["special_input"] = {
                    "text": {"currency": True}
                }
            
            elif field_id in ['is_hoa_property', 'is_furnished', 'pets_allowed']:
                schema_item["display_attributes"]["input_type"] = "checkbox"
                schema_item["display_attributes"]["width"] = 6
                schema_item["display_attributes"]["checkbox_options"] = {
                    "options": [
                        {"display_name": first_field['display_name'], "databaseStored": field_id.upper()}
                    ]
                }
            
            elif field_id == 'parking_spaces':
                schema_item["display_attributes"]["width"] = 3
                schema_item["display_attributes"]["placeholder"] = "2"
                schema_item["display_attributes"]["validation"] = {
                    "loopback": [{
                        "regex": "^\\d+$",
                        "message": "Must be a number"
                    }]
                }
                schema_item["display_attributes"]["special_input"] = {
                    "text": {"number": True}
                }
            
            schema_items.append(schema_item)
            order += 1
    
    # Add signature fields
    signature_fields = []
    initial_fields = []
    
    for unique_id in sorted(consolidated.keys()):
        if 'signature' in unique_id and 'date' not in unique_id:
            signature_fields.append(unique_id)
        elif 'initial' in unique_id:
            initial_fields.append(unique_id)
    
    # Process signatures
    landlord_sig_count = 1
    tenant_sig_count = 1
    
    for sig_id in signature_fields:
        field_group = consolidated[sig_id]
        first_field = field_group[0]
        
        if 'landlord' in sig_id:
            display_name = f"Landlord Signature"
            unique_id = f"landlord_signature_{landlord_sig_count}"
            landlord_sig_count += 1
        elif 'tenant' in sig_id:
            display_name = f"Tenant {tenant_sig_count} Signature"
            unique_id = f"tenant_{tenant_sig_count}_signature"
            tenant_sig_count += 1
        else:
            display_name = "Signature"
            unique_id = sig_id
        
        schema_item = {
            "unique_id": unique_id,
            "pdf_attributes": [],
            "display_attributes": {
                "display_name": display_name,
                "input_type": "signature",
                "order": order,
                "block": "signatures",
                "width": 6,
                "value": {
                    "type": "manual",
                    "output": "SignatureInput__signer"
                }
            }
        }
        
        # Add block style for first signature
        if 'signatures' not in blocks_added:
            schema_item["display_attributes"]["block_style"] = block_styles['signatures']
            blocks_added.add('signatures')
        
        # Add all PDF field mappings
        for field_info in field_group:
            pdf_attr = {
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field_info['field_name']
            }
            
            # Try to find linked date field
            page = field_info['page']
            date_field_id = f'signature_date_page_{page}'
            if date_field_id in consolidated:
                date_fields = consolidated[date_field_id]
                if date_fields:
                    pdf_attr["linked_dates"] = [{"dateFieldName": date_fields[0]['field_name']}]
            
            schema_item["pdf_attributes"].append(pdf_attr)
        
        schema_items.append(schema_item)
        order += 1
    
    # Process initials
    landlord_init_count = 1
    tenant_init_count = 1
    
    for init_id in initial_fields:
        field_group = consolidated[init_id]
        first_field = field_group[0]
        
        if 'landlord' in init_id:
            display_name = f"Landlord Initials"
            unique_id = f"landlord_initials_{landlord_init_count}"
            landlord_init_count += 1
        elif 'tenant' in init_id:
            display_name = f"Tenant {tenant_init_count} Initials"
            unique_id = f"tenant_{tenant_init_count}_initials"
            tenant_init_count += 1
        else:
            display_name = "Initials"
            unique_id = init_id
        
        schema_item = {
            "unique_id": unique_id,
            "pdf_attributes": [],
            "display_attributes": {
                "display_name": display_name,
                "input_type": "signature",
                "order": order,
                "block": "signatures",
                "width": 3,
                "value": {
                    "type": "manual",
                    "output": "SignatureInput__signer"
                }
            }
        }
        
        # Add all PDF field mappings
        for field_info in field_group:
            schema_item["pdf_attributes"].append({
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field_info['field_name']
            })
        
        schema_items.append(schema_item)
        order += 1
    
    print(f"\nGenerated {len(schema_items)} schema items")
    
    return schema_items

def write_typescript_schema(schema_items):
    """Write the final TypeScript schema file"""
    typescript_content = '''import { SchemaItem } from "../../../../types/realtor";

export const residentialLeaseMultiFamilySchema: SchemaItem[] = '''
    
    typescript_content += json.dumps(schema_items, indent=2)
    typescript_content += ";\n"
    
    with open('residential_lease_multi_family_schema.ts', 'w') as f:
        f.write(typescript_content)
    
    print("Schema saved to: residential_lease_multi_family_schema.ts")

if __name__ == "__main__":
    schema_items = generate_final_schema()
    write_typescript_schema(schema_items)