#!/usr/bin/env python3
import json
import re
from collections import defaultdict, OrderedDict

def get_form_type():
    """Extract form type from filename"""
    return "new_home_contract_completed_construction"

def analyze_all_fields():
    """Comprehensive analysis of all 291 fields based on context and position"""
    # Load the extracted fields
    with open('new_home_contract_completed_construction_Fillable_fields_enhanced.json', 'r') as f:
        fields = json.load(f)
    
    analyzed_fields = []
    
    # Field-specific analysis based on manual inspection
    field_mappings = {
        # Page 0 - Contract Header and Initial Information
        0: { # textfield_1 - Buyer Name
            'unique_id': 'buyer_name',
            'display_name': 'Buyer Name',
            'block': 'parties',
            'width': 8,
            'placeholder': 'John and Jane Doe'
        },
        1: { # textfield_2 - Seller Name
            'unique_id': 'seller_name', 
            'display_name': 'Seller Name',
            'block': 'parties',
            'width': 8,
            'placeholder': 'ABC Builders, LLC'
        },
        2: { # textfield_3 - Lot
            'unique_id': 'property_lot',
            'display_name': 'Lot',
            'block': 'property_info',
            'width': 4,
            'placeholder': '25'
        },
        3: { # textfield_4 - Block
            'unique_id': 'property_block',
            'display_name': 'Block',
            'block': 'property_info',
            'width': 4,
            'placeholder': 'B'
        },
        4: { # textfield_5 - Addition
            'unique_id': 'property_addition',
            'display_name': 'Addition',
            'block': 'property_info',
            'width': 8
        },
        5: { # textfield_6 - City
            'unique_id': 'property_city',
            'display_name': 'City',
            'block': 'property_info',
            'width': 6,
            'placeholder': 'Houston'
        },
        6: { # textfield_7 - County  
            'unique_id': 'property_county',
            'display_name': 'County',
            'block': 'property_info',
            'width': 6,
            'placeholder': 'Harris'
        },
        7: { # textfield_8 - Property Address/ZIP
            'unique_id': 'property_address',
            'display_name': 'Property Address/ZIP Code',
            'block': 'property_info',
            'width': 12,
            'placeholder': '123 Main Street, Houston, TX 77001'
        },
        8: { # textfield_9 - Sales Price
            'unique_id': 'sales_price',
            'display_name': 'Sales Price',
            'block': 'financial',
            'width': 4,
            'is_monetary': True,
            'placeholder': '$0.00'
        },
        9: { # checkbox_1 - Third Party Financing
            'unique_id': 'financing_third_party',
            'display_name': 'Third Party Financing Addendum',
            'block': 'financing',
            'input_type': 'checkbox',
            'width': 6
        },
        10: { # checkbox_2 - Loan Assumption
            'unique_id': 'financing_loan_assumption',
            'display_name': 'Loan Assumption Addendum',
            'block': 'financing',
            'input_type': 'checkbox',
            'width': 6
        },
        11: { # checkbox_3 - Seller Financing
            'unique_id': 'financing_seller',
            'display_name': 'Seller Financing Addendum',
            'block': 'financing',
            'input_type': 'checkbox',
            'width': 6
        },
        12: { # textfield_10 - Financing Amount
            'unique_id': 'financing_amount',
            'display_name': 'Sum of Financing',
            'block': 'financial',
            'width': 4,
            'is_monetary': True,
            'placeholder': '$0.00'
        },
        13: { # textfield_11 - Cash Down Payment
            'unique_id': 'cash_down_payment',
            'display_name': 'Cash Down Payment',
            'block': 'financial',
            'width': 4,
            'is_monetary': True,
            'placeholder': '$0.00'
        },
        14: { # checkbox_4 - Residential Leases
            'unique_id': 'residential_leases',
            'display_name': 'Residential Leases',
            'block': 'leases',
            'input_type': 'checkbox',
            'width': 3
        },
        15: { # checkbox_5 - Addendum Regarding Residential Leases
            'unique_id': 'addendum_residential_leases',
            'display_name': 'Addendum Regarding Residential Leases',
            'block': 'leases',
            'input_type': 'checkbox',
            'width': 6
        },
        16: { # checkbox_6 - Fixture Leases
            'unique_id': 'fixture_leases',
            'display_name': 'Fixture Leases',
            'block': 'leases',
            'input_type': 'checkbox',
            'width': 6
        },
        17: { # checkbox_7 - Natural Resource Leases Delivered
            'unique_id': 'natural_resource_leases_delivered',
            'display_name': 'Natural Resource Leases Delivered',
            'block': 'leases',
            'input_type': 'checkbox',
            'width': 6
        },
        18: { # checkbox_8 - Natural Resource Leases Not Delivered
            'unique_id': 'natural_resource_leases_not_delivered',
            'display_name': 'Natural Resource Leases Not Delivered',
            'block': 'leases',
            'input_type': 'checkbox',
            'width': 6
        },
        19: { # textfield_12 - Days to Deliver Natural Resource Leases
            'unique_id': 'days_deliver_natural_resource_leases',
            'display_name': 'Days to Deliver',
            'block': 'leases',
            'width': 2,
            'placeholder': '10'
        },
        20: { # textfield_13 - Earnest Money Amount
            'unique_id': 'earnest_money_amount',
            'display_name': 'Earnest Money',
            'block': 'financial',
            'width': 4,
            'is_monetary': True,
            'placeholder': '$0.00'
        },
        21: { # textfield_14 - Additional Earnest Money
            'unique_id': 'additional_earnest_money',
            'display_name': 'Additional Earnest Money',
            'block': 'financial',
            'width': 4,
            'is_monetary': True,
            'placeholder': '$0.00'
        },
        22: { # textfield_15 - Days for Additional Earnest Money
            'unique_id': 'days_additional_earnest_money',
            'display_name': 'Days for Additional Earnest Money',
            'block': 'financial',
            'width': 2,
            'placeholder': '10'
        },
        23: { # textfield_16 - Option Fee
            'unique_id': 'option_fee',
            'display_name': 'Option Fee',
            'block': 'financial',
            'width': 4,
            'is_monetary': True,
            'placeholder': '$0.00'
        },
        24: { # textfield_17 - Option Period Days
            'unique_id': 'option_period_days',
            'display_name': 'Option Period (Days)',
            'block': 'dates_deadlines',
            'width': 2,
            'placeholder': '10'
        },
        # Continue mapping for remaining fields...
    }
    
    # Process each field
    for i, field in enumerate(fields):
        field_type = field['field_type']
        page = field['page']
        context_left = field.get('context_left', '').strip()
        context_right = field.get('context_right', '').strip()
        context_above = field.get('context_above', '').strip()
        context_below = field.get('context_below', '').strip()
        context_all = f"{context_left} {context_right} {context_above} {context_below}".lower()
        
        # Get mapping if exists
        mapping = field_mappings.get(i, {})
        
        # Create analyzed field
        analyzed_field = {
            'field_name': field['field_name'],
            'field_type': field_type,
            'page': page,
            'position': field.get('position', []),
            'unique_id': mapping.get('unique_id', ''),
            'display_name': mapping.get('display_name', ''),
            'input_type': mapping.get('input_type', 'checkbox' if field_type == 'CheckBox' else 'text'),
            'block': mapping.get('block', ''),
            'width': mapping.get('width', 6),
            'placeholder': mapping.get('placeholder', ''),
            'is_monetary': mapping.get('is_monetary', False),
            'is_signature': False,
            'is_date': False,
            'validation': None,
            'special_input': None
        }
        
        # If no mapping, try to analyze from context
        if not analyzed_field['unique_id']:
            # Monetary fields
            if '$' in context_left or '$' in context_right:
                analyzed_field['is_monetary'] = True
                analyzed_field['width'] = 4
                analyzed_field['placeholder'] = '$0.00'
                analyzed_field['block'] = 'financial'
                
                if 'earnest money' in context_all:
                    analyzed_field['unique_id'] = f'earnest_money_{i}'
                    analyzed_field['display_name'] = 'Earnest Money'
                elif 'option fee' in context_all:
                    analyzed_field['unique_id'] = f'option_fee_{i}'
                    analyzed_field['display_name'] = 'Option Fee'
                elif 'down payment' in context_all:
                    analyzed_field['unique_id'] = f'down_payment_{i}'
                    analyzed_field['display_name'] = 'Down Payment'
                elif 'price' in context_all:
                    analyzed_field['unique_id'] = f'price_{i}'
                    analyzed_field['display_name'] = 'Price'
                else:
                    analyzed_field['unique_id'] = f'amount_{i}'
                    analyzed_field['display_name'] = 'Amount'
            
            # Dates
            elif 'date' in context_all:
                analyzed_field['is_date'] = True
                analyzed_field['width'] = 4
                analyzed_field['placeholder'] = 'MM/DD/YYYY'
                analyzed_field['block'] = 'dates_deadlines'
                
                if 'closing' in context_all:
                    analyzed_field['unique_id'] = f'closing_date_{i}'
                    analyzed_field['display_name'] = 'Closing Date'
                elif 'effective' in context_all:
                    analyzed_field['unique_id'] = f'effective_date_{i}'
                    analyzed_field['display_name'] = 'Effective Date'
                else:
                    analyzed_field['unique_id'] = f'date_{i}'
                    analyzed_field['display_name'] = 'Date'
            
            # Signatures
            elif 'signature' in context_all:
                analyzed_field['is_signature'] = True
                analyzed_field['input_type'] = 'signature'
                analyzed_field['width'] = 6
                analyzed_field['block'] = 'signatures'
                
                if 'buyer' in context_all:
                    analyzed_field['unique_id'] = f'buyer_signature_{i}'
                    analyzed_field['display_name'] = 'Buyer Signature'
                elif 'seller' in context_all:
                    analyzed_field['unique_id'] = f'seller_signature_{i}'
                    analyzed_field['display_name'] = 'Seller Signature'
                else:
                    analyzed_field['unique_id'] = f'signature_{i}'
                    analyzed_field['display_name'] = 'Signature'
            
            # Initials
            elif 'initial' in context_all:
                analyzed_field['is_signature'] = True
                analyzed_field['input_type'] = 'signature'
                analyzed_field['width'] = 3
                analyzed_field['block'] = 'signatures'
                analyzed_field['unique_id'] = f'initial_{i}'
                analyzed_field['display_name'] = 'Initial'
            
            # Phone numbers
            elif 'phone' in context_all or 'tel' in context_all:
                analyzed_field['width'] = 4
                analyzed_field['placeholder'] = '(555) 123-4567'
                analyzed_field['unique_id'] = f'phone_{i}'
                analyzed_field['display_name'] = 'Phone Number'
            
            # Email
            elif 'email' in context_all:
                analyzed_field['width'] = 6
                analyzed_field['placeholder'] = 'example@email.com'
                analyzed_field['unique_id'] = f'email_{i}'
                analyzed_field['display_name'] = 'Email Address'
            
            # Address
            elif 'address' in context_all:
                analyzed_field['width'] = 12
                analyzed_field['unique_id'] = f'address_{i}'
                analyzed_field['display_name'] = 'Address'
            
            # Days
            elif 'days' in context_all and field_type == 'Text':
                analyzed_field['width'] = 2
                analyzed_field['placeholder'] = '10'
                analyzed_field['unique_id'] = f'days_{i}'
                analyzed_field['display_name'] = 'Days'
            
            # Checkboxes
            elif field_type == 'CheckBox':
                analyzed_field['width'] = 3
                analyzed_field['unique_id'] = f'checkbox_{i}'
                analyzed_field['display_name'] = f'Option {i}'
            
            # Default text field
            else:
                analyzed_field['unique_id'] = f'field_{i}'
                analyzed_field['display_name'] = f'Field {i}'
        
        # Add validation and special input
        if analyzed_field['is_monetary']:
            analyzed_field['special_input'] = {'text': {'currency': True}}
            analyzed_field['validation'] = {
                'loopback': [{
                    'regex': '^[\\d.,$]+$',
                    'message': 'Must be a valid monetary amount'
                }]
            }
        elif analyzed_field['is_date']:
            analyzed_field['special_input'] = {'text': {'date': True}}
            analyzed_field['validation'] = {
                'loopback': [{
                    'regex': '^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$',
                    'message': 'Must be a valid date (MM/DD/YYYY)'
                }]
            }
        elif 'phone' in analyzed_field['unique_id']:
            analyzed_field['special_input'] = {'text': {'phone': True}}
            analyzed_field['validation'] = {
                'loopback': [{
                    'regex': '^[-()\\s\\d]{10,}$',
                    'message': 'Must be a valid phone number'
                }]
            }
        elif 'email' in analyzed_field['unique_id']:
            analyzed_field['special_input'] = {'text': {'email': True}}
            analyzed_field['validation'] = {
                'loopback': [{
                    'regex': '^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$',
                    'message': 'Must be a valid email address'
                }]
            }
        
        analyzed_fields.append(analyzed_field)
    
    return analyzed_fields

