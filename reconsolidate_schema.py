#!/usr/bin/env python3
"""
Reconsolidate Schema
Re-runs consolidation on an already consolidated schema, particularly useful for checkbox grouping
"""

import json
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from collections import defaultdict
import re


class SchemaReconsolidator:
    def __init__(self, interactive_mode: bool = False):
        self.field_mapping = {}  # Track all PDF fields to ensure none are lost
        self.interactive_mode = interactive_mode
        
    def parse_typescript_schema(self, file_path: str) -> List[Dict]:
        """Parse TypeScript schema file and extract schema items"""
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Extract the schema array
        start_marker = "SchemaItem[] = ["
        end_marker = "\n];"
        
        start_idx = content.find(start_marker)
        if start_idx == -1:
            raise ValueError("Could not find schema array in file")
        
        start_idx += len(start_marker)
        end_idx = content.rfind(end_marker)
        
        if end_idx == -1:
            raise ValueError("Could not find end of schema array")
        
        # Extract and parse JSON
        array_content = content[start_idx:end_idx]
        
        # Remove trailing commas
        array_content = re.sub(r',(\s*})', r'\1', array_content)
        array_content = re.sub(r',(\s*])', r'\1', array_content)
        
        try:
            schema_items = json.loads('[' + array_content + ']')
        except json.JSONDecodeError:
            # Try as Python literal
            import ast
            schema_items = ast.literal_eval('[' + array_content + ']')
        
        return schema_items
    
    def extract_all_pdf_fields(self, schema_items: List[Dict]) -> Dict[str, str]:
        """Extract all PDF fields to ensure we don't lose any"""
        pdf_fields = {}
        
        for item in schema_items:
            for pdf_attr in item.get('pdf_attributes', []):
                field_name = pdf_attr.get('formfield')
                if field_name:
                    pdf_fields[field_name] = item.get('unique_id', 'unknown')
        
        return pdf_fields
    
    def identify_checkbox_consolidation_opportunities(self, schema_items: List[Dict]) -> Dict[str, List[Dict]]:
        """Identify checkboxes that could be consolidated"""
        checkbox_groups = defaultdict(list)
        
        # Collect all checkbox items
        checkbox_items = []
        for item in schema_items:
            display_attrs = item.get('display_attributes', {})
            if display_attrs.get('input_type') == 'checkbox':
                # Check if it's already consolidated (has multiple pdf_attributes)
                if len(item.get('pdf_attributes', [])) == 1:
                    checkbox_items.append(item)
        
        print(f"Found {len(checkbox_items)} individual checkbox items")
        
        # Group by various strategies
        
        # Strategy 1: Group by unique_id pattern
        for item in checkbox_items:
            unique_id = item.get('unique_id', '')
            display_attrs = item.get('display_attributes', {})
            
            # Remove trailing numbers to find base
            base_id = re.sub(r'_\d+$', '', unique_id)
            base_id = re.sub(r'\d+$', '', base_id).rstrip('_')
            
            if base_id and base_id != unique_id:
                checkbox_groups[f"uid_{base_id}"].append(item)
        
        # Strategy 2: Group by block and attribute
        block_attr_groups = defaultdict(list)
        for item in checkbox_items:
            display_attrs = item.get('display_attributes', {})
            block = display_attrs.get('block', 'Unknown')
            attribute = display_attrs.get('attribute', 'unknown')
            key = f"{block}_{attribute}"
            block_attr_groups[key].append(item)
        
        # Add block groups that have multiple items
        for key, items in block_attr_groups.items():
            if len(items) > 1:
                # Check if they're semantically related
                display_names = [item.get('display_attributes', {}).get('display_name', '') for item in items]
                if self._are_semantically_related(display_names):
                    # In interactive mode, ask the user
                    if self.interactive_mode and not self._ask_user_about_grouping(items):
                        continue  # Skip grouping if user says no
                    checkbox_groups[f"block_{key}"].append(items)
        
        # Remove groups with only one item and flatten
        final_groups = {}
        for key, groups in checkbox_groups.items():
            if isinstance(groups[0], list):
                # Flatten nested groups
                all_items = []
                for group in groups:
                    all_items.extend(group)
                if len(all_items) > 1:
                    final_groups[key] = all_items
            elif len(groups) > 1:
                final_groups[key] = groups
        
        return final_groups
    
    def _are_semantically_related(self, names: List[str]) -> bool:
        """Check if checkbox names are semantically related"""
        # Simple heuristic: check for common words
        if len(names) < 2:
            return False
        
        # Extract words from each name
        word_sets = []
        for name in names:
            words = set(name.lower().split())
            # Remove common words
            words -= {'the', 'a', 'an', 'is', 'are', 'of', 'for', 'to', 'in', 'on', 'with'}
            word_sets.append(words)
        
        # Check for common words across all names
        if word_sets:
            common_words = word_sets[0]
            for word_set in word_sets[1:]:
                common_words &= word_set
            
            # If there's at least one meaningful common word
            return len(common_words) > 0
        
        return False
    
    def _ask_user_about_grouping(self, checkboxes: List[Dict]) -> bool:
        """Ask user whether checkboxes should be grouped together"""
        if not self.interactive_mode:
            return True  # Default to grouping if not in interactive mode
        
        print("\n" + "="*60)
        print("CHECKBOX GROUPING DECISION NEEDED")
        print("="*60)
        print("\nShould these checkboxes be grouped together as options in a single field?\n")
        
        for i, item in enumerate(checkboxes, 1):
            display_attrs = item.get('display_attributes', {})
            print(f"{i}. {display_attrs.get('display_name', 'Unknown')} (ID: {item.get('unique_id', 'unknown')})")
            if display_attrs.get('description'):
                print(f"   Description: {display_attrs['description']}")
        
        print("\nThey are all in the block:", checkboxes[0].get('display_attributes', {}).get('block', 'Unknown'))
        
        while True:
            response = input("\nGroup these checkboxes together? (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")
    
    def consolidate_checkbox_group(self, checkbox_items: List[Dict]) -> Dict:
        """Consolidate a group of checkboxes into one item"""
        if not checkbox_items:
            return None
        
        # Use first item as base
        base_item = checkbox_items[0].copy()
        base_display = base_item.get('display_attributes', {}).copy()
        
        # Collect all options and linked checkbox fields
        options = []
        linked_checkbox_fields = []
        
        for item in checkbox_items:
            display_attrs = item.get('display_attributes', {})
            pdf_attrs = item.get('pdf_attributes', [])
            
            # Get the checkbox field name from pdf_attributes
            field_name = None
            if pdf_attrs and len(pdf_attrs) > 0:
                field_name = pdf_attrs[0].get('formfield')
            
            if field_name:
                # Create linked checkbox field entry
                linked_checkbox_fields.append({
                    'checkboxField': field_name,
                    'displayName': display_attrs.get('display_name', 'Option')
                })
            
            # Create option from this checkbox
            option = {
                'display_name': display_attrs.get('display_name', 'Option'),
                'databaseStored': self._to_database_stored(display_attrs.get('display_name', 'OPTION'))
            }
            
            # Check if it already has options (shouldn't happen for individual checkboxes)
            if 'checkbox_options' in display_attrs:
                existing = display_attrs['checkbox_options'].get('options', [])
                if existing:
                    options.extend(existing)
                else:
                    options.append(option)
            else:
                options.append(option)
        
        # Remove duplicate options
        seen = set()
        unique_options = []
        for opt in options:
            key = opt['databaseStored']
            if key not in seen:
                seen.add(key)
                unique_options.append(opt)
        
        # Update the display attributes
        base_display['checkbox_options'] = {
            'options': unique_options
        }
        
        # Find common theme for display name
        display_names = [item.get('display_attributes', {}).get('display_name', '') for item in checkbox_items]
        common_theme = self._find_common_theme(display_names)
        if common_theme and common_theme != "Options":
            base_display['display_name'] = common_theme
        
        # Create consolidated pdf_attributes with linked_form_fields_checkbox
        base_pdf_attrs = base_item.get('pdf_attributes', [])
        if base_pdf_attrs and len(base_pdf_attrs) > 0:
            form_type = base_pdf_attrs[0].get('formType', 'unknown_form')
            first_field = base_pdf_attrs[0].get('formfield', '')
            
            # Create new pdf_attributes with linked checkboxes
            new_pdf_attributes = [{
                'formType': form_type,
                'formfield': first_field,
                'linked_form_fields_checkbox': linked_checkbox_fields
            }]
            
            base_item['pdf_attributes'] = new_pdf_attributes
        
        # Update the consolidated item
        base_item['display_attributes'] = base_display
        
        return base_item
    
    def _to_database_stored(self, display_name: str) -> str:
        """Convert to UPPERCASE_SNAKE_CASE"""
        cleaned = re.sub(r'[^\w\s]', '', display_name)
        words = cleaned.upper().split()
        return '_'.join(words)
    
    def _find_common_theme(self, names: List[str]) -> str:
        """Find common theme in names"""
        if not names:
            return "Options"
        
        # Count word frequencies
        from collections import Counter
        all_words = []
        
        for name in names:
            words = [w.lower() for w in name.split() if len(w) > 2]
            all_words.extend(words)
        
        word_counts = Counter(all_words)
        common_words = [word for word, count in word_counts.items() if count > 1]
        
        if common_words:
            # Take top 2 most common words
            top_words = sorted(common_words, key=lambda w: word_counts[w], reverse=True)[:2]
            return ' '.join(w.capitalize() for w in top_words)
        
        return "Options"
    
    def reconsolidate_schema(self, schema_items: List[Dict]) -> Tuple[List[Dict], Dict[str, List[str]]]:
        """Reconsolidate schema items"""
        # Track all original PDF fields
        original_fields = self.extract_all_pdf_fields(schema_items)
        print(f"Total PDF fields before reconsolidation: {len(original_fields)}")
        
        # Find consolidation opportunities
        checkbox_groups = self.identify_checkbox_consolidation_opportunities(schema_items)
        print(f"Found {len(checkbox_groups)} potential checkbox groups to consolidate")
        
        # Track which items to remove
        items_to_remove = set()
        new_consolidated_items = []
        
        # Consolidate each group
        consolidation_report = {}
        for group_key, items in checkbox_groups.items():
            # Get unique IDs of items in this group
            item_ids = [item.get('unique_id', '') for item in items]
            
            # Consolidate the group
            consolidated = self.consolidate_checkbox_group(items)
            if consolidated:
                new_consolidated_items.append(consolidated)
                items_to_remove.update(item_ids)
                
                # Report what was consolidated
                consolidation_report[consolidated.get('unique_id', group_key)] = [
                    f"{item.get('unique_id')} - {item.get('display_attributes', {}).get('display_name', 'Unknown')}"
                    for item in items
                ]
        
        # Build final schema keeping non-consolidated items
        final_schema = []
        for item in schema_items:
            if item.get('unique_id') not in items_to_remove:
                final_schema.append(item)
        
        # Add newly consolidated items
        final_schema.extend(new_consolidated_items)
        
        # Verify all fields are preserved
        final_fields = self.extract_all_pdf_fields(final_schema)
        print(f"Total PDF fields after reconsolidation: {len(final_fields)}")
        
        # Check for missing fields
        missing_fields = set(original_fields.keys()) - set(final_fields.keys())
        if missing_fields:
            print(f"WARNING: Missing fields after reconsolidation: {missing_fields}")
        
        # Re-sort and renumber
        final_schema.sort(key=lambda x: (
            x.get('display_attributes', {}).get('order', 999),
            x.get('unique_id', '')
        ))
        
        for i, item in enumerate(final_schema, 1):
            if 'display_attributes' in item:
                item['display_attributes']['order'] = i
        
        return final_schema, consolidation_report


