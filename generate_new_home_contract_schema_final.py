#!/usr/bin/env python3
import json
import re
from collections import defaultdict, OrderedDict

def clean_context(text):
    """Clean and normalize context text"""
    if not text:
        return ""
    # Remove extra spaces and normalize
    text = re.sub(r'\s+', ' ', text.strip())
    return text

def extract_field_number(field_name):
    """Extract the field number from the field name"""
    match = re.search(r'_(\d+)$', field_name)
    return int(match.group(1)) if match else 0

def analyze_field_comprehensive(field, field_index, all_fields):
    """Comprehensive field analysis based on context and position"""
    context_left = clean_context(field.get('context_left', ''))
    context_right = clean_context(field.get('context_right', ''))
    context_above = clean_context(field.get('context_above', ''))
    context_below = clean_context(field.get('context_below', ''))
    
    all_context = f"{context_left} {context_right} {context_above} {context_below}".lower()
    
    field_type = field['field_type']
    page = field['page']
    position = field['position']
    field_num = extract_field_number(field['field_name'])
    
    # Special field names that contain context
    special_field_name = field['field_name']
    
    # Handle special field names
    if "inches which yields an RValue of" in special_field_name:
        return "insulation_r_value", "Insulation R-Value"
    
    if "acknowledged by Seller and Buyers agreement to pay Seller" in special_field_name:
        return "seller_payment_acknowledgment", "Seller Payment Acknowledgment"
    
    if "Initialed for identification by Buyer" in special_field_name:
        return f"buyer_identification_initial_{field_num}", "Buyer Identification Initial"
    
    if "Seller only as Sellers agent" in special_field_name:
        return "seller_agent_representation", "Seller Agent Representation"
    
    # Page 0 - Header and main contract terms
    if page == 0:
        # Contract date at top
        if position[1] < 95 and field_num == 1:
            return "contract_date", "Contract Date"
        
        # Buyer name (field 2)
        if field_num == 2 and "buyer" in all_context:
            return "buyer_name", "Buyer Name"
        
        # Property fields (3-8)
        if field_num == 3 and "lot" in context_left:
            return "property_lot", "Lot"
        elif field_num == 4 and "block" in context_below:
            return "property_block", "Block"
        elif field_num == 5 and "addition" in context_left:
            return "property_addition", "Addition"
        elif field_num == 6 and "city" in context_below:
            return "property_city", "City"
        elif field_num == 7 and ("county" in context_above or "county" in context_below):
            return "property_county", "County"
        elif field_num == 8 and "address" in context_below:
            return "property_street_address", "Property Street Address"
        
        # Sales price (field 9)
        if field_num == 9 and "$" in context_left:
            return "sales_price_total", "Total Sales Price"
        
        # Cash portion and financing
        if "cash portion" in all_context and "$" in context_left:
            return "cash_portion_amount", "Cash Portion Amount"
        elif "sum of all financing" in all_context and "$" in context_right:
            return "total_financing_amount", "Total Financing Amount"
    
    # Checkbox fields - financing options
    if field_type == 'CheckBox':
        checkbox_num = field_num
        
        # Financing type checkboxes
        if checkbox_num == 1 and "third party financing" in all_context:
            return "financing_third_party", "Third Party Financing"
        elif checkbox_num == 2 and "loan assumption" in all_context:
            return "financing_loan_assumption", "Loan Assumption"
        elif checkbox_num == 3 and "seller financing" in all_context:
            return "financing_seller", "Seller Financing"
        
        # Natural Resource Lease
        elif checkbox_num in [4, 5] and "natural resource lease" in all_context:
            if "is not" in context_right:
                return "not_party_to_resource_lease", "Not Party to Natural Resource Lease"
            else:
                return "is_party_to_resource_lease", "Is Party to Natural Resource Lease"
        
        # Natural Resource Lease delivery options
        elif checkbox_num == 6 and "delivered to buyer" in all_context:
            return "resource_lease_delivered", "Natural Resource Lease Delivered"
        elif checkbox_num == 7 and "not delivered" in all_context:
            return "resource_lease_not_delivered", "Natural Resource Lease Not Delivered"
        
        # Title policy expense
        elif checkbox_num in [8, 9] and "title policy" in all_context:
            if "seller's" in all_context:
                return "title_policy_seller_expense", "Title Policy at Seller's Expense"
            elif "buyer's" in all_context:
                return "title_policy_buyer_expense", "Title Policy at Buyer's Expense"
        
        # Survey/boundary amendments
        elif checkbox_num in [10, 11] and "will not be amended" in all_context:
            return "boundary_not_amended", "Boundaries Will Not Be Amended"
        elif checkbox_num in [12, 13] and "shortages in area" in all_context:
            if "buyer" in all_context:
                return "area_shortage_buyer_expense", "Area Shortage at Buyer's Expense"
            elif "seller" in all_context:
                return "area_shortage_seller_expense", "Area Shortage at Seller's Expense"
        
        # Survey options
        elif checkbox_num == 14 and "seller's expense" in all_context and "survey" in all_context:
            return "survey_seller_provides", "Seller Provides Survey"
        elif checkbox_num == 15 and "buyer's expense" in all_context and "survey" in all_context:
            return "survey_buyer_obtains", "Buyer May Obtain Survey"
        
        # HOA membership
        elif checkbox_num in [16, 17] and "property owners association" in all_context:
            if "is not" in all_context:
                return "not_subject_to_hoa", "Not Subject to HOA"
            else:
                return "subject_to_hoa", "Subject to HOA"
        
        # Construction specifications
        elif checkbox_num in [18, 19] and "specifications" in all_context:
            if "(1)" in context_right:
                return "specs_attached", "Specifications Attached"
            elif "(2)" in context_right:
                return "specs_below", "Specifications Listed Below"
        
        # Additional checkboxes for specific terms
        elif page >= 3:
            # Construction and warranty related
            if "seller is" in all_context and "licensed" in all_context:
                return f"seller_licensed_{checkbox_num}", "Seller Licensed Status"
            elif "warranty" in all_context:
                return f"warranty_option_{checkbox_num}", "Warranty Option"
            elif "construction" in all_context:
                return f"construction_term_{checkbox_num}", "Construction Term"
    
    # Text fields by context
    if field_type == 'Text':
        # Dates
        if "effective date" in all_context:
            return "effective_date", "Effective Date"
        elif "closing" in all_context and "date" in all_context:
            return "closing_date", "Closing Date"
        elif "option period" in all_context and "days" in all_context:
            return "option_period_days", "Option Period Days"
        elif "date" in all_context and field_num > 200:
            if "buyer" in all_context:
                return f"buyer_date_{field_num}", "Buyer Date"
            elif "seller" in all_context:
                return f"seller_date_{field_num}", "Seller Date"
        
        # Money amounts
        if "$" in context_left or "$" in context_right:
            if "earnest money" in all_context:
                return "earnest_money_amount", "Earnest Money"
            elif "option fee" in all_context:
                return "option_fee_amount", "Option Fee"
            elif "title policy" in all_context:
                return "title_policy_amount", "Title Policy Amount"
            elif "survey" in all_context:
                return "survey_cost", "Survey Cost"
            elif "hoa" in all_context:
                if "transfer" in all_context:
                    return "hoa_transfer_fee", "HOA Transfer Fee"
                else:
                    return "hoa_fee", "HOA Fee"
            elif field_num < 50:
                return f"amount_{field_num}", "Amount"
            else:
                return f"additional_cost_{field_num}", "Additional Cost"
        
        # Names and contact info
        if "escrow agent" in all_context:
            if "address" in all_context:
                return "escrow_agent_address", "Escrow Agent Address"
            else:
                return "escrow_agent_name", "Escrow Agent Name"
        elif "title company" in all_context:
            return "title_company_name", "Title Company"
        elif "phone" in all_context or "fax" in all_context:
            if "buyer" in all_context:
                return "buyer_phone", "Buyer Phone"
            elif "seller" in all_context:
                return "seller_phone", "Seller Phone"
            elif field_num > 150:
                return f"contact_phone_{field_num}", "Contact Phone"
        elif "email" in all_context:
            if "buyer" in all_context:
                return "buyer_email", "Buyer Email"
            elif "seller" in all_context:
                return "seller_email", "Seller Email"
            else:
                return f"email_{field_num}", "Email"
        
        # Addresses
        if "address" in all_context and "property" not in all_context:
            if "mailing" in all_context:
                return f"mailing_address_{field_num}", "Mailing Address"
            elif field_num > 100:
                return f"address_{field_num}", "Address"
        
        # License numbers
        if "license" in all_context:
            if "broker" in all_context:
                return f"broker_license_{field_num}", "Broker License"
            elif "agent" in all_context or "associate" in all_context:
                return f"agent_license_{field_num}", "Agent License"
        
        # Signatures
        if "signature" in all_context or "sign" in all_context:
            if "buyer" in all_context:
                return f"buyer_signature_{field_num}", "Buyer Signature"
            elif "seller" in all_context:
                return f"seller_signature_{field_num}", "Seller Signature"
            elif "escrow" in all_context:
                return "escrow_officer_signature", "Escrow Officer Signature"
            elif "receipt" in all_context:
                return f"receipt_signature_{field_num}", "Receipt Signature"
        
        # Initials
        if "initial" in all_context:
            if "buyer" in all_context:
                return f"buyer_initial_{field_num}", "Buyer Initial"
            elif "seller" in all_context:
                return f"seller_initial_{field_num}", "Seller Initial"
        
        # Construction related
        if "insulation" in all_context:
            return f"insulation_spec_{field_num}", "Insulation Specification"
        elif "construction" in all_context:
            return f"construction_detail_{field_num}", "Construction Detail"
        
        # Default based on position and size
        field_height = position[3] - position[1]
        field_width = position[2] - position[0]
        
        if field_height > 30 or field_width > 300:
            return f"text_area_{field_num}", "Additional Information"
        else:
            return f"text_field_{field_num}", "Information"
    
    # Default
    return f"field_{field_num}", "Field"

