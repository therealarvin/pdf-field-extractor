#!/usr/bin/env python3
import json
import re
from collections import defaultdict, OrderedDict

def clean_context(text):
    """Clean context text by adding spaces between words"""
    if not text:
        return ""
    # Add spaces before capital letters
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    # Clean up multiple spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def analyze_field_context(field):
    """Deep analysis of field context to determine purpose"""
    contexts = {
        'left': clean_context(field.get('context_left', '')),
        'right': clean_context(field.get('context_right', '')),
        'above': clean_context(field.get('context_above', '')),
        'below': clean_context(field.get('context_below', ''))
    }
    
    all_context = ' '.join(contexts.values()).lower()
    field_name = field['field_name']
    field_type = field['field_type']
    page = field['page']
    
    # Return tuple of (purpose, unique_id, display_name)
    
    # Property Information
    if 'address' in all_context and 'in' in contexts['left'].lower():
        return 'property_address', 'property_address', 'Property Address'
    elif 'unit' in all_context and ('number' in all_context or field_name.endswith('_5')):
        return 'unit_number', 'unit_number', 'Unit Number'
    elif 'county' in all_context and 'texas' in all_context:
        return 'property_county', 'property_county', 'County'
    
    # Landlord fields
    elif 'landlord' in all_context or 'owner' in all_context:
        if field_name.endswith('_1') and page == 0:
            return 'landlord_name', 'landlord_name', 'Landlord Name'
        elif 'phone' in all_context:
            return 'landlord_phone', 'landlord_phone', 'Landlord Phone'
        elif 'email' in all_context or 'e-mail' in all_context:
            return 'landlord_email', 'landlord_email', 'Landlord Email'
        elif 'fax' in all_context:
            return 'landlord_fax', 'landlord_fax', 'Landlord Fax'
        elif 'address' in all_context:
            return 'landlord_address', 'landlord_address', 'Landlord Address'
        elif 'signature' in all_context:
            return 'landlord_signature', f'landlord_signature_page_{page}', 'Landlord Signature'
        elif 'initial' in all_context:
            return 'landlord_initial', f'landlord_initial_page_{page}', 'Landlord Initial'
        else:
            return 'landlord_info', f'landlord_field_{field_name.split("_")[-1]}', 'Landlord Information'
    
    # Tenant fields
    elif 'tenant' in all_context:
        if field_name.endswith('_3') and page == 0:
            return 'tenant_name', 'tenant_1_name', 'Tenant 1 Name'
        elif 'name' in all_context:
            return 'tenant_name', f'tenant_name_{field_name}', 'Tenant Name'
        elif 'phone' in all_context:
            return 'tenant_phone', 'tenant_phone', 'Tenant Phone'
        elif 'email' in all_context:
            return 'tenant_email', 'tenant_email', 'Tenant Email'
        elif 'signature' in all_context:
            return 'tenant_signature', f'tenant_signature_page_{page}', 'Tenant Signature'
        elif 'initial' in all_context:
            return 'tenant_initial', f'tenant_initial_page_{page}', 'Tenant Initial'
        else:
            return 'tenant_info', f'tenant_field_{field_name.split("_")[-1]}', 'Tenant Information'
    
    # Date fields
    elif 'commencement' in all_context and 'date' in all_context:
        return 'lease_start_date', 'lease_start_date', 'Lease Start Date'
    elif 'expiration' in all_context and 'date' in all_context:
        return 'lease_end_date', 'lease_end_date', 'Lease End Date'
    elif 'date' in all_context and 'signature' in all_context:
        return 'signature_date', f'signature_date_page_{page}', 'Date'
    
    # Financial fields
    elif 'rent' in all_context:
        if 'monthly' in all_context or 'per month' in all_context:
            return 'monthly_rent', 'monthly_rent', 'Monthly Rent'
        elif 'late' in all_context and 'initial' in all_context:
            return 'initial_late_fee', 'initial_late_fee', 'Initial Late Fee'
        elif 'late' in all_context and 'daily' in all_context:
            return 'daily_late_fee', 'daily_late_fee', 'Daily Late Fee'
        elif 'late' in all_context:
            return 'late_fee', 'late_fee', 'Late Fee'
    elif 'security' in all_context and 'deposit' in all_context:
        return 'security_deposit', 'security_deposit', 'Security Deposit'
    elif 'pet' in all_context and ('deposit' in all_context or 'fee' in all_context):
        return 'pet_deposit', 'pet_deposit', 'Pet Deposit'
    elif '$' in all_context or 'amount' in all_context:
        return 'monetary_amount', f'amount_{page}_{field_name.split("_")[-1]}', 'Amount'
    
    # Checkboxes
    elif field_type == 'CheckBox':
        if 'automatic' in all_context and 'renew' in all_context:
            return 'automatic_renewal', 'automatic_renewal', 'Automatic Renewal'
        elif 'month-to-month' in all_context:
            return 'month_to_month', 'month_to_month', 'Month-to-Month'
        elif 'hoa' in all_context:
            return 'hoa_property', 'is_hoa_property', 'HOA Property'
        elif 'furnished' in all_context:
            return 'furnished', 'is_furnished', 'Furnished'
        elif 'unfurnished' in all_context:
            return 'unfurnished', 'is_unfurnished', 'Unfurnished'
        else:
            return 'checkbox', f'checkbox_{page}_{field_name.split("_")[-1]}', 'Option'
    
    # Special fields
    elif 'parking' in all_context:
        return 'parking', 'parking_spaces', 'Parking Spaces'
    elif 'notice' in all_context and 'days' in all_context:
        return 'notice_days', 'notice_days', 'Notice Days'
    elif 'occupant' in all_context and 'name' in all_context:
        return 'occupant', f'occupant_{field_name.split("_")[-1]}', 'Occupant Name'
    
    # Default
    else:
        return 'unknown', f'field_{page}_{field_name.split("_")[-1]}', 'Field'
    
    # This should never be reached, but just in case
    return 'unknown', f'field_{page}_{field_name.split("_")[-1]}', 'Field'

