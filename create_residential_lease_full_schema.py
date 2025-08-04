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

def analyze_all_fields():
    """Comprehensive field analysis"""
    with open('residential_lease_for_a_multi_family_property_unit___722_ts04618_unlocked_Fillable_fields_enhanced.json', 'r') as f:
        fields = json.load(f)
    
    analyzed_fields = []
    for field in fields:
        all_context = ' '.join([
            clean_context(field.get('context_left', '')),
            clean_context(field.get('context_right', '')),
            clean_context(field.get('context_above', '')),
            clean_context(field.get('context_below', ''))
        ]).lower()
        
        # Detailed field analysis
        semantic_info = {
            'field': field,
            'all_context': all_context,
            'page': field['page'],
            'type': field['field_type']
        }
        
        # Determine semantic purpose based on context
        if 'landlord' in all_context or 'owner' in all_context:
            if 'name' in all_context or ('landlord' in all_context and field['page'] == 0 and field['field_type'] == 'Text'):
                semantic_info['purpose'] = 'landlord_name'
                semantic_info['unique_id'] = 'landlord_name'
            elif 'address' in all_context:
                semantic_info['purpose'] = 'landlord_address'
                semantic_info['unique_id'] = 'landlord_address'
            elif 'phone' in all_context:
                semantic_info['purpose'] = 'landlord_phone'
                semantic_info['unique_id'] = 'landlord_phone'
            elif 'email' in all_context or 'e-mail' in all_context:
                semantic_info['purpose'] = 'landlord_email'
                semantic_info['unique_id'] = 'landlord_email'
            elif 'signature' in all_context:
                semantic_info['purpose'] = 'landlord_signature'
                semantic_info['unique_id'] = f'landlord_signature_page_{field["page"]}'
            elif 'initial' in all_context:
                semantic_info['purpose'] = 'landlord_initial'
                semantic_info['unique_id'] = f'landlord_initial_page_{field["page"]}'
        
        elif 'tenant' in all_context:
            if 'name' in all_context or ('tenant' in all_context and field['field_name'].endswith('_3')):
                semantic_info['purpose'] = 'tenant_name'
                # Multiple tenant names
                if field['field_name'].endswith('_3'):
                    semantic_info['unique_id'] = 'tenant_1_name'
                else:
                    semantic_info['unique_id'] = 'tenant_name'
            elif 'phone' in all_context:
                semantic_info['purpose'] = 'tenant_phone'
                semantic_info['unique_id'] = 'tenant_phone'
            elif 'email' in all_context:
                semantic_info['purpose'] = 'tenant_email'
                semantic_info['unique_id'] = 'tenant_email'
            elif 'signature' in all_context:
                semantic_info['purpose'] = 'tenant_signature'
                # Multiple tenant signatures
                semantic_info['unique_id'] = f'tenant_signature_page_{field["page"]}'
            elif 'initial' in all_context:
                semantic_info['purpose'] = 'tenant_initial'
                semantic_info['unique_id'] = f'tenant_initial_page_{field["page"]}'
        
        elif 'property' in all_context or 'premises' in all_context or 'address' in all_context:
            if 'address' in all_context or 'street' in all_context:
                semantic_info['purpose'] = 'property_address'
                semantic_info['unique_id'] = 'property_address'
            elif 'city' in all_context:
                semantic_info['purpose'] = 'property_city'
                semantic_info['unique_id'] = 'property_city'
            elif 'state' in all_context:
                semantic_info['purpose'] = 'property_state'
                semantic_info['unique_id'] = 'property_state'
            elif 'zip' in all_context:
                semantic_info['purpose'] = 'property_zip'
                semantic_info['unique_id'] = 'property_zip'
        
        elif 'unit' in all_context and ('number' in all_context or 'no' in all_context or field['field_name'].endswith('_5')):
            semantic_info['purpose'] = 'unit_number'
            semantic_info['unique_id'] = 'unit_number'
        
        elif 'county' in all_context and 'texas' in all_context:
            semantic_info['purpose'] = 'property_county'
            semantic_info['unique_id'] = 'property_county'
        
        elif 'commencement' in all_context and 'date' in all_context:
            semantic_info['purpose'] = 'lease_start_date'
            semantic_info['unique_id'] = 'lease_start_date'
        
        elif 'expiration' in all_context and 'date' in all_context:
            semantic_info['purpose'] = 'lease_end_date'
            semantic_info['unique_id'] = 'lease_end_date'
        
        elif 'rent' in all_context:
            if 'monthly' in all_context or 'per month' in all_context:
                semantic_info['purpose'] = 'monthly_rent'
                semantic_info['unique_id'] = 'monthly_rent'
            elif 'late' in all_context and ('charge' in all_context or 'fee' in all_context):
                semantic_info['purpose'] = 'late_fee'
                semantic_info['unique_id'] = 'late_fee_amount'
            elif 'initial' in all_context and 'late' in all_context:
                semantic_info['purpose'] = 'initial_late_charge'
                semantic_info['unique_id'] = 'initial_late_charge'
            elif 'daily' in all_context and 'late' in all_context:
                semantic_info['purpose'] = 'daily_late_charge'
                semantic_info['unique_id'] = 'daily_late_charge'
        
        elif 'security' in all_context and 'deposit' in all_context:
            semantic_info['purpose'] = 'security_deposit'
            semantic_info['unique_id'] = 'security_deposit'
        
        elif 'pet' in all_context:
            if 'deposit' in all_context:
                semantic_info['purpose'] = 'pet_deposit'
                semantic_info['unique_id'] = 'pet_deposit'
            elif 'fee' in all_context:
                semantic_info['purpose'] = 'pet_fee'
                semantic_info['unique_id'] = 'pet_fee'
        
        elif 'parking' in all_context:
            if 'space' in all_context or 'number' in all_context:
                semantic_info['purpose'] = 'parking_spaces'
                semantic_info['unique_id'] = 'parking_spaces'
        
        elif 'date' in all_context and 'signature' in all_context:
            semantic_info['purpose'] = 'signature_date'
            semantic_info['unique_id'] = f'signature_date_page_{field["page"]}'
        
        elif field['field_type'] == 'CheckBox':
            # Analyze checkbox context
            if 'conventional' in all_context and 'financing' in all_context:
                semantic_info['purpose'] = 'financing_conventional'
                semantic_info['unique_id'] = 'financing_conventional'
            elif 'fha' in all_context:
                semantic_info['purpose'] = 'financing_fha'
                semantic_info['unique_id'] = 'financing_fha'
            elif 'va' in all_context:
                semantic_info['purpose'] = 'financing_va'
                semantic_info['unique_id'] = 'financing_va'
            elif 'automatic' in all_context and 'renew' in all_context:
                semantic_info['purpose'] = 'automatic_renewal'
                semantic_info['unique_id'] = 'automatic_renewal_option'
            elif 'month-to-month' in all_context:
                semantic_info['purpose'] = 'month_to_month'
                semantic_info['unique_id'] = 'month_to_month_option'
            elif 'hoa' in all_context:
                semantic_info['purpose'] = 'hoa_property'
                semantic_info['unique_id'] = 'is_hoa_property'
            else:
                semantic_info['purpose'] = 'checkbox_option'
                semantic_info['unique_id'] = f'checkbox_{field["page"]}_{field["field_name"].split("_")[-1]}'
        
        elif field['field_type'] == 'RadioButton':
            semantic_info['purpose'] = 'radio_option'
            semantic_info['unique_id'] = f'radio_{field["page"]}_{field["field_name"].split("_")[-1]}'
        
        else:
            # Generic field analysis
            if '$' in all_context or 'amount' in all_context:
                semantic_info['purpose'] = 'monetary_amount'
                semantic_info['unique_id'] = f'amount_{field["page"]}_{field["field_name"].split("_")[-1]}'
            elif 'phone' in all_context:
                semantic_info['purpose'] = 'phone_number'
                semantic_info['unique_id'] = 'phone_number'
            elif 'email' in all_context or 'e-mail' in all_context:
                semantic_info['purpose'] = 'email_address'
                semantic_info['unique_id'] = 'email_address'
            elif 'fax' in all_context:
                semantic_info['purpose'] = 'fax_number'
                semantic_info['unique_id'] = 'fax_number'
            elif 'notice' in all_context and 'days' in all_context:
                semantic_info['purpose'] = 'notice_days'
                semantic_info['unique_id'] = 'notice_days'
            else:
                semantic_info['purpose'] = 'unknown'
                semantic_info['unique_id'] = f'field_{field["page"]}_{field["field_name"].split("_")[-1]}'
        
        # Ensure unique_id is always set
        if 'unique_id' not in semantic_info:
            semantic_info['unique_id'] = f'field_{field["page"]}_{field["field_name"].split("_")[-1]}'
        
        analyzed_fields.append(semantic_info)
    
    return analyzed_fields

