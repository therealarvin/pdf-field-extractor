#!/usr/bin/env python3
"""
Detect and Remove Duplicate Schema Items
Finds duplicate unique_ids and display_names in TypeScript schema files
Automatically removes exact duplicate items
"""

import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional, Any
from collections import defaultdict
import hashlib


class SchemaDuplicateDetector:
    def __init__(self, auto_fix: bool = False):
        self.unique_ids = defaultdict(list)
        self.display_names = defaultdict(list)
        self.schema_items = []
        self.auto_fix = auto_fix
        self.files_to_fix = {}
        
    def normalize_item_string(self, item_str: str) -> str:
        """Normalize item string for comparison by removing whitespace variations"""
        # Remove extra whitespace, newlines, and normalize quotes
        normalized = re.sub(r'\s+', ' ', item_str)
        normalized = normalized.strip()
        return normalized
    
    def get_item_hash(self, item_str: str) -> str:
        """Get hash of normalized item for exact duplicate detection"""
        normalized = self.normalize_item_string(item_str)
        return hashlib.md5(normalized.encode()).hexdigest()
    
    def extract_schema_from_typescript(self, file_path: str) -> Tuple[List[Dict], str, str, str]:
        """Extract schema items from TypeScript file"""
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Store original content for fixing
        self.files_to_fix[file_path] = content
        
        # Find the schema array
        schema_match = re.search(r'(export\s+const\s+\w+Schema:\s*SchemaItem\[\]\s*=\s*\[)(.*?)(\];)', 
                                content, re.DOTALL)
        
        if not schema_match:
            raise ValueError(f"Could not find schema array in {file_path}")
        
        prefix = schema_match.group(1)
        schema_content = schema_match.group(2)
        suffix = schema_match.group(3)
        
        # Extract individual schema items
        items = []
        
        # Better pattern for matching schema items
        # This handles nested objects more reliably
        item_matches = []
        brace_count = 0
        current_item_start = None
        
        for i, char in enumerate(schema_content):
            if char == '{':
                if brace_count == 0:
                    current_item_start = i
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0 and current_item_start is not None:
                    item_str = schema_content[current_item_start:i+1]
                    item_matches.append((current_item_start, i+1, item_str))
        
        for start_pos, end_pos, item_str in item_matches:
            # Extract unique_id
            unique_id_match = re.search(r'"unique_id"\s*:\s*"([^"]+)"', item_str)
            unique_id = unique_id_match.group(1) if unique_id_match else None
            
            # Extract display_name from display_attributes
            display_name_match = re.search(r'"display_name"\s*:\s*"([^"]+)"', item_str)
            display_name = display_name_match.group(1) if display_name_match else None
            
            # Extract the PDF attributes to help identify the item
            pdf_formfield_matches = re.findall(r'"formfield"\s*:\s*"([^"]+)"', item_str)
            
            if unique_id or display_name:
                items.append({
                    'unique_id': unique_id,
                    'display_name': display_name,
                    'formfields': pdf_formfield_matches,
                    'item_str': item_str,
                    'item_hash': self.get_item_hash(item_str),
                    'start_pos': start_pos,
                    'end_pos': end_pos
                })
        
        return items, prefix, schema_content, suffix
    
    def analyze_file(self, file_path: str) -> None:
        """Analyze a single TypeScript schema file"""
        print(f"\nAnalyzing: {file_path}")
        
        try:
            items, prefix, schema_content, suffix = self.extract_schema_from_typescript(file_path)
            
            for idx, item in enumerate(items):
                # Track unique_ids
                if item['unique_id']:
                    self.unique_ids[item['unique_id']].append({
                        'file': file_path,
                        'index': idx,
                        'display_name': item['display_name'],
                        'formfields': item['formfields'],
                        'item_hash': item['item_hash'],
                        'item_str': item['item_str'],
                        'start_pos': item['start_pos'],
                        'end_pos': item['end_pos']
                    })
                
                # Track display_names
                if item['display_name']:
                    self.display_names[item['display_name']].append({
                        'file': file_path,
                        'index': idx,
                        'unique_id': item['unique_id'],
                        'formfields': item['formfields'],
                        'item_hash': item['item_hash']
                    })
                
                self.schema_items.append({
                    'file': file_path,
                    'index': idx,
                    'prefix': prefix,
                    'schema_content': schema_content,
                    'suffix': suffix,
                    **item
                })
            
            print(f"  Found {len(items)} schema items")
            
        except Exception as e:
            print(f"  Error analyzing file: {e}")
    
    def find_duplicates(self) -> Dict[str, Any]:
        """Find all duplicates and identify exact duplicates"""
        duplicate_unique_ids = {}
        exact_duplicates = {}
        
        for uid, locations in self.unique_ids.items():
            if len(locations) > 1:
                duplicate_unique_ids[uid] = locations
                
                # Check if all instances are exact duplicates
                hashes = set(loc['item_hash'] for loc in locations)
                if len(hashes) == 1:
                    # All items with this unique_id are exactly the same
                    exact_duplicates[uid] = locations
        
        duplicate_display_names = {
            name: locations 
            for name, locations in self.display_names.items() 
            if len(locations) > 1
        }
        
        return {
            'unique_ids': duplicate_unique_ids,
            'display_names': duplicate_display_names,
            'exact_duplicates': exact_duplicates
        }
    
    def print_report(self, duplicates: Dict[str, List]) -> None:
        """Print duplicate report"""
        print("\n" + "="*60)
        print("DUPLICATE DETECTION REPORT")
        print("="*60)
        
        # Report exact duplicates that can be auto-fixed
        if duplicates.get('exact_duplicates'):
            print(f"\n🔧 EXACT DUPLICATES (can be auto-fixed) ({len(duplicates['exact_duplicates'])} found):")
            print("-"*60)
            
            for uid, locations in sorted(duplicates['exact_duplicates'].items()):
                print(f"\n• unique_id: '{uid}' has {len(locations)} identical copies:")
                for i, loc in enumerate(locations):
                    status = "KEEP" if i == 0 else "REMOVE"
                    print(f"  [{status}] File: {Path(loc['file']).name}, Index: {loc['index']}")
        
        # Report duplicate unique_ids
        if duplicates['unique_ids']:
            non_exact_count = len(duplicates['unique_ids']) - len(duplicates.get('exact_duplicates', {}))
            if non_exact_count > 0:
                print(f"\n🔴 DUPLICATE UNIQUE IDs (different content) ({non_exact_count} found):")
                print("-"*60)
                
                for uid, locations in sorted(duplicates['unique_ids'].items()):
                    if uid not in duplicates.get('exact_duplicates', {}):
                        print(f"\n• unique_id: '{uid}' appears {len(locations)} times with DIFFERENT content:")
                        for loc in locations:
                            print(f"  - File: {Path(loc['file']).name}")
                            print(f"    Index: {loc['index']}")
                            print(f"    Display Name: {loc['display_name']}")
                            if loc['formfields']:
                                print(f"    Form Fields: {', '.join(loc['formfields'][:3])}")
        else:
            print("\n✅ No duplicate unique_ids found")
        
        # Report duplicate display_names
        if duplicates['display_names']:
            print(f"\n⚠️  DUPLICATE DISPLAY NAMES ({len(duplicates['display_names'])} found):")
            print("-"*60)
            
            for name, locations in sorted(duplicates['display_names'].items()):
                # Check if they have different unique_ids (more problematic)
                unique_ids = set(loc['unique_id'] for loc in locations if loc['unique_id'])
                
                if len(unique_ids) > 1:
                    print(f"\n• display_name: '{name}' appears {len(locations)} times with DIFFERENT unique_ids:")
                else:
                    print(f"\n• display_name: '{name}' appears {len(locations)} times:")
                
                for loc in locations:
                    print(f"  - File: {Path(loc['file']).name}")
                    print(f"    Index: {loc['index']}")
                    print(f"    Unique ID: {loc['unique_id']}")
                    if loc['formfields']:
                        print(f"    Form Fields: {', '.join(loc['formfields'][:3])}")
        else:
            print("\n✅ No duplicate display_names found")
        
        # Summary
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)
        print(f"Total schema items analyzed: {len(self.schema_items)}")
        print(f"Total files analyzed: {len(set(item['file'] for item in self.schema_items))}")
        print(f"Duplicate unique_ids: {len(duplicates['unique_ids'])}")
        print(f"  - Exact duplicates (auto-fixable): {len(duplicates.get('exact_duplicates', {}))}")
        print(f"  - Different content: {len(duplicates['unique_ids']) - len(duplicates.get('exact_duplicates', {}))}")
        print(f"Duplicate display_names: {len(duplicates['display_names'])}")
        
        # Most common display names
        if len(self.display_names) > 10:
            print("\nMost common display_names:")
            sorted_names = sorted(self.display_names.items(), 
                                key=lambda x: len(x[1]), reverse=True)[:10]
            for name, locations in sorted_names:
                if len(locations) > 1:
                    print(f"  - '{name}': {len(locations)} occurrences")
    
    def format_schema_item(self, item_str: str, max_lines: int = 20) -> str:
        """Format schema item for display"""
        lines = item_str.split('\n')
        if len(lines) > max_lines:
            # Show first and last lines
            result = '\n'.join(lines[:max_lines//2])
            result += '\n    ... (truncated) ...\n'
            result += '\n'.join(lines[-(max_lines//2):])
            return result
        return item_str
    
    def handle_different_content_duplicates(self, duplicates: Dict[str, Any]) -> Dict[str, List]:
        """Handle duplicates with different content by showing them and letting user choose"""
        items_to_remove = defaultdict(list)
        
        # Get non-exact duplicates
        different_content_dups = {}
        for uid, locations in duplicates['unique_ids'].items():
            if uid not in duplicates.get('exact_duplicates', {}):
                different_content_dups[uid] = locations
        
        if not different_content_dups:
            return items_to_remove
        
        print("\n" + "="*60)
        print("RESOLVE DIFFERENT CONTENT DUPLICATES")
        print("="*60)
        print("The following unique_ids have multiple entries with different content.")
        print("You'll need to choose which ones to keep.\n")
        
        for uid, locations in sorted(different_content_dups.items()):
            print(f"\n{'='*60}")
            print(f"DUPLICATE: unique_id = '{uid}'")
            print(f"Found {len(locations)} different versions:")
            print("="*60)
            
            # Show each version
            for i, loc in enumerate(locations):
                print(f"\n[{i+1}] File: {Path(loc['file']).name} (Index: {loc['index']})")
                print(f"    Display Name: {loc['display_name']}")
                if loc['formfields']:
                    print(f"    Form Fields: {', '.join(loc['formfields'])}")
                print("\n    Content:")
                print("    " + "-"*50)
                formatted_content = self.format_schema_item(loc['item_str'])
                # Indent the content
                for line in formatted_content.split('\n'):
                    print(f"    {line}")
                print("    " + "-"*50)
            
            # Ask user which to keep
            print(f"\nWhich version(s) do you want to KEEP? (others will be removed)")
            print(f"Enter numbers separated by commas (e.g., 1,3) or 'all' to keep all, 'skip' to skip:")
            
            while True:
                choice = input("> ").strip().lower()
                
                if choice == 'skip':
                    print("Skipping this duplicate group.")
                    break
                elif choice == 'all':
                    print("Keeping all versions.")
                    break
                else:
                    try:
                        # Parse the numbers
                        if ',' in choice:
                            keep_indices = [int(x.strip()) - 1 for x in choice.split(',')]
                        else:
                            keep_indices = [int(choice.strip()) - 1]
                        
                        # Validate indices
                        if all(0 <= idx < len(locations) for idx in keep_indices):
                            # Mark items for removal (all except the ones to keep)
                            for i, loc in enumerate(locations):
                                if i not in keep_indices:
                                    items_to_remove[loc['file']].append({
                                        'start_pos': loc['start_pos'],
                                        'end_pos': loc['end_pos'],
                                        'unique_id': uid,
                                        'reason': 'user_choice'
                                    })
                            
                            kept_files = [Path(locations[i]['file']).name for i in keep_indices]
                            print(f"✓ Keeping version(s) in: {', '.join(kept_files)}")
                            break
                        else:
                            print("Invalid selection. Please enter valid numbers.")
                    except ValueError:
                        print("Invalid input. Please enter numbers separated by commas, 'all', or 'skip'.")
        
        return items_to_remove
    
    def remove_exact_duplicates(self, duplicates: Dict[str, Any]) -> Dict[str, int]:
        """Remove exact duplicates from files"""
        if not duplicates.get('exact_duplicates'):
            return {}
        
        files_modified = {}
        items_to_remove = defaultdict(list)
        
        # Collect items to remove (keep first occurrence, remove others)
        for uid, locations in duplicates['exact_duplicates'].items():
            # Sort by file and index to ensure consistent ordering
            sorted_locs = sorted(locations, key=lambda x: (x['file'], x['index']))
            
            # Keep first, mark others for removal
            for loc in sorted_locs[1:]:
                items_to_remove[loc['file']].append({
                    'start_pos': loc['start_pos'],
                    'end_pos': loc['end_pos'],
                    'unique_id': uid
                })
        
        # Process each file
        for file_path, removals in items_to_remove.items():
            # Sort removals by position (reverse order to maintain positions)
            removals.sort(key=lambda x: x['start_pos'], reverse=True)
            
            # Get the schema content
            schema_items = [item for item in self.schema_items if item['file'] == file_path]
            if not schema_items:
                continue
            
            # Get file components
            prefix = schema_items[0]['prefix']
            schema_content = schema_items[0]['schema_content']
            suffix = schema_items[0]['suffix']
            
            # Remove duplicates from schema content
            new_content = schema_content
            removed_count = 0
            
            for removal in removals:
                start = removal['start_pos']
                end = removal['end_pos']
                
                # Find if there's a comma after this item
                after_text = new_content[end:].lstrip()
                if after_text.startswith(','):
                    # Remove the comma too
                    end = end + new_content[end:].index(',') + 1
                else:
                    # Check if there's a comma before this item
                    before_text = new_content[:start].rstrip()
                    if before_text.endswith(','):
                        # Remove the comma before
                        start = start - (len(before_text) - before_text.rstrip(',').rstrip().__len__()) - 1
                
                # Remove the item
                new_content = new_content[:start] + new_content[end:]
                removed_count += 1
            
            # Clean up any double commas or trailing commas
            new_content = re.sub(r',\s*,', ',', new_content)
            new_content = re.sub(r',\s*$', '', new_content.strip())
            
            # Write back to file
            if self.auto_fix:
                backup_path = file_path + '.backup'
                with open(backup_path, 'w') as f:
                    f.write(self.files_to_fix[file_path])
                
                with open(file_path, 'w') as f:
                    f.write(prefix + '\n' + new_content + '\n' + suffix)
                
                print(f"\n✅ Fixed {file_path}: Removed {removed_count} duplicate items")
                print(f"   Backup saved to: {backup_path}")
            
            files_modified[file_path] = removed_count
        
        return files_modified
    
    def remove_duplicates(self, items_to_remove: Dict[str, List]) -> Dict[str, int]:
        """Remove specified duplicate items from files"""
        if not items_to_remove:
            return {}
        
        files_modified = {}
        
        # Process each file
        for file_path, removals in items_to_remove.items():
            # Sort removals by position (reverse order to maintain positions)
            removals.sort(key=lambda x: x['start_pos'], reverse=True)
            
            # Get the schema content
            schema_items = [item for item in self.schema_items if item['file'] == file_path]
            if not schema_items:
                continue
            
            # Get file components
            prefix = schema_items[0]['prefix']
            schema_content = schema_items[0]['schema_content']
            suffix = schema_items[0]['suffix']
            
            # Remove duplicates from schema content
            new_content = schema_content
            removed_count = 0
            
            for removal in removals:
                start = removal['start_pos']
                end = removal['end_pos']
                
                # Find if there's a comma after this item
                after_text = new_content[end:].lstrip()
                if after_text.startswith(','):
                    # Remove the comma too
                    end = end + new_content[end:].index(',') + 1
                else:
                    # Check if there's a comma before this item
                    before_text = new_content[:start].rstrip()
                    if before_text.endswith(','):
                        # Remove the comma before
                        start = start - (len(before_text) - before_text.rstrip(',').rstrip().__len__()) - 1
                
                # Remove the item
                new_content = new_content[:start] + new_content[end:]
                removed_count += 1
            
            # Clean up any double commas or trailing commas
            new_content = re.sub(r',\s*,', ',', new_content)
            new_content = re.sub(r',\s*$', '', new_content.strip())
            
            # Write back to file
            if self.auto_fix:
                backup_path = file_path + '.backup'
                with open(backup_path, 'w') as f:
                    f.write(self.files_to_fix[file_path])
                
                with open(file_path, 'w') as f:
                    f.write(prefix + '\n' + new_content + '\n' + suffix)
                
                print(f"\n✅ Fixed {file_path}: Removed {removed_count} duplicate items")
                print(f"   Backup saved to: {backup_path}")
            
            files_modified[file_path] = removed_count
        
        return files_modified
    
    def export_json(self, duplicates: Dict[str, List], output_path: str) -> None:
        """Export duplicates to JSON file"""
        # Remove schema_content from items to avoid huge JSON files
        clean_items = []
        for item in self.schema_items:
            clean_item = {k: v for k, v in item.items() if k not in ['schema_content', 'prefix', 'suffix', 'item_str']}
            clean_items.append(clean_item)
        
        export_data = {
            'summary': {
                'total_items': len(self.schema_items),
                'total_files': len(set(item['file'] for item in self.schema_items)),
                'duplicate_unique_ids': len(duplicates['unique_ids']),
                'exact_duplicates': len(duplicates.get('exact_duplicates', {})),
                'duplicate_display_names': len(duplicates['display_names'])
            },
            'duplicates': {
                'unique_ids': duplicates['unique_ids'],
                'display_names': duplicates['display_names'],
                'exact_duplicates': duplicates.get('exact_duplicates', {})
            },
            'all_items': clean_items
        }
        
        with open(output_path, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        print(f"\nDetailed report exported to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Detect and remove duplicate schema items in TypeScript schema files'
    )
    parser.add_argument(
        'paths', 
        nargs='+',
        help='Path(s) to TypeScript schema files or directories'
    )
    parser.add_argument(
        '--export',
        help='Export detailed results to JSON file'
    )
    parser.add_argument(
        '--ignore-display-names',
        action='store_true',
        help='Only check for duplicate unique_ids, ignore display_names'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Automatically remove exact duplicates (creates .backup files)'
    )
    
    args = parser.parse_args()
    
    # Initialize detector
    detector = SchemaDuplicateDetector(auto_fix=args.fix)
    
    # Collect all TypeScript files
    ts_files = []
    for path in args.paths:
        path_obj = Path(path)
        if path_obj.is_file() and path_obj.suffix == '.ts':
            ts_files.append(path_obj)
        elif path_obj.is_dir():
            # Find all .ts files that look like schema files
            schema_files = list(path_obj.glob('*_schema.ts'))
            schema_files.extend(path_obj.glob('*Schema.ts'))
            ts_files.extend(schema_files)
    
    if not ts_files:
        print("No TypeScript schema files found!")
        return
    
    print(f"Found {len(ts_files)} schema files to analyze")
    
    # Analyze each file
    for ts_file in ts_files:
        detector.analyze_file(str(ts_file))
    
    # Find duplicates
    duplicates = detector.find_duplicates()
    
    # Filter out display name duplicates if requested
    if args.ignore_display_names:
        duplicates['display_names'] = {}
    
    # Print report
    detector.print_report(duplicates)
    
    # Auto-fix if requested
    if args.fix:
        total_fixes_available = len(duplicates.get('exact_duplicates', {}))
        different_content_count = len(duplicates['unique_ids']) - len(duplicates.get('exact_duplicates', {}))
        
        if total_fixes_available > 0 or different_content_count > 0:
            print("\n" + "="*60)
            print("AUTO-FIX MODE")
            print("="*60)
            
            files_modified = {}
            
            # Handle exact duplicates first
            if duplicates.get('exact_duplicates'):
                print(f"\nFound {total_fixes_available} exact duplicate(s) that can be automatically removed.")
                response = input("Do you want to remove exact duplicates? (y/N): ")
                if response.lower() == 'y':
                    exact_dup_removals = defaultdict(list)
                    
                    # Collect exact duplicates to remove
                    for uid, locations in duplicates['exact_duplicates'].items():
                        sorted_locs = sorted(locations, key=lambda x: (x['file'], x['index']))
                        for loc in sorted_locs[1:]:
                            exact_dup_removals[loc['file']].append({
                                'start_pos': loc['start_pos'],
                                'end_pos': loc['end_pos'],
                                'unique_id': uid
                            })
                    
                    # Remove them
                    exact_files_modified = detector.remove_duplicates(exact_dup_removals)
                    files_modified.update(exact_files_modified)
            
            # Handle different content duplicates
            if different_content_count > 0:
                print(f"\nFound {different_content_count} duplicate(s) with different content.")
                response = input("Do you want to review and resolve these? (y/N): ")
                if response.lower() == 'y':
                    different_content_removals = detector.handle_different_content_duplicates(duplicates)
                    if different_content_removals:
                        diff_files_modified = detector.remove_duplicates(different_content_removals)
                        # Merge the results
                        for file_path, count in diff_files_modified.items():
                            files_modified[file_path] = files_modified.get(file_path, 0) + count
            
            # Print summary
            if files_modified:
                print("\n" + "="*60)
                print("FIX SUMMARY")
                print("="*60)
                print(f"Files modified: {len(files_modified)}")
                for file_path, count in files_modified.items():
                    print(f"  - {Path(file_path).name}: {count} items removed")
            else:
                print("\nNo files were modified.")
        else:
            print("\nNo duplicates found to fix.")
    
    # Export if requested
    if args.export:
        detector.export_json(duplicates, args.export)


if __name__ == "__main__":
    main()