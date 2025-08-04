#!/usr/bin/env python3
"""
Groq Schema Generator
Parallel API processing for field analysis using Groq
"""

import json
import base64
from typing import Dict, List, Optional, Any
from pathlib import Path
import time
from dataclasses import dataclass
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import random


@dataclass
class OpenAIConfig:
    api_key: str
    model: str = "gpt-4o-mini"  # GPT-4 mini with vision capabilities
    api_url: str = "https://api.openai.com/v1/chat/completions"
    max_retries: int = 100  # Very high to ensure eventual success
    timeout: int = 30
    rate_limit_retry_base: float = 5.0  # Base wait time for rate limits


class OpenAISchemaGenerator:
    def __init__(self, api_key: str):
        self.config = OpenAIConfig(api_key=api_key)
        self.system_prompt = self._load_system_prompt()
        self.group_system_prompt = self._load_group_system_prompt()
        self.existing_blocks = {}  # Track existing blocks as they're created
        self.existing_display_names = set()  # Track all display names to prevent duplicates
        self.last_request_time = 0
        self.request_count = 0
        self.rate_limit_window = 60  # 1 minute window
        self.rate_limit_delay = 0.5  # Minimum delay between requests
        
    def _load_system_prompt(self) -> str:
        """Load the system prompt from file or use default"""
        prompt_path = Path(__file__).parent / "prompts" / "system_prompt.txt"
        
        if prompt_path.exists():
            with open(prompt_path, 'r') as f:
                return f.read()
        else:
            # Use embedded prompt if file doesn't exist
            return self._get_default_system_prompt()
    
    def _load_group_system_prompt(self) -> str:
        """Load the group system prompt from file"""
        prompt_path = Path(__file__).parent / "prompts" / "group_system_prompt.txt"
        
        if prompt_path.exists():
            with open(prompt_path, 'r') as f:
                return f.read()
        else:
            # Fallback to regular prompt if group prompt doesn't exist
            return self._load_system_prompt()
    
    def _get_default_system_prompt(self) -> str:
        """Get the default system prompt"""
        return """You are a PDF form field analyzer specializing in generating TypeScript schema items. You will analyze a screenshot of a PDF form field (highlighted with a red rectangle) and generate a complete schema item definition.

CRITICAL CONTEXT:
- The field names are programmatically generated (e.g., form_name_textfield_1, form_name_checkbox_2) and carry NO semantic meaning
- You MUST determine the field's purpose entirely from the visual context around it
- Look for labels, surrounding text, section headers, and nearby fields to understand what data this field should collect

YOUR TASK:
Analyze the highlighted field and generate a JSON object with ALL required schema properties. The field type is: {field_type}

For ALL fields, you must provide:

1. **unique_id**: A semantic identifier based on the field's purpose (e.g., "buyer_name", "property_address", "financing_conventional")
   - Use snake_case
   - Be descriptive but concise
   - NEVER use the iterative field name

2. **display_name**: User-friendly label (e.g., "Buyer Name", "Property Address")
   - Use proper capitalization
   - Be clear and professional
   - Keep it concise

3. **description**: Optional help text if the field needs clarification

4. **attribute**: Simple semantic tag (e.g., "name", "address", "date", "signature")

5. **order**: Sequential number (you can use placeholder 1, will be adjusted later)

6. **block**: Logical grouping name (e.g., "Property Information", "Buyer Details", "Financial Terms")

7. **block_style**: Style object for the block:
   - title: Display title for the block
   - icon: Icon name (home, user, dollar-sign, calendar, pen-tool, etc.)
   - color_theme: blue, green, orange, purple, or gray

8. **width**: Grid width 1-12:
   - 12: Full width (addresses, descriptions)
   - 8-9: Three-quarters (company names, long text)
   - 6: Half width (names, emails)
   - 4: Third width (dates, phones, amounts)
   - 3: Quarter width (state, ZIP, checkboxes)

9. **placeholder**: Example text for the field

10. **validation**: Validation rules based on field type:
    - Phone: regex for phone format
    - Email: regex for email format
    - Date: regex for MM/DD/YYYY
    - Currency: regex for monetary amounts
    - Percentage: regex for percentages

11. **special_input**: Modifiers for special formatting:
    - For monetary fields: { "text": { "currency": true } }
    - For phone fields: { "text": { "phone": true } }
    - For date fields: { "text": { "date": true } }
    - For percentage fields: { "text": { "percentage": true } }
    - For email fields: { "text": { "email": true } }

12. **isCached**: true for realtor/agent/broker information fields

13. **isRequired**: true for essential fields (names, addresses, signatures)

14. **input_type**: The type of input control:
    - "text" for standard text fields
    - "text-area" for multi-line text (descriptions, notes, terms)
    - "signature" for signature/initial fields
    - "checkbox" for checkbox fields
    - "radio" for radio button groups
    - "info" for informational headers (rarely used)

15. **value**: Object defining how the field value is handled:
    - For most fields: { "type": "manual" }
    - For signatures: { "type": "manual", "output": "SignatureInput__signer" }
    - For pre-filled realtor info: { "type": "reserved", "reserved": "realtor_name_spaced" }

FOR CHECKBOX FIELDS, additionally provide:

16. **checkbox_options**: Object with:
    - options: Array of objects, each with:
      - display_name: User-friendly option name
      - databaseStored: UPPERCASE_SNAKE_CASE version
      - linkedFields: Array of field IDs that appear when this option is selected (if applicable)
    - maxSelected: Maximum selections allowed (omit for unlimited)
    - minSelected: Minimum selections required

17. **visibleIf**: Conditions for showing this field (if it depends on other fields)

FOR TEXT FIELDS that might be:
- **Signatures**: Set input_type to "signature" if the field is for signatures/initials
- **Text areas**: Set input_type to "text-area" for long descriptions/notes
- **Radio buttons**: If you see multiple related options that should be single-select, note this

IMPORTANT PATTERNS TO RECOGNIZE:
- Fields with "$" or "amount" or "price" → Add currency special_input
- Fields with "%" or "percent" or "rate" → Add percentage special_input
- Fields near signatures with "date" → These are linked date fields
- Multiple checkboxes in a group → These might be financing options, property features, etc.
- Fields that repeat on multiple pages → These are same-value fields

RESPONSE FORMAT:
Return ONLY a valid JSON object with the schema properties. Do not include any explanation or markdown formatting.

Example response for a text field:
{
  "unique_id": "buyer_full_name",
  "display_name": "Buyer Full Name",
  "description": "Legal name of the property buyer",
  "attribute": "name",
  "order": 1,
  "block": "Buyer Information",
  "block_style": {
    "title": "Buyer Information",
    "icon": "user",
    "color_theme": "green"
  },
  "width": 6,
  "placeholder": "John Doe",
  "validation": null,
  "special_input": null,
  "isCached": false,
  "isRequired": true,
  "input_type": "text",
  "value": {
    "type": "manual"
  }
}

Example response for a checkbox field:
{
  "unique_id": "financing_options",
  "display_name": "Financing Type",
  "description": "Select the type of financing for this purchase",
  "attribute": "financing",
  "order": 1,
  "block": "Financial Details",
  "block_style": {
    "title": "Financial Details",
    "icon": "dollar-sign",
    "color_theme": "orange"
  },
  "width": 12,
  "placeholder": null,
  "validation": null,
  "special_input": null,
  "isCached": false,
  "isRequired": true,
  "input_type": "checkbox",
  "value": {
    "type": "manual"
  },
  "checkbox_options": {
    "options": [
      {
        "display_name": "Conventional",
        "databaseStored": "CONVENTIONAL",
        "linkedFields": ["conventional_loan_amount"]
      },
      {
        "display_name": "FHA",
        "databaseStored": "FHA",
        "linkedFields": ["fha_case_number"]
      }
    ],
    "minSelected": 1,
    "maxSelected": 1
  }
}"""
    
    def analyze_field_sync(self, field_data: Dict, screenshot_base64: str, full_page_base64: Optional[str] = None) -> Dict[str, Any]:
        """
        Analyze a single field synchronously
        
        Args:
            field_data: Field information dictionary
            screenshot_base64: Base64 encoded screenshot of field context
            full_page_base64: Optional base64 encoded full page screenshot
            
        Returns:
            Dictionary with field analysis results
        """
        field_type = field_data.get('field_type', 'Unknown')
        field_name = field_data.get('field_name', 'unknown_field')
        
        # Format system prompt with field type and existing blocks
        system_prompt = self.system_prompt.replace('{field_type}', field_type)
        
        # Add existing blocks context if we have any
        if self.existing_blocks:
            blocks_context = "\n\nEXISTING BLOCKS IN THIS FORM:\n"
            for block_name, block_info in self.existing_blocks.items():
                blocks_context += f"- {block_name}: {block_info['icon']} ({block_info['color_theme']})\n"
            blocks_context += "\nYou should use one of these existing blocks if the field belongs to that category, but you can create a new block if none of these are appropriate.\n"
            system_prompt = system_prompt + blocks_context
        
        # Add existing display names to prevent duplicates
        if self.existing_display_names:
            names_context = "\n\nALREADY USED DISPLAY NAMES IN THIS FORM:\n"
            names_context += ", ".join(sorted(self.existing_display_names)[:20])  # Show first 20
            if len(self.existing_display_names) > 20:
                names_context += f", ... and {len(self.existing_display_names) - 20} more"
            names_context += "\n\nYou MUST create a different, more specific display name that doesn't duplicate any of these.\n"
            system_prompt = system_prompt + names_context
        
        # Prepare the request
        headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json"
        }
        
        # Build the message - check screenshot size
        screenshot_size = len(screenshot_base64)
        if screenshot_size > 5500000:  # ~4MB after base64 encoding
            print(f"Warning: Screenshot for {field_name} is {screenshot_size/1024/1024:.1f}MB (base64), may be too large")
        
        user_message = {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Analyze this PDF form field '{field_name}' (highlighted in red rectangle) and generate a complete schema item definition. The field type is: {field_type}"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{screenshot_base64}"
                    }
                }
            ]
        }
        
        payload = {
            "model": self.config.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                user_message
            ],
            "temperature": 0.1,  # Low temperature for consistent output
            "max_tokens": 2000
        }
        
        # Retry logic
        for attempt in range(self.config.max_retries):
            try:
                # Rate limiting - ensure minimum delay between requests
                current_time = time.time()
                time_since_last = current_time - self.last_request_time
                if time_since_last < self.rate_limit_delay:
                    time.sleep(self.rate_limit_delay - time_since_last)
                
                self.last_request_time = time.time()
                response = requests.post(
                    self.config.api_url,
                    headers=headers,
                    json=payload,
                    timeout=self.config.timeout
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Check for API errors in response
                    if 'error' in result:
                        return {
                            'field_name': field_name,
                            'status': 'error',
                            'error': f"API returned error: {result['error']}"
                        }
                    
                    # Extract the content
                    content = result.get('choices', [{}])[0].get('message', {}).get('content', '')
                    
                    # Debug first response
                    if field_name.endswith('_1'):
                        print(f"First field response preview: {content[:200]}")
                    
                    # Parse JSON from content
                    try:
                        # First try to parse as-is
                        schema_item = json.loads(content)
                        
                        # Track the block if it's new
                        if 'block' in schema_item and 'block_style' in schema_item:
                            block_name = schema_item['block']
                            if block_name not in self.existing_blocks:
                                self.existing_blocks[block_name] = {
                                    'title': schema_item['block_style'].get('title', block_name),
                                    'icon': schema_item['block_style'].get('icon', 'file'),
                                    'color_theme': schema_item['block_style'].get('color_theme', 'gray')
                                }
                        
                        # Track the display name
                        if 'display_name' in schema_item:
                            self.existing_display_names.add(schema_item['display_name'])
                        
                        return {
                            'field_name': field_name,
                            'status': 'success',
                            'schema_item': schema_item,
                            'raw_response': result
                        }
                    except json.JSONDecodeError as e:
                        # Try various markdown unwrapping approaches
                        cleaned_content = content.strip()
                        
                        # Check for ```json wrapper
                        if cleaned_content.startswith('```json') and cleaned_content.endswith('```'):
                            cleaned_content = cleaned_content[7:-3].strip()
                        # Check for plain ``` wrapper
                        elif cleaned_content.startswith('```') and cleaned_content.endswith('```'):
                            # Find the first newline after opening ```
                            first_newline = cleaned_content.find('\n')
                            if first_newline > 0:
                                cleaned_content = cleaned_content[first_newline+1:-3].strip()
                            else:
                                cleaned_content = cleaned_content[3:-3].strip()
                        
                        # Try parsing the cleaned content
                        try:
                            schema_item = json.loads(cleaned_content)
                            
                            # Track the block if it's new
                            if 'block' in schema_item and 'block_style' in schema_item:
                                block_name = schema_item['block']
                                if block_name not in self.existing_blocks:
                                    self.existing_blocks[block_name] = {
                                        'title': schema_item['block_style'].get('title', block_name),
                                        'icon': schema_item['block_style'].get('icon', 'file'),
                                        'color_theme': schema_item['block_style'].get('color_theme', 'gray')
                                    }
                            
                            # Track the display name
                            if 'display_name' in schema_item:
                                self.existing_display_names.add(schema_item['display_name'])
                            
                            return {
                                'field_name': field_name,
                                'status': 'success',
                                'schema_item': schema_item,
                                'raw_response': result
                            }
                        except json.JSONDecodeError as parse_error:
                            # Log more details for debugging
                            print(f"JSON parse error for {field_name}:")
                            print(f"  Original content start: {repr(content[:100])}")
                            print(f"  Cleaned content start: {repr(cleaned_content[:100])}")
                            print(f"  Parse error: {str(parse_error)}")
                            return {
                                'field_name': field_name,
                                'status': 'error',
                                'error': f"Failed to parse JSON response: {str(e)}",
                                'raw_content': content
                            }
                else:
                    error_msg = f"API error {response.status_code}: {response.text[:200]}"
                    
                    # Special handling for rate limit errors
                    if response.status_code == 429:
                        if attempt < self.config.max_retries - 1:
                            # Extract retry-after header if available
                            retry_after = response.headers.get('Retry-After')
                            if retry_after:
                                wait_time = int(retry_after) + random.uniform(1, 3)
                            else:
                                # Aggressive exponential backoff for rate limits with cap at 5 minutes
                                wait_time = min(300, self.config.rate_limit_retry_base * (2 ** attempt)) + random.uniform(0, 5)
                            
                            print(f"  Rate limited on {field_name}. Waiting {wait_time:.1f} seconds before retry {attempt + 2}/{self.config.max_retries}...")
                            time.sleep(wait_time)
                            continue
                    elif attempt < self.config.max_retries - 1:
                        # Regular errors get normal backoff
                        wait_time = (2 ** attempt) + random.uniform(0, 1)
                        print(f"  Error {response.status_code} on {field_name}. Retrying in {wait_time:.1f} seconds...")
                        time.sleep(wait_time)
                        continue
                    
                    # Final failure after all retries
                    print(f"Failed after {self.config.max_retries} attempts for {field_name}: {error_msg}")
                    return {
                        'field_name': field_name,
                        'status': 'error',
                        'error': error_msg
                    }
                    
            except requests.exceptions.Timeout:
                if attempt < self.config.max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                return {
                    'field_name': field_name,
                    'status': 'error',
                    'error': 'Request timeout'
                }
            except Exception as e:
                if attempt < self.config.max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                return {
                    'field_name': field_name,
                    'status': 'error',
                    'error': f"Unexpected error: {str(e)}"
                }
        
        return {
            'field_name': field_name,
            'status': 'error',
            'error': 'Max retries exceeded'
        }
    
    def analyze_field_group_sync(self, field_group: Dict, screenshot_base64: str) -> Dict[str, Any]:
        """
        Analyze a group of related fields together
        
        Args:
            field_group: Dictionary containing group information and fields
            screenshot_base64: Base64 encoded screenshot showing all fields in the group
            
        Returns:
            Dictionary with analysis results for the group
        """
        group_type = field_group.get('group_type', 'unknown')
        fields = field_group.get('fields', [])
        
        # Prepare context for the group prompt
        field_types = list(set(f.get('field_type', 'Unknown') for f in fields))
        field_names = [f.get('field_name', 'unknown') for f in fields]
        
        # Format system prompt with group context
        system_prompt = self.group_system_prompt.replace('{group_type}', group_type)
        system_prompt = system_prompt.replace('{num_fields}', str(len(fields)))
        system_prompt = system_prompt.replace('{field_types}', ', '.join(field_types))
        
        # Add existing blocks context
        if self.existing_blocks:
            blocks_context = "\n\nEXISTING BLOCKS IN THIS FORM:\n"
            for block_name, block_info in self.existing_blocks.items():
                blocks_context += f"- {block_name}: {block_info['icon']} ({block_info['color_theme']})\n"
            blocks_context += "\nYou should use one of these existing blocks if the fields belong to that category, but you can create a new block if none of these are appropriate.\n"
            system_prompt = system_prompt.replace('{existing_blocks_context}', blocks_context)
        else:
            system_prompt = system_prompt.replace('{existing_blocks_context}', '')
        
        # Add existing display names to prevent duplicates
        if self.existing_display_names:
            names_context = "\n\nALREADY USED DISPLAY NAMES IN THIS FORM:\n"
            names_context += ", ".join(sorted(self.existing_display_names)[:30])  # Show first 30
            if len(self.existing_display_names) > 30:
                names_context += f", ... and {len(self.existing_display_names) - 30} more"
            names_context += "\n\nYou MUST create a different, more specific display name that doesn't duplicate any of these.\n"
            system_prompt = system_prompt + names_context
        
        # Prepare the request
        headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json"
        }
        
        # Create a descriptive message about the group
        group_description = f"This is a {group_type} group containing {len(fields)} fields"
        if group_type == 'checkbox':
            group_description += ". All checkboxes should be analyzed together as options for a single schema item."
        elif group_type == 'text_continuation':
            group_description += ". These text fields continue each other and should be treated as one logical field."
        elif group_type == 'linked_date':
            group_description += ". This is a signature field with its associated date field."
        
        user_message = {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Analyze this group of PDF form fields (all highlighted in red rectangles) and generate a single consolidated schema item. {group_description}"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{screenshot_base64}"
                    }
                }
            ]
        }
        
        payload = {
            "model": self.config.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                user_message
            ],
            "temperature": 0.1,
            "max_tokens": 2000
        }
        
        # Retry logic
        for attempt in range(self.config.max_retries):
            try:
                # Rate limiting - ensure minimum delay between requests
                current_time = time.time()
                time_since_last = current_time - self.last_request_time
                if time_since_last < self.rate_limit_delay:
                    time.sleep(self.rate_limit_delay - time_since_last)
                
                self.last_request_time = time.time()
                response = requests.post(
                    self.config.api_url,
                    headers=headers,
                    json=payload,
                    timeout=self.config.timeout
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Extract and parse content
                    content = result.get('choices', [{}])[0].get('message', {}).get('content', '')
                    
                    try:
                        # Parse JSON
                        schema_item = json.loads(content)
                        
                        # Track the block if it's new
                        if 'block' in schema_item and 'block_style' in schema_item:
                            block_name = schema_item['block']
                            if block_name not in self.existing_blocks:
                                self.existing_blocks[block_name] = {
                                    'title': schema_item['block_style'].get('title', block_name),
                                    'icon': schema_item['block_style'].get('icon', 'file'),
                                    'color_theme': schema_item['block_style'].get('color_theme', 'gray')
                                }
                        
                        # Track the display name
                        if 'display_name' in schema_item:
                            self.existing_display_names.add(schema_item['display_name'])
                        
                        return {
                            'group_type': group_type,
                            'field_names': field_names,
                            'status': 'success',
                            'schema_item': schema_item,
                            'raw_response': result
                        }
                    except json.JSONDecodeError as e:
                        # Try cleaning content
                        cleaned_content = content.strip()
                        if cleaned_content.startswith('```json') and cleaned_content.endswith('```'):
                            cleaned_content = cleaned_content[7:-3].strip()
                        elif cleaned_content.startswith('```') and cleaned_content.endswith('```'):
                            first_newline = cleaned_content.find('\n')
                            if first_newline > 0:
                                cleaned_content = cleaned_content[first_newline+1:-3].strip()
                        
                        try:
                            schema_item = json.loads(cleaned_content)
                            
                            # Track the block
                            if 'block' in schema_item and 'block_style' in schema_item:
                                block_name = schema_item['block']
                                if block_name not in self.existing_blocks:
                                    self.existing_blocks[block_name] = {
                                        'title': schema_item['block_style'].get('title', block_name),
                                        'icon': schema_item['block_style'].get('icon', 'file'),
                                        'color_theme': schema_item['block_style'].get('color_theme', 'gray')
                                    }
                            
                            # Track the display name
                            if 'display_name' in schema_item:
                                self.existing_display_names.add(schema_item['display_name'])
                            
                            return {
                                'group_type': group_type,
                                'field_names': field_names,
                                'status': 'success',
                                'schema_item': schema_item,
                                'raw_response': result
                            }
                        except json.JSONDecodeError:
                            return {
                                'group_type': group_type,
                                'field_names': field_names,
                                'status': 'error',
                                'error': f"Failed to parse JSON response: {str(e)}",
                                'raw_content': content
                            }
                else:
                    error_msg = f"API error {response.status_code}: {response.text[:200]}"
                    
                    # Special handling for rate limit errors
                    if response.status_code == 429:
                        if attempt < self.config.max_retries - 1:
                            # Extract retry-after header if available
                            retry_after = response.headers.get('Retry-After')
                            if retry_after:
                                wait_time = int(retry_after) + random.uniform(1, 3)
                            else:
                                # Aggressive exponential backoff for rate limits with cap at 5 minutes
                                wait_time = min(300, self.config.rate_limit_retry_base * (2 ** attempt)) + random.uniform(0, 5)
                            
                            print(f"  Rate limited on {group_type} group. Waiting {wait_time:.1f} seconds before retry {attempt + 2}/{self.config.max_retries}...")
                            time.sleep(wait_time)
                            continue
                    elif attempt < self.config.max_retries - 1:
                        # Regular errors get normal backoff
                        wait_time = (2 ** attempt) + random.uniform(0, 1)
                        print(f"  Error {response.status_code} on {group_type} group. Retrying in {wait_time:.1f} seconds...")
                        time.sleep(wait_time)
                        continue
                    
                    # Final failure after all retries
                    print(f"Failed after {self.config.max_retries} attempts for {group_type} group: {error_msg}")
                    return {
                        'group_type': group_type,
                        'field_names': field_names,
                        'status': 'error',
                        'error': error_msg
                    }
                    
            except Exception as e:
                if attempt < self.config.max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                return {
                    'group_type': group_type,
                    'field_names': field_names,
                    'status': 'error',
                    'error': f"Unexpected error: {str(e)}"
                }
        
        return {
            'group_type': group_type,
            'field_names': field_names,
            'status': 'error',
            'error': 'Max retries exceeded'
        }
    
    def reset_blocks(self):
        """Reset the existing blocks tracker for a new form"""
        self.existing_blocks = {}
        self.existing_display_names = set()
    
    def analyze_fields(self, fields_with_screenshots: List[Dict], max_concurrent: int = 10) -> List[Dict[str, Any]]:
        """
        Analyze multiple fields in parallel using ThreadPoolExecutor
        
        Args:
            fields_with_screenshots: List of dictionaries with field data and screenshots
            max_concurrent: Maximum number of concurrent API calls (default: 10, reduce this if you get rate limited)
            
        Returns:
            List of analysis results
        """
        results = []
        
        print(f"Processing {len(fields_with_screenshots)} fields with max {max_concurrent} concurrent API calls...")
        
        # Reset blocks for new form
        self.reset_blocks()
        
        # Process fields in batches to maintain block context while still being parallel
        batch_size = min(5, max_concurrent)  # Process in smaller batches
        field_index_map = {}  # Map to maintain original order
        
        for batch_start in range(0, len(fields_with_screenshots), batch_size):
            batch_end = min(batch_start + batch_size, len(fields_with_screenshots))
            batch = fields_with_screenshots[batch_start:batch_end]
            
            print(f"  Processing batch {batch_start//batch_size + 1} (fields {batch_start+1}-{batch_end})...")
            
            with ThreadPoolExecutor(max_workers=min(len(batch), max_concurrent)) as executor:
                future_to_field = {}
                
                for i, field_data in enumerate(batch):
                    actual_index = batch_start + i
                    
                    if field_data.get('screenshot'):  # Only process if screenshot available
                        future = executor.submit(
                            self.analyze_field_sync,
                            field_data['field'],
                            field_data['screenshot'],
                            field_data.get('full_page')
                        )
                        future_to_field[future] = (field_data, actual_index)
                    else:
                        # Add placeholder for fields without screenshots
                        field_index_map[actual_index] = {
                            'field_name': field_data['field'].get('field_name', 'unknown'),
                            'status': 'error',
                            'error': 'No screenshot available'
                        }
                
                # Process completed futures in this batch
                for future in as_completed(future_to_field):
                    try:
                        result = future.result()
                        field_data, index = future_to_field[future]
                        field_index_map[index] = result
                    except Exception as e:
                        field_data, index = future_to_field[future]
                        field_index_map[index] = {
                            'field_name': field_data['field'].get('field_name', 'unknown'),
                            'status': 'error',
                            'error': str(e)
                        }
            
            # Add delay between batches to avoid rate limits
            if batch_end < len(fields_with_screenshots):
                time.sleep(1.0)
        
        # Return results in original order
        for i in range(len(fields_with_screenshots)):
            if i in field_index_map:
                results.append(field_index_map[i])
        
        return results
    
    def print_analysis_summary(self, results: List[Dict[str, Any]]):
        """Print a summary of the analysis results"""
        total = len(results)
        successful = sum(1 for r in results if r.get('status') == 'success')
        failed = total - successful
        
        print(f"\n{'='*60}")
        print(f"ANALYSIS SUMMARY")
        print(f"{'='*60}")
        print(f"Total fields processed: {total}")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        
        if self.existing_blocks:
            print(f"\nBlocks identified ({len(self.existing_blocks)}):")
            for block_name, block_info in self.existing_blocks.items():
                print(f"  - {block_name}: {block_info['icon']} ({block_info['color_theme']})")
        
        if failed > 0:
            print(f"\nFailed fields:")
            for result in results:
                if result.get('status') != 'success':
                    print(f"  - {result.get('field_name')}: {result.get('error')}")
        
        print(f"{'='*60}\n")
    
    def analyze_field_groups(self, groups_with_screenshots: List[Dict], max_concurrent: int = 10) -> List[Dict[str, Any]]:
        """
        Analyze multiple field groups in parallel using ThreadPoolExecutor
        
        Args:
            groups_with_screenshots: List of dictionaries with field groups and screenshots
            max_concurrent: Maximum number of concurrent API calls
            
        Returns:
            List of analysis results
        """
        results = []
        
        print(f"Processing {len(groups_with_screenshots)} field groups with max {max_concurrent} concurrent API calls...")
        
        # Reset blocks for new form
        self.reset_blocks()
        
        # Process groups in batches
        batch_size = min(5, max_concurrent)
        group_index_map = {}
        
        for batch_start in range(0, len(groups_with_screenshots), batch_size):
            batch_end = min(batch_start + batch_size, len(groups_with_screenshots))
            batch = groups_with_screenshots[batch_start:batch_end]
            
            print(f"  Processing batch {batch_start//batch_size + 1} (groups {batch_start+1}-{batch_end})...")
            
            with ThreadPoolExecutor(max_workers=min(len(batch), max_concurrent)) as executor:
                future_to_group = {}
                
                for i, group_data in enumerate(batch):
                    actual_index = batch_start + i
                    
                    if group_data.get('screenshot'):  # Only process if screenshot available
                        future = executor.submit(
                            self.analyze_field_group_sync,
                            group_data['group'],
                            group_data['screenshot']
                        )
                        future_to_group[future] = (group_data, actual_index)
                    else:
                        # Add placeholder for groups without screenshots
                        group_index_map[actual_index] = {
                            'group_type': group_data['group'].get('group_type', 'unknown'),
                            'field_names': [f.get('field_name', 'unknown') for f in group_data['group'].get('fields', [])],
                            'status': 'error',
                            'error': 'No screenshot available'
                        }
                
                # Process completed futures in this batch
                for future in as_completed(future_to_group):
                    try:
                        result = future.result()
                        group_data, index = future_to_group[future]
                        group_index_map[index] = result
                    except Exception as e:
                        group_data, index = future_to_group[future]
                        group_index_map[index] = {
                            'group_type': group_data['group'].get('group_type', 'unknown'),
                            'field_names': [f.get('field_name', 'unknown') for f in group_data['group'].get('fields', [])],
                            'status': 'error',
                            'error': str(e)
                        }
            
            # Add delay between batches to avoid rate limits
            if batch_end < len(groups_with_screenshots):
                time.sleep(1.0)
        
        # Return results in original order
        for i in range(len(groups_with_screenshots)):
            if i in group_index_map:
                results.append(group_index_map[i])
        
        return results


def main():
    """Test the Groq schema generator"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python groq_schema_generator.py <api_key>")
        sys.exit(1)
    
    api_key = sys.argv[1]
    
    # Create test data
    test_fields = [
        {
            'field': {
                'field_name': 'test_textfield_1',
                'field_type': 'Text'
            },
            'screenshot': 'base64_encoded_image_data_here',
            'full_page': None
        }
    ]
    
    # Initialize generator
    generator = OpenAISchemaGenerator(api_key)
    
    # Analyze fields
    print("Testing OpenAI API integration...")
    results = generator.analyze_fields(test_fields, max_concurrent=5)
    
    # Print summary
    generator.print_analysis_summary(results)
    
    # Print detailed results
    for result in results:
        print(f"\nField: {result.get('field_name')}")
        if result.get('status') == 'success':
            print(f"Schema item: {json.dumps(result.get('schema_item'), indent=2)}")
        else:
            print(f"Error: {result.get('error')}")


if __name__ == "__main__":
    main()