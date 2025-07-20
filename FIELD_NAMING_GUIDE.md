# PDF Field Naming Guide for Optimal Schema Generation

This guide outlines the ideal naming conventions for PDF form fields to ensure the best performance with the schema generator. Following these conventions will result in more accurate schema generation and better data extraction.

## Table of Contents
1. [General Naming Principles](#general-naming-principles)
2. [Field Type Conventions](#field-type-conventions)
3. [Common Field Names](#common-field-names)
4. [Grouping and Relationships](#grouping-and-relationships)
5. [Best Practices](#best-practices)
6. [Examples](#examples)

## General Naming Principles

### 1. Use Descriptive, Semantic Names
- **Good**: `first_name`, `email_address`, `property_street`
- **Bad**: `field1`, `text_123`, `undefined`

### 2. Use Consistent Separators
- Prefer underscores (`_`) for word separation
- Alternative: camelCase (`firstName`)
- **Avoid**: spaces, hyphens, or mixed conventions

### 3. Include Type Suffixes When Helpful
- `_date` for date fields: `start_date`, `birth_date`
- `_amount` for currency: `rent_amount`, `deposit_amount`
- `_number` for numeric fields: `phone_number`, `account_number`

### 4. Be Specific Rather Than Generic
- **Good**: `tenant_first_name` vs just `name`
- **Good**: `property_zip_code` vs just `zip`

## Field Type Conventions

### Text Fields
```
Pattern: {entity}_{attribute}
Examples:
- tenant_first_name
- tenant_last_name
- property_address
- broker_email
```

### Checkboxes
```
Pattern: {condition}_checkbox or is_{condition}
Examples:
- pets_allowed_checkbox
- is_furnished
- has_parking
- utilities_included_checkbox
```

### Radio Buttons
```
Pattern: {choice_group}_option
Examples:
- payment_method_option
- lease_term_option
- property_type_option
```

### Dropdowns/Select
```
Pattern: {category}_select or {category}_dropdown
Examples:
- state_select
- country_dropdown
- property_type_select
```

### Date Fields
```
Pattern: {event}_date
Examples:
- lease_start_date
- lease_end_date
- inspection_date
- payment_due_date
```

### Signature Fields
```
Pattern: {signer}_signature
Examples:
- tenant_signature
- landlord_signature
- witness_signature
- broker_signature
```

## Common Field Names

### Personal Information
```
first_name
last_name
middle_name
full_name
date_of_birth / birth_date
ssn / social_security_number
driver_license_number
```

### Contact Information
```
email / email_address
phone / phone_number
mobile_number
work_phone
fax_number
```

### Address Fields
```
street_address / address_line_1
address_line_2
city
state / state_province
zip_code / postal_code
country
```

### Real Estate Specific
```
# Property Information
property_address
property_type
bedrooms_count
bathrooms_count
square_footage
year_built
mls_number
parcel_number

# Lease Terms
monthly_rent
security_deposit
lease_start_date
lease_end_date
lease_term_months
pet_deposit
utilities_included

# Parties
tenant_name / tenant_full_name
landlord_name / owner_name
property_manager_name
broker_name
broker_license_number
```

### Financial Fields
```
amount
total_amount
subtotal
tax_amount
discount_amount
payment_amount
balance_due
account_number
routing_number
```

## Grouping and Relationships

### 1. Numbered Groups
When you have multiple similar entities, use consistent numbering:
```
tenant_1_first_name
tenant_1_last_name
tenant_1_email

tenant_2_first_name
tenant_2_last_name
tenant_2_email
```

### 2. Nested Relationships
Use prefixes to show relationships:
```
property_address_street
property_address_city
property_address_state
property_address_zip

billing_address_street
billing_address_city
billing_address_state
billing_address_zip
```

### 3. Section Prefixes
Group related fields with section prefixes:
```
contact_phone
contact_email
contact_address

emergency_contact_name
emergency_contact_phone
emergency_contact_relationship
```

### 4. Same-Value Linked Fields
When multiple fields should contain the same value (e.g., repeated signatures, dates, names, or addresses across pages):

#### Pattern: `{base_name}_linked_{n}` or `{base_name}_page_{n}`
```
# Same person signing in multiple places
tenant_name_linked_1
tenant_name_linked_2
tenant_name_linked_3

# Same date appearing multiple times
agreement_date_linked_1
agreement_date_linked_2

# Alternative: page-based naming
tenant_signature_page_1
tenant_signature_page_3
tenant_signature_page_5
```

#### Best Practices for Same-Value Fields:
- Use `_linked_` suffix to indicate fields that should have identical values
- Include sequential numbers to maintain uniqueness
- Consider using page numbers if fields appear on specific pages
- Group all linked fields with the same base name

### 5. Continuation Linked Fields
When a single piece of content spans multiple fields (e.g., long text that continues across fields):

#### Pattern: `{base_name}_cont_{n}` or `{base_name}_part_{n}`
```
# Long description split across fields
property_description_part_1
property_description_part_2
property_description_part_3

# Terms and conditions spanning multiple fields
lease_terms_cont_1
lease_terms_cont_2
lease_terms_cont_3
lease_terms_cont_4

# Additional notes with continuation
additional_notes_cont_1
additional_notes_cont_2
```

#### Best Practices for Continuation Fields:
- Use `_cont_` or `_part_` suffix to indicate continuation
- Number sequentially starting from 1
- Keep the base name identical for all parts
- Consider adding a total count if known: `description_part_1_of_3`

### 6. Radio Button Groups (Linked Options)
For radio buttons that work together as a group:

#### Pattern: `{choice_name}_option_{value}` or `{choice_name}_radio_{value}`
```
# Payment method selection
payment_method_radio_cash
payment_method_radio_check
payment_method_radio_ach

# Lease term selection
lease_term_option_6months
lease_term_option_12months
lease_term_option_24months

# Property type selection
property_type_radio_single_family
property_type_radio_condo
property_type_radio_apartment
```

### 7. Checkbox Groups (Multiple Selection)
For checkboxes that represent related options:

#### Pattern: `{feature_set}_{specific_feature}_checkbox`
```
# Included utilities
utilities_water_checkbox
utilities_gas_checkbox
utilities_electric_checkbox
utilities_trash_checkbox

# Amenities
amenities_parking_checkbox
amenities_storage_checkbox
amenities_gym_checkbox
amenities_pool_checkbox
```

## Best Practices

### 1. Avoid These Common Mistakes
- ❌ Generic names: `field1`, `text`, `input`
- ❌ Special characters: `name@field`, `field#1`
- ❌ Inconsistent casing: mixing `firstName` and `last_name`
- ❌ Overly abbreviated: `fn` instead of `first_name`
- ❌ Spaces in names: `first name` (use `first_name`)

### 2. Make Fields Self-Documenting
The field name should clearly indicate:
- What data it contains
- Who/what it relates to
- The expected format (when relevant)

### 3. Consider the Schema Generator
The schema generator performs better when:
- Field names clearly indicate data type
- Related fields share common prefixes
- Naming is consistent throughout the form

### 4. Plan for Validation
Include hints in field names that help with validation:
- `email` or `email_address` → email validation
- `phone_number` → phone format validation
- `zip_code` → postal code validation
- `_date` suffix → date picker/validation

## Examples

### Good PDF Field Naming Example
```
# Tenant Information Section
tenant_first_name
tenant_last_name
tenant_email
tenant_phone_number
tenant_current_address

# Property Details Section
property_street_address
property_city
property_state
property_zip_code
property_type_select
bedrooms_count
bathrooms_count
monthly_rent_amount

# Lease Terms Section
lease_start_date
lease_end_date
security_deposit_amount
pet_allowed_checkbox
utilities_included_checkbox

# Same-Value Linked Fields (appears on multiple pages)
tenant_name_linked_1          # Page 1
tenant_name_linked_2          # Page 3
tenant_name_linked_3          # Page 5

agreement_date_linked_1       # Page 1
agreement_date_linked_2       # Page 5

# Continuation Fields
property_description_part_1   # First text box
property_description_part_2   # Continuation box
property_description_part_3   # Final continuation

special_terms_cont_1          # Additional terms section
special_terms_cont_2
special_terms_cont_3

# Radio Button Groups
lease_duration_radio_6months
lease_duration_radio_12months
lease_duration_radio_24months
lease_duration_radio_other

# Checkbox Groups
included_appliances_refrigerator_checkbox
included_appliances_stove_checkbox
included_appliances_dishwasher_checkbox
included_appliances_washer_checkbox
included_appliances_dryer_checkbox

# Signatures Section
tenant_signature
tenant_signature_date
landlord_signature
landlord_signature_date
```

### How This Helps Schema Generation

1. **Clear Data Types**: The generator can infer that `_date` fields need date validation, `_email` needs email validation, etc.

2. **Logical Grouping**: Fields with common prefixes (`tenant_`, `property_`) are automatically grouped in the schema.

3. **Relationship Detection**: The generator can identify that `tenant_signature` and `tenant_signature_date` are related.

4. **Validation Rules**: Suffixes like `_amount`, `_number`, `_date` help the generator apply appropriate validation rules.

5. **UI Generation**: Clear field names help generate better labels and placeholder text in the UI.

6. **Same-Value Field Linking**: The `_linked_` pattern allows the schema generator to:
   - Automatically synchronize values across linked fields
   - Create a single input that populates multiple PDF fields
   - Reduce redundant data entry
   - Ensure consistency across the document

7. **Continuation Field Handling**: The `_cont_` or `_part_` pattern enables:
   - Automatic text overflow from one field to the next
   - Single textarea input that spans multiple PDF fields
   - Proper character limit handling across continued fields
   - Seamless reading experience when displaying data

8. **Radio Group Recognition**: Consistent radio button naming helps:
   - Automatic grouping into single selection controls
   - Proper mutual exclusivity enforcement
   - Clear option labeling in the UI

9. **Checkbox Set Management**: Grouped checkbox naming enables:
   - Logical grouping in the UI
   - Multi-select handling
   - Related validation rules (e.g., "select at least one")

## Testing Your Field Names

Before finalizing your PDF, test your field names:

1. **Clarity Test**: Can someone unfamiliar with your form understand what each field is for?
2. **Consistency Test**: Do all similar fields follow the same naming pattern?
3. **Grouping Test**: Are related fields named in a way that shows their relationship?
4. **Type Test**: Do field names indicate their expected data type?

## Migration Guide

If you have existing PDFs with poor field names:

1. Use the PDF Field Renamer tool to automatically rename fields based on surrounding text
2. Review and adjust the suggested names to match these conventions
3. Test the renamed PDF with the schema generator
4. Iterate until you achieve optimal results

Remember: Well-named fields lead to better schemas, which lead to better data collection and validation!