def determine_input_type(field, unique_id):
    """Determine the appropriate input type"""
    field_type = field['field_type']
    
    if field_type == 'CheckBox':
        return 'checkbox'
    elif field_type == 'RadioButton':
        return 'radio'
    elif 'signature' in unique_id:
        return 'signature'
    elif 'initial' in unique_id:
        return 'signature'
    elif 'text_area' in unique_id or 'additional_information' in unique_id:
        return 'text-area'
    else:
        return 'text'

def determine_width(unique_id, input_type, field):
    """Determine field width based on type and content"""
    position = field['position']
    field_width = position[2] - position[0]
    
    if input_type == 'text-area':
        return 12
    elif input_type == 'signature':
        return 6
    elif 'address' in unique_id and 'street' in unique_id:
        return 9
    elif field_width > 400:
        return 12
    elif field_width > 300:
        return 9
    elif field_width > 200:
        return 6
    elif field_width > 100:
        return 4
    elif input_type == 'checkbox':
        return 3
    else:
        return 3

def determine_block(unique_id):
    """Determine which block a field belongs to"""
    blocks = {
        'contract_information': ['contract_date', 'effective_date'],
        'parties': ['buyer_name', 'seller_name', 'buyer_', 'seller_'],
        'property_details': ['property_', 'lot', 'block', 'addition', 'city', 'county', 'street_address'],
        'sales_price': ['sales_price', 'cash_portion', 'financing_amount', 'price'],
        'financing': ['financing_', 'loan_'],
        'earnest_money': ['earnest_money', 'escrow_agent', 'option_fee', 'option_period'],
        'title_and_survey': ['title_', 'survey_', 'boundary_', 'area_shortage'],
        'property_condition': ['insulation_', 'construction_', 'warranty_', 'specs_'],
        'closing': ['closing_', 'possession_'],
        'hoa': ['hoa_', 'subject_to_hoa', 'not_subject_to_hoa'],
        'natural_resources': ['resource_lease', 'natural_resource'],
        'broker_information': ['broker_', 'agent_', 'license_', 'receipt_'],
        'additional_provisions': ['text_area_', 'additional_', 'special_provisions'],
        'signatures': ['signature_', 'initial_', 'date_']
    }
    
    for block_name, keywords in blocks.items():
        if any(keyword in unique_id for keyword in keywords):
            return block_name
    
    return 'additional_information'

