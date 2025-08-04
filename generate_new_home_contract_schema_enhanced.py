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
    # Remove special characters but keep important ones like $ and %
    text = re.sub(r'[^\w\s$%.-]', ' ', text)
    return text.strip()

def analyze_field_context_enhanced(field, field_index, all_fields):
    """Enhanced context analysis for more accurate field identification"""
    # Get all context
    context_left = clean_context(field.get('context_left', ''))
    context_right = clean_context(field.get('context_right', ''))
    context_above = clean_context(field.get('context_above', ''))
    context_below = clean_context(field.get('context_below', ''))
    
    # Combine all context for analysis
    all_context = f"{context_left} {context_right} {context_above} {context_below}".lower()
    
    field_type = field['field_type']
    page = field['page']
    position = field['position']
    
    # Special handling for specific field names that include context
    field_name = field['field_name']
    
    # Page 1 - Contract header and parties
    if page == 0:
        # Top of page - contract date
        if position[1] < 100 and "NEW HOME CONTRACT" in context_above:
            return "contract_date", "Contract Date"
        
        # Parties section
        if "1.PARTIES:" in context_left or "parties" in all_context:
            if "buyer" in all_context and "seller" not in context_right:
                return "buyer_name", "Buyer Name"
            elif "seller" in context_left and "buyer" in context_right:
                return "seller_name", "Seller Name"
        
        # Property section
        if "2.PROPERTY:" in context_left or "property" in all_context:
            if "lot" in all_context and position[0] < 250:
                return "property_lot", "Lot Number"
            elif "block" in all_context and position[0] > 200 and position[0] < 350:
                return "property_block", "Block Number"
            elif "addition" in all_context and position[0] > 300:
                return "property_addition", "Addition"
            elif "city of" in all_context:
                return "property_city", "City"
            elif "county of" in all_context and "texas" in all_context:
                return "property_county", "County"
            elif "address" in all_context or "zip code" in all_context:
                return "property_address", "Property Address"
        
        # Sales price section
        if "3.SALES PRICE:" in context_above or "sales price" in all_context:
            if "cash portion" in all_context:
                return "cash_portion", "Cash Portion of Sales Price"
            elif "sum of all financing" in all_context:
                return "financing_amount", "Total Financing Amount"
            elif position[1] > 200 and position[1] < 220 and "$" in context_left:
                return "sales_price", "Sales Price"
    
    # Financing checkboxes
    if field_type == 'CheckBox':
        if "third party financing" in all_context:
            return "financing_third_party", "Third Party Financing"
        elif "loan assumption" in all_context:
            return "financing_loan_assumption", "Loan Assumption"
        elif "seller financing" in all_context:
            return "financing_seller", "Seller Financing"
        elif "conventional" in all_context:
            return "financing_conventional", "Conventional"
        elif "texas veterans" in all_context or "va " in all_context:
            return "financing_va", "VA"
        elif "fha" in all_context:
            return "financing_fha", "FHA"
        elif "usda" in all_context:
            return "financing_usda", "USDA"
        elif "other" in all_context and ("financing" in all_context or field_index > 20):
            return "financing_other", "Other Financing"
    
    # Earnest money and escrow
    if "earnest money" in all_context:
        if "$" in context_left or "amount" in all_context:
            return "earnest_money_amount", "Earnest Money Amount"
        elif "escrow agent" in all_context and "address" not in all_context:
            return "escrow_agent_name", "Escrow Agent Name"
        elif "address" in all_context:
            return "escrow_agent_address", "Escrow Agent Address"
    
    # Option fee and period
    if "option fee" in all_context:
        if "$" in context_left:
            return "option_fee_amount", "Option Fee Amount"
        elif "days" in all_context:
            return "option_period_days", "Option Period (Days)"
    
    # Title policy
    if "title policy" in all_context:
        if "expense" in all_context or "$" in context_left:
            return "title_policy_expense", "Title Policy Expense"
        elif "company" in all_context:
            return "title_company", "Title Company"
    
    # Survey
    if "survey" in all_context:
        if "expense" in all_context or "$" in all_context:
            return "survey_expense", "Survey Expense"
        elif "company" in all_context:
            return "survey_company", "Survey Company"
    
    # HOA fees
    if "hoa" in all_context or "homeowners association" in all_context:
        if "fee" in all_context or "$" in all_context:
            return "hoa_fee", "HOA Fee"
        elif "transfer" in all_context:
            return "hoa_transfer_fee", "HOA Transfer Fee"
    
    # Closing date and possession
    if "closing" in all_context:
        if "date" in all_context or "on or before" in all_context:
            return "closing_date", "Closing Date"
        elif "possession" in all_context:
            return "possession_date", "Possession Date"
    
    # Dates
    if "date" in all_context:
        if "effective" in all_context:
            return "effective_date", "Effective Date"
        elif "closing" in all_context:
            return "closing_date", "Closing Date"
        elif field_index > 200:  # Signature dates are usually at the end
            if "buyer" in all_context:
                return f"buyer_signature_date_{field_index}", "Buyer Signature Date"
            elif "seller" in all_context:
                return f"seller_signature_date_{field_index}", "Seller Signature Date"
    
    # Signatures and initials
    if "signature" in all_context or "sign" in all_context:
        if "buyer" in all_context:
            return f"buyer_signature_{field_index}", "Buyer Signature"
        elif "seller" in all_context:
            return f"seller_signature_{field_index}", "Seller Signature"
        elif "escrow" in all_context:
            return "escrow_agent_signature", "Escrow Agent Signature"
        elif "other" in all_context:
            return f"other_party_signature_{field_index}", "Other Party Signature"
    
    if "initial" in all_context:
        if "buyer" in all_context:
            return f"buyer_initial_{field_index}", "Buyer Initial"
        elif "seller" in all_context:
            return f"seller_initial_{field_index}", "Seller Initial"
    
    # Contact information
    if "phone" in all_context or "tel" in all_context:
        if "buyer" in all_context:
            return "buyer_phone", "Buyer Phone"
        elif "seller" in all_context:
            return "seller_phone", "Seller Phone"
        elif "agent" in all_context:
            return "agent_phone", "Agent Phone"
    
    if "email" in all_context:
        if "buyer" in all_context:
            return "buyer_email", "Buyer Email"
        elif "seller" in all_context:
            return "seller_email", "Seller Email"
        elif "agent" in all_context:
            return "agent_email", "Agent Email"
    
    # Agent/Broker information
    if "license" in all_context and "number" in all_context:
        if "agent" in all_context or "associate" in all_context:
            return "agent_license", "Agent License Number"
        elif "broker" in all_context:
            return "broker_license", "Broker License Number"
    
    # Addresses
    if "address" in all_context:
        if "property" in all_context:
            return "property_address", "Property Address"
        elif "mailing" in all_context:
            return "mailing_address", "Mailing Address"
        elif "escrow" in all_context:
            return "escrow_agent_address", "Escrow Agent Address"
    
    # Special fields from field names
    if "inches which yields an RValue of" in field_name:
        return "insulation_r_value", "Insulation R-Value"
    
    if "acknowledged by Seller and Buyers agreement to pay Seller" in field_name:
        return "seller_payment_agreement", "Seller Payment Agreement"
    
    if "Initialed for identification by Buyer" in field_name:
        return f"buyer_identification_initial_{field_index}", "Buyer Identification Initial"
    
    if "Seller only as Sellers agent" in field_name:
        return "seller_agent_acknowledgment", "Seller Agent Acknowledgment"
    
    # Default based on context and position
    if "$" in context_left or "amount" in all_context or "price" in all_context:
        return f"amount_{field_index}", f"Amount"
    
    if field_type == "CheckBox":
        return f"checkbox_{field_index}", f"Option"
    
    # Generic fields based on type
    if field_type == "Text":
        if position[3] - position[1] > 50:  # Tall field - likely text area
            return f"text_area_{field_index}", "Additional Information"
        else:
            return f"text_field_{field_index}", "Text Field"
    
    return f"field_{field_index}", "Field"

