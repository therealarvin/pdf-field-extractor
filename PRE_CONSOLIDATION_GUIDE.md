# Pre-Consolidation Workflow Guide

This document explains the new pre-consolidation workflow that groups related fields before AI analysis.

## Overview

The updated schema generation workflow now follows these steps:

1. **Extract Fields** - Extract all form fields from the PDF
2. **Pre-Consolidate** - Group related fields together (checkboxes, continuations, etc.)
3. **Capture Group Screenshots** - Take screenshots with ALL fields in each group highlighted
4. **Analyze Groups** - Send each group to AI for consolidated analysis
5. **Generate Schema** - Create final TypeScript schema

## Benefits

- **Better Context**: AI sees all related fields together
- **Fewer API Calls**: One call per group instead of per field
- **More Accurate**: Prevents conflicting schemas for related fields
- **Clearer Visuals**: All checkboxes/fields in a group are highlighted together

## Usage

### Basic Usage
```bash
python generate_schema_with_openai.py form.pdf
```

### With Interactive Mode
```bash
python generate_schema_with_openai.py form.pdf --interactive
```

### Save Preview Screenshot
```bash
# Save screenshot of the 5th group
python generate_schema_with_openai.py form.pdf --save-preview 5
```

### Save Intermediate Results
```bash
python generate_schema_with_openai.py form.pdf --save-intermediate
```

## Pre-Consolidation Groups

The system automatically identifies these types of field groups:

### 1. Checkbox Groups
The system detects multiple types of checkbox arrangements:

**Horizontal Groups** (High priority):
- Checkboxes in a row (e.g., □ Yes □ No □ Maybe)
- Within 20px vertically and reasonable horizontal spacing

**Vertical Groups**:
- Checkboxes in a column
- Respects natural boundaries like (a), (b) section markers
- Splits groups when large gaps (>100px) are detected

**Mixed Groups**:
- Clusters of checkboxes that could be grouped multiple ways
- User chooses between horizontal, vertical, or combined grouping

In interactive mode, you'll see multiple options:
- Option 0: No grouping
- Option 1: Horizontal grouping
- Option 2: Vertical grouping
- Option 3: Combined grouping
- Option 4: Multiple separate groups

### 2. Text Continuations
- Fields with "_continued", "_line_2" suffixes
- Horizontally aligned fields close vertically
- Multi-line addresses, descriptions

### 3. Linked Dates
- Signature fields with nearby date fields
- Automatically linked based on proximity

### 4. Radio Groups
- Already grouped by field name in PDFs
- All options analyzed together

### 5. Same-Value Fields
- Same field appearing on multiple pages
- Similar position and type

### 6. Individual Fields
- Fields that don't match any grouping pattern
- Processed individually

## Group Analysis

When the AI analyzes a group, it:
- Sees ALL fields highlighted in red
- Understands they're related
- Creates ONE schema item for the entire group
- For checkboxes: creates proper `checkbox_options`
- For continuations: may suggest `text-area` input type

## Output Structure

The final schema uses proper structures:

### Checkbox Groups
```typescript
{
  pdf_attributes: [{
    formType: "form_name",
    formfield: "checkbox_1",
    linked_form_fields_checkbox: [
      { checkboxField: "checkbox_1", displayName: "Option 1" },
      { checkboxField: "checkbox_2", displayName: "Option 2" },
      { checkboxField: "checkbox_3", displayName: "Option 3" }
    ]
  }],
  display_attributes: {
    input_type: "checkbox",
    checkbox_options: {
      options: [
        { display_name: "Option 1", databaseStored: "OPTION_1" },
        { display_name: "Option 2", databaseStored: "OPTION_2" },
        { display_name: "Option 3", databaseStored: "OPTION_3" }
      ]
    }
  }
}
```

## Interactive Mode

When using `--interactive`, the system will ask for your input on:

### 1. Checkbox Groupings
- Shows uncertain checkbox groupings
- Displays all checkboxes in the potential group with their positions
- Asks if they should be grouped together
- Uses your decision for final grouping

### 2. Text Continuations
- Shows ALL potential text field continuations
- Displays field positions, dimensions, and context
- Warns about sequential field numbers
- Requires confirmation before grouping

### 3. Same-Value Fields
- Shows ALL fields that appear in similar positions on different pages
- Displays page numbers, positions, and dimensions
- Requires confirmation that fields should contain the same value
- Examples: buyer name on multiple pages, property address repeated

## Debugging

To debug grouping decisions:

1. Use `--save-intermediate` to see:
   - `*_field_groups.json` - How fields were grouped
   - `*_group_analysis_results.json` - AI analysis of each group

2. Use `--save-preview N` to save a screenshot of group N

3. Check confidence scores in the groups JSON

## Customization

### Proximity Thresholds
The system uses adaptive thresholds based on document layout:
- Calculates average spacing between fields
- Groups checkboxes within 1.5x median spacing
- Maximum threshold of 50px

### Semantic Grouping
Checkboxes are grouped by:
- Document keywords (addendum, disclosure, etc.)
- Option keywords (type, method, style)
- Property keywords (amenity, appliance, utility)
- Common words between names