def get_block_style(block_name):
    """Get block styling configuration"""
    styles = {
        'contract_information': {
            'title': 'Contract Information',
            'description': 'Contract date and basic information',
            'icon': 'file-text',
            'color_theme': 'blue'
        },
        'parties': {
            'title': 'Parties',
            'description': 'Buyer and Seller information',
            'icon': 'users',
            'color_theme': 'green'
        },
        'property_details': {
            'title': 'Property Description',
            'description': 'Legal description and address',
            'icon': 'home',
            'color_theme': 'blue'
        },
        'sales_price': {
            'title': 'Sales Price',
            'description': 'Purchase price and payment terms',
            'icon': 'dollar-sign',
            'color_theme': 'orange'
        },
        'financing': {
            'title': 'Financing',
            'description': 'Financing arrangements',
            'icon': 'credit-card',
            'color_theme': 'orange'
        },
        'earnest_money': {
            'title': 'Earnest Money & Option Fee',
            'description': 'Deposit and option period details',
            'icon': 'shield',
            'color_theme': 'purple'
        },
        'title_and_survey': {
            'title': 'Title Policy & Survey',
            'description': 'Title insurance and property survey',
            'icon': 'map',
            'color_theme': 'blue'
        },
        'property_condition': {
            'title': 'Property Condition & Construction',
            'description': 'Construction specifications and warranties',
            'icon': 'tool',
            'color_theme': 'gray'
        },
        'closing': {
            'title': 'Closing & Possession',
            'description': 'Closing date and possession details',
            'icon': 'calendar',
            'color_theme': 'purple'
        },
        'hoa': {
            'title': 'HOA Information',
            'description': 'Homeowners association details',
            'icon': 'home',
            'color_theme': 'green'
        },
        'natural_resources': {
            'title': 'Natural Resources',
            'description': 'Natural resource leases',
            'icon': 'leaf',
            'color_theme': 'green'
        },
        'broker_information': {
            'title': 'Broker Information',
            'description': 'Real estate broker and agent details',
            'icon': 'briefcase',
            'color_theme': 'purple'
        },
        'additional_provisions': {
            'title': 'Additional Provisions',
            'description': 'Special provisions and additional terms',
            'icon': 'file-text',
            'color_theme': 'gray'
        },
        'signatures': {
            'title': 'Signatures & Acknowledgments',
            'description': 'Required signatures and dates',
            'icon': 'pen-tool',
            'color_theme': 'gray'
        },
        'additional_information': {
            'title': 'Additional Information',
            'description': 'Other contract details',
            'icon': 'info',
            'color_theme': 'gray'
        }
    }
    return styles.get(block_name, {
        'title': block_name.replace('_', ' ').title(),
        'icon': 'file-text',
        'color_theme': 'gray'
    })

