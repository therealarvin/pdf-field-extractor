#!/usr/bin/env python3
import json
import re
from collections import defaultdict

def get_form_type():
    """Extract form type from filename"""
    return "new_home_contract_completed_construction"

def analyze_field_comprehensive(field, field_index, all_fields):
    """Comprehensive field analysis based on context"""
    context_left = field.get('context_left', '').strip()
    context_right = field.get('context_right', '').strip()
    context_above = field.get('context_above', '').strip()
    context_below = field.get('context_below', '').strip()
    
    # Combined context for easier searching
    context_all = f"{context_left} {context_right} {context_above} {context_below}".lower()
    
    field_type = field['field_type']
    page = field['page']
    position = field.get('position', [])
    
    # Initialize result
    result = {
        'field_name': field['field_name'],
        'field_type': field_type,
        'page': page,
        'position': position,
        'purpose': '',
        'unique_id': '',
        'display_name': '',
        'input_type': 'text',
        'width': 6,
        'block': '',
        'validation': None,
        'special_input': None,
        'placeholder': '',
        'is_signature': False,
        'is_date': False,
        'is_monetary': False,
        'linked_fields': []
    }
    
    # === ANALYZE BASED ON POSITION AND CONTEXT ===
    
    # Page 0 - Contract Header and Property Information
    if page == 0:
        if field_index == 0:  # textfield_1
            result['purpose'] = 'Buyer Name'
            result['unique_id'] = 'buyer_name'
            result['display_name'] = 'Buyer Name'
            result['width'] = 8
            result['block'] = 'parties'
            result['placeholder'] = 'John and Jane Doe'
        elif field_index == 1:  # textfield_2
            result['purpose'] = 'Seller Name'
            result['unique_id'] = 'seller_name'
            result['display_name'] = 'Seller Name'
            result['width'] = 8
            result['block'] = 'parties'
            result['placeholder'] = 'ABC Builders, LLC'
        elif field_index == 2:  # textfield_3 - Lot
            if 'lot' in context_left.lower():
                result['purpose'] = 'Lot Number'
                result['unique_id'] = 'property_lot'
                result['display_name'] = 'Lot'
                result['width'] = 4
                result['block'] = 'property_info'
                result['placeholder'] = '25'
        elif field_index == 3:  # textfield_4 - Block
            if 'block' in context_below.lower():
                result['purpose'] = 'Block Number'
                result['unique_id'] = 'property_block'
                result['display_name'] = 'Block'
                result['width'] = 4
                result['block'] = 'property_info'
                result['placeholder'] = 'B'
        elif field_index == 4:  # textfield_5 - Addition
            if 'addition' in context_below.lower():
                result['purpose'] = 'Addition'
                result['unique_id'] = 'property_addition'
                result['display_name'] = 'Addition'
                result['width'] = 8
                result['block'] = 'property_info'
        elif field_index == 5:  # textfield_6 - City
            if 'city' in context_below.lower():
                result['purpose'] = 'City'
                result['unique_id'] = 'property_city'
                result['display_name'] = 'City'
                result['width'] = 6
                result['block'] = 'property_info'
                result['placeholder'] = 'Houston'
        elif field_index == 6:  # textfield_7 - County
            if 'county' in context_all:
                result['purpose'] = 'County'
                result['unique_id'] = 'property_county'
                result['display_name'] = 'County'
                result['width'] = 6
                result['block'] = 'property_info'
                result['placeholder'] = 'Harris'
        elif field_index == 7:  # textfield_8 - Address/ZIP
            if 'address' in context_below.lower() or 'zip' in context_below.lower():
                result['purpose'] = 'Property Address'
                result['unique_id'] = 'property_address'
                result['display_name'] = 'Property Address/ZIP Code'
                result['width'] = 12
                result['block'] = 'property_info'
                result['placeholder'] = '123 Main Street, Houston, TX 77001'
        elif field_index == 8:  # textfield_9 - Sales Price
            if '$' in context_left:
                result['purpose'] = 'Sales Price'
                result['unique_id'] = 'sales_price'
                result['display_name'] = 'Sales Price'
                result['width'] = 4
                result['block'] = 'financial'
                result['is_monetary'] = True
                result['special_input'] = {'text': {'currency': True}}
                result['placeholder'] = '$0.00'
                result['validation'] = {
                    'loopback': [{
                        'regex': '^[\\d.,$]+$',
                        'message': 'Must be a valid monetary amount'
                    }]
                }
    
    # Checkboxes for financing types
    elif field_type == 'CheckBox':
        if 'third party financing' in context_right.lower():
            result['purpose'] = 'Third Party Financing'
            result['unique_id'] = 'financing_third_party'
            result['display_name'] = 'Third Party Financing Addendum'
            result['input_type'] = 'checkbox'
            result['width'] = 6
            result['block'] = 'financing'
        elif 'loan assumption' in context_right.lower():
            result['purpose'] = 'Loan Assumption'
            result['unique_id'] = 'financing_loan_assumption'
            result['display_name'] = 'Loan Assumption Addendum'
            result['input_type'] = 'checkbox'
            result['width'] = 6
            result['block'] = 'financing'
        elif 'seller financing' in context_right.lower():
            result['purpose'] = 'Seller Financing'
            result['unique_id'] = 'financing_seller'
            result['display_name'] = 'Seller Financing Addendum'
            result['input_type'] = 'checkbox'
            result['width'] = 6
            result['block'] = 'financing'
        elif 'va' in context_all:
            result['purpose'] = 'VA Loan'
            result['unique_id'] = 'financing_va'
            result['display_name'] = 'VA Loan'
            result['input_type'] = 'checkbox'
            result['width'] = 3
            result['block'] = 'financing'
        elif 'fha' in context_all:
            result['purpose'] = 'FHA Loan'
            result['unique_id'] = 'financing_fha'
            result['display_name'] = 'FHA Loan'
            result['input_type'] = 'checkbox'
            result['width'] = 3
            result['block'] = 'financing'
        elif 'conventional' in context_all:
            result['purpose'] = 'Conventional Financing'
            result['unique_id'] = 'financing_conventional'
            result['display_name'] = 'Conventional Financing'
            result['input_type'] = 'checkbox'
            result['width'] = 3
            result['block'] = 'financing'
        elif 'usda' in context_all:
            result['purpose'] = 'USDA Loan'
            result['unique_id'] = 'financing_usda'
            result['display_name'] = 'USDA Loan'
            result['input_type'] = 'checkbox'
            result['width'] = 3
            result['block'] = 'financing'
        else:
            result['input_type'] = 'checkbox'
            result['width'] = 3
    
    # Financial amounts
    elif '$' in context_left or '$' in context_right or 'price' in context_all or 'amount' in context_all:
        result['is_monetary'] = True
        result['special_input'] = {'text': {'currency': True}}
        result['validation'] = {
            'loopback': [{
                'regex': '^[\\d.,$]+$',
                'message': 'Must be a valid monetary amount'
            }]
        }
        result['placeholder'] = '$0.00'
        result['width'] = 4
        result['block'] = 'financial'
        
        if 'down payment' in context_all:
            result['purpose'] = 'Down Payment'
            result['unique_id'] = 'down_payment'
            result['display_name'] = 'Down Payment'
        elif 'earnest money' in context_all:
            result['purpose'] = 'Earnest Money'
            result['unique_id'] = 'earnest_money'
            result['display_name'] = 'Earnest Money'
        elif 'option fee' in context_all:
            result['purpose'] = 'Option Fee'
            result['unique_id'] = 'option_fee'
            result['display_name'] = 'Option Fee'
        elif 'financing' in context_all:
            result['purpose'] = 'Financing Amount'
            result['unique_id'] = 'financing_amount'
            result['display_name'] = 'Financing Amount'
    
    # Dates
    elif 'date' in context_all or 'days' in context_all:
        if 'closing' in context_all:
            result['purpose'] = 'Closing Date'
            result['unique_id'] = 'closing_date'
            result['display_name'] = 'Closing Date'
            result['is_date'] = True
            result['width'] = 4
            result['block'] = 'dates_deadlines'
            result['special_input'] = {'text': {'date': True}}
            result['placeholder'] = 'MM/DD/YYYY'
        elif 'effective' in context_all:
            result['purpose'] = 'Effective Date'
            result['unique_id'] = 'effective_date'
            result['display_name'] = 'Effective Date'
            result['is_date'] = True
            result['width'] = 4
            result['block'] = 'dates_deadlines'
            result['special_input'] = {'text': {'date': True}}
            result['placeholder'] = 'MM/DD/YYYY'
        elif 'possession' in context_all:
            result['purpose'] = 'Possession Date'
            result['unique_id'] = 'possession_date'
            result['display_name'] = 'Possession Date'
            result['is_date'] = True
            result['width'] = 4
            result['block'] = 'dates_deadlines'
            result['special_input'] = {'text': {'date': True}}
            result['placeholder'] = 'MM/DD/YYYY'
        elif 'days' in context_all and field_type == 'Text':
            result['purpose'] = 'Number of Days'
            result['unique_id'] = 'days'
            result['display_name'] = 'Days'
            result['width'] = 2
            result['placeholder'] = '10'
            result['validation'] = {
                'loopback': [{
                    'regex': '^\\d+$',
                    'message': 'Must be a number'
                }]
            }
    
    # Signatures
    elif 'signature' in context_all or 'sign' in context_all:
        result['is_signature'] = True
        result['input_type'] = 'signature'
        result['width'] = 6
        result['block'] = 'signatures'
        
        if 'buyer' in context_all:
            if '1' in context_all or 'first' in context_all:
                result['purpose'] = 'Buyer 1 Signature'
                result['unique_id'] = 'buyer_1_signature'
                result['display_name'] = 'Buyer 1 Signature'
            elif '2' in context_all or 'second' in context_all:
                result['purpose'] = 'Buyer 2 Signature'
                result['unique_id'] = 'buyer_2_signature'
                result['display_name'] = 'Buyer 2 Signature'
            else:
                result['purpose'] = 'Buyer Signature'
                result['unique_id'] = 'buyer_signature'
                result['display_name'] = 'Buyer Signature'
        elif 'seller' in context_all:
            if '1' in context_all or 'first' in context_all:
                result['purpose'] = 'Seller 1 Signature'
                result['unique_id'] = 'seller_1_signature'
                result['display_name'] = 'Seller 1 Signature'
            elif '2' in context_all or 'second' in context_all:
                result['purpose'] = 'Seller 2 Signature'
                result['unique_id'] = 'seller_2_signature'
                result['display_name'] = 'Seller 2 Signature'
            else:
                result['purpose'] = 'Seller Signature'
                result['unique_id'] = 'seller_signature'
                result['display_name'] = 'Seller Signature'
    
    # Initials
    elif 'initial' in context_all:
        result['is_signature'] = True
        result['input_type'] = 'signature'
        result['width'] = 3
        result['block'] = 'signatures'
        
        if 'buyer' in context_all:
            result['purpose'] = 'Buyer Initial'
            result['unique_id'] = 'buyer_initial'
            result['display_name'] = 'Buyer Initial'
        elif 'seller' in context_all:
            result['purpose'] = 'Seller Initial'
            result['unique_id'] = 'seller_initial'
            result['display_name'] = 'Seller Initial'
    
    # Contact Information
    elif 'phone' in context_all or 'tel' in context_all:
        result['purpose'] = 'Phone Number'
        result['width'] = 4
        result['special_input'] = {'text': {'phone': True}}
        result['placeholder'] = '(555) 123-4567'
        result['validation'] = {
            'loopback': [{
                'regex': '^[-()\\s\\d]{10,}$',
                'message': 'Must be a valid phone number'
            }]
        }
        if 'buyer' in context_all:
            result['unique_id'] = 'buyer_phone'
            result['display_name'] = 'Buyer Phone'
            result['block'] = 'parties'
        elif 'seller' in context_all:
            result['unique_id'] = 'seller_phone'
            result['display_name'] = 'Seller Phone'
            result['block'] = 'parties'
    
    elif 'email' in context_all:
        result['purpose'] = 'Email Address'
        result['width'] = 6
        result['special_input'] = {'text': {'email': True}}
        result['placeholder'] = 'example@email.com'
        result['validation'] = {
            'loopback': [{
                'regex': '^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$',
                'message': 'Must be a valid email address'
            }]
        }
        if 'buyer' in context_all:
            result['unique_id'] = 'buyer_email'
            result['display_name'] = 'Buyer Email'
            result['block'] = 'parties'
        elif 'seller' in context_all:
            result['unique_id'] = 'seller_email'
            result['display_name'] = 'Seller Email'
            result['block'] = 'parties'
    
    # Title Company / Escrow
    elif 'escrow' in context_all or 'title company' in context_all:
        result['block'] = 'escrow_title'
        if 'agent' in context_all or 'company' in context_all:
            result['purpose'] = 'Escrow Agent/Title Company'
            result['unique_id'] = 'escrow_agent'
            result['display_name'] = 'Escrow Agent/Title Company'
            result['width'] = 8
        elif 'address' in context_all:
            result['purpose'] = 'Escrow Agent Address'
            result['unique_id'] = 'escrow_address'
            result['display_name'] = 'Escrow Agent Address'
            result['width'] = 12
    
    # Broker/Agent Information
    elif 'broker' in context_all or 'license' in context_all:
        result['block'] = 'broker_info'
        if 'listing' in context_all:
            if 'license' in context_all:
                result['purpose'] = 'Listing Broker License'
                result['unique_id'] = 'listing_broker_license'
                result['display_name'] = 'Listing Broker License #'
                result['width'] = 4
                result['placeholder'] = 'RE123456'
            else:
                result['purpose'] = 'Listing Broker'
                result['unique_id'] = 'listing_broker_name'
                result['display_name'] = 'Listing Broker Name'
                result['width'] = 8
        elif 'selling' in context_all or 'other' in context_all:
            if 'license' in context_all:
                result['purpose'] = 'Selling Broker License'
                result['unique_id'] = 'selling_broker_license'
                result['display_name'] = 'Selling Broker License #'
                result['width'] = 4
                result['placeholder'] = 'RE123456'
            else:
                result['purpose'] = 'Selling Broker'
                result['unique_id'] = 'selling_broker_name'
                result['display_name'] = 'Selling Broker Name'
                result['width'] = 8
    
    # Address components
    elif 'address' in context_all:
        result['purpose'] = 'Address'
        result['unique_id'] = 'address'
        result['display_name'] = 'Address'
        result['width'] = 12
        result['placeholder'] = '123 Main Street'
    elif 'city' in context_all:
        result['purpose'] = 'City'
        result['unique_id'] = 'city'
        result['display_name'] = 'City'
        result['width'] = 6
        result['placeholder'] = 'Houston'
    elif 'state' in context_all:
        result['purpose'] = 'State'
        result['unique_id'] = 'state'
        result['display_name'] = 'State'
        result['width'] = 2
        result['placeholder'] = 'TX'
    elif 'zip' in context_all or 'postal' in context_all:
        result['purpose'] = 'ZIP Code'
        result['unique_id'] = 'zip_code'
        result['display_name'] = 'ZIP Code'
        result['width'] = 4
        result['placeholder'] = '77001'
    
    # MLS Number
    elif 'mls' in context_all:
        result['purpose'] = 'MLS Number'
        result['unique_id'] = 'mls_number'
        result['display_name'] = 'MLS #'
        result['width'] = 4
        result['placeholder'] = 'MLS123456'
    
    # Time
    elif 'time' in context_all:
        result['purpose'] = 'Time'
        result['unique_id'] = 'time'
        result['display_name'] = 'Time'
        result['width'] = 3
        result['placeholder'] = '5:00 PM'
    
    # If no specific purpose identified
    if not result['purpose']:
        result['purpose'] = 'Unknown'
        result['unique_id'] = f'field_{field_index}'
        result['display_name'] = f'Field {field_index}'
    
    return result