def group_related_fields(all_items):
    """Group related fields (same-value links, continuations, etc.)"""
    grouped_items = []
    used_indices = set()
    
    # First pass - identify linked fields
    name_groups = defaultdict(list)
    for i, item in enumerate(all_items):
        if i in used_indices:
            continue
            
        unique_id = item['unique_id']
        base_id = re.sub(r'_\d+$', '', unique_id)
        
        # Group signatures with their dates
        if 'signature' in unique_id and not 'date' in unique_id:
            # Look for corresponding date field
            for j, other in enumerate(all_items):
                if j != i and j not in used_indices:
                    if 'signature_date' in other['unique_id'] and base_id.replace('_signature', '') in other['unique_id']:
                        # Link signature with date
                        item['display_attributes']['linked_dates'] = [{
                            'dateFieldName': other['pdf_attributes'][0]['formfield']
                        }]
                        used_indices.add(j)
                        break
        
        # Group fields with same semantic meaning
        if base_id in ['buyer_name', 'seller_name', 'property_address', 'property_lot', 'property_block']:
            name_groups[base_id].append((i, item))
    
    # Process groups
    for base_id, group in name_groups.items():
        if len(group) > 1:
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
    
    # Add remaining ungrouped items
    for i, item in enumerate(all_items):
        if i not in used_indices:
            grouped_items.append(item)
    
    return grouped_items

