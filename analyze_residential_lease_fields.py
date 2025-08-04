#\!/usr/bin/env python3
import json
import re
from collections import defaultdict

def load_fields(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def extract_field_purpose(field):
    """Extract the purpose of a field based on context and position"""
    context = f"{field.get('context_left', '')} {field.get('context_right', '')} {field.get('context_above', '')} {field.get('context_below', '')}"
    context = context.lower()
    
    # Common patterns
    patterns = {
        'date': r'date|move.*in|move.*out|birth',
        'address': r'address|street|city|state|zip|apt',
        'phone': r'phone|ph\.|mobile|home|work',
        'email': r'email|e-mail',
        'name': r'name|landlord|employer|applicant|co-applicant',
        'money': r'\$|rent|deposit|income|salary',
        'ssn': r'soc\.sec|social security',
        'id': r'license|driver|id\s*no',
        'vehicle': r'vehicle|auto|car|make|model|plate',
        'reference': r'reference|contact',
        'employment': r'employer|occupation|position|supervisor',
        'bank': r'bank|account|checking|savings',
        'pet': r'pet|animal|dog|cat',
        'emergency': r'emergency|notify',
        'checkbox': r'yes|no|check',
        'signature': r'sign|initial|date.*sign'
    }
    
    field_info = {
        'name': field['field_name'],
        'type': field['field_type'],
        'page': field['page'],
        'context': context,
        'purpose': 'unknown'
    }
    
    for purpose, pattern in patterns.items():
        if re.search(pattern, context):
            field_info['purpose'] = purpose
            break
    
    return field_info

def group_fields_by_section(fields):
    """Group fields by logical sections based on page and context"""
    sections = defaultdict(list)
    
    for field in fields:
        field_info = extract_field_purpose(field)
        page = field['page']
        
        # Determine section based on page and context
        if page == 0:
            if 'applicant' in field_info['context']:
                sections['applicant_info'].append(field_info)
            elif 'property' in field_info['context']:
                sections['property_info'].append(field_info)
            else:
                sections['general_info'].append(field_info)
        elif page == 1:
            if 'current' in field_info['context']:
                sections['current_residence'].append(field_info)
            elif 'previous' in field_info['context']:
                sections['previous_residence'].append(field_info)
            elif 'vehicle' in field_info['context']:
                sections['vehicle_info'].append(field_info)
            else:
                sections['residence_history'].append(field_info)
        elif page == 2:
            if 'employer' in field_info['context'] or 'employment' in field_info['context']:
                sections['employment'].append(field_info)
            elif 'income' in field_info['context']:
                sections['income'].append(field_info)
            elif 'reference' in field_info['context']:
                sections['references'].append(field_info)
            else:
                sections['financial_info'].append(field_info)
        elif page == 3:
            if 'emergency' in field_info['context']:
                sections['emergency_contacts'].append(field_info)
            elif 'bank' in field_info['context']:
                sections['banking'].append(field_info)
            else:
                sections['additional_info'].append(field_info)
        else:
            sections['disclosures'].append(field_info)
    
    return sections

def main():
    fields = load_fields('residential_lease_application_Fillable_fields_enhanced.json')
    sections = group_fields_by_section(fields)
    
    print(f"Total fields: {len(fields)}")
    print("\nField distribution by section:")
    for section, field_list in sections.items():
        print(f"{section}: {len(field_list)} fields")
        
    # Save grouped analysis
    with open('residential_lease_fields_analysis.json', 'w') as f:
        json.dump(sections, f, indent=2)
    
    print("\nAnalysis saved to residential_lease_fields_analysis.json")

if __name__ == "__main__":
    main()