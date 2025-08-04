#!/usr/bin/env python3
import json
import re
from collections import defaultdict

def analyze_living_areas_fields():
    """Analyze living areas fields and generate TypeScript schema."""
    
    # Load the living areas fields
    with open('/Users/arvin/WebDev/field_extraction/living_areas_fields_only.json', 'r') as f:
        fields = json.load(f)
    
    # Group fields by room and component
    room_components = defaultdict(lambda: defaultdict(list))
    
    for field in fields:
        field_name = field['field_name']
        
        # Extract room (living, dining, family)
        if field_name.startswith('living_'):
            room = 'living'
            component_part = field_name[7:]  # Remove 'living_'
        elif field_name.startswith('dining_'):
            room = 'dining'
            component_part = field_name[7:]  # Remove 'dining_'
        elif field_name.startswith('family_'):
            room = 'family'
            component_part = field_name[7:]  # Remove 'family_'
        else:
            continue
        
        # Extract component and type
        if component_part.endswith('_move_in_comments'):
            component = component_part.replace('_move_in_comments', '')
            comment_type = 'move_in'
        elif component_part.endswith('_landlords_move_out_comments'):
            component = component_part.replace('_landlords_move_out_comments', '')
            comment_type = 'move_out'
        else:
            continue
        
        # Handle ceiling/ceilings inconsistency in family room
        if component == 'ceiling' and room == 'family':
            component = 'ceilings'  # Normalize to plural form
        
        room_components[room][component].append({
            'field': field,
            'comment_type': comment_type
        })
    
    # Generate schema items
    schema_items = []
    order = 1
    
    # Define component order for each room
    component_orders = {
        'living': ['ceilings', 'paint', 'doors', 'door_locks', 'flooring', 'lights', 'windows', 'window_latches', 'plugs', 'fireplace', 'drapes', 'cabinets', 'other'],
        'dining': ['ceilings', 'paint', 'door', 'door_locks', 'flooring', 'lights', 'windows', 'window_latches', 'plugs', 'drapes', 'cabinets', 'other'],
        'family': ['ceilings', 'paint', 'doors', 'door_locks', 'flooring', 'lights', 'windows', 'window_latches', 'drapes', 'plugs', 'closet', 'cabinets', 'fireplace', 'other']
    }
    
    # Room styling
    room_styles = {
        'living': {
            'title': 'Living Room',
            'description': 'Living room condition assessment',
            'icon': 'home',
            'color_theme': 'blue'
        },
        'dining': {
            'title': 'Dining Room', 
            'description': 'Dining room condition assessment',
            'icon': 'home',
            'color_theme': 'green'
        },
        'family': {
            'title': 'Family Room',
            'description': 'Family room condition assessment', 
            'icon': 'home',
            'color_theme': 'purple'
        }
    }
    
    consolidation_report = []
    
    # Process each room
    for room in ['living', 'dining', 'family']:
        room_data = room_components[room]
        
        # Add room header
        schema_items.append({
            'unique_id': f'{room}_room_header',
            'pdf_attributes': [{
                'formType': 'residential_lease_inventory_and_condition',
                'formfield': f'{room}_room_header'
            }],
            'display_attributes': {
                'display_name': room_styles[room]['title'],
                'input_type': 'info',
                'order': order,
                'block': f'{room}_room',
                'block_style': room_styles[room],
                'width': 12,
                'value': {'type': 'manual'},
                'breakBefore': True
            }
        })
        order += 1
        
        # Process components in order
        for component in component_orders[room]:
            if component not in room_data:
                continue
                
            component_fields = room_data[component]
            
            # Create consolidated schema item for this component
            move_in_field = None
            move_out_field = None
            
            for cf in component_fields:
                if cf['comment_type'] == 'move_in':
                    move_in_field = cf['field']
                elif cf['comment_type'] == 'move_out':
                    move_out_field = cf['field']
            
            if move_in_field and move_out_field:
                # Both move-in and move-out comments - create consolidated item
                display_name = format_display_name(component)
                
                schema_item = {
                    'unique_id': f'{room}_{component}_comments',
                    'pdf_attributes': [{
                        'formType': 'residential_lease_inventory_and_condition',
                        'formfield': move_in_field['field_name'],
                        'linked_form_fields_text': [move_out_field['field_name']]
                    }],
                    'display_attributes': {
                        'display_name': f'{display_name} Comments',
                        'input_type': 'text-area',
                        'description': f'Move-in and move-out comments for {room} room {component.lower()}',
                        'order': order,
                        'block': f'{room}_room',
                        'placeholder': f'Enter comments about {component.lower()} condition...',
                        'width': 12,
                        'value': {'type': 'manual'},
                        'isRequired': False
                    }
                }
                
                schema_items.append(schema_item)
                
                consolidation_report.append({
                    'consolidated_field': f'{room}_{component}_comments',
                    'source_fields': [move_in_field['field_name'], move_out_field['field_name']],
                    'consolidation_type': 'text_continuation',
                    'reasoning': f'Move-in and move-out comments for {room} room {component} consolidated into single text area'
                })
                
            elif move_in_field:
                # Only move-in comment
                display_name = format_display_name(component)
                
                schema_item = {
                    'unique_id': f'{room}_{component}_move_in_comments',
                    'pdf_attributes': [{
                        'formType': 'residential_lease_inventory_and_condition',
                        'formfield': move_in_field['field_name']
                    }],
                    'display_attributes': {
                        'display_name': f'{display_name} Move-In Comments',
                        'input_type': 'text-area',
                        'order': order,
                        'block': f'{room}_room',
                        'placeholder': f'Enter move-in comments about {component.lower()}...',
                        'width': 12,
                        'value': {'type': 'manual'},
                        'isRequired': False
                    }
                }
                
                schema_items.append(schema_item)
                
            elif move_out_field:
                # Only move-out comment
                display_name = format_display_name(component)
                
                schema_item = {
                    'unique_id': f'{room}_{component}_move_out_comments',
                    'pdf_attributes': [{
                        'formType': 'residential_lease_inventory_and_condition',
                        'formfield': move_out_field['field_name']
                    }],
                    'display_attributes': {
                        'display_name': f'{display_name} Move-Out Comments',
                        'input_type': 'text-area',
                        'order': order,
                        'block': f'{room}_room',
                        'placeholder': f'Enter move-out comments about {component.lower()}...',
                        'width': 12,
                        'value': {'type': 'manual'},
                        'isRequired': False
                    }
                }
                
                schema_items.append(schema_item)
            
            order += 1
    
    return schema_items, consolidation_report

