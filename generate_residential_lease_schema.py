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

def analyze_field_purpose(field):
    """Analyze field purpose from all context"""
    contexts = {
        'left': clean_context(field.get('context_left', '')),
        'right': clean_context(field.get('context_right', '')),
        'above': clean_context(field.get('context_above', '')),
        'below': clean_context(field.get('context_below', ''))
    }
    
    all_context = ' '.join(contexts.values()).lower()
    
    # More specific pattern matching
    if 'landlord' in all_context or 'owner' in all_context:
        if 'name' in all_context:
            return 'landlord_name', contexts
        elif 'address' in all_context or 'street' in all_context:
            return 'landlord_address', contexts
        elif 'phone' in all_context:
            return 'landlord_phone', contexts
        elif 'email' in all_context:
            return 'landlord_email', contexts
        elif 'signature' in all_context:
            return 'landlord_signature', contexts
        elif 'initial' in all_context:
            return 'landlord_initial', contexts
    
    elif 'tenant' in all_context or 'lessee' in all_context:
        if 'name' in all_context:
            return 'tenant_name', contexts
        elif 'signature' in all_context:
            return 'tenant_signature', contexts
        elif 'initial' in all_context:
            return 'tenant_initial', contexts
        elif 'phone' in all_context:
            return 'tenant_phone', contexts
        elif 'email' in all_context:
            return 'tenant_email', contexts
    
    elif 'unit' in all_context and ('number' in all_context or 'no' in all_context):
        return 'unit_number', contexts
    
    elif 'property' in all_context or 'premises' in all_context:
        if 'address' in all_context or 'street' in all_context:
            return 'property_address', contexts
        elif 'city' in all_context:
            return 'property_city', contexts
        elif 'state' in all_context:
            return 'property_state', contexts
        elif 'zip' in all_context:
            return 'property_zip', contexts
    
    elif 'address' in all_context and 'in' in contexts.get('left', ''):
        return 'property_address', contexts
    
    elif 'county' in all_context and 'texas' in all_context:
        return 'property_county', contexts
    
    elif 'rent' in all_context:
        if 'monthly' in all_context or 'per month' in all_context:
            return 'monthly_rent', contexts
        elif 'security' in all_context or 'deposit' in all_context:
            return 'security_deposit', contexts
        elif 'late' in all_context:
            return 'late_fee', contexts
    
    elif 'deposit' in all_context and ('security' in all_context or '$' in all_context):
        return 'security_deposit', contexts
    
    elif 'commencement' in all_context and 'date' in all_context:
        return 'lease_start_date', contexts
    
    elif 'expiration' in all_context and 'date' in all_context:
        return 'lease_end_date', contexts
    
    elif 'date' in all_context:
        if 'signature' in all_context:
            return 'signature_date', contexts
        else:
            return 'date_field', contexts
    
    elif '$' in all_context or 'amount' in all_context or 'fee' in all_context:
        return 'monetary_amount', contexts
    
    elif 'parking' in all_context:
        return 'parking_spaces', contexts
    
    elif 'pet' in all_context:
        if 'deposit' in all_context:
            return 'pet_deposit', contexts
        else:
            return 'pet_info', contexts
    
    elif 'utilities' in all_context:
        return 'utilities_info', contexts
    
    elif 'phone' in all_context:
        return 'phone_number', contexts
    
    elif 'fax' in all_context:
        return 'fax_number', contexts
    
    elif 'email' in all_context or '@' in all_context:
        return 'email_address', contexts
    
    elif field['field_type'] == 'CheckBox':
        return 'checkbox_option', contexts
    
    elif field['field_type'] == 'RadioButton':
        return 'radio_option', contexts
    
    return 'unknown', contexts

