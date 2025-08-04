#!/usr/bin/env python3
"""
Schema Consolidator
Handles field relationships and consolidation logic
"""

from typing import Dict, List, Optional, Set, Tuple
import re
import json
from collections import defaultdict


class SchemaConsolidator:
    def __init__(self, interactive_mode: bool = False):
        self.consolidated_fields = []
        self.field_mapping = {}  # Maps original field names to consolidated unique_ids
        self.interactive_mode = interactive_mode
        
    def consolidate_fields(
        self,
        analyzed_fields: List[Dict],
        extracted_fields: List[Dict]
    ) -> List[Dict]:
        """
        Consolidate related fields based on analysis results
        
        Args:
            analyzed_fields: List of fields with schema analysis from Groq
            extracted_fields: Original extracted fields with position data
            
        Returns:
            List of consolidated schema items
        """
        # Create lookup maps
        analysis_map = {f['field_name']: f for f in analyzed_fields if f.get('status') == 'success'}
        extraction_map = {f['field_name']: f for f in extracted_fields}
        
        # Group fields by various criteria
        same_value_groups = self._identify_same_value_fields(analyzed_fields, extraction_map)
        continuation_groups = self._identify_continuation_fields(analyzed_fields, extraction_map)
        linked_date_groups = self._identify_linked_dates(analyzed_fields, extraction_map)
        radio_groups = self._identify_radio_groups(extracted_fields)
        checkbox_groups = self._identify_checkbox_groups(analyzed_fields, extraction_map)
        
        # Track which fields have been processed
        processed_fields = set()
        consolidated_items = []
        
        # Process radio button groups first
        for group_name, radio_fields in radio_groups.items():
            if group_name not in processed_fields:
                consolidated_item = self._consolidate_radio_group(
                    group_name,
                    radio_fields,
                    analysis_map,
                    extraction_map
                )
                if consolidated_item:
                    consolidated_items.append(consolidated_item)
                    processed_fields.add(group_name)
                    for field in radio_fields:
                        processed_fields.add(field['field_name'])
        
        # Process checkbox groups
        for group_key, checkbox_fields in checkbox_groups.items():
            # Check if any fields in this group haven't been processed
            unprocessed = [f for f in checkbox_fields if f not in processed_fields]
            if unprocessed:
                consolidated_item = self._consolidate_checkbox_group(
                    group_key,
                    checkbox_fields,
                    analysis_map,
                    extraction_map
                )
                if consolidated_item:
                    consolidated_items.append(consolidated_item)
                    processed_fields.update(checkbox_fields)
        
        # Process same-value groups
        for unique_id, field_names in same_value_groups.items():
            if not all(name in processed_fields for name in field_names):
                consolidated_item = self._consolidate_same_value_fields(
                    unique_id,
                    field_names,
                    analysis_map,
                    extraction_map
                )
                if consolidated_item:
                    consolidated_items.append(consolidated_item)
                    processed_fields.update(field_names)
        
        # Process continuation fields
        for main_field, continuation_fields in continuation_groups.items():
            if main_field not in processed_fields:
                consolidated_item = self._consolidate_continuation_fields(
                    main_field,
                    continuation_fields,
                    analysis_map,
                    extraction_map
                )
                if consolidated_item:
                    consolidated_items.append(consolidated_item)
                    processed_fields.add(main_field)
                    processed_fields.update(continuation_fields)
        
        # Process linked dates
        for signature_field, date_field in linked_date_groups:
            if signature_field not in processed_fields:
                consolidated_item = self._consolidate_linked_dates(
                    signature_field,
                    date_field,
                    analysis_map,
                    extraction_map
                )
                if consolidated_item:
                    consolidated_items.append(consolidated_item)
                    processed_fields.add(signature_field)
                    processed_fields.add(date_field)
        
        # Process remaining individual fields
        for field_name, analysis in analysis_map.items():
            if field_name not in processed_fields and analysis.get('schema_item'):
                schema_item = analysis['schema_item']
                # Add pdf_attributes structure
                consolidated_item = self._create_schema_item(
                    schema_item,
                    field_name,
                    extraction_map.get(field_name, {})
                )
                consolidated_items.append(consolidated_item)
                processed_fields.add(field_name)
        
        # Normalize blocks before sorting
        self._normalize_blocks(consolidated_items)
        
        # Sort by order and reassign sequential order numbers
        consolidated_items.sort(key=lambda x: (
            x.get('display_attributes', {}).get('order', 999),
            x.get('unique_id', '')
        ))
        
        for i, item in enumerate(consolidated_items, 1):
            item['display_attributes']['order'] = i
        
        return consolidated_items
    
    def _identify_same_value_fields(
        self,
        analyzed_fields: List[Dict],
        extraction_map: Dict
    ) -> Dict[str, List[str]]:
        """Identify fields that should contain the same value"""
        same_value_groups = defaultdict(list)
        
        # Group by unique_id from analysis
        for field in analyzed_fields:
            if field.get('status') == 'success' and field.get('schema_item'):
                unique_id = field['schema_item'].get('unique_id')
                if unique_id:
                    same_value_groups[unique_id].append(field['field_name'])
        
        # Only keep groups with multiple fields
        return {k: v for k, v in same_value_groups.items() if len(v) > 1}
    
    def _identify_continuation_fields(
        self,
        analyzed_fields: List[Dict],
        extraction_map: Dict
    ) -> Dict[str, List[str]]:
        """Identify text continuation fields"""
        continuation_groups = {}
        
        # Look for fields with similar unique_ids or explicit continuation markers
        for field in analyzed_fields:
            if field.get('status') == 'success' and field.get('schema_item'):
                field_name = field['field_name']
                unique_id = field['schema_item'].get('unique_id', '')
                
                # Check for continuation patterns
                if '_continued' in unique_id or '_line_2' in unique_id:
                    base_id = unique_id.replace('_continued', '').replace('_line_2', '').replace('_line_3', '')
                    # Find the main field
                    for other_field in analyzed_fields:
                        if (other_field.get('status') == 'success' and 
                            other_field['schema_item'].get('unique_id') == base_id):
                            main_field = other_field['field_name']
                            if main_field not in continuation_groups:
                                continuation_groups[main_field] = []
                            continuation_groups[main_field].append(field_name)
                            break
        
        return continuation_groups
    
    def _identify_linked_dates(
        self,
        analyzed_fields: List[Dict],
        extraction_map: Dict
    ) -> List[Tuple[str, str]]:
        """Identify signature fields with linked date fields"""
        linked_pairs = []
        
        # Find signature fields
        signature_fields = []
        date_fields = []
        
        for field in analyzed_fields:
            if field.get('status') == 'success' and field.get('schema_item'):
                schema_item = field['schema_item']
                field_name = field['field_name']
                
                if schema_item.get('input_type') == 'signature' or schema_item.get('attribute') == 'signature':
                    signature_fields.append((field_name, extraction_map.get(field_name, {})))
                elif schema_item.get('attribute') == 'date' or 'date' in schema_item.get('unique_id', ''):
                    date_fields.append((field_name, extraction_map.get(field_name, {})))
        
        # Match signatures with nearby dates
        for sig_name, sig_data in signature_fields:
            sig_page = sig_data.get('page', 0)
            sig_pos = sig_data.get('position', [0, 0, 0, 0])
            
            # Find closest date field on same page
            closest_date = None
            min_distance = float('inf')
            
            for date_name, date_data in date_fields:
                if date_data.get('page') == sig_page:
                    date_pos = date_data.get('position', [0, 0, 0, 0])
                    
                    # Calculate distance (horizontal proximity is more important)
                    h_dist = abs(date_pos[0] - sig_pos[2])  # Distance from sig right to date left
                    v_dist = abs(date_pos[1] - sig_pos[1])  # Vertical distance
                    
                    # Weighted distance (horizontal proximity weighted more)
                    distance = h_dist + (v_dist * 0.5)
                    
                    if distance < min_distance and distance < 150:  # Within 150 pixels
                        closest_date = date_name
                        min_distance = distance
            
            if closest_date:
                linked_pairs.append((sig_name, closest_date))
        
        return linked_pairs
    
    def _identify_radio_groups(self, extracted_fields: List[Dict]) -> Dict[str, List[Dict]]:
        """Identify radio button groups"""
        radio_groups = defaultdict(list)
        
        for field in extracted_fields:
            if field.get('field_type') == 'RadioButton':
                # Radio buttons with the same field name are part of the same group
                group_name = field['field_name']
                radio_groups[group_name].append(field)
        
        return dict(radio_groups)
    
    def _identify_checkbox_groups(self, analyzed_fields: List[Dict], extraction_map: Dict) -> Dict[str, List[str]]:
        """
        Identify checkboxes that should be grouped together
        Groups are based on:
        1. Same unique_id base (e.g., financing_type_1, financing_type_2)
        2. Same block AND semantically related (similar purpose/theme)
        3. Proximity on the same page
        """
        checkbox_groups = defaultdict(list)
        checkbox_fields = []
        
        # First, collect all checkbox fields with their analysis
        for field in analyzed_fields:
            if field.get('status') == 'success' and field.get('schema_item'):
                schema_item = field['schema_item']
                field_name = field['field_name']
                
                # Check if it's a checkbox
                if schema_item.get('input_type') == 'checkbox':
                    extracted_info = extraction_map.get(field_name, {})
                    checkbox_fields.append({
                        'field_name': field_name,
                        'schema_item': schema_item,
                        'unique_id': schema_item.get('unique_id', ''),
                        'display_name': schema_item.get('display_name', ''),
                        'block': schema_item.get('block', ''),
                        'attribute': schema_item.get('attribute', ''),
                        'page': extracted_info.get('page', 0),
                        'position': extracted_info.get('position', [0, 0, 0, 0])
                    })
        
        # Group by various strategies
        
        # Strategy 1: Group by unique_id base (remove trailing numbers)
        for checkbox in checkbox_fields:
            unique_id = checkbox['unique_id']
            # Remove trailing _1, _2, etc. or just numbers
            import re
            base_id = re.sub(r'_\d+$', '', unique_id)
            base_id = re.sub(r'\d+$', '', base_id).rstrip('_')
            
            if base_id and base_id != unique_id:
                group_key = f"uid_{base_id}"
                checkbox_groups[group_key].append(checkbox['field_name'])
        
        # Strategy 2: Group by block + semantic similarity
        from collections import defaultdict
        block_groups = defaultdict(list)
        
        for checkbox in checkbox_fields:
            block_groups[checkbox['block']].append(checkbox)
        
        # For each block, find semantically related checkboxes
        for block, checkboxes in block_groups.items():
            if len(checkboxes) > 1:
                # Group checkboxes by semantic themes
                semantic_groups = self._group_by_semantic_similarity(checkboxes)
                
                for group_idx, semantic_group in enumerate(semantic_groups):
                    if len(semantic_group) > 1:
                        group_key = f"semantic_{block}_{group_idx}"
                        for cb in semantic_group:
                            if cb['field_name'] not in checkbox_groups[group_key]:
                                checkbox_groups[group_key].append(cb['field_name'])
        
        # Strategy 3: Group by proximity (only if on same page and very close)
        page_groups = defaultdict(list)
        for checkbox in checkbox_fields:
            page_groups[checkbox['page']].append(checkbox)
        
        for page, page_checkboxes in page_groups.items():
            if len(page_checkboxes) > 1:
                # Sort by vertical position
                page_checkboxes.sort(key=lambda x: x['position'][1])
                
                # Group checkboxes that are very close vertically (within 30 pixels)
                current_group = [page_checkboxes[0]]
                
                for i in range(1, len(page_checkboxes)):
                    prev_pos = page_checkboxes[i-1]['position']
                    curr_pos = page_checkboxes[i]['position']
                    
                    # Check vertical distance
                    v_distance = abs(curr_pos[1] - prev_pos[1])
                    
                    if v_distance < 30:  # Very close vertically
                        # Also check if they're semantically related
                        if self._are_checkboxes_related(current_group[-1], page_checkboxes[i]):
                            current_group.append(page_checkboxes[i])
                    else:
                        # Process current group
                        if len(current_group) > 1:
                            group_key = f"proximity_{page}_{len(checkbox_groups)}"
                            for cb in current_group:
                                if cb['field_name'] not in checkbox_groups[group_key]:
                                    checkbox_groups[group_key].append(cb['field_name'])
                        current_group = [page_checkboxes[i]]
                
                # Don't forget the last group
                if len(current_group) > 1:
                    group_key = f"proximity_{page}_{len(checkbox_groups)}"
                    for cb in current_group:
                        if cb['field_name'] not in checkbox_groups[group_key]:
                            checkbox_groups[group_key].append(cb['field_name'])
        
        # Create a map of field names to checkbox data for refinement
        checkbox_fields_map = {cb['field_name']: cb for cb in checkbox_fields}
        
        # Remove groups with only one checkbox
        checkbox_groups = {k: v for k, v in checkbox_groups.items() if len(v) > 1}
        
        # Refine groups with user input if in interactive mode
        if self.interactive_mode:
            checkbox_groups = self._refine_checkbox_groups(checkbox_groups, checkbox_fields_map)
        
        return checkbox_groups
    
    def _consolidate_same_value_fields(
        self,
        unique_id: str,
        field_names: List[str],
        analysis_map: Dict,
        extraction_map: Dict
    ) -> Optional[Dict]:
        """Consolidate fields that should have the same value"""
        # Use the first field's analysis as base
        base_field = None
        for field_name in field_names:
            if field_name in analysis_map:
                base_field = analysis_map[field_name]
                break
        
        if not base_field or not base_field.get('schema_item'):
            return None
        
        schema_item = base_field['schema_item'].copy()
        
        # Create pdf_attributes array with one entry per field
        pdf_attributes = []
        form_type = self._extract_form_type(field_names[0])
        
        for field_name in field_names:
            pdf_attributes.append({
                'formType': form_type,
                'formfield': field_name
            })
        
        # Build the consolidated schema item
        return {
            'unique_id': unique_id,
            'pdf_attributes': pdf_attributes,
            'display_attributes': schema_item
        }
    
    def _consolidate_continuation_fields(
        self,
        main_field: str,
        continuation_fields: List[str],
        analysis_map: Dict,
        extraction_map: Dict
    ) -> Optional[Dict]:
        """Consolidate text continuation fields"""
        if main_field not in analysis_map:
            return None
        
        base_analysis = analysis_map[main_field]
        if not base_analysis.get('schema_item'):
            return None
        
        schema_item = base_analysis['schema_item'].copy()
        form_type = self._extract_form_type(main_field)
        
        # Create pdf_attributes with linked_form_fields_text
        pdf_attributes = [{
            'formType': form_type,
            'formfield': main_field,
            'linked_form_fields_text': continuation_fields
        }]
        
        return {
            'unique_id': schema_item.get('unique_id'),
            'pdf_attributes': pdf_attributes,
            'display_attributes': schema_item
        }
    
    def _consolidate_linked_dates(
        self,
        signature_field: str,
        date_field: str,
        analysis_map: Dict,
        extraction_map: Dict
    ) -> Optional[Dict]:
        """Consolidate signature with linked date"""
        if signature_field not in analysis_map:
            return None
        
        base_analysis = analysis_map[signature_field]
        if not base_analysis.get('schema_item'):
            return None
        
        schema_item = base_analysis['schema_item'].copy()
        form_type = self._extract_form_type(signature_field)
        
        # Create pdf_attributes with linked_dates
        pdf_attributes = [{
            'formType': form_type,
            'formfield': signature_field,
            'linked_dates': [{'dateFieldName': date_field}]
        }]
        
        return {
            'unique_id': schema_item.get('unique_id'),
            'pdf_attributes': pdf_attributes,
            'display_attributes': schema_item
        }
    
    def _consolidate_radio_group(
        self,
        group_name: str,
        radio_fields: List[Dict],
        analysis_map: Dict,
        extraction_map: Dict
    ) -> Optional[Dict]:
        """Consolidate radio button group"""
        # Try to find analysis for the group
        if group_name in analysis_map:
            base_analysis = analysis_map[group_name]
            if base_analysis.get('schema_item'):
                schema_item = base_analysis['schema_item'].copy()
            else:
                return None
        else:
            # Create a basic schema item for the radio group
            schema_item = {
                'unique_id': self._sanitize_to_snake_case(group_name),
                'display_name': self._humanize_field_name(group_name),
                'input_type': 'radio',
                'attribute': 'selection',
                'order': 1,
                'width': 12
            }
        
        form_type = self._extract_form_type(group_name)
        
        # Extract radio options
        options = []
        for field in radio_fields:
            if 'radio_options' in field:
                options.extend(field['radio_options'])
        
        # Remove duplicates
        unique_options = list(set(options))
        
        # Create linked_form_fields_radio
        linked_radio = [
            {
                'radioField': opt,
                'displayName': self._humanize_field_name(opt)
            }
            for opt in unique_options
        ]
        
        # Create pdf_attributes
        pdf_attributes = [{
            'formType': form_type,
            'formfield': group_name,
            'linked_form_fields_radio': linked_radio
        }]
        
        # Add display_radio_options to schema_item
        schema_item['display_radio_options'] = [item['displayName'] for item in linked_radio]
        
        return {
            'unique_id': schema_item.get('unique_id'),
            'pdf_attributes': pdf_attributes,
            'display_attributes': schema_item
        }
    
    def _create_schema_item(
        self,
        schema_item: Dict,
        field_name: str,
        extraction_data: Dict
    ) -> Dict:
        """Create a standard schema item structure"""
        form_type = self._extract_form_type(field_name)
        
        return {
            'unique_id': schema_item.get('unique_id'),
            'pdf_attributes': [{
                'formType': form_type,
                'formfield': field_name
            }],
            'display_attributes': schema_item
        }
    
    def _extract_form_type(self, field_name: str) -> str:
        """Extract form type from field name"""
        # Assuming field names follow pattern: formtype_fieldtype_number
        parts = field_name.split('_')
        if len(parts) >= 3:
            # Remove the field type and number parts
            return '_'.join(parts[:-2])
        return 'unknown_form'
    
    def _sanitize_to_snake_case(self, text: str) -> str:
        """Convert text to snake_case"""
        # Remove special characters and convert to lowercase
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', '_', text)
        return text.lower()
    
    def _humanize_field_name(self, field_name: str) -> str:
        """Convert field name to human-readable format"""
        # Remove underscores and capitalize words
        words = field_name.split('_')
        # Remove common suffixes
        if words and words[-1].isdigit():
            words = words[:-1]
        if words and words[-1] in ['textfield', 'checkbox', 'radio']:
            words = words[:-1]
        
        return ' '.join(word.capitalize() for word in words)
    
    def _normalize_blocks(self, consolidated_items: List[Dict]):
        """
        Normalize block names and styles across all items
        to ensure consistency
        """
        # First pass: collect all blocks and their variations
        block_variations = defaultdict(list)
        
        for item in consolidated_items:
            display_attrs = item.get('display_attributes', {})
            block = display_attrs.get('block')
            block_style = display_attrs.get('block_style', {})
            
            if block:
                # Store the variation with its style
                block_key = self._normalize_block_name(block)
                block_variations[block_key].append({
                    'original': block,
                    'style': block_style,
                    'count': 1
                })
        
        # Second pass: determine canonical versions
        canonical_blocks = {}
        
        for block_key, variations in block_variations.items():
            # Count occurrences of each variation
            variation_counts = defaultdict(int)
            style_counts = defaultdict(lambda: {'count': 0, 'style': {}})
            
            for var in variations:
                variation_counts[var['original']] += 1
                style_key = json.dumps(var['style'], sort_keys=True)
                style_counts[style_key]['count'] += 1
                style_counts[style_key]['style'] = var['style']
            
            # Choose most common variation as canonical
            canonical_name = max(variation_counts.items(), key=lambda x: x[1])[0]
            
            # Choose most common style as canonical
            canonical_style = max(style_counts.values(), key=lambda x: x['count'])['style']
            
            canonical_blocks[block_key] = {
                'name': canonical_name,
                'style': canonical_style
            }
        
        # Third pass: apply canonical versions
        for item in consolidated_items:
            display_attrs = item.get('display_attributes', {})
            block = display_attrs.get('block')
            
            if block:
                block_key = self._normalize_block_name(block)
                if block_key in canonical_blocks:
                    display_attrs['block'] = canonical_blocks[block_key]['name']
                    display_attrs['block_style'] = canonical_blocks[block_key]['style']
    
    def _normalize_block_name(self, block_name: str) -> str:
        """
        Normalize a block name for comparison
        """
        # Convert to lowercase and remove extra spaces
        normalized = block_name.lower().strip()
        normalized = ' '.join(normalized.split())
        
        # Remove common variations
        replacements = {
            'information': 'info',
            'details': 'info',
            'buyer': 'buyer',
            'seller': 'seller',
            'property': 'property',
            'financial': 'financial',
            'finance': 'financial',
            'signatures': 'signatures',
            'signature': 'signatures'
        }
        
        for old, new in replacements.items():
            normalized = normalized.replace(old, new)
        
        return normalized
    
    def _consolidate_checkbox_group(
        self,
        group_key: str,
        checkbox_field_names: List[str],
        analysis_map: Dict,
        extraction_map: Dict
    ) -> Optional[Dict]:
        """Consolidate multiple checkboxes into a single schema item with checkbox_options"""
        # Collect all checkbox data
        checkbox_items = []
        base_schema = None
        
        for field_name in checkbox_field_names:
            if field_name in analysis_map:
                analysis = analysis_map[field_name]
                if analysis.get('schema_item'):
                    checkbox_items.append({
                        'field_name': field_name,
                        'schema_item': analysis['schema_item'],
                        'extraction': extraction_map.get(field_name, {})
                    })
                    
                    # Use the first checkbox as base
                    if base_schema is None:
                        base_schema = analysis['schema_item'].copy()
        
        if not checkbox_items or not base_schema:
            return None
        
        # Build checkbox options from individual checkboxes
        options = []
        linked_checkbox_fields = []
        
        for item in checkbox_items:
            schema = item['schema_item']
            field_name = item['field_name']
            
            # Create linked checkbox field entry
            linked_checkbox_fields.append({
                'checkboxField': field_name,
                'displayName': schema.get('display_name', 'Option')
            })
            
            # Create option from individual checkbox
            option = {
                'display_name': schema.get('display_name', 'Option'),
                'databaseStored': self._to_database_stored(schema.get('display_name', 'OPTION'))
            }
            
            # Check if this checkbox had any linkedFields mentioned
            if 'checkbox_options' in schema and schema['checkbox_options'].get('options'):
                # This checkbox already had options defined, use them
                existing_options = schema['checkbox_options']['options']
                if existing_options:
                    options.extend(existing_options)
            else:
                # Single checkbox, add it as an option
                options.append(option)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_options = []
        for opt in options:
            opt_key = opt['databaseStored']
            if opt_key not in seen:
                seen.add(opt_key)
                unique_options.append(opt)
        
        # Update the base schema
        base_schema['checkbox_options'] = {
            'options': unique_options
        }
        
        # Determine if this is single or multi-select based on context
        # If it's in the same unique_id group, likely single-select
        if group_key.startswith('uid_'):
            base_schema['checkbox_options']['maxSelected'] = 1
            base_schema['checkbox_options']['minSelected'] = 1
        
        # Update display name to be more general
        if len(unique_options) > 1:
            # Try to find a common theme in the display names
            common_words = self._find_common_theme(
                [cb['schema_item'].get('display_name', '') for cb in checkbox_items]
            )
            if common_words:
                base_schema['display_name'] = common_words
        
        # Create pdf_attributes with linked_form_fields_checkbox
        form_type = self._extract_form_type(checkbox_field_names[0])
        
        # Use the first checkbox field as the main field
        pdf_attributes = [{
            'formType': form_type,
            'formfield': checkbox_field_names[0],
            'linked_form_fields_checkbox': linked_checkbox_fields
        }]
        
        return {
            'unique_id': base_schema.get('unique_id'),
            'pdf_attributes': pdf_attributes,
            'display_attributes': base_schema
        }
    
    def _to_database_stored(self, display_name: str) -> str:
        """Convert display name to database stored format (UPPERCASE_SNAKE_CASE)"""
        # Remove special characters and convert to uppercase
        import re
        cleaned = re.sub(r'[^\w\s]', '', display_name)
        words = cleaned.upper().split()
        return '_'.join(words)
    
    def _find_common_theme(self, names: List[str]) -> str:
        """Find common theme in a list of names"""
        if not names:
            return ""
        
        # Simple approach: find common words
        from collections import Counter
        all_words = []
        
        for name in names:
            words = name.lower().split()
            all_words.extend(words)
        
        # Count word frequency
        word_counts = Counter(all_words)
        
        # Find words that appear in multiple names
        common_words = [word for word, count in word_counts.items() 
                       if count > 1 and len(word) > 2]
        
        if common_words:
            # Capitalize and join
            return ' '.join(word.capitalize() for word in common_words[:2])
        
        return "Options"
    
    def _group_by_semantic_similarity(self, checkboxes: List[Dict]) -> List[List[Dict]]:
        """Group checkboxes by semantic similarity"""
        groups = []
        processed = set()
        
        for i, checkbox in enumerate(checkboxes):
            if i in processed:
                continue
                
            # Start a new group with this checkbox
            current_group = [checkbox]
            processed.add(i)
            
            # Find similar checkboxes
            for j, other_checkbox in enumerate(checkboxes):
                if j in processed or i == j:
                    continue
                    
                if self._are_checkboxes_related(checkbox, other_checkbox):
                    current_group.append(other_checkbox)
                    processed.add(j)
            
            groups.append(current_group)
        
        return groups
    
    def _are_checkboxes_related(self, cb1: Dict, cb2: Dict) -> bool:
        """Check if two checkboxes are semantically related"""
        # Get display names
        name1 = cb1.get('display_name', '').lower()
        name2 = cb2.get('display_name', '').lower()
        
        # Check for common keywords that indicate they're related
        # Keywords for addenda/documents
        doc_keywords = ['addendum', 'addenda', 'disclosure', 'information', 'authorization', 
                       'document', 'form', 'notice', 'agreement', 'report']
        
        # Keywords for options/features
        option_keywords = ['type', 'option', 'method', 'style', 'feature', 'included', 'available']
        
        # Keywords for property features
        property_keywords = ['amenity', 'appliance', 'utility', 'service', 'included']
        
        # Check if both names contain keywords from the same category
        name1_has_doc = any(keyword in name1 for keyword in doc_keywords)
        name2_has_doc = any(keyword in name2 for keyword in doc_keywords)
        
        name1_has_option = any(keyword in name1 for keyword in option_keywords)
        name2_has_option = any(keyword in name2 for keyword in option_keywords)
        
        name1_has_property = any(keyword in name1 for keyword in property_keywords)
        name2_has_property = any(keyword in name2 for keyword in property_keywords)
        
        # They're related if they're in the same category
        if name1_has_doc and name2_has_doc:
            return True
        if name1_has_option and name2_has_option:
            return True
        if name1_has_property and name2_has_property:
            return True
        
        # Also check attribute similarity
        attr1 = cb1.get('attribute', '')
        attr2 = cb2.get('attribute', '')
        if attr1 and attr2 and attr1 == attr2:
            return True
        
        # Check for common words (excluding stop words)
        stop_words = {'the', 'a', 'an', 'is', 'are', 'of', 'for', 'to', 'in', 'on', 'with', 'by'}
        words1 = set(name1.split()) - stop_words
        words2 = set(name2.split()) - stop_words
        
        # If they share significant words, they might be related
        common_words = words1.intersection(words2)
        if len(common_words) >= 2 or (len(common_words) == 1 and len(words1) <= 3 and len(words2) <= 3):
            return True
        
        return False
    
    def _ask_user_about_grouping(self, checkboxes: List[Dict], reason: str) -> bool:
        """Ask user whether checkboxes should be grouped together"""
        if not self.interactive_mode:
            return True  # Default to grouping if not in interactive mode
        
        print("\n" + "="*60)
        print("CHECKBOX GROUPING DECISION NEEDED")
        print("="*60)
        print(f"\nReason: {reason}\n")
        print("Should these checkboxes be grouped together as options in a single field?\n")
        
        for i, cb in enumerate(checkboxes, 1):
            print(f"{i}. {cb.get('display_name', 'Unknown')} (ID: {cb.get('unique_id', 'unknown')})")
            if cb.get('schema_item', {}).get('description'):
                print(f"   Description: {cb['schema_item']['description']}")
        
        print("\nThey are all in the block:", checkboxes[0].get('block', 'Unknown'))
        
        while True:
            response = input("\nGroup these checkboxes together? (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")
    
    def _refine_checkbox_groups(self, checkbox_groups: Dict[str, List[str]], 
                               checkbox_fields_map: Dict[str, Dict]) -> Dict[str, List[str]]:
        """Refine checkbox groups with user input if in interactive mode"""
        if not self.interactive_mode:
            return checkbox_groups
        
        refined_groups = {}
        
        for group_key, field_names in checkbox_groups.items():
            # Get the checkbox details
            checkboxes = []
            for field_name in field_names:
                if field_name in checkbox_fields_map:
                    checkboxes.append(checkbox_fields_map[field_name])
            
            if len(checkboxes) < 2:
                continue
            
            # Determine confidence in grouping
            confidence_score = self._calculate_grouping_confidence(checkboxes)
            
            # Ask user if confidence is medium (between 0.4 and 0.7)
            if 0.4 <= confidence_score <= 0.7:
                reason = f"Medium confidence (score: {confidence_score:.2f}) - similar but not clearly related"
                if self._ask_user_about_grouping(checkboxes, reason):
                    refined_groups[group_key] = field_names
            elif confidence_score > 0.7:
                # High confidence - auto group
                refined_groups[group_key] = field_names
            # Low confidence - don't group (unless user said yes above)
        
        return refined_groups
    
    def _calculate_grouping_confidence(self, checkboxes: List[Dict]) -> float:
        """Calculate confidence score for grouping checkboxes (0-1)"""
        score = 0.0
        
        # Check if they have the same attribute
        attributes = [cb.get('attribute', '') for cb in checkboxes]
        if len(set(attributes)) == 1 and attributes[0]:
            score += 0.3
        
        # Check if they're semantically related
        all_related = True
        for i in range(len(checkboxes)):
            for j in range(i + 1, len(checkboxes)):
                if not self._are_checkboxes_related(checkboxes[i], checkboxes[j]):
                    all_related = False
                    break
            if not all_related:
                break
        
        if all_related:
            score += 0.4
        
        # Check proximity
        pages = [cb.get('page', 0) for cb in checkboxes]
        if len(set(pages)) == 1:  # All on same page
            positions = [cb.get('position', [0, 0, 0, 0]) for cb in checkboxes]
            # Check if they're close together
            y_positions = [pos[1] for pos in positions]
            if max(y_positions) - min(y_positions) < 100:  # Within 100 pixels
                score += 0.3
        
        return min(score, 1.0)
    
    def generate_summary(self, consolidated_items: List[Dict], original_count: int) -> str:
        """Generate a summary of the consolidation process"""
        summary = []
        summary.append(f"Consolidation Summary:")
        summary.append(f"- Original fields: {original_count}")
        summary.append(f"- Consolidated schema items: {len(consolidated_items)}")
        summary.append(f"- Reduction: {original_count - len(consolidated_items)} fields")
        
        # Count different types
        same_value_count = sum(1 for item in consolidated_items 
                              if len(item.get('pdf_attributes', [])) > 1)
        continuation_count = sum(1 for item in consolidated_items 
                               if any('linked_form_fields_text' in attr 
                                     for attr in item.get('pdf_attributes', [])))
        linked_date_count = sum(1 for item in consolidated_items 
                              if any('linked_dates' in attr 
                                    for attr in item.get('pdf_attributes', [])))
        radio_count = sum(1 for item in consolidated_items 
                         if any('linked_form_fields_radio' in attr 
                               for attr in item.get('pdf_attributes', [])))
        checkbox_count = sum(1 for item in consolidated_items 
                            if item.get('display_attributes', {}).get('input_type') == 'checkbox' and
                            'checkbox_options' in item.get('display_attributes', {}) and
                            len(item.get('pdf_attributes', [])) > 1)
        
        summary.append(f"\nConsolidation types:")
        summary.append(f"- Same-value fields: {same_value_count}")
        summary.append(f"- Continuation fields: {continuation_count}")
        summary.append(f"- Linked date fields: {linked_date_count}")
        summary.append(f"- Radio button groups: {radio_count}")
        summary.append(f"- Checkbox groups: {checkbox_count}")
        
        return '\n'.join(summary)


