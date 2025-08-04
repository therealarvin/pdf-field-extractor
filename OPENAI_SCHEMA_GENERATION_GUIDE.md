# OpenAI Schema Generation Guide

This guide explains how to use the automated schema generation system that uses OpenAI GPT-4o-mini to analyze PDF form fields and generate TypeScript schemas.

## Overview

The system analyzes PDF forms with iteratively named fields (e.g., `form_name_textfield_1`, `form_name_checkbox_2`) and generates complete TypeScript schema definitions by:

1. Pre-consolidating related fields into logical groups
2. Taking screenshots with ALL fields in each group highlighted
3. Using OpenAI GPT-4o-mini to analyze each group with full context
4. Generating properly formatted TypeScript schema files

### Benefits of Pre-Consolidation

- **Better Context**: AI sees all related fields together (e.g., all checkboxes for "Addenda Documents")
- **Fewer API Calls**: One API call per group instead of per field (10 checkboxes = 1 call instead of 10)
- **More Accurate**: Prevents conflicting schemas for related fields
- **Proper Structure**: Automatically uses `linked_form_fields_checkbox` for checkbox groups

## Prerequisites

1. Python 3.7+ installed
2. Required Python packages:
   ```bash
   pip install PyMuPDF pdfplumber PyPDF2 aiohttp
   ```

3. PDF forms must have iteratively named fields (processed through the iterative naming workflow)

## Basic Usage

The simplest way to generate a schema:

```bash
python generate_schema_with_openai.py "path/to/your/form.pdf"
```

This will:
- Extract all fields from the PDF
- Capture visual context for each field
- Analyze fields using OpenAI GPT-4o-mini in parallel
- Generate a TypeScript schema file in the current directory

### Rate Limiting

The system now includes automatic retry logic for rate limit errors (429). If you encounter rate limiting:

```bash
# Default: 5 concurrent calls (reduced from 10 for better stability)
python generate_schema_with_openai.py "form.pdf"

# Heavy forms or persistent rate limits: 2-3 concurrent calls
python generate_schema_with_openai.py "form.pdf" --max-concurrent 3

# Single-threaded (slowest but most reliable)
python generate_schema_with_openai.py "form.pdf" --max-concurrent 1
```

**Automatic Rate Limit Handling:**
- Retries up to 100 times (will wait as long as needed)
- Exponential backoff: 5s, 10s, 20s, 40s... up to 5 minutes
- Adds random jitter to prevent thundering herd
- Respects Retry-After headers when provided
- Minimum 0.5s delay between all requests
- **Will always eventually complete** - just be patient!

## Command Line Options

```bash
python generate_schema_with_openai.py [PDF_PATH] [OPTIONS]
```

### Options:

- `--output-dir PATH`: Specify output directory for the schema file (default: current directory)
  ```bash
  python generate_schema_with_openai.py "form.pdf" --output-dir schemas/
  ```

- `--save-intermediate`: Save intermediate JSON files for debugging
  ```bash
  python generate_schema_with_openai.py "form.pdf" --save-intermediate
  ```

- `--max-concurrent N`: Set maximum concurrent API requests (default: 5)
  ```bash
  python generate_schema_with_openai.py "form.pdf" --max-concurrent 3
  ```

- `--api-key KEY`: Override the built-in API key (optional)
  ```bash
  python generate_schema_with_openai.py "form.pdf" --api-key "your_api_key_here"
  ```

- `--interactive`: Enable interactive mode for field grouping decisions
  ```bash
  python generate_schema_with_openai.py "form.pdf" --interactive
  ```
  
  Interactive mode will ask for your confirmation on:
  - Checkbox groupings (which checkboxes form a single field)
  - Text continuations (which text fields are multi-line)
  - Same-value fields (which fields contain the same data on different pages)