def get_validation_and_special_input(unique_id, display_name):
    """Get validation rules and special input configuration"""
    validation = {}
    special_input = {}
    
    # Phone fields
    if 'phone' in unique_id or 'fax' in unique_id:
        validation = {
            "loopback": [{
                "regex": "^[-()\\s\\d]{10,}$",
                "message": "Must be a valid phone number"
            }]
        }
        special_input = {"text": {"phone": True}}
    
    # Email fields
    elif 'email' in unique_id:
        validation = {
            "loopback": [{
                "regex": "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$",
                "message": "Must be a valid email address"
            }]
        }
        special_input = {"text": {"email": True}}
    
    # Money fields
    elif any(term in unique_id for term in ['price', 'amount', 'fee', 'money', 'cost', 'expense']):
        validation = {
            "loopback": [{
                "regex": "^[\\d.,$]+$",
                "message": "Must be a valid monetary amount"
            }]
        }
        special_input = {"text": {"currency": True}}
    
    # Date fields
    elif 'date' in unique_id and 'signature_date' not in unique_id:
        validation = {
            "loopback": [{
                "regex": "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
                "message": "Must be a valid date (MM/DD/YYYY)"
            }]
        }
        special_input = {"text": {"date": True}}
    
    # Number fields
    elif 'days' in unique_id or 'number' in unique_id:
        validation = {
            "loopback": [{
                "regex": "^\\d+$",
                "message": "Must be a number"
            }]
        }
        special_input = {"text": {"number": True}}
    
    # License numbers
    elif 'license' in unique_id:
        validation = {
            "loopback": [{
                "regex": "^[A-Za-z0-9]+$",
                "message": "Must be a valid license number"
            }]
        }
    
    return validation, special_input

