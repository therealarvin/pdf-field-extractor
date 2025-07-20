# PDF Field Extraction and Renaming Tool

A modular Python solution for extracting form fields from PDF files and automatically renaming them according to best practices for optimal schema generation.

## Features

- **Intelligent Field Extraction**: Extracts all fillable form fields from PDFs with surrounding context
- **Directional Context Analysis**: Captures text from left, right, above, and below each field
- **Automated Renaming**: Applies semantic naming conventions based on field context and position
- **Linked Field Detection**: Identifies and properly names fields that appear across multiple pages
- **Modular Architecture**: Separate scripts for extraction, visualization, and renaming

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Extract fields from your PDF
python3 extract_pdf_fields_enhanced.py "your_document.pdf"

# Automatically rename fields
python3 auto_rename_fields.py "your_document_fields_enhanced.json" "your_document.pdf"
```

This creates:
- `your_document_renamed_[timestamp].pdf` - PDF with properly named fields
- `your_document_fields_enhanced_renamed.json` - Updated field metadata

## Documentation

- [**USAGE_GUIDE.md**](USAGE_GUIDE.md) - Complete usage instructions and examples
- [**FIELD_NAMING_GUIDE.md**](FIELD_NAMING_GUIDE.md) - Best practices for field naming conventions

## Scripts Overview

### extract_pdf_fields_enhanced.py
Extracts all form fields with positional context:
- Uses PyMuPDF for accurate field detection
- Captures surrounding text in all four directions
- Outputs detailed JSON with field metadata

### auto_rename_fields.py
Automatically renames fields based on context:
- Analyzes field names and surrounding text
- Applies semantic naming patterns
- Handles linked fields across pages
- Creates timestamped backups

### visualize_fields.py
Provides insights into extracted fields:
- Categorizes fields by type
- Shows field statistics
- Groups related fields

### rename_pdf_fields.py
Interactive field renaming tool:
- Review each field with context
- Manually specify new names
- Skip or quit options

## Use Cases

- **Form Automation**: Prepare PDFs for automated form filling systems
- **Schema Generation**: Create well-structured schemas from PDF forms
- **Data Collection**: Standardize field names across multiple forms
- **Document Processing**: Improve PDF form accessibility and usability

## Example

Transform unclear field names into semantic, self-documenting names:

**Before:**
```
Client 1
Email Fax
undefined_2
TERM This agreement begins on
```

**After:**
```
client_name_1
client_email
page_number_linked_2
agreement_start_date
```

## Requirements

- Python 3.6+
- PyPDF2 >= 3.0.0
- pdfplumber >= 0.9.0
- PyMuPDF >= 1.23.0

## Contributing

Contributions are welcome! Feel free to:
- Add industry-specific naming patterns
- Improve context detection algorithms
- Add support for more field types
- Enhance the visualization features

## License

MIT License - See LICENSE file for details

## Acknowledgments

Built to solve the common problem of poorly named PDF form fields that make automation difficult.