def identify_same_value_fields(analyzed_fields):
    """Identify fields that should share the same value across pages"""
    same_value_groups = defaultdict(list)
    
    # Group by unique_id to find duplicates
    for field in analyzed_fields:
        if field['unique_id'] and not field['unique_id'].startswith('field_'):
            base_id = field['unique_id'].replace(f"_page_{field['page']}", '')
            same_value_groups[base_id].append(field)
    
    # Return groups with more than one field
    return {k: v for k, v in same_value_groups.items() if len(v) > 1}

def generate_schema_items(analyzed_fields, same_value_groups):
    """Generate schema items from analyzed fields"""
    schema_items = []
    processed_fields = set()
    order = 1
    
    # Define block order and styling
    block_config = {
        'parties': {
            'title': 'Parties Information',
            'icon': 'users',
            'color_theme': 'green',
            'order': 1
        },
        'property_info': {
            'title': 'Property Information',
            'icon': 'home',
            'color_theme': 'blue',
            'order': 2
        },
        'financial': {
            'title': 'Financial Details',
            'icon': 'dollar-sign',
            'color_theme': 'orange',
            'order': 3
        },
        'financing': {
            'title': 'Financing Options',
            'icon': 'credit-card',
            'color_theme': 'purple',
            'order': 4
        },
        'dates_deadlines': {
            'title': 'Dates and Deadlines',
            'icon': 'calendar',
            'color_theme': 'blue',
            'order': 5
        },
        'escrow_title': {
            'title': 'Escrow and Title',
            'icon': 'building',
            'color_theme': 'green',
            'order': 6
        },
        'broker_info': {
            'title': 'Broker Information',
            'icon': 'briefcase',
            'color_theme': 'purple',
            'order': 7
        },
        'signatures': {
            'title': 'Signatures',
            'icon': 'pen-tool',
            'color_theme': 'gray',
            'order': 8
        }
    }
    
    # Process fields by block order
    for block_name, block_info in sorted(block_config.items(), key=lambda x: x[1]['order']):
        block_fields = [f for f in analyzed_fields if f['block'] == block_name and f['field_name'] not in processed_fields]
        
        for field in block_fields:
            if field['field_name'] in processed_fields:
                continue
            
            # Check if this field is part of a same-value group
            base_id = field['unique_id'].replace(f"_page_{field['page']}", '')
            if base_id in same_value_groups and len(same_value_groups[base_id]) > 1:
                # Create schema item with multiple pdf_attributes
                pdf_attributes = []
                for same_field in same_value_groups[base_id]:
                    pdf_attributes.append({
                        'formType': get_form_type(),
                        'formfield': same_field['field_name']
                    })
                    processed_fields.add(same_field['field_name'])
                
                schema_item = {
                    'unique_id': base_id,
                    'pdf_attributes': pdf_attributes,
                    'display_attributes': {
                        'display_name': field['display_name'],
                        'input_type': field['input_type'],
                        'order': order,
                        'block': field['block'],
                        'block_style': {
                            'title': block_info['title'],
                            'icon': block_info['icon'],
                            'color_theme': block_info['color_theme']
                        },
                        'width': field['width'],
                        'value': {
                            'type': 'manual',
                            'output': 'SignatureInput__signer' if field['is_signature'] else None
                        }
                    }
                }
            else:
                # Single field
                processed_fields.add(field['field_name'])
                schema_item = {
                    'unique_id': field['unique_id'],
                    'pdf_attributes': [{
                        'formType': get_form_type(),
                        'formfield': field['field_name']
                    }],
                    'display_attributes': {
                        'display_name': field['display_name'],
                        'input_type': field['input_type'],
                        'order': order,
                        'block': field['block'],
                        'block_style': {
                            'title': block_info['title'],
                            'icon': block_info['icon'],
                            'color_theme': block_info['color_theme']
                        },
                        'width': field['width'],
                        'value': {
                            'type': 'manual',
                            'output': 'SignatureInput__signer' if field['is_signature'] else None
                        }
                    }
                }
            
            # Add optional fields
            if field['placeholder']:
                schema_item['display_attributes']['placeholder'] = field['placeholder']
            if field['validation']:
                schema_item['display_attributes']['validation'] = field['validation']
            if field['special_input']:
                schema_item['display_attributes']['special_input'] = field['special_input']
            
            # Clean up value field if not signature
            if not field['is_signature'] and schema_item['display_attributes']['value'].get('output') is None:
                schema_item['display_attributes']['value'] = {'type': 'manual'}
            
            schema_items.append(schema_item)
            order += 1
    
    # Process any remaining fields not in a block
    remaining_fields = [f for f in analyzed_fields if f['field_name'] not in processed_fields]
    for field in remaining_fields:
        processed_fields.add(field['field_name'])
        schema_item = {
            'unique_id': field['unique_id'],
            'pdf_attributes': [{
                'formType': get_form_type(),
                'formfield': field['field_name']
            }],
            'display_attributes': {
                'display_name': field['display_name'],
                'input_type': field['input_type'],
                'order': order,
                'width': field['width'],
                'value': {
                    'type': 'manual',
                    'output': 'SignatureInput__signer' if field['is_signature'] else None
                }
            }
        }
        
        # Add optional fields
        if field['placeholder']:
            schema_item['display_attributes']['placeholder'] = field['placeholder']
        if field['validation']:
            schema_item['display_attributes']['validation'] = field['validation']
        if field['special_input']:
            schema_item['display_attributes']['special_input'] = field['special_input']
        
        # Clean up value field if not signature
        if not field['is_signature'] and schema_item['display_attributes']['value'].get('output') is None:
            schema_item['display_attributes']['value'] = {'type': 'manual'}
        
        schema_items.append(schema_item)
        order += 1
    
    return schema_items