def main():
    """Test the schema consolidator"""
    # Example test data
    analyzed_fields = [
        {
            'field_name': 'form_textfield_1',
            'status': 'success',
            'schema_item': {
                'unique_id': 'buyer_name',
                'display_name': 'Buyer Name',
                'input_type': 'text'
            }
        },
        {
            'field_name': 'form_textfield_5',
            'status': 'success',
            'schema_item': {
                'unique_id': 'buyer_name',
                'display_name': 'Buyer Name',
                'input_type': 'text'
            }
        }
    ]
    
    extracted_fields = [
        {
            'field_name': 'form_textfield_1',
            'field_type': 'Text',
            'page': 0,
            'position': [100, 100, 300, 120]
        },
        {
            'field_name': 'form_textfield_5',
            'field_type': 'Text',
            'page': 2,
            'position': [100, 200, 300, 220]
        }
    ]
    
    consolidator = SchemaConsolidator()
    consolidated = consolidator.consolidate_fields(analyzed_fields, extracted_fields)
    
    print("Consolidated schema items:")
    for item in consolidated:
        print(f"- {item['unique_id']}: {len(item['pdf_attributes'])} PDF fields")
    
    print("\n" + consolidator.generate_summary(consolidated, len(extracted_fields)))


if __name__ == "__main__":
    main()