def consolidate_same_value_fields(analyzed_fields):
    """Group fields that should share the same value"""
    consolidated = defaultdict(list)
    
    for field_info in analyzed_fields:
        unique_id = field_info['unique_id']
        # Group same-value fields
        if unique_id in ['landlord_name', 'tenant_1_name', 'property_address', 'unit_number', 
                         'property_county', 'monthly_rent', 'security_deposit']:
            consolidated[unique_id].append(field_info['field'])
        else:
            # Keep separate entries for different pages/instances
            consolidated[unique_id].append(field_info['field'])
    
    return consolidated

def generate_typescript_schema():
    """Generate the complete TypeScript schema"""
    analyzed_fields = analyze_all_fields()
    consolidated_fields = consolidate_same_value_fields(analyzed_fields)
    
    schema_items = []
    order = 1
    
    # Property Information Block
    if 'property_address' in consolidated_fields:
        schema_items.append({
            "unique_id": "property_address",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['property_address']],
            "display_attributes": {
                "display_name": "Property Address",
                "input_type": "text",
                "order": order,
                "block": "property_information",
                "block_style": {
                    "title": "Property Information",
                    "icon": "home",
                    "color_theme": "blue"
                },
                "width": 9,
                "placeholder": "123 Main Street",
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'unit_number' in consolidated_fields:
        schema_items.append({
            "unique_id": "unit_number",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['unit_number']],
            "display_attributes": {
                "display_name": "Unit Number",
                "input_type": "text",
                "order": order,
                "block": "property_information",
                "width": 3,
                "placeholder": "Unit 101",
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'property_city' in consolidated_fields:
        schema_items.append({
            "unique_id": "property_city",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['property_city']],
            "display_attributes": {
                "display_name": "City",
                "input_type": "text",
                "order": order,
                "block": "property_information",
                "width": 6,
                "placeholder": "Houston",
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'property_county' in consolidated_fields:
        schema_items.append({
            "unique_id": "property_county",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['property_county']],
            "display_attributes": {
                "display_name": "County",
                "input_type": "text",
                "order": order,
                "block": "property_information",
                "width": 4,
                "placeholder": "Harris",
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'property_state' in consolidated_fields:
        schema_items.append({
            "unique_id": "property_state",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['property_state']],
            "display_attributes": {
                "display_name": "State",
                "input_type": "text",
                "order": order,
                "block": "property_information",
                "width": 2,
                "placeholder": "TX",
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    # Landlord Information Block
    if 'landlord_name' in consolidated_fields:
        schema_items.append({
            "unique_id": "landlord_name",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['landlord_name']],
            "display_attributes": {
                "display_name": "Landlord Name",
                "input_type": "text",
                "order": order,
                "block": "landlord_information",
                "block_style": {
                    "title": "Landlord Information",
                    "icon": "user",
                    "color_theme": "green"
                },
                "width": 6,
                "placeholder": "John Doe",
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'landlord_phone' in consolidated_fields:
        schema_items.append({
            "unique_id": "landlord_phone",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['landlord_phone'][:1]],  # Just first instance
            "display_attributes": {
                "display_name": "Landlord Phone",
                "input_type": "text",
                "order": order,
                "block": "landlord_information",
                "width": 4,
                "placeholder": "(555) 123-4567",
                "validation": {
                    "loopback": [{
                        "regex": "^[-()\\s\\d]{10,}$",
                        "message": "Must be a valid phone number"
                    }]
                },
                "special_input": {
                    "text": {"phone": True}
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'landlord_email' in consolidated_fields:
        schema_items.append({
            "unique_id": "landlord_email",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['landlord_email']],
            "display_attributes": {
                "display_name": "Landlord Email",
                "input_type": "text",
                "order": order,
                "block": "landlord_information",
                "width": 6,
                "placeholder": "landlord@example.com",
                "validation": {
                    "loopback": [{
                        "regex": "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$",
                        "message": "Must be a valid email address"
                    }]
                },
                "special_input": {
                    "text": {"email": True}
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'landlord_address' in consolidated_fields:
        schema_items.append({
            "unique_id": "landlord_address",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['landlord_address']],
            "display_attributes": {
                "display_name": "Landlord Address",
                "input_type": "text",
                "order": order,
                "block": "landlord_information",
                "width": 12,
                "placeholder": "456 Oak Avenue, Houston, TX 77001",
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    # Tenant Information Block
    if 'tenant_1_name' in consolidated_fields:
        schema_items.append({
            "unique_id": "tenant_1_name",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['tenant_1_name']],
            "display_attributes": {
                "display_name": "Tenant 1 Name",
                "input_type": "text",
                "order": order,
                "block": "tenant_information",
                "block_style": {
                    "title": "Tenant Information",
                    "icon": "users",
                    "color_theme": "green"
                },
                "width": 6,
                "placeholder": "Jane Smith",
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    # Additional tenant names (if any)
    tenant_count = 2
    for key in consolidated_fields:
        if key.startswith('tenant_') and key.endswith('_name') and key != 'tenant_1_name':
            schema_items.append({
                "unique_id": f"tenant_{tenant_count}_name",
                "pdf_attributes": [{
                    "formType": "residential_lease_for_a_multi_family_property_unit",
                    "formfield": field['field_name']
                } for field in consolidated_fields[key]],
                "display_attributes": {
                    "display_name": f"Tenant {tenant_count} Name",
                    "input_type": "text",
                    "order": order,
                    "block": "tenant_information",
                    "width": 6,
                    "placeholder": "John Smith",
                    "value": {
                        "type": "manual"
                    }
                }
            })
            order += 1
            tenant_count += 1
    
    if 'tenant_phone' in consolidated_fields:
        schema_items.append({
            "unique_id": "tenant_phone",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['tenant_phone'][:1]],  # Just first instance
            "display_attributes": {
                "display_name": "Tenant Phone",
                "input_type": "text",
                "order": order,
                "block": "tenant_information",
                "width": 4,
                "placeholder": "(555) 987-6543",
                "validation": {
                    "loopback": [{
                        "regex": "^[-()\\s\\d]{10,}$",
                        "message": "Must be a valid phone number"
                    }]
                },
                "special_input": {
                    "text": {"phone": True}
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'tenant_email' in consolidated_fields:
        schema_items.append({
            "unique_id": "tenant_email",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['tenant_email']],
            "display_attributes": {
                "display_name": "Tenant Email",
                "input_type": "text",
                "order": order,
                "block": "tenant_information",
                "width": 6,
                "placeholder": "tenant@example.com",
                "validation": {
                    "loopback": [{
                        "regex": "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$",
                        "message": "Must be a valid email address"
                    }]
                },
                "special_input": {
                    "text": {"email": True}
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    # Lease Terms Block
    if 'lease_start_date' in consolidated_fields:
        schema_items.append({
            "unique_id": "lease_start_date",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['lease_start_date']],
            "display_attributes": {
                "display_name": "Lease Start Date",
                "input_type": "text",
                "order": order,
                "block": "lease_terms",
                "block_style": {
                    "title": "Lease Terms",
                    "icon": "calendar",
                    "color_theme": "purple"
                },
                "width": 4,
                "placeholder": "01/01/2024",
                "validation": {
                    "loopback": [{
                        "regex": "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
                        "message": "Must be a valid date (MM/DD/YYYY)"
                    }]
                },
                "special_input": {
                    "text": {"date": True}
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'lease_end_date' in consolidated_fields:
        schema_items.append({
            "unique_id": "lease_end_date",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['lease_end_date']],
            "display_attributes": {
                "display_name": "Lease End Date",
                "input_type": "text",
                "order": order,
                "block": "lease_terms",
                "width": 4,
                "placeholder": "12/31/2024",
                "validation": {
                    "loopback": [{
                        "regex": "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
                        "message": "Must be a valid date (MM/DD/YYYY)"
                    }],
                    "crossField": [{
                        "rule": ">",
                        "unique_id": "lease_start_date",
                        "message": "End date must be after start date"
                    }]
                },
                "special_input": {
                    "text": {"date": True}
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    # Renewal Options
    if 'automatic_renewal_option' in consolidated_fields:
        schema_items.append({
            "unique_id": "lease_renewal_type",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": "lease_renewal_options",
                "linked_form_fields_checkbox": [
                    {"fromDatabase": "AUTOMATIC_RENEWAL", "pdfAttribute": consolidated_fields['automatic_renewal_option'][0]['field_name']},
                    {"fromDatabase": "MONTH_TO_MONTH", "pdfAttribute": consolidated_fields.get('month_to_month_option', [{}])[0].get('field_name', '')}
                ]
            }],
            "display_attributes": {
                "display_name": "Lease Renewal Type",
                "input_type": "checkbox",
                "order": order,
                "block": "lease_terms",
                "width": 8,
                "checkbox_options": {
                    "options": [
                        {"display_name": "Automatic Renewal", "databaseStored": "AUTOMATIC_RENEWAL"},
                        {"display_name": "Month-to-Month", "databaseStored": "MONTH_TO_MONTH"}
                    ],
                    "maxSelected": 1,
                    "minSelected": 1
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'notice_days' in consolidated_fields:
        schema_items.append({
            "unique_id": "notice_days",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['notice_days']],
            "display_attributes": {
                "display_name": "Notice Period (Days)",
                "input_type": "text",
                "order": order,
                "block": "lease_terms",
                "width": 4,
                "placeholder": "30",
                "validation": {
                    "loopback": [{
                        "regex": "^\\d+$",
                        "message": "Must be a number"
                    }]
                },
                "special_input": {
                    "text": {"number": True}
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    # Financial Information Block
    if 'monthly_rent' in consolidated_fields:
        schema_items.append({
            "unique_id": "monthly_rent",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['monthly_rent']],
            "display_attributes": {
                "display_name": "Monthly Rent",
                "input_type": "text",
                "order": order,
                "block": "financial_information",
                "block_style": {
                    "title": "Financial Information",
                    "icon": "dollar-sign",
                    "color_theme": "orange"
                },
                "width": 4,
                "placeholder": "$2,500.00",
                "validation": {
                    "loopback": [{
                        "regex": "^[\\d.,$]+$",
                        "message": "Must be a valid monetary amount"
                    }]
                },
                "special_input": {
                    "text": {"currency": True}
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'security_deposit' in consolidated_fields:
        schema_items.append({
            "unique_id": "security_deposit",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['security_deposit']],
            "display_attributes": {
                "display_name": "Security Deposit",
                "input_type": "text",
                "order": order,
                "block": "financial_information",
                "width": 4,
                "placeholder": "$2,500.00",
                "validation": {
                    "loopback": [{
                        "regex": "^[\\d.,$]+$",
                        "message": "Must be a valid monetary amount"
                    }]
                },
                "special_input": {
                    "text": {"currency": True}
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'pet_deposit' in consolidated_fields:
        schema_items.append({
            "unique_id": "pet_deposit",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['pet_deposit']],
            "display_attributes": {
                "display_name": "Pet Deposit",
                "input_type": "text",
                "order": order,
                "block": "financial_information",
                "width": 4,
                "placeholder": "$500.00",
                "validation": {
                    "loopback": [{
                        "regex": "^[\\d.,$]+$",
                        "message": "Must be a valid monetary amount"
                    }]
                },
                "special_input": {
                    "text": {"currency": True}
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    # Late Fee Information
    if 'initial_late_charge' in consolidated_fields:
        schema_items.append({
            "unique_id": "initial_late_charge",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['initial_late_charge']],
            "display_attributes": {
                "display_name": "Initial Late Charge",
                "input_type": "text",
                "order": order,
                "block": "financial_information",
                "width": 4,
                "placeholder": "$50.00",
                "validation": {
                    "loopback": [{
                        "regex": "^[\\d.,$]+$",
                        "message": "Must be a valid monetary amount"
                    }]
                },
                "special_input": {
                    "text": {"currency": True}
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'daily_late_charge' in consolidated_fields:
        schema_items.append({
            "unique_id": "daily_late_charge",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['daily_late_charge']],
            "display_attributes": {
                "display_name": "Daily Late Charge",
                "input_type": "text",
                "order": order,
                "block": "financial_information",
                "width": 4,
                "placeholder": "$10.00",
                "validation": {
                    "loopback": [{
                        "regex": "^[\\d.,$]+$",
                        "message": "Must be a valid monetary amount"
                    }]
                },
                "special_input": {
                    "text": {"currency": True}
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    # Property Features Block
    if 'is_hoa_property' in consolidated_fields:
        schema_items.append({
            "unique_id": "is_hoa_property",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['is_hoa_property']],
            "display_attributes": {
                "display_name": "HOA Property",
                "input_type": "checkbox",
                "order": order,
                "block": "property_features",
                "block_style": {
                    "title": "Property Features",
                    "icon": "home",
                    "color_theme": "blue"
                },
                "width": 6,
                "checkbox_options": {
                    "options": [
                        {"display_name": "This property is subject to HOA rules", "databaseStored": "HOA_PROPERTY"}
                    ]
                },
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    if 'parking_spaces' in consolidated_fields:
        schema_items.append({
            "unique_id": "parking_spaces",
            "pdf_attributes": [{
                "formType": "residential_lease_for_a_multi_family_property_unit",
                "formfield": field['field_name']
            } for field in consolidated_fields['parking_spaces']],
            "display_attributes": {
                "display_name": "Parking Spaces",
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
                "value": {
                    "type": "manual"
                }
            }
        })
        order += 1
    
    # Signatures Block
    # Landlord Signatures
    landlord_sig_count = 1
    for key in sorted(consolidated_fields.keys()):
        if key.startswith('landlord_signature_page_'):
            page = key.split('_')[-1]
            schema_items.append({
                "unique_id": f"landlord_signature_{landlord_sig_count}",
                "pdf_attributes": [{
                    "formType": "residential_lease_for_a_multi_family_property_unit",
                    "formfield": field['field_name'],
                    "linked_dates": [{"dateFieldName": consolidated_fields.get(f'signature_date_page_{page}', [{}])[0].get('field_name', '')}]
                } for field in consolidated_fields[key]],
                "display_attributes": {
                    "display_name": f"Landlord Signature",
                    "input_type": "signature",
                    "order": order,
                    "block": "signatures",
                    "block_style": {
                        "title": "Signatures",
                        "icon": "pen-tool",
                        "color_theme": "gray"
                    },
                    "width": 6,
                    "value": {
                        "type": "manual",
                        "output": "SignatureInput__signer"
                    }
                }
            })
            order += 1
            landlord_sig_count += 1
    
    # Tenant Signatures
    tenant_sig_count = 1
    for key in sorted(consolidated_fields.keys()):
        if key.startswith('tenant_signature_page_'):
            page = key.split('_')[-1]
            schema_items.append({
                "unique_id": f"tenant_{tenant_sig_count}_signature",
                "pdf_attributes": [{
                    "formType": "residential_lease_for_a_multi_family_property_unit",
                    "formfield": field['field_name'],
                    "linked_dates": [{"dateFieldName": consolidated_fields.get(f'signature_date_page_{page}', [{}])[0].get('field_name', '')}]
                } for field in consolidated_fields[key]],
                "display_attributes": {
                    "display_name": f"Tenant {tenant_sig_count} Signature",
                    "input_type": "signature",
                    "order": order,
                    "block": "signatures",
                    "width": 6,
                    "value": {
                        "type": "manual",
                        "output": "SignatureInput__signer"
                    }
                }
            })
            order += 1
            tenant_sig_count += 1
    
    # Add initials if found
    # Landlord Initials
    landlord_initial_count = 1
    for key in sorted(consolidated_fields.keys()):
        if key.startswith('landlord_initial_page_'):
            schema_items.append({
                "unique_id": f"landlord_initials_{landlord_initial_count}",
                "pdf_attributes": [{
                    "formType": "residential_lease_for_a_multi_family_property_unit",
                    "formfield": field['field_name']
                } for field in consolidated_fields[key]],
                "display_attributes": {
                    "display_name": f"Landlord Initials",
                    "input_type": "signature",
                    "order": order,
                    "block": "signatures",
                    "width": 3,
                    "value": {
                        "type": "manual",
                        "output": "SignatureInput__signer"
                    }
                }
            })
            order += 1
            landlord_initial_count += 1
    
    # Tenant Initials
    tenant_initial_count = 1
    for key in sorted(consolidated_fields.keys()):
        if key.startswith('tenant_initial_page_'):
            schema_items.append({
                "unique_id": f"tenant_{tenant_initial_count}_initials",
                "pdf_attributes": [{
                    "formType": "residential_lease_for_a_multi_family_property_unit",
                    "formfield": field['field_name']
                } for field in consolidated_fields[key]],
                "display_attributes": {
                    "display_name": f"Tenant {tenant_initial_count} Initials",
                    "input_type": "signature",
                    "order": order,
                    "block": "signatures",
                    "width": 3,
                    "value": {
                        "type": "manual",
                        "output": "SignatureInput__signer"
                    }
                }
            })
            order += 1
            tenant_initial_count += 1
    
    return schema_items

def write_typescript_file(schema_items):
    """Write the TypeScript schema file"""
    typescript_content = '''import { SchemaItem } from "../../../../types/realtor";

export const residentialLeaseMultiFamilySchema: SchemaItem[] = '''
    
    typescript_content += json.dumps(schema_items, indent=2)
    typescript_content += ";\n"
    
    with open('residential_lease_multi_family_schema.ts', 'w') as f:
        f.write(typescript_content)
    
    print(f"\nGenerated TypeScript schema with {len(schema_items)} items")
    print("Saved to: residential_lease_multi_family_schema.ts")

if __name__ == "__main__":
    schema_items = generate_typescript_schema()
    write_typescript_file(schema_items)