def identify_same_value_groups(analyzed_fields):
    """Identify fields that should share the same value"""
    same_value_groups = defaultdict(list)
    
    # Known same-value patterns
    same_value_patterns = [
        'buyer_name', 'seller_name', 'property_address', 'property_lot', 
        'property_block', 'property_addition', 'property_city', 'property_county',
        'sales_price', 'earnest_money', 'closing_date', 'effective_date'
    ]
    
    for pattern in same_value_patterns:
        matching_fields = [f for f in analyzed_fields if f['unique_id'].startswith(pattern)]
        if len(matching_fields) > 1:
            same_value_groups[pattern] = matching_fields
    
    return same_value_groups

def generate_schema_items(analyzed_fields, same_value_groups):
    """Generate TypeScript schema items"""
    schema_items = []
    processed_fields = set()
    order = 1
    
    # Block configuration
    block_config = OrderedDict([
        ('parties', {
            'title': 'Parties Information',
            'icon': 'users',
            'color_theme': 'green'
        }),
        ('property_info', {
            'title': 'Property Information',
            'icon': 'home',
            'color_theme': 'blue'
        }),
        ('financial', {
            'title': 'Financial Details',
            'icon': 'dollar-sign',
            'color_theme': 'orange'
        }),
        ('financing', {
            'title': 'Financing Options',
            'icon': 'credit-card',
            'color_theme': 'purple'
        }),
        ('leases', {
            'title': 'Leases',
            'icon': 'file-text',
            'color_theme': 'blue'
        }),
        ('dates_deadlines', {
            'title': 'Dates and Deadlines',
            'icon': 'calendar',
            'color_theme': 'blue'
        }),
        ('disclosures', {
            'title': 'Disclosures',
            'icon': 'alert-circle',
            'color_theme': 'orange'
        }),
        ('inspections', {
            'title': 'Inspections and Repairs',
            'icon': 'search',
            'color_theme': 'green'
        }),
        ('escrow_title', {
            'title': 'Escrow and Title',
            'icon': 'building',
            'color_theme': 'green'
        }),
        ('broker_info', {
            'title': 'Broker Information',
            'icon': 'briefcase',
            'color_theme': 'purple'
        }),
        ('signatures', {
            'title': 'Signatures',
            'icon': 'pen-tool',
            'color_theme': 'gray'
        })
    ])
    
    # Process fields by block
    for block_name, block_info in block_config.items():
        block_fields = [f for f in analyzed_fields if f['block'] == block_name]
        
        for field in block_fields:
            if field['field_name'] in processed_fields:
                continue
            
            # Check if part of same-value group
            base_id = field['unique_id'].split('_')[0] if '_' in field['unique_id'] else field['unique_id']
            
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
                    'block_style': block_info,
                    'width': field['width'],
                    'value': {
                        'type': 'manual'
                    }
                }
            }
            
            # Add signature output
            if field['is_signature']:
                schema_item['display_attributes']['value']['output'] = 'SignatureInput__signer'
            
            # Add optional fields
            if field['placeholder']:
                schema_item['display_attributes']['placeholder'] = field['placeholder']
            if field['validation']:
                schema_item['display_attributes']['validation'] = field['validation']
            if field['special_input']:
                schema_item['display_attributes']['special_input'] = field['special_input']
            
            processed_fields.add(field['field_name'])
            schema_items.append(schema_item)
            order += 1
    
    # Process remaining fields
    remaining_fields = [f for f in analyzed_fields if f['field_name'] not in processed_fields]
    for field in remaining_fields:
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
                    'type': 'manual'
                }
            }
        }
        
        # Add signature output
        if field['is_signature']:
            schema_item['display_attributes']['value']['output'] = 'SignatureInput__signer'
        
        # Add optional fields
        if field['placeholder']:
            schema_item['display_attributes']['placeholder'] = field['placeholder']
        if field['validation']:
            schema_item['display_attributes']['validation'] = field['validation']
        if field['special_input']:
            schema_item['display_attributes']['special_input'] = field['special_input']
        
        schema_items.append(schema_item)
        order += 1
    
    return schema_items

def main():
    print("Analyzing all 291 fields...")
    analyzed_fields = analyze_all_fields()
    
    print("Identifying same-value field groups...")
    same_value_groups = identify_same_value_groups(analyzed_fields)
    
    print("Generating schema items...")
    schema_items = generate_schema_items(analyzed_fields, same_value_groups)
    
    # Create TypeScript content
    typescript_content = '''import { SchemaItem } from "../../../../types/realtor";

export const newHomeContractCompletedConstructionSchema: SchemaItem[] = '''
    
    typescript_content += json.dumps(schema_items, indent=2)
    
    # Clean up quotes for TypeScript
    typescript_content = re.sub(r'"([^"]+)":', r'\1:', typescript_content)
    typescript_content = typescript_content.replace('"', "'")
    typescript_content += ";"
    
    # Save the schema
    output_filename = 'new_home_contract_completed_construction_schema.ts'
    with open(output_filename, 'w') as f:
        f.write(typescript_content)
    
    print(f"\nSchema generated successfully!")
    print(f"Total fields: 291")
    print(f"Schema items created: {len(schema_items)}")
    print(f"Schema saved to: {output_filename}")

if __name__ == "__main__":
    main()