def format_display_name(component):
    """Format component name for display."""
    # Handle special cases
    component_names = {
        'ceilings': 'Ceilings',
        'ceiling': 'Ceiling',
        'paint': 'Paint',
        'doors': 'Doors',
        'door': 'Door',
        'door_locks': 'Door Locks',
        'flooring': 'Flooring',
        'lights': 'Lights',
        'windows': 'Windows',
        'window_latches': 'Window Latches',
        'plugs': 'Electrical Plugs',
        'fireplace': 'Fireplace',
        'drapes': 'Drapes',
        'cabinets': 'Cabinets',
        'closet': 'Closet',
        'other': 'Other'
    }
    
    return component_names.get(component, component.title())

def generate_typescript_schema(schema_items):
    """Generate TypeScript schema code."""
    
    typescript_code = '''import { SchemaItem } from "../../../../types/realtor";

export const livingAreasPartialSchema: SchemaItem[] = [
'''
    
    for i, item in enumerate(schema_items):
        # Convert to TypeScript format
        typescript_code += '  {\n'
        typescript_code += f'    unique_id: "{item["unique_id"]}",\n'
        typescript_code += '    pdf_attributes: [\n'
        
        for pdf_attr in item['pdf_attributes']:
            typescript_code += '      {\n'
            typescript_code += f'        formType: "{pdf_attr["formType"]}",\n'
            typescript_code += f'        formfield: "{pdf_attr["formfield"]}"'
            
            if 'linked_form_fields_text' in pdf_attr:
                typescript_code += ',\n        linked_form_fields_text: [\n'
                for linked_field in pdf_attr['linked_form_fields_text']:
                    typescript_code += f'          "{linked_field}",\n'
                typescript_code = typescript_code.rstrip(',\n') + '\n        ]'
            
            typescript_code += '\n      }'
        
        typescript_code += '\n    ],\n'
        typescript_code += '    display_attributes: {\n'
        
        disp_attr = item['display_attributes']
        typescript_code += f'      display_name: "{disp_attr["display_name"]}",\n'
        typescript_code += f'      input_type: "{disp_attr["input_type"]}",\n'
        
        if 'description' in disp_attr:
            typescript_code += f'      description: "{disp_attr["description"]}",\n'
        
        typescript_code += f'      order: {disp_attr["order"]},\n'
        
        if 'block' in disp_attr:
            typescript_code += f'      block: "{disp_attr["block"]}",\n'
        
        if 'block_style' in disp_attr:
            block_style = disp_attr['block_style']
            typescript_code += '      block_style: {\n'
            typescript_code += f'        title: "{block_style["title"]}",\n'
            typescript_code += f'        description: "{block_style["description"]}",\n'
            typescript_code += f'        icon: "{block_style["icon"]}",\n'
            typescript_code += f'        color_theme: "{block_style["color_theme"]}"\n'
            typescript_code += '      },\n'
        
        if 'placeholder' in disp_attr:
            typescript_code += f'      placeholder: "{disp_attr["placeholder"]}",\n'
        
        typescript_code += f'      width: {disp_attr["width"]},\n'
        typescript_code += f'      value: {{ type: "{disp_attr["value"]["type"]}" }},\n'
        typescript_code += f'      isRequired: {str(disp_attr.get("isRequired", False)).lower()}'
        
        if 'breakBefore' in disp_attr:
            typescript_code += f',\n      breakBefore: {str(disp_attr["breakBefore"]).lower()}'
        
        typescript_code += '\n    }'
        
        if i < len(schema_items) - 1:
            typescript_code += '\n  },\n'
        else:
            typescript_code += '\n  }\n'
    
    typescript_code += '];\n'
    
    return typescript_code