def main():
    parser = argparse.ArgumentParser(
        description='Re-consolidate an existing schema, particularly for checkbox grouping'
    )
    parser.add_argument('schema_file', help='Path to TypeScript schema file')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('--report', action='store_true', help='Generate consolidation report')
    parser.add_argument('--interactive', action='store_true', help='Enable interactive mode for grouping decisions')
    
    args = parser.parse_args()
    
    # Check file exists
    if not Path(args.schema_file).exists():
        print(f"Error: File not found: {args.schema_file}")
        return
    
    reconsolidator = SchemaReconsolidator(interactive_mode=args.interactive)
    
    try:
        # Parse schema
        print(f"Parsing schema from {args.schema_file}...")
        schema_items = reconsolidator.parse_typescript_schema(args.schema_file)
        print(f"Found {len(schema_items)} schema items")
        
        # Reconsolidate
        print("\nReconsolidating...")
        reconsolidated, report = reconsolidator.reconsolidate_schema(schema_items)
        
        print(f"\nReconsolidation complete:")
        print(f"- Original items: {len(schema_items)}")
        print(f"- Final items: {len(reconsolidated)}")
        print(f"- Reduction: {len(schema_items) - len(reconsolidated)} items")
        
        # Print report if requested
        if args.report and report:
            print("\nConsolidation Report:")
            print("="*60)
            for consolidated_id, original_items in report.items():
                print(f"\n{consolidated_id}:")
                for item in original_items:
                    print(f"  - {item}")
        
        # Write output
        output_path = args.output or args.schema_file.replace('.ts', '_reconsolidated.ts')
        
        # Read original file to preserve structure
        with open(args.schema_file, 'r') as f:
            original_content = f.read()
        
        # Find the array boundaries
        start_marker = "SchemaItem[] = ["
        end_marker = "\n];"
        start_idx = original_content.find(start_marker) + len(start_marker)
        end_idx = original_content.rfind(end_marker)
        
        # Convert reconsolidated items to JSON
        json_items = []
        for item in reconsolidated:
            item_json = json.dumps(item, indent=2)
            indented_json = '\n'.join('  ' + line for line in item_json.split('\n'))
            json_items.append(indented_json)
        
        new_array_content = ',\n'.join(json_items)
        
        # Reconstruct file
        new_content = original_content[:start_idx] + '\n' + new_array_content + original_content[end_idx:]
        
        with open(output_path, 'w') as f:
            f.write(new_content)
        
        print(f"\nReconsolidated schema saved to: {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()