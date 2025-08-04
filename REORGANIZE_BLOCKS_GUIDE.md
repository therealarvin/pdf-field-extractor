# Schema Block Reorganization Guide

This script reorganizes schema items to group them by their blocks, making the schema more organized and easier to navigate.

## What it does

- Groups all schema items that belong to the same block together
- Maintains the relative order of items within each block
- Reassigns sequential order numbers after reorganization
- Provides a summary of blocks and their contents
- Works with both TypeScript (.ts) and JSON (.json) schema files

## Installation

No additional dependencies required - uses Python standard library only.

## Usage

### Basic usage:

```bash
# Reorganize a TypeScript schema file
python reorganize_schema_by_blocks.py path/to/schema.ts

# Reorganize a JSON schema file
python reorganize_schema_by_blocks.py path/to/schema.json
```

### Specify output file:

```bash
python reorganize_schema_by_blocks.py schema.ts -o organized_schema.ts
```

### Command line options:

- `schema_file`: Path to the schema file to reorganize (required)
- `-o, --output`: Custom output file path (default: adds `_reorganized` suffix)
- `--preserve-order`: Keep original order numbers (default: reassign sequentially)

## Examples

### Example 1: Reorganize a generated schema

```bash
# After generating a schema
python generate_schema_with_openai.py "lease_agreement.pdf"

# Reorganize it by blocks
python reorganize_schema_by_blocks.py lease_agreement_schema.ts
```

This creates `lease_agreement_schema_reorganized.ts` with all items grouped by blocks.

### Example 2: Reorganize with custom output

```bash
python reorganize_schema_by_blocks.py residential_lease_schema.ts -o final_lease_schema.ts
```

### Example 3: Process multiple schemas

```bash
for schema in *_schema.ts; do
    python reorganize_schema_by_blocks.py "$schema"
done
```

## Output

The script provides a summary like this:

```
============================================================
BLOCK ORGANIZATION SUMMARY
============================================================

Property Information:
  - Icon: home
  - Color: blue
  - Items: 8
    1. Property Address (property_address)
    2. City (property_city)
    3. State (property_state)
    ... and 5 more

Landlord Information:
  - Icon: user
  - Color: green
  - Items: 5
    1. Landlord Name (landlord_name)
    2. Landlord Phone (landlord_phone)
    3. Landlord Email (landlord_email)
    ... and 2 more

Financial Terms:
  - Icon: dollar-sign
  - Color: orange
  - Items: 6
    1. Monthly Rent (monthly_rent)
    2. Security Deposit (security_deposit)
    3. Late Fee (late_fee)
    ... and 3 more

Total items: 19
============================================================

Reorganized schema saved to: lease_agreement_schema_reorganized.ts
```

## How it works

1. **Parsing**: Reads the TypeScript or JSON file and extracts schema items
2. **Grouping**: Groups items by their `display_attributes.block` value
3. **Ordering**: Maintains block order based on first appearance
4. **Reorganizing**: Rebuilds the array with grouped items
5. **Renumbering**: Assigns new sequential order numbers (1, 2, 3...)
6. **Output**: Writes the reorganized schema maintaining original format

## Benefits

- **Better Organization**: Related fields are kept together
- **Easier Navigation**: Find all fields in a section quickly  
- **Consistent Structure**: Blocks appear in a predictable order
- **Maintains Relationships**: Items within blocks keep their relative positions
- **Clean Output**: Proper TypeScript/JSON formatting is preserved

## Integration with Schema Generation

After generating a schema with OpenAI:

```bash
# Generate schema
python generate_schema_with_openai.py "form.pdf"

# Reorganize by blocks
python reorganize_schema_by_blocks.py form_schema.ts

# Move to application
mv form_schema_reorganized.ts /path/to/app/schemas/
```

## Notes

- The script preserves all schema properties
- Block order is determined by first appearance in original schema
- Items without a block are grouped as "Unknown Block"
- Original file is not modified unless you use `-o` with same filename
- Works with any schema following the standard SchemaItem structure