def main():
    """Main function to generate living areas schema."""
    
    print("Analyzing living areas fields...")
    schema_items, consolidation_report = analyze_living_areas_fields()
    
    print(f"Generated {len(schema_items)} schema items")
    print(f"Consolidated {len(consolidation_report)} field relationships")
    
    # Generate TypeScript schema
    typescript_schema = generate_typescript_schema(schema_items)
    
    # Write schema file
    with open('/Users/arvin/WebDev/field_extraction/living_areas_partial_schema.ts', 'w') as f:
        f.write(typescript_schema)
    
    # Write consolidation report
    report_content = "# Living Areas Fields Consolidation Report\n\n"
    report_content += f"## Summary\n\n"
    report_content += f"- **Total source fields**: 78\n"
    report_content += f"- **Final schema items**: {len(schema_items)}\n"
    report_content += f"- **Consolidations performed**: {len(consolidation_report)}\n\n"
    
    report_content += "## Field Structure\n\n"
    report_content += "### Room Breakdown:\n"
    report_content += "- **Living Room**: 26 fields (13 move-in + 13 move-out)\n"
    report_content += "- **Dining Room**: 24 fields (12 move-in + 12 move-out)\n"
    report_content += "- **Family Room**: 28 fields (14 move-in + 14 move-out)\n\n"
    
    report_content += "## Consolidation Details\n\n"
    
    for i, consolidation in enumerate(consolidation_report, 1):
        report_content += f"### {i}. {consolidation['consolidated_field']}\n"
        report_content += f"- **Type**: {consolidation['consolidation_type']}\n"
        report_content += f"- **Source Fields**: {', '.join(consolidation['source_fields'])}\n"
        report_content += f"- **Reasoning**: {consolidation['reasoning']}\n\n"
    
    report_content += "## Schema Structure\n\n"
    report_content += "The generated schema creates logical groupings by room:\n\n"
    
    living_count = sum(1 for item in schema_items if 'living' in item['unique_id'])
    dining_count = sum(1 for item in schema_items if 'dining' in item['unique_id'])
    family_count = sum(1 for item in schema_items if 'family' in item['unique_id'])
    
    report_content += f"- **Living Room Block**: {living_count} items\n"
    report_content += f"- **Dining Room Block**: {dining_count} items\n"
    report_content += f"- **Family Room Block**: {family_count} items\n\n"
    
    report_content += "Each room includes standardized components:\n"
    report_content += "- Ceiling/Ceilings\n"
    report_content += "- Paint\n"
    report_content += "- Doors/Door\n"
    report_content += "- Door Locks\n"
    report_content += "- Flooring\n"
    report_content += "- Lights\n"
    report_content += "- Windows\n"
    report_content += "- Window Latches\n"
    report_content += "- Drapes\n"
    report_content += "- Electrical Plugs\n"
    report_content += "- Cabinets\n"
    report_content += "- Room-specific: Fireplace (Living/Family), Closet (Family)\n"
    report_content += "- Other\n\n"
    
    report_content += "## Key Features\n\n"
    report_content += "- **Text Continuation**: Move-in and move-out comments consolidated into single text areas\n"
    report_content += "- **Logical Grouping**: Fields organized by room with appropriate styling\n"
    report_content += "- **User-Friendly Labels**: Technical field names converted to readable display names\n"
    report_content += "- **Consistent Layout**: All comment fields use text-area input type with 12-unit width\n"
    report_content += "- **Manual Value Type**: All fields use manual input without output field\n\n"
    
    with open('/Users/arvin/WebDev/field_extraction/living_areas_consolidation_report.md', 'w') as f:
        f.write(report_content)
    
    print(f"\nFiles generated:")
    print(f"- Schema: /Users/arvin/WebDev/field_extraction/living_areas_partial_schema.ts")
    print(f"- Report: /Users/arvin/WebDev/field_extraction/living_areas_consolidation_report.md")
    
    return schema_items, consolidation_report

if __name__ == "__main__":
    main()