- `--gui`: Enable GUI mode for visual field grouping (requires tkinter)
  ```bash
  python generate_schema_with_openai.py "form.pdf" --gui
  ```
  
  GUI mode provides a visual interface where you can:
  - See the PDF with field rectangles overlaid
  - Click fields to select them for grouping
  - Create custom groups with complete control
  - Filter fields by type (checkboxes, text, etc.)
  - Export your grouping decisions
  
  **Important**: In GUI mode:
  - NO automatic grouping is performed
  - ONLY user-created groups are used
  - AI analysis starts after you export groups from GUI
  - Fields not grouped will be processed individually

- `--save-preview N`: Save a preview screenshot of group N (1-indexed)
  ```bash
  python generate_schema_with_openai.py "form.pdf" --save-preview 5
  ```

## Examples

### Generate schema for a single form:
```bash
python generate_schema_with_openai.py "Purchase_Agreement_Fillable.pdf"
```

### Generate schema and save to specific directory:
```bash
python generate_schema_with_openai.py "Lease_Agreement_Fillable.pdf" --output-dir /path/to/schemas/
```

### Debug mode with intermediate files:
```bash
python generate_schema_with_openai.py "form.pdf" --save-intermediate
```

This creates:
- `form_name_extracted_fields.json` - Raw field extraction
- `form_name_field_groups.json` - Pre-consolidation grouping results
- `form_name_group_analysis_results.json` - AI analysis results for each group
- `form_name_consolidated_schema.json` - Consolidated schema before TypeScript conversion

### Process forms with limited API concurrency:
```bash
python generate_schema_with_openai.py "large_form.pdf" --max-concurrent 3
```

### Use interactive mode for field grouping:
```bash
python generate_schema_with_openai.py "complex_form.pdf" --interactive
```

Interactive mode will prompt you for various grouping decisions:

#### Checkbox Grouping:
```
============================================================
CHECKBOX GROUPING DECISION NEEDED
============================================================
Reason: Medium confidence - similar but not clearly related

Should these checkboxes be grouped together as options in a single field?

1. Addendum Regarding Lead-Based Paint
2. Addendum Regarding Rental Flood Disclosure  
3. Information About Brokerage Services

They are all in the block: Addenda and Other Documents

Group these checkboxes together? (y/n): y
```

#### Text Continuation:
```
============================================================
TEXT CONTINUATION DECISION NEEDED
============================================================
These text fields are close together and might be continuations of each other.
Should they be grouped as a single multi-line field?

1. form_textfield_95 (Page 2)
   Position: x=100, y=200, width=400, height=20
   
2. form_textfield_96 (Page 2)
   Position: x=100, y=220, width=400, height=20

⚠️  These fields are numbered sequentially: [95, 96]

Note: Only group these if they form one logical field split across multiple lines.
DO NOT group if they're separate fields for different values.

Group these as text continuation? (y/n): y
```

#### Same-Value Fields:
```
============================================================
SAME-VALUE FIELD DECISION NEEDED
============================================================
These fields appear in similar positions on different pages.
Should they be grouped as fields that will contain the SAME value?

1. form_textfield_15 (Page 1)
   Type: Text
   Position: x=150, y=300
   Size: 200 x 20

2. form_textfield_145 (Page 5)
   Type: Text
   Position: x=150, y=300
   Size: 200 x 20

Note: Only group these if they represent the SAME information repeated on multiple pages.

Group these as same-value fields? (y/n): y
```

## Output

The script generates a TypeScript schema file named `[form_type]_schema.ts` containing:

```typescript
import { SchemaItem } from "../../../../types/realtor";

export const formTypeSchema: SchemaItem[] = [
  {
    unique_id: "buyer_name",
    pdf_attributes: [{
      formType: "purchase_agreement",
      formfield: "purchase_agreement_textfield_1"
    }],
    display_attributes: {
      display_name: "Buyer Name",
      input_type: "text",
      // ... other attributes
    }
  },
  // ... more schema items
];
```

## Moving Schemas to Application

After generation, move the schema to your application:

```bash
mv purchase_agreement_schema.ts /Users/arvin/WebDev/onroad_full/onroad_express/src/logic/realtor/centralIntelligence/schemas/
```