def get_placeholder(unique_id, display_name):
    """Generate appropriate placeholder text"""
    placeholders = {
        'phone': '(555) 123-4567',
        'fax': '(555) 123-4568',
        'email': 'example@email.com',
        'date': 'MM/DD/YYYY',
        'days': '10',
        'license': '123456',
        'lot': '1',
        'block': 'A',
        'addition': 'Subdivision Name',
        'city': 'Austin',
        'county': 'Travis',
        'address': '123 Main Street',
        'street_address': '123 Main Street',
        'buyer_name': 'John and Jane Doe',
        'seller_name': 'Property Owner LLC',
        'company': 'Company Name',
        'agent': 'Agent Name',
        'broker': 'Broker Name'
    }
    
    # Check for specific terms in unique_id
    for term, placeholder in placeholders.items():
        if term in unique_id:
            return placeholder
    
    # Money fields
    if any(term in unique_id for term in ['price', 'amount', 'fee', 'money', 'cost']):
        return '$0.00'
    
    return ''

def group_related_fields(all_items):
    """Group related fields and consolidate same-value fields"""
    grouped_items = []
    used_indices = set()
    
    # Group fields by base unique_id
    field_groups = defaultdict(list)
    
    for i, item in enumerate(all_items):
        if i in used_indices:
            continue
        
        unique_id = item['unique_id']
        
        # Fields that should be consolidated
        consolidate_patterns = [
            'buyer_name', 'seller_name', 'property_address', 'property_street_address',
            'property_lot', 'property_block', 'property_addition', 'property_city',
            'property_county', 'escrow_agent_name', 'escrow_agent_address',
            'title_company_name', 'closing_date', 'effective_date'
        ]
        
        # Check if this field should be consolidated
        base_id = None
        for pattern in consolidate_patterns:
            if unique_id.startswith(pattern):
                base_id = pattern
                break
        
        if base_id:
            field_groups[base_id].append((i, item))
        else:
            # Check for signature-date relationships
            if 'signature_' in unique_id and not 'date' in unique_id:
                # Look for corresponding date field
                for j, other in enumerate(all_items):
                    if j != i and j not in used_indices:
                        other_id = other['unique_id']
                        # Match buyer_signature_X with buyer_date_X
                        if unique_id.replace('signature', 'date') == other_id:
                            # Add linked date
                            if 'pdf_attributes' in item and len(item['pdf_attributes']) > 0:
                                item['pdf_attributes'][0]['linked_dates'] = [{
                                    'dateFieldName': other['pdf_attributes'][0]['formfield']
                                }]
                            used_indices.add(j)
                            break
            
            # Check for grouped checkboxes (financing options)
            if unique_id.startswith('financing_'):
                if 'financing_options' not in field_groups:
                    # Create a combined financing options field
                    financing_item = {
                        'unique_id': 'financing_options',
                        'pdf_attributes': [{
                            'formType': 'new_home_contract_incomplete_construction',
                            'formfield': 'financing_type',
                            'linked_form_fields_checkbox': []
                        }],
                        'display_attributes': {
                            'display_name': 'Financing Type',
                            'input_type': 'checkbox',
                            'order': item['display_attributes']['order'],
                            'block': 'financing',
                            'width': 12,
                            'value': {'type': 'manual'},
                            'checkbox_options': {
                                'options': [],
                                'maxSelected': 1,
                                'minSelected': 1
                            }
                        }
                    }
                    field_groups['financing_options'] = [(i, financing_item)]
                
                # Add this option to the financing options
                option_name = unique_id.replace('financing_', '').replace('_', ' ').title()
                db_value = unique_id.replace('financing_', '').upper()
                
                financing_group = field_groups['financing_options'][0][1]
                financing_group['display_attributes']['checkbox_options']['options'].append({
                    'display_name': option_name,
                    'databaseStored': db_value
                })
                financing_group['pdf_attributes'][0]['linked_form_fields_checkbox'].append({
                    'fromDatabase': db_value,
                    'pdfAttribute': item['pdf_attributes'][0]['formfield']
                })
                used_indices.add(i)
                continue
    
    # Process consolidated groups
    for base_id, group in field_groups.items():
        if len(group) > 1 and base_id != 'financing_options':
            # Create single item with multiple pdf_attributes
            main_item = group[0][1].copy()
            main_item['unique_id'] = base_id
            
            # Combine all pdf_attributes
            pdf_attrs = []
            for idx, item in group:
                pdf_attrs.extend(item['pdf_attributes'])
                used_indices.add(idx)
            
            main_item['pdf_attributes'] = pdf_attrs
            grouped_items.append(main_item)
        elif base_id == 'financing_options':
            # Add the combined financing options field
            grouped_items.append(group[0][1])
            for idx, _ in group:
                used_indices.add(idx)
        elif len(group) == 1:
            # Single item groups
            grouped_items.append(group[0][1])
            used_indices.add(group[0][0])
    
    # Add remaining ungrouped items
    for i, item in enumerate(all_items):
        if i not in used_indices:
            grouped_items.append(item)
    
    # Sort by order to maintain logical flow
    grouped_items.sort(key=lambda x: x['display_attributes']['order'])
    
    # Renumber orders
    for i, item in enumerate(grouped_items):
        item['display_attributes']['order'] = i + 1
    
    return grouped_items

