#!/usr/bin/env python3
"""
Pre-Consolidator for PDF Fields
Groups related fields together before AI analysis
"""

from typing import Dict, List, Tuple, Optional, Set
from collections import defaultdict
import re
from dataclasses import dataclass
import statistics


@dataclass
class FieldGroup:
    """Represents a group of related fields"""
    group_type: str  # 'checkbox', 'text_continuation', 'radio', 'linked_date', 'same_value'
    fields: List[Dict]
    confidence: float  # 0.0 to 1.0
    reason: str  # Explanation for grouping


class PreConsolidator:
    def __init__(self, interactive_mode: bool = False, gui_mode: bool = False, pdf_path: str = None):
        self.interactive_mode = interactive_mode
        self.gui_mode = gui_mode
        self.pdf_path = pdf_path
        self.document_stats = {}
        
    def pre_consolidate_fields(self, extracted_fields: List[Dict]) -> List[FieldGroup]:
        """
        Pre-consolidate fields into groups before AI analysis
        
        Args:
            extracted_fields: List of extracted PDF fields
            
        Returns:
            List of FieldGroup objects
        """
        # GUI Mode - return empty list, GUI will handle everything
        if self.gui_mode:
            return []
        
        # Calculate document statistics for adaptive thresholds
        self._calculate_document_stats(extracted_fields)
        
        # Track which fields have been grouped
        grouped_fields = set()
        field_groups = []
        
        # 1. Group radio buttons (highest priority - they're already grouped by name)
        radio_groups = self._group_radio_buttons(extracted_fields, grouped_fields)
        field_groups.extend(radio_groups)
        
        # 2. Group checkboxes with smart proximity and pattern detection
        checkbox_groups = self._group_checkboxes(extracted_fields, grouped_fields)
        field_groups.extend(checkbox_groups)
        
        # 3. Group text continuations
        continuation_groups = self._group_text_continuations(extracted_fields, grouped_fields)
        field_groups.extend(continuation_groups)
        
        # 4. Group linked signature/date fields
        linked_date_groups = self._group_linked_dates(extracted_fields, grouped_fields)
        field_groups.extend(linked_date_groups)
        
        # 5. Group same-value fields (fields that appear on multiple pages)
        same_value_groups = self._group_same_value_fields(extracted_fields, grouped_fields)
        field_groups.extend(same_value_groups)
        
        # 6. Create individual groups for remaining fields
        for field in extracted_fields:
            if field['field_name'] not in grouped_fields:
                field_groups.append(FieldGroup(
                    group_type='individual',
                    fields=[field],
                    confidence=1.0,
                    reason='No grouping pattern detected'
                ))
        
        return field_groups
    
    def _calculate_document_stats(self, fields: List[Dict]):
        """Calculate document-wide statistics for adaptive thresholds"""
        # Calculate average vertical spacing between fields
        y_positions = []
        for field in fields:
            if 'position' in field and field['position']:
                y_positions.append(field['position'][1])  # Top y coordinate
        
        if len(y_positions) > 1:
            y_positions.sort()
            spacings = [y_positions[i+1] - y_positions[i] for i in range(len(y_positions)-1)]
            
            self.document_stats['avg_spacing'] = statistics.mean(spacings) if spacings else 50
            self.document_stats['median_spacing'] = statistics.median(spacings) if spacings else 50
            self.document_stats['min_spacing'] = min(spacings) if spacings else 10
            self.document_stats['max_spacing'] = max(spacings) if spacings else 100
        else:
            # Default values
            self.document_stats['avg_spacing'] = 50
            self.document_stats['median_spacing'] = 50
            self.document_stats['min_spacing'] = 10
            self.document_stats['max_spacing'] = 100
    
    def _group_radio_buttons(self, fields: List[Dict], grouped: Set[str]) -> List[FieldGroup]:
        """Group radio buttons by field name"""
        radio_groups = defaultdict(list)
        
        for field in fields:
            if field.get('field_type') == 'RadioButton':
                radio_groups[field['field_name']].append(field)
        
        groups = []
        for group_name, group_fields in radio_groups.items():
            if len(group_fields) > 0:
                groups.append(FieldGroup(
                    group_type='radio',
                    fields=group_fields,
                    confidence=1.0,
                    reason=f'Radio button group: {group_name}'
                ))
                for field in group_fields:
                    grouped.add(field['field_name'])
        
        return groups
    
    def _group_checkboxes(self, fields: List[Dict], grouped: Set[str]) -> List[FieldGroup]:
        """Group checkboxes using advanced proximity and pattern detection"""
        checkbox_fields = []
        
        # Collect all ungrouped checkboxes
        for field in fields:
            if (field.get('field_type') == 'CheckBox' and 
                field['field_name'] not in grouped):
                checkbox_fields.append(field)
        
        if not checkbox_fields:
            return []
        
        # GUI Mode - skip automatic grouping and return empty list
        # The GUI will handle ALL grouping later
        if self.gui_mode and self.pdf_path:
            return []
        
        # First, detect all possible groupings
        all_possible_groups = []
        
        # 1. Detect horizontal groups (checkboxes in a row)
        horizontal_groups = self._detect_horizontal_checkbox_groups(checkbox_fields)
        all_possible_groups.extend(horizontal_groups)
        
        # 2. Detect vertical groups (checkboxes in a column)
        vertical_groups = self._detect_vertical_checkbox_groups(checkbox_fields)
        all_possible_groups.extend(vertical_groups)
        
        # 3. Detect mixed groups (could be either or combined)
        mixed_groups = self._detect_mixed_checkbox_groups(checkbox_fields)
        all_possible_groups.extend(mixed_groups)
        
        # Remove duplicates and sort by confidence
        unique_groups = self._deduplicate_groups(all_possible_groups)
        unique_groups.sort(key=lambda g: (g.confidence, len(g.fields)), reverse=True)
        
        # Process groups based on mode
        final_groups = []
        already_grouped = set()
        
        for group in unique_groups:
            # Skip if any checkbox is already in a final group
            if any(f['field_name'] in already_grouped for f in group.fields):
                continue
            
            if self.interactive_mode:
                # In interactive mode, present grouping options to user
                if len(group.fields) > 1:
                    options = self._get_grouping_options(group, checkbox_fields, already_grouped)
                    chosen_groups = self._ask_user_about_checkbox_options(options)
                    
                    for chosen_group in chosen_groups:
                        final_groups.append(chosen_group)
                        for field in chosen_group.fields:
                            already_grouped.add(field['field_name'])
                            grouped.add(field['field_name'])
            else:
                # Non-interactive: use high-confidence groups
                if group.confidence > 0.5 and len(group.fields) > 1:
                    final_groups.append(group)
                    for field in group.fields:
                        already_grouped.add(field['field_name'])
                        grouped.add(field['field_name'])
        
        return final_groups
    
    def _detect_horizontal_checkbox_groups(self, checkboxes: List[Dict]) -> List[FieldGroup]:
        """Detect checkboxes arranged horizontally"""
        groups = []
        
        # Group by page and similar Y position
        by_page_and_y = defaultdict(list)
        for cb in checkboxes:
            page = cb.get('page', 0)
            y_pos = cb.get('position', [0, 0, 0, 0])[1]
            # Round Y to nearest 20px to group items on same line
            y_key = round(y_pos / 20) * 20
            by_page_and_y[(page, y_key)].append(cb)
        
        for (page, y_key), cbs in by_page_and_y.items():
            if len(cbs) > 1:
                # Sort by X position
                cbs.sort(key=lambda c: c.get('position', [0, 0, 0, 0])[0])
                
                # Check if they form a horizontal line
                x_positions = [c.get('position', [0, 0, 0, 0])[0] for c in cbs]
                max_gap = max(x_positions[i+1] - x_positions[i] for i in range(len(x_positions)-1))
                
                # If gap between any two is reasonable, consider it a horizontal group
                if max_gap < 200:  # Adjust threshold as needed
                    groups.append(FieldGroup(
                        group_type='checkbox',
                        fields=cbs,
                        confidence=0.8,
                        reason=f'Horizontal checkbox group on page {page}'
                    ))
        
        return groups
    
    def _detect_vertical_checkbox_groups(self, checkboxes: List[Dict]) -> List[FieldGroup]:
        """Detect checkboxes arranged vertically"""
        groups = []
        
        # Group by page and similar X position
        by_page_and_x = defaultdict(list)
        for cb in checkboxes:
            page = cb.get('page', 0)
            x_pos = cb.get('position', [0, 0, 0, 0])[0]
            # Round X to nearest 50px to group items in same column
            x_key = round(x_pos / 50) * 50
            by_page_and_x[(page, x_key)].append(cb)
        
        for (page, x_key), cbs in by_page_and_x.items():
            if len(cbs) > 1:
                # Sort by Y position
                cbs.sort(key=lambda c: c.get('position', [0, 0, 0, 0])[1])
                
                # Look for natural breaks (like section headers)
                subgroups = []
                current_subgroup = [cbs[0]]
                
                for i in range(1, len(cbs)):
                    prev_y = cbs[i-1].get('position', [0, 0, 0, 0])[1]
                    curr_y = cbs[i].get('position', [0, 0, 0, 0])[1]
                    gap = curr_y - prev_y
                    
                    # Check for section break indicators
                    has_section_break = False
                    
                    # Check if there's a label like (a), (b) in context
                    prev_context = cbs[i-1].get('context_left', '') + cbs[i-1].get('context_above', '')
                    curr_context = cbs[i].get('context_left', '') + cbs[i].get('context_above', '')
                    
                    if (re.search(r'\([a-z]\)', prev_context) and re.search(r'\([a-z]\)', curr_context)):
                        # Different section labels
                        has_section_break = True
                    
                    # Large gap also indicates section break
                    if gap > 100 or has_section_break:
                        if len(current_subgroup) > 1:
                            subgroups.append(current_subgroup)
                        current_subgroup = [cbs[i]]
                    else:
                        current_subgroup.append(cbs[i])
                
                # Don't forget the last subgroup
                if len(current_subgroup) > 1:
                    subgroups.append(current_subgroup)
                
                # Create groups for each subgroup
                for subgroup in subgroups:
                    groups.append(FieldGroup(
                        group_type='checkbox',
                        fields=subgroup,
                        confidence=0.7,
                        reason=f'Vertical checkbox group on page {page}'
                    ))
        
        return groups
    
    def _detect_mixed_checkbox_groups(self, checkboxes: List[Dict]) -> List[FieldGroup]:
        """Detect checkboxes that could be grouped multiple ways"""
        groups = []
        
        # Find clusters of checkboxes that are close together
        by_page = defaultdict(list)
        for cb in checkboxes:
            by_page[cb.get('page', 0)].append(cb)
        
        for page, page_checkboxes in by_page.items():
            if len(page_checkboxes) < 2:
                continue
            
            # Use DBSCAN-like clustering
            clusters = []
            visited = set()
            
            for cb in page_checkboxes:
                if cb['field_name'] in visited:
                    continue
                
                cluster = [cb]
                visited.add(cb['field_name'])
                
                # Find all checkboxes within proximity
                cb_pos = cb.get('position', [0, 0, 0, 0])
                
                for other in page_checkboxes:
                    if other['field_name'] in visited:
                        continue
                    
                    other_pos = other.get('position', [0, 0, 0, 0])
                    x_dist = abs(cb_pos[0] - other_pos[0])
                    y_dist = abs(cb_pos[1] - other_pos[1])
                    
                    # Within reasonable proximity
                    if x_dist < 150 and y_dist < 100:
                        cluster.append(other)
                        visited.add(other['field_name'])
                
                if len(cluster) > 1:
                    clusters.append(cluster)
            
            # Create groups for clusters
            for cluster in clusters:
                groups.append(FieldGroup(
                    group_type='checkbox',
                    fields=cluster,
                    confidence=0.5,
                    reason=f'Checkbox cluster on page {page}'
                ))
        
        return groups
    
    def _deduplicate_groups(self, groups: List[FieldGroup]) -> List[FieldGroup]:
        """Remove duplicate groups based on field membership"""
        unique_groups = []
        seen_sets = []
        
        for group in groups:
            field_set = frozenset(f['field_name'] for f in group.fields)
            if field_set not in seen_sets:
                seen_sets.append(field_set)
                unique_groups.append(group)
        
        return unique_groups
    
    def _get_grouping_options(self, base_group: FieldGroup, all_checkboxes: List[Dict], 
                             already_grouped: Set[str]) -> List[FieldGroup]:
        """Generate different grouping options for user to choose from"""
        options = []
        
        # Get all checkboxes in the vicinity that aren't already grouped
        available_cbs = [cb for cb in all_checkboxes if cb['field_name'] not in already_grouped]
        
        # Option 1: The original detected group
        options.append(base_group)
        
        # Option 2: Try to find smaller subgroups within
        if len(base_group.fields) > 3:
            # Try horizontal subgroups
            h_groups = self._detect_horizontal_checkbox_groups(base_group.fields)
            options.extend(h_groups)
            
            # Try vertical subgroups
            v_groups = self._detect_vertical_checkbox_groups(base_group.fields)
            options.extend(v_groups)
        
        # Option 3: Try to expand the group if there are nearby ungrouped checkboxes
        expanded_fields = base_group.fields.copy()
        base_positions = [f.get('position', [0, 0, 0, 0]) for f in base_group.fields]
        avg_x = sum(p[0] for p in base_positions) / len(base_positions)
        avg_y = sum(p[1] for p in base_positions) / len(base_positions)
        
        for cb in available_cbs:
            if cb not in base_group.fields:
                cb_pos = cb.get('position', [0, 0, 0, 0])
                if abs(cb_pos[0] - avg_x) < 200 and abs(cb_pos[1] - avg_y) < 150:
                    expanded_fields.append(cb)
        
        if len(expanded_fields) > len(base_group.fields):
            options.append(FieldGroup(
                group_type='checkbox',
                fields=expanded_fields,
                confidence=0.4,
                reason='Expanded checkbox group'
            ))
        
        # Remove duplicates
        return self._deduplicate_groups(options)
    
    def _ask_user_about_checkbox_options(self, options: List[FieldGroup]) -> List[FieldGroup]:
        """Present multiple grouping options to user"""
        if not options:
            return []
        
        print("\n" + "="*60)
        print("CHECKBOX GROUPING OPTIONS")
        print("="*60)
        
        # If only one option, use the simpler interface
        if len(options) == 1:
            if self._ask_user_about_grouping(options[0].fields, options[0].reason):
                return [options[0]]
            return []
        
        print("\nMultiple grouping options detected. Please choose:")
        print("\nOption 0: No grouping (keep all checkboxes separate)")
        
        for i, option in enumerate(options, 1):
            print(f"\nOption {i}: {option.reason}")
            print(f"Confidence: {option.confidence:.2f}")
            print(f"Checkboxes ({len(option.fields)}):")
            
            # Sort for display
            sorted_fields = sorted(option.fields, key=lambda f: 
                                 (f.get('page', 0), f.get('position', [0, 0, 0, 0])[1], 
                                  f.get('position', [0, 0, 0, 0])[0]))
            
            for field in sorted_fields:
                pos = field.get('position', [0, 0, 0, 0])
                label = field.get('context_left', '') or field.get('context_above', '')
                print(f"  - {field['field_name']} at ({pos[0]:.0f}, {pos[1]:.0f})")
                if label:
                    print(f"    Label: \"{label}\"")
        
        # Option for multiple separate groups
        print(f"\nOption {len(options) + 1}: Create multiple separate groups")
        print("(You'll be asked about each potential subgroup)")
        
        # Option for custom selection
        print(f"\nOption {len(options) + 2}: Custom selection")
        print("(Select specific checkboxes to group together)")
        
        while True:
            try:
                choice = input(f"\nSelect option (0-{len(options) + 2}): ").strip()
                choice_num = int(choice)
                
                if choice_num == 0:
                    return []
                elif 1 <= choice_num <= len(options):
                    return [options[choice_num - 1]]
                elif choice_num == len(options) + 1:
                    # Ask about each subgroup
                    chosen_groups = []
                    for option in options:
                        if len(option.fields) > 1:
                            print(f"\n--- Subgroup: {option.reason} ---")
                            if self._ask_user_about_grouping(option.fields, option.reason):
                                chosen_groups.append(option)
                    return chosen_groups
                elif choice_num == len(options) + 2:
                    # Custom selection
                    custom_groups = self._custom_checkbox_selection(options)
                    return custom_groups
                else:
                    print(f"Please enter a number between 0 and {len(options) + 2}")
            except ValueError:
                print(f"Please enter a number between 0 and {len(options) + 2}")
    
    def _custom_checkbox_selection(self, options: List[FieldGroup]) -> List[FieldGroup]:
        """Allow user to select specific checkboxes to group"""
        # Collect all unique checkboxes from all options
        all_checkboxes = {}
        for option in options:
            for field in option.fields:
                if field['field_name'] not in all_checkboxes:
                    all_checkboxes[field['field_name']] = field
        
        # Sort by position for display
        sorted_checkboxes = sorted(all_checkboxes.values(), 
                                 key=lambda f: (f.get('page', 0), 
                                              f.get('position', [0, 0, 0, 0])[1],
                                              f.get('position', [0, 0, 0, 0])[0]))
        
        print("\n" + "="*60)
        print("CUSTOM CHECKBOX SELECTION")
        print("="*60)
        print("\nAll available checkboxes:")
        
        for i, cb in enumerate(sorted_checkboxes):
            pos = cb.get('position', [0, 0, 0, 0])
            label = cb.get('context_left', '') or cb.get('context_above', '')
            print(f"{i+1}. {cb['field_name']} (Page {cb.get('page', 'Unknown')})")
            print(f"   Position: ({pos[0]:.0f}, {pos[1]:.0f})")
            if label:
                print(f"   Label: \"{label}\"")
        
        groups = []
        remaining_indices = set(range(len(sorted_checkboxes)))
        
        while remaining_indices:
            print(f"\n{len(remaining_indices)} checkboxes remaining")
            print("Enter checkbox numbers to group together (comma-separated)")
            print("Or press Enter to skip remaining checkboxes")
            
            selection = input("Selection: ").strip()
            
            if not selection:
                break
            
            try:
                # Parse selection
                indices = [int(x.strip()) - 1 for x in selection.split(',')]
                
                # Validate indices
                valid_indices = []
                for idx in indices:
                    if 0 <= idx < len(sorted_checkboxes) and idx in remaining_indices:
                        valid_indices.append(idx)
                    else:
                        print(f"Invalid or already used index: {idx + 1}")
                
                if len(valid_indices) > 1:
                    # Create group
                    group_fields = [sorted_checkboxes[idx] for idx in valid_indices]
                    groups.append(FieldGroup(
                        group_type='checkbox',
                        fields=group_fields,
                        confidence=0.9,  # High confidence since user selected
                        reason=f'User-selected group of {len(group_fields)} checkboxes'
                    ))
                    
                    # Remove from remaining
                    for idx in valid_indices:
                        remaining_indices.remove(idx)
                    
                    print(f"✓ Created group with {len(group_fields)} checkboxes")
                elif len(valid_indices) == 1:
                    print("Please select at least 2 checkboxes to group")
                
            except ValueError:
                print("Invalid input. Please enter numbers separated by commas.")
        
        return groups
    
    def _should_group_checkbox(self, prev_checkbox: Dict, curr_checkbox: Dict, 
                              proximity_threshold: float) -> Tuple[bool, str]:
        """Determine if two checkboxes should be grouped"""
        # Different pages - don't group
        if prev_checkbox.get('page', 0) != curr_checkbox.get('page', 0):
            return False, "Different pages"
        
        # Check proximity
        prev_pos = prev_checkbox.get('position', [0, 0, 0, 0])
        curr_pos = curr_checkbox.get('position', [0, 0, 0, 0])
        
        vertical_distance = abs(curr_pos[1] - prev_pos[1])
        horizontal_distance = abs(curr_pos[0] - prev_pos[0])
        
        # Too far vertically
        if vertical_distance > proximity_threshold:
            return False, f"Vertical distance {vertical_distance} exceeds threshold {proximity_threshold}"
        
        # Check for alignment (similar horizontal position suggests grouping)
        if horizontal_distance < 80:  # More generous alignment threshold
            return True, "Vertically proximate and horizontally aligned"
        
        # Check for indentation pattern (might indicate sub-options)
        if 20 < horizontal_distance < 150:  # More generous indentation range
            return True, "Vertically proximate with consistent indentation"
        
        # Even if not perfectly aligned, if very close vertically, consider grouping
        if vertical_distance < 30:  # Very close vertically
            return True, f"Very close vertically ({vertical_distance:.0f}px), despite horizontal offset"
        
        return False, "Not well-aligned"
    
    def _calculate_group_confidence(self, checkboxes: List[Dict]) -> float:
        """Calculate confidence score for a checkbox group"""
        if len(checkboxes) < 2:
            return 0.0
        
        score = 0.0
        
        # 1. Consistent spacing (30% weight)
        positions = [cb.get('position', [0, 0, 0, 0])[1] for cb in checkboxes]
        if len(positions) > 2:
            spacings = [positions[i+1] - positions[i] for i in range(len(positions)-1)]
            avg_spacing = statistics.mean(spacings)
            spacing_variance = statistics.variance(spacings) if len(spacings) > 1 else 0
            
            # Low variance means consistent spacing
            if spacing_variance < (avg_spacing * 0.3) ** 2:
                score += 0.3
        else:
            score += 0.3  # Only two items, spacing is consistent by definition
        
        # 2. Horizontal alignment (30% weight)
        x_positions = [cb.get('position', [0, 0, 0, 0])[0] for cb in checkboxes]
        x_variance = statistics.variance(x_positions) if len(x_positions) > 1 else 0
        if x_variance < 100:  # Well-aligned horizontally
            score += 0.3
        
        # 3. Pattern detection (40% weight)
        # Look for common prefixes or patterns in field names
        field_names = [cb.get('field_name', '') for cb in checkboxes]
        if self._have_common_pattern(field_names):
            score += 0.4
        
        return min(score, 1.0)
    
    def _have_common_pattern(self, field_names: List[str]) -> bool:
        """Check if field names have a common pattern"""
        if not field_names:
            return False
        
        # Check for common prefix (removing numbers)
        base_names = []
        for name in field_names:
            # Remove trailing numbers
            base = re.sub(r'_\d+$', '', name)
            base_names.append(base)
        
        # If all have the same base, they're related
        return len(set(base_names)) == 1
    
    def _create_checkbox_group(self, checkboxes: List[Dict], confidence: float) -> FieldGroup:
        """Create a checkbox field group"""
        # Determine group characteristics
        pages = set(cb.get('page', 0) for cb in checkboxes)
        
        reason = f"Checkbox group with {len(checkboxes)} items"
        if len(pages) == 1:
            reason += f" on page {list(pages)[0]}"
        
        return FieldGroup(
            group_type='checkbox',
            fields=checkboxes,
            confidence=confidence,
            reason=reason
        )
    
    def _group_text_continuations(self, fields: List[Dict], grouped: Set[str]) -> List[FieldGroup]:
        """Group text fields that are continuations"""
        groups = []
        field_map = {f['field_name']: f for f in fields if f['field_name'] not in grouped}
        
        # Extract field numbers for pattern detection
        field_numbers = {}
        for fname in field_map:
            # Extract number from field name (e.g., "form_textfield_94" -> 94)
            parts = fname.split('_')
            if parts and parts[-1].isdigit():
                field_numbers[fname] = int(parts[-1])
        
        # Look for continuation patterns
        for field_name, field in field_map.items():
            if field_name in grouped or field.get('field_type') != 'Text':
                continue
                
            # Check for EXPLICIT continuation patterns only
            continuation_fields = []
            
            # Pattern 1: _continued, _line_2, etc. (explicit suffixes)
            base_name = field_name
            has_continuation_suffix = False
            for suffix in ['_continued', '_line_2', '_line_3', '_cont']:
                if suffix in field_name:
                    base_name = field_name.replace(suffix, '')
                    has_continuation_suffix = True
                    break
            
            # Only look for related fields if we have an explicit continuation pattern
            if has_continuation_suffix:
                # Find all related fields with continuation suffixes
                for other_name, other_field in field_map.items():
                    if (other_name != field_name and 
                        other_name.startswith(base_name) and 
                        any(suffix in other_name for suffix in ['_continued', '_line_', '_cont'])):
                        continuation_fields.append(other_field)
            
            # For proximity-based continuations, analyze patterns
            elif field.get('field_type') == 'Text':
                # Get field number
                curr_num = field_numbers.get(field_name)
                if curr_num is None:
                    continue
                
                # Look for sequential fields
                candidates = []
                same_page_fields = [
                    (fname, f) for fname, f in field_map.items()
                    if (f.get('page') == field.get('page') and 
                        f.get('field_type') == 'Text' and
                        fname != field_name and
                        fname not in grouped)
                ]
                
                # Check for sequential patterns
                for other_name, other_field in same_page_fields:
                    other_num = field_numbers.get(other_name)
                    if other_num and other_num == curr_num + 1:
                        # Found next sequential field
                        if self._is_likely_continuation(field, other_field):
                            candidates.append((other_name, other_field))
                
                # Analyze candidates
                if candidates:
                    # Check if there's a pattern of 2+ sequential fields
                    sequential_group = [field]
                    next_num = curr_num + 1
                    
                    while candidates:
                        found = False
                        for cname, cfield in candidates:
                            if field_numbers.get(cname) == next_num:
                                if len(sequential_group) == 1 or self._is_likely_continuation(sequential_group[-1], cfield):
                                    sequential_group.append(cfield)
                                    next_num += 1
                                    found = True
                                    break
                        if not found:
                            break
                    
                    # Only group if we have exactly 2-3 fields (more likely to be continuations)
                    # or if fields are very wide (likely multi-line text)
                    if len(sequential_group) >= 2:
                        avg_width = sum((f.get('position', [0,0,0,0])[2] - f.get('position', [0,0,0,0])[0]) 
                                      for f in sequential_group) / len(sequential_group)
                        
                        # Wide fields (>400px) or small groups (2-3 fields) are more likely continuations
                        if avg_width > 400 or len(sequential_group) <= 3:
                            continuation_fields = sequential_group[1:]
            
            if continuation_fields:
                all_fields = [field] + continuation_fields
                # Sort by position to maintain order
                all_fields.sort(key=lambda f: (f.get('page', 0), f.get('position', [0, 0, 0, 0])[1]))
                
                confidence = 0.9 if has_continuation_suffix else 0.5  # Lower confidence for proximity-based
                
                # In interactive mode, ALWAYS ask about text continuations
                if self.interactive_mode:
                    if self._ask_user_about_text_continuation(all_fields):
                        groups.append(FieldGroup(
                            group_type='text_continuation',
                            fields=all_fields,
                            confidence=0.8,  # Higher confidence with user confirmation
                            reason=f'User confirmed: Text continuation with {len(continuation_fields)} additional fields'
                        ))
                        
                        for f in all_fields:
                            grouped.add(f['field_name'])
                else:
                    # Non-interactive: only group high-confidence continuations
                    if confidence >= 0.8:
                        groups.append(FieldGroup(
                            group_type='text_continuation',
                            fields=all_fields,
                            confidence=confidence,
                            reason=f'Text continuation with {len(continuation_fields)} additional fields'
                        ))
                        
                        for f in all_fields:
                            grouped.add(f['field_name'])
        
        return groups
    
    def _is_likely_continuation(self, field1: Dict, field2: Dict) -> bool:
        """Check if field2 is likely a continuation of field1"""
        pos1 = field1.get('position', [0, 0, 0, 0])
        pos2 = field2.get('position', [0, 0, 0, 0])
        
        # Check if field2 is below field1
        vertical_distance = pos2[1] - pos1[3]  # Top of field2 - bottom of field1
        
        # For text continuations, we need VERY strict criteria:
        # 1. Must be VERY close vertically (less than 10 pixels)
        # 2. Must be perfectly aligned horizontally
        # 3. Should have similar widths (likely part of same text flow)
        
        horizontal_alignment = abs(pos1[0] - pos2[0]) < 5  # Very strict alignment
        very_close_vertically = 0 < vertical_distance < 10  # Much stricter
        similar_width = abs((pos1[2] - pos1[0]) - (pos2[2] - pos2[0])) < 50
        
        # Also check if fields are small (likely continuation) vs large (likely separate)
        field1_width = pos1[2] - pos1[0]
        field2_width = pos2[2] - pos2[0]
        both_wide = field1_width > 200 and field2_width > 200  # Wide fields less likely to be continuations
        
        return horizontal_alignment and very_close_vertically and similar_width and not both_wide
    
    def _group_linked_dates(self, fields: List[Dict], grouped: Set[str]) -> List[FieldGroup]:
        """Group signature fields with their linked date fields"""
        groups = []
        
        signature_fields = [
            f for f in fields 
            if f.get('field_type') == 'Signature' and f['field_name'] not in grouped
        ]
        
        date_fields = [
            f for f in fields 
            if f.get('field_type') == 'Text' and 
            'date' in f.get('field_name', '').lower() and 
            f['field_name'] not in grouped
        ]
        
        for sig_field in signature_fields:
            sig_pos = sig_field.get('position', [0, 0, 0, 0])
            sig_page = sig_field.get('page', 0)
            
            # Find closest date field on same page
            closest_date = None
            min_distance = float('inf')
            
            for date_field in date_fields:
                if date_field.get('page') == sig_page:
                    date_pos = date_field.get('position', [0, 0, 0, 0])
                    
                    # Calculate distance (prioritize horizontal proximity)
                    h_distance = abs(date_pos[0] - sig_pos[2])  # Left of date to right of signature
                    v_distance = abs(date_pos[1] - sig_pos[1])  # Vertical alignment
                    
                    weighted_distance = h_distance + (v_distance * 0.5)
                    
                    if weighted_distance < min_distance and weighted_distance < 150:
                        closest_date = date_field
                        min_distance = weighted_distance
            
            if closest_date:
                groups.append(FieldGroup(
                    group_type='linked_date',
                    fields=[sig_field, closest_date],
                    confidence=0.9,
                    reason='Signature field with linked date'
                ))
                grouped.add(sig_field['field_name'])
                grouped.add(closest_date['field_name'])
        
        return groups
    
    def _group_same_value_fields(self, fields: List[Dict], grouped: Set[str]) -> List[FieldGroup]:
        """Group fields that should have the same value across pages"""
        # This is harder to detect without AI analysis
        # For now, we'll use simple heuristics
        groups = []
        
        # Group by similar field names on different pages
        field_by_type_and_position = defaultdict(list)
        
        for field in fields:
            if field['field_name'] not in grouped:
                field_type = field.get('field_type', 'Unknown')
                page = field.get('page', 0)
                position = field.get('position', [0, 0, 0, 0])
                
                # Create a key based on field type and relative position
                # Use slightly larger tolerance (75px) to catch minor variations
                key = (field_type, round(position[0]/75)*75, round(position[1]/75)*75)
                field_by_type_and_position[key].append(field)
        
        # Group fields with same type and similar position on different pages
        for fields_list in field_by_type_and_position.values():
            if len(fields_list) > 1:
                pages = set(f.get('page', 0) for f in fields_list)
                if len(pages) > 1:  # Fields on different pages
                    # In interactive mode, ALWAYS ask about same-value fields
                    if self.interactive_mode:
                        if self._ask_user_about_same_value_fields(fields_list):
                            groups.append(FieldGroup(
                                group_type='same_value',
                                fields=fields_list,
                                confidence=0.7,  # Higher confidence if user confirmed
                                reason=f'User confirmed: Similar fields on pages {sorted(pages)}'
                            ))
                            for f in fields_list:
                                grouped.add(f['field_name'])
                    else:
                        # Non-interactive mode: be conservative
                        groups.append(FieldGroup(
                            group_type='same_value',
                            fields=fields_list,
                            confidence=0.5,  # Lower confidence without user confirmation
                            reason=f'Similar position fields on {len(pages)} different pages'
                        ))
                        for f in fields_list:
                            grouped.add(f['field_name'])
        
        return groups
    
    def _ask_user_about_grouping(self, fields: List[Dict], reason: str) -> bool:
        """Ask user whether fields should be grouped together"""
        if not self.interactive_mode:
            return True
        
        print("\n" + "="*60)
        print("CHECKBOX GROUPING DECISION NEEDED")
        print("="*60)
        print(f"\nReason: {reason}")
        print(f"Number of checkboxes: {len(fields)}")
        print("\nShould these checkboxes be grouped together as options in a single field?\n")
        
        # Sort by vertical position for clarity
        sorted_fields = sorted(fields, key=lambda f: f.get('position', [0, 0, 0, 0])[1])
        
        # Calculate spacing between consecutive checkboxes
        spacings = []
        for i in range(len(sorted_fields) - 1):
            pos1 = sorted_fields[i].get('position', [0, 0, 0, 0])
            pos2 = sorted_fields[i + 1].get('position', [0, 0, 0, 0])
            spacing = pos2[1] - pos1[1]
            spacings.append(spacing)
        
        for i, field in enumerate(sorted_fields, 1):
            pos = field.get('position', [0, 0, 0, 0])
            print(f"{i}. {field['field_name']} (Page {field.get('page', 'Unknown')})")
            print(f"   Position: x={pos[0]:.0f}, y={pos[1]:.0f}")
            
            # Show context if available
            if field.get('context_left'):
                print(f"   Label: \"{field['context_left']}\"")
            elif field.get('context_above'):
                print(f"   Label: \"{field['context_above']}\"")
            
            # Show spacing to next checkbox
            if i < len(sorted_fields) and spacings:
                print(f"   ↓ {spacings[i-1]:.0f}px to next checkbox")
        
        if spacings:
            avg_spacing = sum(spacings) / len(spacings)
            print(f"\nAverage spacing: {avg_spacing:.0f}px")
        
        print("\nNote: Group these if they represent different options for the same question/category.")
        print("DO NOT group if they're unrelated checkboxes that happen to be near each other.")
        
        while True:
            response = input("\nGroup these checkboxes together? (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")
    
    def _ask_user_about_text_continuation(self, fields: List[Dict]) -> bool:
        """Ask user whether text fields should be treated as continuations"""
        if not self.interactive_mode:
            return True
        
        print("\n" + "="*60)
        print("TEXT CONTINUATION DECISION NEEDED")
        print("="*60)
        print("\nThese text fields are close together and might be continuations of each other.")
        print("Should they be grouped as a single multi-line field?\n")
        
        # Extract field numbers for pattern info
        field_numbers = []
        for field in fields:
            parts = field['field_name'].split('_')
            if parts and parts[-1].isdigit():
                field_numbers.append(int(parts[-1]))
        
        # Check if sequential
        is_sequential = False
        if field_numbers and len(field_numbers) == len(fields):
            is_sequential = all(field_numbers[i] == field_numbers[0] + i for i in range(len(field_numbers)))
        
        for i, field in enumerate(fields, 1):
            print(f"{i}. {field['field_name']} (Page {field.get('page', 'Unknown')})")
            pos = field.get('position', [0, 0, 0, 0])
            print(f"   Position: x={pos[0]:.0f}, y={pos[1]:.0f}, width={pos[2]-pos[0]:.0f}, height={pos[3]-pos[1]:.0f}")
            
            # Show context if available
            if field.get('context_left'):
                print(f"   Left context: \"{field['context_left']}\"")
            if field.get('context_above'):
                print(f"   Above context: \"{field['context_above']}\"")
        
        if is_sequential:
            print(f"\n⚠️  These fields are numbered sequentially: {field_numbers}")
        
        print("\nNote: Only group these if they form one logical field split across multiple lines.")
        print("DO NOT group if they're separate fields for different values.")
        print("Example: Address lines should be grouped, but separate percentage fields should NOT.")
        
        while True:
            response = input("\nGroup these as text continuation? (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")
    
    def _ask_user_about_same_value_fields(self, fields: List[Dict]) -> bool:
        """Ask user whether fields should have the same value across pages"""
        if not self.interactive_mode:
            return True
        
        print("\n" + "="*60)
        print("SAME-VALUE FIELD DECISION NEEDED")
        print("="*60)
        print("\nThese fields appear in similar positions on different pages.")
        print("Should they be grouped as fields that will contain the SAME value?\n")
        
        # Sort fields by page for clarity
        sorted_fields = sorted(fields, key=lambda f: f.get('page', 0))
        
        for i, field in enumerate(sorted_fields, 1):
            pos = field.get('position', [0, 0, 0, 0])
            print(f"{i}. {field['field_name']} (Page {field.get('page', 'Unknown')})")
            print(f"   Type: {field.get('field_type', 'Unknown')}")
            print(f"   Position: x={pos[0]:.0f}, y={pos[1]:.0f}")
            print(f"   Size: {pos[2]-pos[0]:.0f} x {pos[3]-pos[1]:.0f}")
        
        print("\nNote: Only group these if they represent the SAME information repeated on multiple pages.")
        print("Examples: buyer name appearing on multiple pages, property address on each page.")
        
        while True:
            response = input("\nGroup these as same-value fields? (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")