## Batch Processing

To process multiple PDFs:

```bash
for pdf in *.pdf; do
    python generate_schema_with_openai.py "$pdf" --output-dir schemas/
done
```

## How It Works

1. **Field Extraction**: Uses `extract_pdf_fields_enhanced.py` to get all form fields with directional context

2. **Pre-Consolidation**: Groups related fields before AI analysis:
   - **Checkbox Groups**: Based on proximity, semantic similarity, and document structure
   - **Text Continuations**: Fields with "_continued" or "_line_2" patterns
   - **Linked Dates**: Signature fields with nearby date fields
   - **Radio Groups**: Already grouped by field name
   - **Same-Value Fields**: Similar fields on different pages

3. **Visual Context Capture**: Takes full-width screenshots with 200px vertical padding to capture section headers and context

4. **Context-Aware AI Analysis**: 
   - AI receives list of already-used display names to prevent duplicates
   - Emphasis on creating SPECIFIC, DESCRIPTIVE display names
   - Context includes existing blocks for consistency
   - Automatic handling of checkbox special inputs (asRadio, horizontal)

5. **Automatic Field Processing**:
   - **unique_id**: Auto-generated from field names (AI doesn't create these)
   - **value**: Always set to `{ "type": "manual" }`
   - **validation**: Not generated (handled by application)
   - **databaseStored**: Auto-generated for checkbox options

6. **Block Normalization**: Ensures consistent block naming across independently analyzed groups

7. **Schema Generation**: Creates properly formatted TypeScript with all required attributes

## Key Features

- **Pre-Consolidation**: Groups related fields BEFORE AI analysis for better context
- **Duplicate Prevention**: AI tracks and avoids duplicate display names
- **Specific Display Names**: Enforces descriptive names like "Listing Agent License Number" instead of generic "License No."
- **Automatic unique_id Generation**: Creates IDs from field names, not AI-generated
- **Checkbox Special Inputs**: Supports `asRadio` (single-select) and `horizontal` (column layout)
- **Context-Aware Analysis**: AI sees existing display names and blocks
- **Enhanced Screenshots**: 200px vertical padding captures section headers
- **Interactive Mode**: Optional user input for uncertain groupings
- **GUI Mode**: Visual field grouping interface
- **Block Normalization**: Ensures consistent grouping despite independent analysis
- **Error Recovery**: Failed groups don't stop the process

## Troubleshooting

### "No form fields found in the PDF"
- Ensure the PDF has fillable form fields
- Check that fields follow iterative naming pattern

### API Errors
- Check your internet connection
- Reduce `--max-concurrent` if getting rate limit errors (429 status code)
- The script includes automatic retry with exponential backoff for rate limits
- Use `--save-intermediate` to debug which fields are failing
- The script processes fields in batches of 5 with 1-second delays between batches

### Block Inconsistencies
- The system automatically normalizes similar block names
- Manual review may be needed for very different naming patterns

### Large Forms
- For forms with 100+ fields, consider using `--max-concurrent 5`
- Processing time scales with number of field groups (not individual fields)
- Pre-consolidation reduces API calls significantly

### Checkbox Grouping Issues
- Use `--interactive` mode for full control over grouping decisions
- The system detects horizontal, vertical, and mixed checkbox arrangements
- You'll be presented with multiple grouping options when ambiguous
- Save preview screenshots with `--save-preview N` to see what the AI sees
- Check `*_field_groups.json` to understand grouping decisions

When checkboxes could be grouped multiple ways, you'll see:
```
CHECKBOX GROUPING OPTIONS
============================================================
Multiple grouping options detected. Please choose:

Option 0: No grouping (keep all checkboxes separate)

Option 1: Horizontal checkbox group on page 3
Confidence: 0.80
Checkboxes (3):
  - checkbox_45 at (100, 200)
    Label: "Yes"
  - checkbox_46 at (200, 200)
    Label: "No"
  - checkbox_47 at (300, 200)
    Label: "Maybe"

Option 2: Vertical checkbox group on page 3
Confidence: 0.70
Checkboxes (4):
  - checkbox_45 at (100, 200)
  - checkbox_48 at (100, 230)
  - checkbox_49 at (100, 260)
  - checkbox_50 at (100, 290)

Option 3: Checkbox cluster on page 3
Confidence: 0.50
Checkboxes (7):
  [All checkboxes in the area]

Option 4: Create multiple separate groups
(You'll be asked about each potential subgroup)

Option 5: Custom selection
(Select specific checkboxes to group together)

Select option (0-5): _
```

When you choose custom selection (Option 5), you'll see:
```
============================================================
CUSTOM CHECKBOX SELECTION
============================================================
All available checkboxes:

1. checkbox_45 (Page 3)
   Position: (100, 200)
   Label: "Yes"

2. checkbox_46 (Page 3)
   Position: (200, 200)
   Label: "No"

3. checkbox_47 (Page 3)
   Position: (300, 200)
   Label: "Maybe"

4. checkbox_48 (Page 3)
   Position: (100, 230)
   Label: "N/A"

4 checkboxes remaining
Enter checkbox numbers to group together (comma-separated)
Or press Enter to skip remaining checkboxes
Selection: 1,2,3

✓ Created group with 3 checkboxes

1 checkboxes remaining
Enter checkbox numbers to group together (comma-separated)
Or press Enter to skip remaining checkboxes
Selection: [Enter]
```

### GUI Mode Usage:

When using `--gui`, a visual interface launches for complete manual control:

**Workflow:**
1. GUI opens showing your PDF with all fields
2. You create groups manually by selecting fields
3. When you export, the GUI closes
4. AI analysis begins using ONLY your groups
5. Schema is generated based on your grouping

**Main Features:**
1. **PDF Viewer**: Shows the PDF with field rectangles overlaid
   - Green = Selected fields
   - Blue = Already grouped fields  
   - Gray = Unselected fields

2. **Controls Panel**: 
   - Filter by field type (checkboxes, text, other)
   - View selected fields list
   - Create groups with custom types

3. **Navigation**:
   - Use Previous/Next buttons to navigate pages
   - Click directly on fields to select/deselect them
   - Hover over fields to see their details

4. **Creating Groups**:
   1. Click fields to select them (they turn green)
   2. Choose a group type from the dropdown
   3. Click "Create Group from Selected"
   4. Groups appear in the Groups list

5. **Exporting**:
   - Click "Export Groups" when done
   - Creates a `*_gui_groups.json` file
   - GUI closes and AI analysis begins
   - **Note**: Fields not in any group will be analyzed individually

**Requirements:**
- Python tkinter module (`pip install tk`)
- PyMuPDF (`pip install PyMuPDF`)
- Pillow (`pip install Pillow`)

**GUI vs Interactive Mode:**
- **GUI Mode**: Full manual control, no automatic grouping
- **Interactive Mode**: Automatic grouping with user confirmation
- Use GUI when you need precise control over every grouping decision

## Performance Tips

1. **Optimal Concurrency**: 10 concurrent requests works well for most forms
2. **Network Speed**: Faster internet = faster processing
3. **Field Count**: 50 fields typically process in 5-10 seconds
4. **Debugging**: Use `--save-intermediate` only when needed (creates extra files)

## Schema Quality

The generated schemas include:
- Semantic field IDs based on context
- User-friendly display names
- Appropriate validation rules
- Special input types (currency, phone, date, etc.)
- Field relationships (same-value, continuation, linked dates)
- Consistent block organization

## Next Steps

After generating schemas:
1. Review the generated TypeScript for accuracy
2. Move to your application's schema directory
3. Test the schema with your form renderer
4. Make any manual adjustments if needed

## Support

If you encounter issues:
1. Check the console output for specific error messages
2. Use `--save-intermediate` to inspect the process at each stage
3. Verify your PDF has properly named fields using the iterative naming convention
4. Ensure all required Python packages are installed