def generate_enhanced_schema():
    """Generate the enhanced TypeScript schema with better context analysis"""
    # Read the extracted fields
    with open('New_Home_Contract_(Incomplete_Construction)_Fillable_fields_enhanced.json', 'r') as f:
        fields = json.load(f)
    
    print(f"Processing {len(fields)} fields...")
    
    # Process fields and create schema items
    all_items = []
    seen_blocks = OrderedDict()
    
    # Group fields by page and position for better organization
    fields_by_page = defaultdict(list)
    for i, field in enumerate(fields):
        field['index'] = i
        fields_by_page[field['page']].append(field)
    
    # Sort fields within each page by position (top to bottom, left to right)
    for page in sorted(fields_by_page.keys()):
        page_fields = fields_by_page[page]
        page_fields.sort(key=lambda f: (f['position'][1], f['position'][0]))
        
        for field in page_fields:
            # Enhanced context analysis
            unique_id, display_name = analyze_field_context_enhanced(field, field['index'], fields)
            
            # Determine field properties
            input_type = determine_input_type_enhanced(field, unique_id)
            width = determine_width_enhanced(unique_id, input_type, field)
            block = determine_block_enhanced(unique_id)
            
            # Get validation and special input
            validation, special_input = get_validation_enhanced(unique_id, display_name)
            placeholder = get_placeholder_enhanced(unique_id, display_name)
            
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
                schema_item["display_attributes"]["block_style"] = get_enhanced_block_style(block)
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
            
            all_items.append(schema_item)
    
    # Group related fields
    grouped_items = group_related_fields(all_items)
    
    # Re-order items
    for i, item in enumerate(grouped_items):
        item['display_attributes']['order'] = i + 1
    
    # Generate TypeScript file
    ts_content = '''import { SchemaItem } from "../../../../types/realtor";

export const newHomeContractIncompleteConstructionSchema: SchemaItem[] = [
'''
    
    for i, item in enumerate(grouped_items):
        ts_content += '  ' + json.dumps(item, indent=2).replace('\n', '\n  ')
        if i < len(grouped_items) - 1:
            ts_content += ','
        ts_content += '\n'
    
    ts_content += '];\n'
    
    # Save the schema
    with open('new_home_contract_incomplete_construction_schema.ts', 'w') as f:
        f.write(ts_content)
    
    print(f"Schema generated with {len(grouped_items)} items (consolidated from {len(fields)} fields)")
    print(f"Blocks created: {', '.join(seen_blocks.keys())}")

def determine_input_type_enhanced(field, unique_id):
    """Enhanced input type determination"""
    field_type = field['field_type']
    
    if field_type == 'CheckBox':
        return 'checkbox'
    elif field_type == 'RadioButton':
        return 'radio'
    elif 'signature' in unique_id:
        return 'signature'
    elif 'initial' in unique_id:
        return 'signature'
    elif 'text_area' in unique_id:
        return 'text-area'
    else:
        return 'text'

def determine_width_enhanced(unique_id, input_type, field):
    """Enhanced width determination based on field position and type"""
    position = field['position']
    field_width = position[2] - position[0]
    
    if input_type == 'text-area':
        return 12
    elif input_type == 'signature':
        return 6
    elif field_width > 400:
        return 12
    elif field_width > 300:
        return 9
    elif field_width > 200:
        return 6
    elif field_width > 100:
        return 4
    else:
        return 3

def determine_block_enhanced(unique_id):
    """Enhanced block determination"""
    if any(term in unique_id for term in ['buyer_', 'purchaser_']):
        return 'buyer_information'
    elif any(term in unique_id for term in ['seller_', 'vendor_']):
        return 'seller_information'
    elif any(term in unique_id for term in ['property_', 'lot', 'block', 'addition', 'city', 'county']):
        return 'property_details'
    elif any(term in unique_id for term in ['price', 'amount', 'fee', 'money', 'financing', 'loan', 'cash_portion']):
        return 'financial_terms'
    elif any(term in unique_id for term in ['earnest_money', 'escrow', 'option_fee']):
        return 'earnest_money_and_option'
    elif any(term in unique_id for term in ['title', 'survey', 'hoa']):
        return 'title_and_survey'
    elif any(term in unique_id for term in ['closing', 'possession', 'effective_date']):
        return 'closing_information'
    elif any(term in unique_id for term in ['signature', 'initial']):
        return 'signatures'
    elif any(term in unique_id for term in ['agent', 'broker', 'license']):
        return 'broker_information'
    else:
        return 'additional_provisions'