def generate_comprehensive_schema():
    """Generate a comprehensive TypeScript schema"""
    with open('residential_lease_for_a_multi_family_property_unit___722_ts04618_unlocked_Fillable_fields_enhanced.json', 'r') as f:
        fields = json.load(f)
    
    print(f"Processing {len(fields)} fields...")
    
    # Analyze all fields
    analyzed_fields = []
    field_groups = defaultdict(list)
    
    for field in fields:
        purpose, unique_id, display_name = analyze_field_context(field)
        field_info = {
            'field': field,
            'purpose': purpose,
            'unique_id': unique_id,
            'display_name': display_name
        }
        analyzed_fields.append(field_info)
        field_groups[unique_id].append(field)
    
    # Generate schema items
    schema_items = []
    order = 1
    processed_ids = set()
    
    # Property Information Block
    property_fields = ['property_address', 'unit_number', 'property_county']
    for field_id in property_fields:
        if field_id in field_groups and field_id not in processed_ids:
            fields_list = field_groups[field_id]
            field_info = next((f for f in analyzed_fields if f['unique_id'] == field_id), None)
            if field_info:
                schema_item = {
                    "unique_id": field_id,
                    "pdf_attributes": [
                        {
                            "formType": "residential_lease_for_a_multi_family_property_unit",
                            "formfield": f['field_name']
                        } for f in fields_list
                    ],
                    "display_attributes": {
                        "display_name": field_info['display_name'],
                        "input_type": "text",
                        "order": order,
                        "block": "property_information",
                        "value": {"type": "manual"}
                    }
                }
                
                # Add block style for first item
                if order == 1:
                    schema_item["display_attributes"]["block_style"] = {
                        "title": "Property Information",
                        "icon": "home",
                        "color_theme": "blue"
                    }
                
                # Set widths
                if field_id == 'property_address':
                    schema_item["display_attributes"]["width"] = 9
                    schema_item["display_attributes"]["placeholder"] = "123 Main Street"
                elif field_id == 'unit_number':
                    schema_item["display_attributes"]["width"] = 3
                    schema_item["display_attributes"]["placeholder"] = "Unit 101"
                elif field_id == 'property_county':
                    schema_item["display_attributes"]["width"] = 6
                    schema_item["display_attributes"]["placeholder"] = "Harris"
                
                schema_items.append(schema_item)
                processed_ids.add(field_id)
                order += 1
    
    # Landlord Information Block
    landlord_fields = ['landlord_name', 'landlord_phone', 'landlord_email', 'landlord_fax', 'landlord_address']
    for field_id in landlord_fields:
        if field_id in field_groups and field_id not in processed_ids:
            fields_list = field_groups[field_id]
            field_info = next((f for f in analyzed_fields if f['unique_id'] == field_id), None)
            if field_info:
                schema_item = {
                    "unique_id": field_id,
                    "pdf_attributes": [
                        {
                            "formType": "residential_lease_for_a_multi_family_property_unit",
                            "formfield": f['field_name']
                        } for f in fields_list
                    ],
                    "display_attributes": {
                        "display_name": field_info['display_name'],
                        "input_type": "text",
                        "order": order,
                        "block": "landlord_information",
                        "value": {"type": "manual"}
                    }
                }
                
                # Add block style for first landlord item
                if field_id == 'landlord_name':
                    schema_item["display_attributes"]["block_style"] = {
                        "title": "Landlord Information",
                        "icon": "user",
                        "color_theme": "green"
                    }
                
                # Set field-specific properties
                if field_id == 'landlord_name':
                    schema_item["display_attributes"]["width"] = 6
                    schema_item["display_attributes"]["placeholder"] = "John Doe"
                elif field_id == 'landlord_phone':
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
                elif field_id == 'landlord_email':
                    schema_item["display_attributes"]["width"] = 6
                    schema_item["display_attributes"]["placeholder"] = "landlord@example.com"
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
                
                schema_items.append(schema_item)
                processed_ids.add(field_id)
                order += 1
    
    # Tenant Information Block
    tenant_fields = ['tenant_1_name', 'tenant_phone', 'tenant_email']
    for field_id in tenant_fields:
        if field_id in field_groups and field_id not in processed_ids:
            fields_list = field_groups[field_id]
            field_info = next((f for f in analyzed_fields if f['unique_id'] == field_id), None)
            if field_info:
                schema_item = {
                    "unique_id": field_id,
                    "pdf_attributes": [
                        {
                            "formType": "residential_lease_for_a_multi_family_property_unit",
                            "formfield": f['field_name']
                        } for f in fields_list
                    ],
                    "display_attributes": {
                        "display_name": field_info['display_name'],
                        "input_type": "text",
                        "order": order,
                        "block": "tenant_information",
                        "value": {"type": "manual"}
                    }
                }
                
                # Add block style for first tenant item
                if field_id == 'tenant_1_name':
                    schema_item["display_attributes"]["block_style"] = {
                        "title": "Tenant Information",
                        "icon": "users",
                        "color_theme": "green"
                    }
                
                # Set field-specific properties
                if field_id == 'tenant_1_name':
                    schema_item["display_attributes"]["width"] = 6
                    schema_item["display_attributes"]["placeholder"] = "Jane Smith"
                elif field_id == 'tenant_phone':
                    schema_item["display_attributes"]["width"] = 4
                    schema_item["display_attributes"]["placeholder"] = "(555) 987-6543"
                    schema_item["display_attributes"]["validation"] = {
                        "loopback": [{
                            "regex": "^[-()\\s\\d]{10,}$",
                            "message": "Must be a valid phone number"
                        }]
                    }
                    schema_item["display_attributes"]["special_input"] = {
                        "text": {"phone": True}
                    }
                elif field_id == 'tenant_email':
                    schema_item["display_attributes"]["width"] = 6
                    schema_item["display_attributes"]["placeholder"] = "tenant@example.com"
                    schema_item["display_attributes"]["validation"] = {
                        "loopback": [{
                            "regex": "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$",
                            "message": "Must be a valid email address"
                        }]
                    }
                    schema_item["display_attributes"]["special_input"] = {
                        "text": {"email": True}
                    }
                
                schema_items.append(schema_item)
                processed_ids.add(field_id)
                order += 1
    
    # Additional Tenants
    tenant_count = 2
    for unique_id in sorted(field_groups.keys()):
        if unique_id.startswith('tenant_name_') and unique_id not in processed_ids:
            fields_list = field_groups[unique_id]
            schema_item = {
                "unique_id": f"tenant_{tenant_count}_name",
                "pdf_attributes": [
                    {
                        "formType": "residential_lease_for_a_multi_family_property_unit",
                        "formfield": f['field_name']
                    } for f in fields_list
                ],
                "display_attributes": {
                    "display_name": f"Tenant {tenant_count} Name",
                    "input_type": "text",
                    "order": order,
                    "block": "tenant_information",
                    "width": 6,
                    "placeholder": "Additional Tenant",
                    "value": {"type": "manual"}
                }
            }
            schema_items.append(schema_item)
            processed_ids.add(unique_id)
            order += 1
            tenant_count += 1
            if tenant_count > 4:  # Limit to 4 tenants
                break
    
    # Lease Terms Block
    lease_fields = ['lease_start_date', 'lease_end_date', 'automatic_renewal', 'month_to_month', 'notice_days']
    for field_id in lease_fields:
        if field_id in field_groups and field_id not in processed_ids:
            fields_list = field_groups[field_id]
            field_info = next((f for f in analyzed_fields if f['unique_id'] == field_id), None)
            if field_info:
                if field_id in ['automatic_renewal', 'month_to_month']:
                    # Handle as checkboxes
                    if field_id == 'automatic_renewal':
                        schema_item = {
                            "unique_id": "lease_renewal_type",
                            "pdf_attributes": [{
                                "formType": "residential_lease_for_a_multi_family_property_unit",
                                "formfield": "lease_renewal_options",
                                "linked_form_fields_checkbox": [
                                    {
                                        "fromDatabase": "AUTOMATIC_RENEWAL",
                                        "pdfAttribute": fields_list[0]['field_name']
                                    },
                                    {
                                        "fromDatabase": "MONTH_TO_MONTH",
                                        "pdfAttribute": field_groups.get('month_to_month', [{}])[0].get('field_name', '')
                                    }
                                ]
                            }],
                            "display_attributes": {
                                "display_name": "Lease Renewal Type",
                                "input_type": "checkbox",
                                "order": order,
                                "block": "lease_terms",
                                "block_style": {
                                    "title": "Lease Terms",
                                    "icon": "calendar",
                                    "color_theme": "purple"
                                },
                                "width": 12,
                                "checkbox_options": {
                                    "options": [
                                        {"display_name": "Automatic Renewal", "databaseStored": "AUTOMATIC_RENEWAL"},
                                        {"display_name": "Month-to-Month", "databaseStored": "MONTH_TO_MONTH"}
                                    ],
                                    "maxSelected": 1,
                                    "minSelected": 1
                                },
                                "value": {"type": "manual"}
                            }
                        }
                        schema_items.append(schema_item)
                        processed_ids.add('automatic_renewal')
                        processed_ids.add('month_to_month')
                        order += 1
                else:
                    # Handle as text fields
                    schema_item = {
                        "unique_id": field_id,
                        "pdf_attributes": [
                            {
                                "formType": "residential_lease_for_a_multi_family_property_unit",
                                "formfield": f['field_name']
                            } for f in fields_list
                        ],
                        "display_attributes": {
                            "display_name": field_info['display_name'],
                            "input_type": "text",
                            "order": order,
                            "block": "lease_terms",
                            "value": {"type": "manual"}
                        }
                    }
                    
                    # Add block style for first lease term item
                    if field_id == 'lease_start_date':
                        schema_item["display_attributes"]["block_style"] = {
                            "title": "Lease Terms",
                            "icon": "calendar",
                            "color_theme": "purple"
                        }
                    
                    # Set field-specific properties
                    if field_id == 'lease_start_date':
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
                    elif field_id == 'lease_end_date':
                        schema_item["display_attributes"]["width"] = 4
                        schema_item["display_attributes"]["placeholder"] = "12/31/2024"
                        schema_item["display_attributes"]["validation"] = {
                            "loopback": [{
                                "regex": "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
                                "message": "Must be a valid date (MM/DD/YYYY)"
                            }],
                            "crossField": [{
                                "rule": ">",
                                "unique_id": "lease_start_date",
                                "message": "End date must be after start date"
                            }]
                        }
                        schema_item["display_attributes"]["special_input"] = {
                            "text": {"date": True}
                        }
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
                    
                    schema_items.append(schema_item)
                    processed_ids.add(field_id)
                    order += 1
    
    # Financial Information Block
    financial_fields = ['monthly_rent', 'security_deposit', 'pet_deposit', 'initial_late_fee', 'daily_late_fee']
    for field_id in financial_fields:
        if field_id in field_groups and field_id not in processed_ids:
            fields_list = field_groups[field_id]
            field_info = next((f for f in analyzed_fields if f['unique_id'] == field_id), None)
            if field_info:
                schema_item = {
                    "unique_id": field_id,
                    "pdf_attributes": [
                        {
                            "formType": "residential_lease_for_a_multi_family_property_unit",
                            "formfield": f['field_name']
                        } for f in fields_list
                    ],
                    "display_attributes": {
                        "display_name": field_info['display_name'],
                        "input_type": "text",
                        "order": order,
                        "block": "financial_information",
                        "width": 4,
                        "validation": {
                            "loopback": [{
                                "regex": "^[\\d.,$]+$",
                                "message": "Must be a valid monetary amount"
                            }]
                        },
                        "special_input": {
                            "text": {"currency": True}
                        },
                        "value": {"type": "manual"}
                    }
                }
                
                # Add block style for first financial item
                if field_id == 'monthly_rent':
                    schema_item["display_attributes"]["block_style"] = {
                        "title": "Financial Information",
                        "icon": "dollar-sign",
                        "color_theme": "orange"
                    }
                
                # Set placeholders
                if field_id == 'monthly_rent':
                    schema_item["display_attributes"]["placeholder"] = "$2,500.00"
                elif field_id == 'security_deposit':
                    schema_item["display_attributes"]["placeholder"] = "$2,500.00"
                elif field_id == 'pet_deposit':
                    schema_item["display_attributes"]["placeholder"] = "$500.00"
                elif field_id == 'initial_late_fee':
                    schema_item["display_attributes"]["placeholder"] = "$50.00"
                elif field_id == 'daily_late_fee':
                    schema_item["display_attributes"]["placeholder"] = "$10.00"
                
                schema_items.append(schema_item)
                processed_ids.add(field_id)
                order += 1
    
    # Property Features Block
    feature_fields = ['is_hoa_property', 'parking_spaces', 'is_furnished', 'is_unfurnished']
    for field_id in feature_fields:
        if field_id in field_groups and field_id not in processed_ids:
            fields_list = field_groups[field_id]
            field_info = next((f for f in analyzed_fields if f['unique_id'] == field_id), None)
            if field_info:
                if field_id in ['is_hoa_property', 'is_furnished', 'is_unfurnished']:
                    # Handle as checkboxes
                    schema_item = {
                        "unique_id": field_id,
                        "pdf_attributes": [
                            {
                                "formType": "residential_lease_for_a_multi_family_property_unit",
                                "formfield": f['field_name']
                            } for f in fields_list
                        ],
                        "display_attributes": {
                            "display_name": field_info['display_name'],
                            "input_type": "checkbox",
                            "order": order,
                            "block": "property_features",
                            "width": 6,
                            "checkbox_options": {
                                "options": [
                                    {"display_name": field_info['display_name'], "databaseStored": field_id.upper()}
                                ]
                            },
                            "value": {"type": "manual"}
                        }
                    }
                else:
                    # Handle as text field
                    schema_item = {
                        "unique_id": field_id,
                        "pdf_attributes": [
                            {
                                "formType": "residential_lease_for_a_multi_family_property_unit",
                                "formfield": f['field_name']
                            } for f in fields_list
                        ],
                        "display_attributes": {
                            "display_name": field_info['display_name'],
                            "input_type": "text",
                            "order": order,
                            "block": "property_features",
                            "width": 3,
                            "placeholder": "2",
                            "validation": {
                                "loopback": [{
                                    "regex": "^\\d+$",
                                    "message": "Must be a number"
                                }]
                            },
                            "special_input": {
                                "text": {"number": True}
                            },
                            "value": {"type": "manual"}
                        }
                    }
                
                # Add block style for first feature item
                if order == len(schema_items) + 1:  # First item in this block
                    schema_item["display_attributes"]["block_style"] = {
                        "title": "Property Features",
                        "icon": "home",
                        "color_theme": "blue"
                    }
                
                schema_items.append(schema_item)
                processed_ids.add(field_id)
                order += 1
    
    # Signatures Block
    # Process all signature fields
    signature_fields = []
    for unique_id in sorted(field_groups.keys()):
        if 'signature' in unique_id and unique_id not in processed_ids:
            signature_fields.append(unique_id)
    
    # Group by party and page
    landlord_sigs = []
    tenant_sigs = []
    
    for sig_field in signature_fields:
        if 'landlord' in sig_field:
            landlord_sigs.append(sig_field)
        elif 'tenant' in sig_field:
            tenant_sigs.append(sig_field)
    
    # Add landlord signatures
    for i, sig_id in enumerate(sorted(landlord_sigs)):
        fields_list = field_groups[sig_id]
        page = sig_id.split('_')[-1]
        
        # Find corresponding date field
        date_field_id = f'signature_date_page_{page}'
        date_fields = field_groups.get(date_field_id, [])
        
        schema_item = {
            "unique_id": f"landlord_signature_{i+1}",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": f['field_name']
            } for f in fields_list],
            "display_attributes": {
                "display_name": "Landlord Signature",
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
        
        # Add linked date if found
        if date_fields:
            schema_item["pdf_attributes"][0]["linked_dates"] = [
                {"dateFieldName": date_fields[0]['field_name']}
            ]
        
        # Add block style for first signature
        if i == 0:
            schema_item["display_attributes"]["block_style"] = {
                "title": "Signatures",
                "icon": "pen-tool",
                "color_theme": "gray"
            }
        
        schema_items.append(schema_item)
        processed_ids.add(sig_id)
        order += 1
    
    # Add tenant signatures
    for i, sig_id in enumerate(sorted(tenant_sigs)):
        fields_list = field_groups[sig_id]
        page = sig_id.split('_')[-1]
        
        # Find corresponding date field
        date_field_id = f'signature_date_page_{page}'
        date_fields = field_groups.get(date_field_id, [])
        
        schema_item = {
            "unique_id": f"tenant_{i+1}_signature",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": f['field_name']
            } for f in fields_list],
            "display_attributes": {
                "display_name": f"Tenant {i+1} Signature",
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
        
        # Add linked date if found
        if date_fields:
            schema_item["pdf_attributes"][0]["linked_dates"] = [
                {"dateFieldName": date_fields[0]['field_name']}
            ]
        
        schema_items.append(schema_item)
        processed_ids.add(sig_id)
        order += 1
    
    # Process initials
    initial_fields = []
    for unique_id in sorted(field_groups.keys()):
        if 'initial' in unique_id and unique_id not in processed_ids:
            initial_fields.append(unique_id)
    
    # Add landlord initials
    landlord_initials = [f for f in initial_fields if 'landlord' in f]
    for i, init_id in enumerate(sorted(landlord_initials)):
        fields_list = field_groups[init_id]
        
        schema_item = {
            "unique_id": f"landlord_initials_{i+1}",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": f['field_name']
            } for f in fields_list],
            "display_attributes": {
                "display_name": "Landlord Initials",
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
        
        schema_items.append(schema_item)
        processed_ids.add(init_id)
        order += 1
    
    # Add tenant initials
    tenant_initials = [f for f in initial_fields if 'tenant' in f]
    for i, init_id in enumerate(sorted(tenant_initials)):
        fields_list = field_groups[init_id]
        
        schema_item = {
            "unique_id": f"tenant_{i+1}_initials",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": f['field_name']
            } for f in fields_list],
            "display_attributes": {
                "display_name": f"Tenant {i+1} Initials",
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
        
        schema_items.append(schema_item)
        processed_ids.add(init_id)
        order += 1
    
    print(f"\nGenerated {len(schema_items)} schema items from {len(fields)} fields")
    print(f"Processed {len(processed_ids)} unique field groups")
    print(f"Unprocessed field groups: {len(field_groups) - len(processed_ids)}")
    
    return schema_items

def write_typescript_file(schema_items):
    """Write the TypeScript schema file"""
    typescript_content = '''import { SchemaItem } from "../../../../types/realtor";

export const residentialLeaseMultiFamilySchema: SchemaItem[] = '''
    
    typescript_content += json.dumps(schema_items, indent=2)
    typescript_content += ";\n"
    
    with open('residential_lease_multi_family_schema.ts', 'w') as f:
        f.write(typescript_content)
    
    print(f"\nSaved TypeScript schema to: residential_lease_multi_family_schema.ts")

if __name__ == "__main__":
    schema_items = generate_comprehensive_schema()
    write_typescript_file(schema_items)