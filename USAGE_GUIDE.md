# PDF Field Extraction and Renaming Usage Guide

This guide explains how to extract form fields from a PDF and rename them according to best practices using the provided Python scripts.

## Table of Contents
1. [Quick Start](#quick-start)
2. [Prerequisites](#prerequisites)
3. [Step-by-Step Process](#step-by-step-process)
4. [Script Details](#script-details)
5. [Examples](#examples)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Usage](#advanced-usage)

## Quick Start

To rename PDF fields according to the naming guide:

```bash
# Step 1: Extract fields with context
python3 extract_pdf_fields_enhanced.py "your_document.pdf"

# Step 2: Automatically rename fields
python3 auto_rename_fields.py "your_document_fields_enhanced.json" "your_document.pdf"
```

This will create:
- `your_document_renamed_[timestamp].pdf` - PDF with renamed fields
- `your_document_fields_enhanced_renamed.json` - Updated field data

## Prerequisites

### 1. Install Required Libraries

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install PyPDF2 pdfplumber PyMuPDF
```

### 2. Required Files
- Your PDF file with fillable form fields
- `extract_pdf_fields_enhanced.py` - Field extraction script
- `auto_rename_fields.py` - Automated renaming script
- `FIELD_NAMING_GUIDE.md` - Naming conventions reference

## Step-by-Step Process

### Step 1: Extract Fields from PDF

First, extract all form fields and their surrounding context:

```bash
python3 extract_pdf_fields_enhanced.py "Document.pdf"
```

**What this does:**
- Detects all fillable form fields in the PDF
- Captures field positions and metadata
- Extracts surrounding text context (left, right, above, below)
- Saves results to `Document_fields_enhanced.json`

**Optional flags:**
- `-o output.json` - Specify custom output filename
- `-p` - Print results to console

**Example output:**
```json
{
  "field_name": "Client 1",
  "field_type": "Text",
  "current_value": "",
  "page": 0,
  "position": [108.0, 164.52, 576.24, 176.04],
  "context_left": "Client:",
  "context_right": "",
  "context_above": "",
  "context_below": ""
}
```

### Step 2: Review Extracted Fields (Optional)

You can visualize the extracted fields to understand the form structure:

```bash
python3 visualize_fields.py "Document_fields_enhanced.json"
```

This shows:
- Total number of fields
- Field types (Text, Signature, etc.)
- Fields organized by category
- Context snippets for each field

### Step 3: Rename Fields Automatically

Run the automated renaming script:

```bash
python3 auto_rename_fields.py "Document_fields_enhanced.json" "Document.pdf"
```

**What this does:**
- Analyzes each field's context and current name
- Applies naming rules from FIELD_NAMING_GUIDE.md
- Renames fields to semantic, descriptive names
- Creates both renamed PDF and updated JSON

**Example transformations:**
- `Client 1` → `client_name_1`
- `EmailFax` → `client_email`
- `undefined` → `page_number_linked_1`
- `Brokers Signature` → `broker_signature`

**Optional flags:**
- `-o output.pdf` - Specify custom PDF output name
- `-j output.json` - Specify custom JSON output name

### Step 4: Verify Results

Open the renamed PDF to verify:
1. All fields are properly renamed
2. Field functionality is preserved
3. No fields were missed

## Script Details

### extract_pdf_fields_enhanced.py

**Purpose:** Extract form fields with directional context

**Key Features:**
- Uses PyMuPDF for accurate field position detection
- Falls back to PyPDF2 if needed
- Extracts text within proximity thresholds:
  - Left/Right: 80 pixels horizontally
  - Above/Below: 40 pixels vertically
- Handles multi-page PDFs

**Usage:**
```bash
python3 extract_pdf_fields_enhanced.py <pdf_file> [-o output_file] [-p]
```

### auto_rename_fields.py

**Purpose:** Automatically rename fields based on context and naming guide

**Key Features:**
- Intelligent field name detection based on:
  - Current field name patterns
  - Surrounding context text
  - Field position on page
  - Field type (Text, Signature, etc.)
- Handles linked fields across pages
- Preserves already well-named fields
- Creates timestamped backups

**Usage:**
```bash
python3 auto_rename_fields.py <json_file> <pdf_file> [-o output_pdf] [-j output_json]
```

## Examples

### Example 1: Basic Usage

```bash
# Extract fields from a lease agreement
python3 extract_pdf_fields_enhanced.py "lease_agreement.pdf"

# Rename fields automatically
python3 auto_rename_fields.py "lease_agreement_fields_enhanced.json" "lease_agreement.pdf"
```

Output files:
- `lease_agreement_renamed_20250719_140523.pdf`
- `lease_agreement_fields_enhanced_renamed.json`

### Example 2: Custom Output Names

```bash
# Extract with custom output name
python3 extract_pdf_fields_enhanced.py "form.pdf" -o "form_analysis.json"

# Rename with custom output names
python3 auto_rename_fields.py "form_analysis.json" "form.pdf" \
  -o "form_final.pdf" \
  -j "form_final_fields.json"
```

### Example 3: Preview Before Renaming

```bash
# Extract and print to console
python3 extract_pdf_fields_enhanced.py "document.pdf" -p

# Review field categories
python3 visualize_fields.py "document_fields_enhanced.json"

# If satisfied, proceed with renaming
python3 auto_rename_fields.py "document_fields_enhanced.json" "document.pdf"
```

## Troubleshooting

### Common Issues

1. **"No form fields found in the PDF"**
   - Ensure your PDF has fillable form fields (not just text)
   - Try opening in Adobe Acrobat to verify fields exist

2. **ModuleNotFoundError**
   - Install missing dependencies: `pip install -r requirements.txt`
   - Check Python version (requires Python 3.6+)

3. **Permission denied errors**
   - Ensure the PDF is not open in another program
   - Check file permissions

4. **Fields not renamed as expected**
   - Review the context in the JSON file
   - Check if the field already has a good name (script preserves these)
   - Modify `auto_rename_fields.py` to add custom rules

### Debugging

To see what the script is doing:

```bash
# Extract with console output
python3 extract_pdf_fields_enhanced.py "document.pdf" -p > extraction_log.txt

# Check the JSON for context information
cat document_fields_enhanced.json | python -m json.tool | less
```

## Advanced Usage

### Interactive Renaming

For manual control over field names:

```bash
python3 rename_pdf_fields.py "document_fields_enhanced.json" "document.pdf"
```

This allows you to:
- Review each field individually
- Enter custom names
- Skip fields
- Quit and save partial progress

### Batch Processing

Process multiple PDFs:

```bash
#!/bin/bash
for pdf in *.pdf; do
    echo "Processing $pdf..."
    python3 extract_pdf_fields_enhanced.py "$pdf"
    json_file="${pdf%.pdf}_fields_enhanced.json"
    python3 auto_rename_fields.py "$json_file" "$pdf"
done
```

### Custom Naming Rules

Modify `auto_rename_fields.py` to add your own rules:

```python
# Add to determine_new_name() method
elif 'custom_pattern' in current_name.lower():
    return 'my_custom_field_name'
elif context_left == 'Special Label:':
    return 'special_field'
```

### Integration with Other Tools

The JSON output can be used with other tools:

```python
import json

# Load field data
with open('document_fields_enhanced_renamed.json', 'r') as f:
    fields = json.load(f)

# Generate form schema
schema = {
    "fields": [
        {
            "name": field['field_name'],
            "type": field['field_type'],
            "required": True
        }
        for field in fields
    ]
}
```

## Best Practices

1. **Always keep backups** - The scripts create new files by default
2. **Review the JSON** - Check extracted context before renaming
3. **Test with one PDF first** - Ensure the process works for your use case
4. **Follow naming conventions** - Refer to FIELD_NAMING_GUIDE.md
5. **Document custom rules** - If you modify the scripts, document your changes

## Next Steps

After renaming your PDF fields:

1. **Generate schemas** - Use the well-named fields to create form schemas
2. **Build forms** - Create web forms that map to PDF fields
3. **Automate filling** - Use the field names to programmatically fill PDFs
4. **Validate data** - Implement validation based on field naming patterns

## Support

If you encounter issues:

1. Check the field extraction worked: `cat *_fields_enhanced.json`
2. Verify PDF has fillable fields: Open in Adobe Acrobat
3. Review error messages carefully
4. Ensure all dependencies are installed
5. Try with a simpler PDF first

Remember: Good field names lead to better automation!