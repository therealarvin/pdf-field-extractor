# Manual Field Mapping Workflow

This document describes the process for manually mapping PDF form fields to semantic names.

## Overview

The workflow consists of three main steps:
1. Extract fields with directional context from the PDF
2. Create a manual mapping file based on the extracted context
3. Apply the mapping to rename fields in the PDF

## Step-by-Step Process

### 1. Extract PDF Fields with Context

Use the enhanced extraction script to get fields with directional context:

```bash
python3 extract_pdf_fields_enhanced.py <input.pdf>
```

This creates a JSON file with all fields and their surrounding context (left, right, above, below).

### 2. Create Manual Field Mapping

Analyze the extracted fields JSON and create a mapping file (`field_mapping_<document>.json`) with the structure:

```json
{
  "field_mappings": {
    "original_field_name": "semantic_field_name",
    ...
  },
  "metadata": {
    "total_fields": <count>,
    "mapped_fields": <count>,
    "created_date": "<YYYY-MM-DD>",
    "pdf_file": "<filename>"
  }
}
```

#### Naming Conventions:
- Use descriptive, lowercase names with underscores
- For same value fields across pages, use `_linked_` suffix with page number
- For continuation fields, use `_cont` suffix
- Group related fields with common prefixes (e.g., `tenant_`, `landlord_`, `property_`)
- For checkbox/option fields, use descriptive names indicating the option

### 3. Apply the Mapping

Use the PyMuPDF-based script to apply the mapping:

```bash
python3 apply_field_mapping_fitz.py field_mapping_<document>.json <input.pdf> <extracted_fields.json>
```

This creates:
- A new PDF with renamed fields: `<input>_mapped_[timestamp].pdf`
- Updated JSON metadata: `<extracted_fields>_mapped.json`

## Example Commands

For residential_lease_unlocked.pdf:
```bash
# Extract fields
python3 extract_pdf_fields_enhanced.py residential_lease_unlocked.pdf

# Create mapping (manual step - analyze JSON and create field_mapping.json)

# Apply mapping
python3 apply_field_mapping_fitz.py field_mapping.json residential_lease_unlocked.pdf residential_lease_unlocked_fields_enhanced.json
```

## Important Notes

- The mapping is applied exactly as specified - no automatic renaming occurs
- PyMuPDF (fitz) is used instead of PyPDF2 for reliable field renaming
- Always verify the output PDF to ensure all fields were renamed correctly
- Keep the original PDF as backup

## Completed Documents

1. **residential_lease_unlocked.pdf** (2025-01-20)
   - 287 fields mapped
   - Mapping file: `field_mapping.json`
   - Output: `residential_lease_unlocked_mapped_20250720_165949.pdf`

2. **Exclusive_Right_to_Lease_Commercial_(2).pdf** (2025-01-20)
   - 217 fields mapped
   - Mapping file: `field_mapping_exclusive_lease.json`
   - Output: `Exclusive_Right_to_Lease_Commercial_(2)_mapped_20250720_201631.pdf`

3. **addendum_regarding_residential_leases.pdf** (2025-01-21)
   - 16 fields mapped
   - Mapping file: `field_mapping_addendum_residential_leases.json`
   - Output: `addendum_regarding_residential_leases_mapped_20250720_204250.pdf`