def get_enhanced_block_style(block_name):
    """Enhanced block styling"""
    styles = {
        'buyer_information': {
            'title': 'Buyer Information',
            'description': 'Buyer details and contact information',
            'icon': 'user',
            'color_theme': 'green'
        },
        'seller_information': {
            'title': 'Seller Information',
            'description': 'Seller details and contact information',
            'icon': 'user',
            'color_theme': 'green'
        },
        'property_details': {
            'title': 'Property Details',
            'description': 'Property location and description',
            'icon': 'home',
            'color_theme': 'blue'
        },
        'financial_terms': {
            'title': 'Financial Terms',
            'description': 'Sales price and financing details',
            'icon': 'dollar-sign',
            'color_theme': 'orange'
        },
        'earnest_money_and_option': {
            'title': 'Earnest Money & Option Fee',
            'description': 'Earnest money and option period details',
            'icon': 'shield',
            'color_theme': 'purple'
        },
        'title_and_survey': {
            'title': 'Title Policy & Survey',
            'description': 'Title insurance and survey information',
            'icon': 'file-text',
            'color_theme': 'blue'
        },
        'closing_information': {
            'title': 'Closing Information',
            'description': 'Closing date and possession details',
            'icon': 'calendar',
            'color_theme': 'purple'
        },
        'broker_information': {
            'title': 'Broker Information',
            'description': 'Real estate broker and agent details',
            'icon': 'briefcase',
            'color_theme': 'purple'
        },
        'signatures': {
            'title': 'Signatures',
            'description': 'Required signatures and dates',
            'icon': 'pen-tool',
            'color_theme': 'gray'
        },
        'additional_provisions': {
            'title': 'Additional Provisions',
            'description': 'Additional terms and conditions',
            'icon': 'file-text',
            'color_theme': 'gray'
        }
    }
    return styles.get(block_name, {
        'title': block_name.replace('_', ' ').title(),
        'icon': 'file-text',
        'color_theme': 'gray'
    })

def get_validation_enhanced(unique_id, display_name):
    """Enhanced validation rules"""
    validation = {}
    special_input = {}
    
    if 'phone' in unique_id:
        validation = {
            "loopback": [{
                "regex": "^[-()\\s\\d]{10,}$",
                "message": "Must be a valid phone number"
            }]
        }
        special_input = {"text": {"phone": True}}
    elif 'email' in unique_id:
        validation = {
            "loopback": [{
                "regex": "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$",
                "message": "Must be a valid email address"
            }]
        }
        special_input = {"text": {"email": True}}
    elif any(term in unique_id for term in ['price', 'amount', 'fee', 'money', 'expense', 'cash_portion']):
        validation = {
            "loopback": [{
                "regex": "^[\\d.,$]+$",
                "message": "Must be a valid monetary amount"
            }]
        }
        special_input = {"text": {"currency": True}}
    elif 'date' in unique_id:
        validation = {
            "loopback": [{
                "regex": "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
                "message": "Must be a valid date (MM/DD/YYYY)"
            }]
        }
        special_input = {"text": {"date": True}}
    elif 'days' in unique_id:
        validation = {
            "loopback": [{
                "regex": "^\\d+$",
                "message": "Must be a number"
            }]
        }
        special_input = {"text": {"number": True}}
    elif 'percent' in unique_id or 'rate' in unique_id:
        validation = {
            "loopback": [{
                "regex": "^[\\d.]+%?$",
                "message": "Must be a valid percentage"
            }]
        }
        special_input = {"text": {"percentage": True}}
    
    return validation, special_input

def get_placeholder_enhanced(unique_id, display_name):
    """Enhanced placeholder generation"""
    if 'phone' in unique_id:
        return "(555) 123-4567"
    elif 'email' in unique_id:
        return "example@email.com"
    elif 'date' in unique_id:
        return "MM/DD/YYYY"
    elif any(term in unique_id for term in ['price', 'amount', 'fee', 'money']):
        return "$0.00"
    elif 'days' in unique_id:
        return "0"
    elif 'percent' in unique_id:
        return "0.00%"
    elif 'license' in unique_id:
        return "123456"
    elif 'lot' in unique_id:
        return "1"
    elif 'block' in unique_id:
        return "A"
    elif 'city' in unique_id:
        return "Austin"
    elif 'county' in unique_id:
        return "Travis"
    elif 'address' in unique_id:
        return "123 Main Street"
    elif 'name' in unique_id:
        if 'buyer' in unique_id:
            return "John and Jane Doe"
        elif 'seller' in unique_id:
            return "Property Owner LLC"
        elif 'agent' in unique_id or 'escrow' in unique_id:
            return "Company Name"
        else:
            return "Full Name"
    return ""

if __name__ == "__main__":
    generate_enhanced_schema()