def generate_schema():
    # Load the enhanced fields
    with open('residential_lease_for_a_multi_family_property_unit___722_ts04618_unlocked_Fillable_fields_enhanced.json', 'r') as f:
        fields = json.load(f)
    
    print(f"Analyzing {len(fields)} fields...")
    
    # Analyze each field
    field_purposes = []
    for field in fields:
        purpose, contexts = analyze_field_purpose(field)
        field_purposes.append({
            'field': field,
            'purpose': purpose,
            'contexts': contexts
        })
    
    # Group similar fields
    grouped_fields = defaultdict(list)
    for fp in field_purposes:
        grouped_fields[fp['purpose']].append(fp)
    
    # Print analysis
    print("\nField Analysis Summary:")
    for purpose, items in sorted(grouped_fields.items()):
        print(f"\n{purpose}: {len(items)} fields")
        # Show first few examples
        for i, item in enumerate(items[:3]):
            field = item['field']
            print(f"  {i+1}. {field['field_name']} (Page {field['page']})")
            ctx = item['contexts']
            if ctx['left']: print(f"     Left: {ctx['left']}")
            if ctx['right']: print(f"     Right: {ctx['right']}")
            if ctx['above']: print(f"     Above: {ctx['above']}")
            if ctx['below']: print(f"     Below: {ctx['below']}")
    
    # Generate schema items
    schema_items = []
    order = 1
    
    # Property Information Block
    if grouped_fields['property_address']:
        field = grouped_fields['property_address'][0]['field']
        schema_items.append({
            'unique_id': 'property_address',
            'pdf_attributes': [{
                'formType': 'residential_lease_for_a_multi_family_property_unit',
                'formfield': field['field_name']
            }],
            'display_attributes': {
                'display_name': 'Property Address',
                'input_type': 'text',
                'order': order,
                'block': 'property_information',
                'block_style': {
                    'title': 'Property Information',
                    'icon': 'home',
                    'color_theme': 'blue'
                },
                'width': 9,
                'placeholder': '123 Main Street'
            }
        })
        order += 1
    
    if grouped_fields['unit_number']:
        field = grouped_fields['unit_number'][0]['field']
        schema_items.append({
            'unique_id': 'unit_number',
            'pdf_attributes': [{
                'formType': 'residential_lease_for_a_multi_family_property_unit',
                'formfield': field['field_name']
            }],
            'display_attributes': {
                'display_name': 'Unit Number',
                'input_type': 'text',
                'order': order,
                'block': 'property_information',
                'width': 3,
                'placeholder': 'Unit 101'
            }
        })
        order += 1
    
    if grouped_fields['property_county']:
        field = grouped_fields['property_county'][0]['field']
        schema_items.append({
            'unique_id': 'property_county',
            'pdf_attributes': [{
                'formType': 'residential_lease_for_a_multi_family_property_unit',
                'formfield': field['field_name']
            }],
            'display_attributes': {
                'display_name': 'County',
                'input_type': 'text',
                'order': order,
                'block': 'property_information',
                'width': 6,
                'placeholder': 'Harris County'
            }
        })
        order += 1
    
    # Landlord Information Block
    if grouped_fields['landlord_name']:
        # Find all landlord name fields across pages
        landlord_name_fields = grouped_fields['landlord_name']
        pdf_attrs = []
        for item in landlord_name_fields:
            pdf_attrs.append({
                'formType': 'residential_lease_for_a_multi_family_property_unit',
                'formfield': item['field']['field_name']
            })
        
        schema_items.append({
            'unique_id': 'landlord_name',
            'pdf_attributes': pdf_attrs,
            'display_attributes': {
                'display_name': 'Landlord Name',
                'input_type': 'text',
                'order': order,
                'block': 'landlord_information',
                'block_style': {
                    'title': 'Landlord Information',
                    'icon': 'user',
                    'color_theme': 'green'
                },
                'width': 6,
                'placeholder': 'John Doe'
            }
        })
        order += 1
    
    # Tenant Information Block
    if grouped_fields['tenant_name']:
        # Get first tenant name field
        field = grouped_fields['tenant_name'][0]['field']
        schema_items.append({
            'unique_id': 'tenant_1_name',
            'pdf_attributes': [{
                'formType': 'residential_lease_for_a_multi_family_property_unit',
                'formfield': field['field_name']
            }],
            'display_attributes': {
                'display_name': 'Tenant 1 Name',
                'input_type': 'text',
                'order': order,
                'block': 'tenant_information',
                'block_style': {
                    'title': 'Tenant Information',
                    'icon': 'users',
                    'color_theme': 'green'
                },
                'width': 6,
                'placeholder': 'Jane Smith'
            }
        })
        order += 1
    
    # Lease Terms Block
    if grouped_fields['lease_start_date']:
        field = grouped_fields['lease_start_date'][0]['field']
        schema_items.append({
            'unique_id': 'lease_start_date',
            'pdf_attributes': [{
                'formType': 'residential_lease_for_a_multi_family_property_unit',
                'formfield': field['field_name']
            }],
            'display_attributes': {
                'display_name': 'Lease Start Date',
                'input_type': 'text',
                'order': order,
                'block': 'lease_terms',
                'block_style': {
                    'title': 'Lease Terms',
                    'icon': 'calendar',
                    'color_theme': 'purple'
                },
                'width': 4,
                'placeholder': '01/01/2024',
                'validation': {
                    'loopback': [{
                        'regex': '^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$',
                        'message': 'Must be a valid date (MM/DD/YYYY)'
                    }]
                },
                'special_input': {
                    'text': {'date': True}
                }
            }
        })
        order += 1
    
    if grouped_fields['lease_end_date']:
        field = grouped_fields['lease_end_date'][0]['field']
        schema_items.append({
            'unique_id': 'lease_end_date',
            'pdf_attributes': [{
                'formType': 'residential_lease_for_a_multi_family_property_unit',
                'formfield': field['field_name']
            }],
            'display_attributes': {
                'display_name': 'Lease End Date',
                'input_type': 'text',
                'order': order,
                'block': 'lease_terms',
                'width': 4,
                'placeholder': '12/31/2024',
                'validation': {
                    'loopback': [{
                        'regex': '^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$',
                        'message': 'Must be a valid date (MM/DD/YYYY)'
                    }]
                },
                'special_input': {
                    'text': {'date': True}
                }
            }
        })
        order += 1
    
    # Financial Information Block
    if grouped_fields['monthly_rent']:
        field = grouped_fields['monthly_rent'][0]['field']
        schema_items.append({
            'unique_id': 'monthly_rent',
            'pdf_attributes': [{
                'formType': 'residential_lease_for_a_multi_family_property_unit',
                'formfield': field['field_name']
            }],
            'display_attributes': {
                'display_name': 'Monthly Rent',
                'input_type': 'text',
                'order': order,
                'block': 'financial_information',
                'block_style': {
                    'title': 'Financial Information',
                    'icon': 'dollar-sign',
                    'color_theme': 'orange'
                },
                'width': 4,
                'placeholder': '$2,500.00',
                'validation': {
                    'loopback': [{
                        'regex': '^[\\d.,$]+$',
                        'message': 'Must be a valid monetary amount'
                    }]
                },
                'special_input': {
                    'text': {'currency': True}
                }
            }
        })
        order += 1
    
    # Output the first part of the schema
    print("\n\nGenerating TypeScript schema...")
    print("\nFirst 10 schema items preview:")
    for item in schema_items[:10]:
        print(f"\n{item['unique_id']}:")
        print(f"  Display: {item['display_attributes']['display_name']}")
        print(f"  Type: {item['display_attributes']['input_type']}")
        print(f"  Width: {item['display_attributes'].get('width', 12)}")
    
    return schema_items, grouped_fields

if __name__ == "__main__":
    schema_items, grouped_fields = generate_schema()
    
    # Save intermediate analysis
    with open('residential_lease_schema_analysis.json', 'w') as f:
        analysis = {
            'total_fields': sum(len(items) for items in grouped_fields.values()),
            'field_groups': {k: len(v) for k, v in grouped_fields.items()},
            'sample_schema_items': schema_items[:10]
        }
        json.dump(analysis, f, indent=2)