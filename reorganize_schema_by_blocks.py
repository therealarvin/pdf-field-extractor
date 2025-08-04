#!/usr/bin/env python3
"""
Reorganize Schema by Blocks
Groups schema items by their block while maintaining relative order within each block
"""

import json
import argparse
from pathlib import Path
from typing import List, Dict, Tuple
from collections import OrderedDict


def extract_block_info(schema_item: Dict) -> Tuple[str, Dict]:
    """
    Extract block name and style from a schema item
    
    Returns:
        Tuple of (block_name, block_style)
    """
    display_attrs = schema_item.get('display_attributes', {})
    block_name = display_attrs.get('block', 'Unknown Block')
    block_style = display_attrs.get('block_style', {})
    
    return block_name, block_style


def group_schema_by_blocks(schema_items: List[Dict]) -> OrderedDict:
    """
    Group schema items by their blocks while maintaining order
    
    Args:
        schema_items: List of schema items
        
    Returns:
        OrderedDict with block names as keys and lists of items as values
    """
    # Use OrderedDict to maintain block order based on first appearance
    blocks = OrderedDict()
    
    for item in schema_items:
        block_name, block_style = extract_block_info(item)
        
        if block_name not in blocks:
            blocks[block_name] = {
                'style': block_style,
                'items': []
            }
        
        blocks[block_name]['items'].append(item)
    
    return blocks


def reorganize_schema(schema_items: List[Dict]) -> List[Dict]:
    """
    Reorganize schema items grouped by blocks
    
    Args:
        schema_items: Original list of schema items
        
    Returns:
        Reorganized list with items grouped by blocks
    """
    # Group by blocks
    blocks = group_schema_by_blocks(schema_items)
    
    # Rebuild the list with grouped items
    reorganized = []
    
    for block_name, block_data in blocks.items():
        # Add all items from this block
        reorganized.extend(block_data['items'])
    
    # Reassign order numbers to maintain sequential ordering
    for i, item in enumerate(reorganized, 1):
        if 'display_attributes' in item:
            item['display_attributes']['order'] = i
    
    return reorganized


def print_block_summary(blocks: OrderedDict):
    """Print a summary of blocks and their item counts"""
    print("\n" + "="*60)
    print("BLOCK ORGANIZATION SUMMARY")
    print("="*60)
    
    total_items = 0
    for block_name, block_data in blocks.items():
        item_count = len(block_data['items'])
        total_items += item_count
        
        style = block_data['style']
        icon = style.get('icon', 'file')
        color = style.get('color_theme', 'gray')
        
        print(f"\n{block_name}:")
        print(f"  - Icon: {icon}")
        print(f"  - Color: {color}")
        print(f"  - Items: {item_count}")
        
        # Show first few items
        for i, item in enumerate(block_data['items'][:3]):
            display_attrs = item.get('display_attributes', {})
            print(f"    {i+1}. {display_attrs.get('display_name', 'Unknown')} ({item.get('unique_id', 'unknown')})")
        
        if item_count > 3:
            print(f"    ... and {item_count - 3} more")
    
    print(f"\nTotal items: {total_items}")
    print("="*60 + "\n")


def process_typescript_file(file_path: str, output_path: str = None):
    """
    Process a TypeScript schema file and reorganize by blocks
    
    Args:
        file_path: Path to the TypeScript schema file
        output_path: Optional output path (defaults to _reorganized suffix)
    """
    # Read the TypeScript file
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract the schema array
    # Look for the schema array between [ and ];
    start_marker = "SchemaItem[] = ["
    end_marker = "\n];"
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("Error: Could not find schema array in file")
        return
    
    start_idx += len(start_marker)
    end_idx = content.rfind(end_marker)
    
    if end_idx == -1:
        print("Error: Could not find end of schema array")
        return
    
    # Extract the JSON array content
    array_content = content[start_idx:end_idx]
    
    # Parse the JSON
    try:
        # Remove any trailing commas before parsing
        import re
        array_content = re.sub(r',(\s*})', r'\1', array_content)
        array_content = re.sub(r',(\s*])', r'\1', array_content)
        
        schema_items = json.loads('[' + array_content + ']')
    except json.JSONDecodeError as e:
        print(f"Error parsing schema JSON: {e}")
        print("Attempting to fix common issues...")
        
        # Try to fix by evaluating as Python literal
        try:
            import ast
            schema_items = ast.literal_eval('[' + array_content + ']')
        except Exception as e2:
            print(f"Failed to parse schema: {e2}")
            return
    
    # Group by blocks for summary
    blocks = group_schema_by_blocks(schema_items)
    print_block_summary(blocks)
    
    # Reorganize the schema
    reorganized_items = reorganize_schema(schema_items)
    
    # Reconstruct the TypeScript file
    prefix = content[:start_idx]
    suffix = content[end_idx:]
    
    # Convert back to JSON with proper formatting
    json_items = []
    for item in reorganized_items:
        item_json = json.dumps(item, indent=2)
        # Indent each line by 2 spaces
        indented_json = '\n'.join('  ' + line for line in item_json.split('\n'))
        json_items.append(indented_json)
    
    # Join with commas
    new_array_content = ',\n'.join(json_items)
    
    # Reconstruct the full content
    new_content = prefix + '\n' + new_array_content + suffix
    
    # Determine output path
    if not output_path:
        input_path = Path(file_path)
        output_path = input_path.parent / f"{input_path.stem}_reorganized{input_path.suffix}"
    
    # Write the reorganized file
    with open(output_path, 'w') as f:
        f.write(new_content)
    
    print(f"\nReorganized schema saved to: {output_path}")


def process_json_file(file_path: str, output_path: str = None):
    """
    Process a JSON schema file and reorganize by blocks
    
    Args:
        file_path: Path to the JSON schema file
        output_path: Optional output path (defaults to _reorganized suffix)
    """
    # Read the JSON file
    with open(file_path, 'r') as f:
        schema_items = json.load(f)
    
    # Ensure it's a list
    if not isinstance(schema_items, list):
        print("Error: JSON file must contain an array of schema items")
        return
    
    # Group by blocks for summary
    blocks = group_schema_by_blocks(schema_items)
    print_block_summary(blocks)
    
    # Reorganize the schema
    reorganized_items = reorganize_schema(schema_items)
    
    # Determine output path
    if not output_path:
        input_path = Path(file_path)
        output_path = input_path.parent / f"{input_path.stem}_reorganized{input_path.suffix}"
    
    # Write the reorganized file
    with open(output_path, 'w') as f:
        json.dump(reorganized_items, f, indent=2)
    
    print(f"\nReorganized schema saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Reorganize schema items by grouping them by blocks'
    )
    parser.add_argument(
        'schema_file',
        help='Path to the schema file (.ts or .json)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file path (default: adds _reorganized suffix)'
    )
    parser.add_argument(
        '--preserve-order',
        action='store_true',
        help='Preserve original order numbers instead of reassigning'
    )
    
    args = parser.parse_args()
    
    # Check if file exists
    if not Path(args.schema_file).exists():
        print(f"Error: File not found: {args.schema_file}")
        return
    
    # Determine file type and process accordingly
    file_path = Path(args.schema_file)
    
    if file_path.suffix == '.ts':
        process_typescript_file(args.schema_file, args.output)
    elif file_path.suffix == '.json':
        process_json_file(args.schema_file, args.output)
    else:
        print(f"Error: Unsupported file type: {file_path.suffix}")
        print("Supported types: .ts (TypeScript), .json")


if __name__ == "__main__":
    main()