def main():
    """Test the pre-consolidator"""
    import json
    
    # Example test data
    test_fields = [
        {
            'field_name': 'checkbox_1',
            'field_type': 'CheckBox',
            'page': 0,
            'position': [100, 100, 120, 120]
        },
        {
            'field_name': 'checkbox_2',
            'field_type': 'CheckBox',
            'page': 0,
            'position': [100, 130, 120, 150]
        },
        {
            'field_name': 'checkbox_3',
            'field_type': 'CheckBox',
            'page': 0,
            'position': [100, 160, 120, 180]
        },
        {
            'field_name': 'signature_1',
            'field_type': 'Signature',
            'page': 1,
            'position': [100, 500, 300, 550]
        },
        {
            'field_name': 'date_1',
            'field_type': 'Text',
            'page': 1,
            'position': [320, 510, 420, 530]
        }
    ]
    
    consolidator = PreConsolidator(interactive_mode=False)
    groups = consolidator.pre_consolidate_fields(test_fields)
    
    print("Pre-consolidation Results:")
    print("="*60)
    for i, group in enumerate(groups, 1):
        print(f"\nGroup {i}:")
        print(f"  Type: {group.group_type}")
        print(f"  Confidence: {group.confidence:.2f}")
        print(f"  Reason: {group.reason}")
        print(f"  Fields: {[f['field_name'] for f in group.fields]}")


if __name__ == "__main__":
    main()