def generate_final_schema():
    """Generate the final comprehensive TypeScript schema"""
    # Read the extracted fields
    with open('New_Home_Contract_(Incomplete_Construction)_Fillable_fields_enhanced.json', 'r') as f:
        fields = json.load(f)
    
    print(f"Processing {len(fields)} fields...")
    
    # Process fields
    all_items = []
    seen_blocks = OrderedDict()
    
    # Sort fields by page and position
    fields_sorted = sorted(fields, key=lambda f: (f['page'], f['position'][1], f['position'][0]))
    
    for i, field in enumerate(fields_sorted):
        # Comprehensive field analysis
        unique_id, display_name = analyze_field_comprehensive(field, i, fields)
        
        # Determine field properties
        input_type = determine_input_type(field, unique_id)
        width = determine_width(unique_id, input_type, field)
        block = determine_block(unique_id)
        
        # Get validation and special input
        validation, special_input = get_validation_and_special_input(unique_id, display_name)
        placeholder = get_placeholder(unique_id, display_name)
        
        # Create schema item
        schema_item = {
            "unique_id": unique_id,
            "pdf_attributes": [{
                "formType": "new_home_contract_incomplete_construction",
                "formfield": field['field_name']
            }],
            "display_attributes": {
                "display_name": display_name,
                "input_type": input_type,
                "order": len(all_items) + 1,
                "block": block,
                "width": width,
                "value": {
                    "type": "manual"
                }
            }
        }
        
        # Add block style for first occurrence
        if block not in seen_blocks:
            schema_item["display_attributes"]["block_style"] = get_block_style(block)
            seen_blocks[block] = True
        
        # Add optional fields
        if placeholder:
            schema_item["display_attributes"]["placeholder"] = placeholder
        
        if validation:
            schema_item["display_attributes"]["validation"] = validation
        
        if special_input:
            schema_item["display_attributes"]["special_input"] = special_input
        
        # Special handling for signatures
        if input_type == 'signature':
            schema_item["display_attributes"]["value"]["output"] = "SignatureInput__signer"
        
        # Add required fields for important items
        if any(term in unique_id for term in ['buyer_name', 'seller_name', 'property_address', 
                                               'sales_price', 'closing_date', 'buyer_signature',
                                               'seller_signature']):
            schema_item["display_attributes"]["isRequired"] = True
        
        all_items.append(schema_item)
    
    # Group related fields
    grouped_items = group_related_fields(all_items)
    
    print(f"After grouping: {len(grouped_items)} schema items")
    
    # Generate TypeScript file
    ts_content = '''import { SchemaItem } from "../../../../types/realtor";

export const newHomeContractIncompleteConstructionSchema: SchemaItem[] = [
'''
    
    # Convert to TypeScript format
    for i, item in enumerate(grouped_items):
        # Format the JSON with proper indentation
        item_json = json.dumps(item, indent=2)
        # Add proper indentation for array items
        item_json = '\n'.join('  ' + line for line in item_json.split('\n'))
        
        ts_content += item_json
        if i < len(grouped_items) - 1:
            ts_content += ','
        ts_content += '\n'
    
    ts_content += '];\n'
    
    # Save the schema
    output_file = 'new_home_contract_incomplete_construction_schema.ts'
    with open(output_file, 'w') as f:
        f.write(ts_content)
    
    print(f"\nSchema successfully generated: {output_file}")
    print(f"Total fields processed: {len(fields)}")
    print(f"Schema items created: {len(grouped_items)}")
    print(f"Blocks created: {len(seen_blocks)}")
    print(f"Block order: {', '.join(seen_blocks.keys())}")

if __name__ == "__main__":
    generate_final_schema()