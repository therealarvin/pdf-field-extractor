#!/usr/bin/env python3
import json
from extract_pdf_fields_enhanced import EnhancedPDFFieldExtractor

# Extract fields - using the actual UTF-8 character
extractor = EnhancedPDFFieldExtractor("renamed-forms/buyer's_temporary_residential_lease_Fillable.pdf")
fields = extractor.extract_all_fields_with_enhanced_context()

# Save results
output_file = "buyers_temporary_residential_lease_Fillable_fields_enhanced.json"
with open(output_file, 'w') as f:
    json.dump(fields, f, indent=2)

print(f"Extracted {len(fields)} fields")
print(f"Results saved to: {output_file}")