def main():
    # Load the extracted fields
    with open('new_home_contract_completed_construction_Fillable_fields_enhanced.json', 'r') as f:
        fields = json.load(f)
    
    print(f"Processing {len(fields)} fields...")
    
    # Analyze all fields
    analyzed_fields = []
    for i, field in enumerate(fields):
        analysis = analyze_field_comprehensive(field, i, fields)
        analyzed_fields.append(analysis)
    
    # Identify same-value fields
    same_value_groups = identify_same_value_fields(analyzed_fields)
    print(f"\nFound {len(same_value_groups)} groups of same-value fields")
    
    # Generate schema items
    schema_items = generate_schema_items(analyzed_fields, same_value_groups)
    print(f"\nGenerated {len(schema_items)} schema items from {len(fields)} fields")
    
    # Create the TypeScript schema file
    typescript_content = '''import { SchemaItem } from "../../../../types/realtor";

export const newHomeContractCompletedConstructionSchema: SchemaItem[] = '''
    
    # Convert schema items to TypeScript
    typescript_content += json.dumps(schema_items, indent=2)
    typescript_content = typescript_content.replace('"', "'")
    typescript_content = typescript_content.replace("'unique_id':", "unique_id:")
    typescript_content = typescript_content.replace("'pdf_attributes':", "pdf_attributes:")
    typescript_content = typescript_content.replace("'formType':", "formType:")
    typescript_content = typescript_content.replace("'formfield':", "formfield:")
    typescript_content = typescript_content.replace("'display_attributes':", "display_attributes:")
    typescript_content = typescript_content.replace("'display_name':", "display_name:")
    typescript_content = typescript_content.replace("'input_type':", "input_type:")
    typescript_content = typescript_content.replace("'order':", "order:")
    typescript_content = typescript_content.replace("'block':", "block:")
    typescript_content = typescript_content.replace("'block_style':", "block_style:")
    typescript_content = typescript_content.replace("'title':", "title:")
    typescript_content = typescript_content.replace("'icon':", "icon:")
    typescript_content = typescript_content.replace("'color_theme':", "color_theme:")
    typescript_content = typescript_content.replace("'width':", "width:")
    typescript_content = typescript_content.replace("'value':", "value:")
    typescript_content = typescript_content.replace("'type':", "type:")
    typescript_content = typescript_content.replace("'output':", "output:")
    typescript_content = typescript_content.replace("'placeholder':", "placeholder:")
    typescript_content = typescript_content.replace("'validation':", "validation:")
    typescript_content = typescript_content.replace("'loopback':", "loopback:")
    typescript_content = typescript_content.replace("'regex':", "regex:")
    typescript_content = typescript_content.replace("'message':", "message:")
    typescript_content = typescript_content.replace("'special_input':", "special_input:")
    typescript_content = typescript_content.replace("'text':", "text:")
    typescript_content = typescript_content.replace("'currency':", "currency:")
    typescript_content = typescript_content.replace("'phone':", "phone:")
    typescript_content = typescript_content.replace("'email':", "email:")
    typescript_content = typescript_content.replace("'date':", "date:")
    typescript_content = typescript_content.replace("'linked_form_fields_text':", "linked_form_fields_text:")
    typescript_content = typescript_content.replace("'linked_form_fields_radio':", "linked_form_fields_radio:")
    typescript_content = typescript_content.replace("'linked_form_fields_checkbox':", "linked_form_fields_checkbox:")
    typescript_content = typescript_content.replace("'linked_dates':", "linked_dates:")
    typescript_content = typescript_content.replace("'checkbox_options':", "checkbox_options:")
    typescript_content = typescript_content.replace("'options':", "options:")
    typescript_content = typescript_content.replace("'databaseStored':", "databaseStored:")
    typescript_content = typescript_content.replace("'linkedFields':", "linkedFields:")
    typescript_content = typescript_content.replace("'maxSelected':", "maxSelected:")
    typescript_content = typescript_content.replace("'minSelected':", "minSelected:")
    typescript_content = typescript_content.replace("'visibleIf':", "visibleIf:")
    typescript_content = typescript_content.replace("'operation':", "operation:")
    typescript_content = typescript_content.replace("'valueChecked':", "valueChecked:")
    typescript_content = typescript_content.replace("'isCached':", "isCached:")
    typescript_content = typescript_content.replace("'isRequired':", "isRequired:")
    typescript_content = typescript_content.replace("'isHidden':", "isHidden:")
    typescript_content = typescript_content.replace("'breakBefore':", "breakBefore:")
    typescript_content = typescript_content.replace("'description':", "description:")
    typescript_content = typescript_content.replace("'attribute':", "attribute:")
    typescript_content = typescript_content.replace("null", "null")
    typescript_content = typescript_content.replace("true", "true")
    typescript_content = typescript_content.replace("false", "false")
    
    typescript_content += ";"
    
    # Save the schema
    output_filename = 'new_home_contract_completed_construction_schema.ts'
    with open(output_filename, 'w') as f:
        f.write(typescript_content)
    
    print(f"\nSchema saved to {output_filename}")
    
    # Summary statistics
    print("\n=== SUMMARY ===")
    print(f"Total fields processed: {len(fields)}")
    print(f"Schema items created: {len(schema_items)}")
    print(f"Fields consolidated: {len(fields) - len(schema_items)}")
    
    # Block distribution
    block_counts = defaultdict(int)
    for item in schema_items:
        block = item['display_attributes'].get('block', 'uncategorized')
        block_counts[block] += 1
    
    print("\n=== FIELDS BY BLOCK ===")
    for block, count in sorted(block_counts.items()):
        print(f"{block}: {count} fields")

if __name__ == "__main__":
    main()