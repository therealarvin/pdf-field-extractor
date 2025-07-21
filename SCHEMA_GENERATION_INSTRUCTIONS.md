# Schema Generation Instructions

This document provides step-by-step instructions for AI agents to generate TypeScript schemas from renamed PDF forms in the `renamed-and-reviewed-forms` folder.

## Overview

The schema generation process converts a renamed PDF form into a TypeScript file containing an array of `SchemaItem` objects that define the form's structure, relationships, validation, and display properties.

## Prerequisites

Before starting, ensure:
1. The PDF is in the `renamed-and-reviewed-forms` folder
2. The PDF has already been through the field mapping process (fields have semantic names)
3. Python scripts are available in the working directory

## Step-by-Step Process

### Step 1: Extract Field Information

Extract all field information from the renamed PDF:

```bash
python3 extract_pdf_fields_enhanced.py renamed-and-reviewed-forms/<pdf_filename>
```

This creates a JSON file with field details, types, positions, and contextual information.

### Step 2: Analyze Field Relationships

Examine the extracted fields to identify:

#### Same-Value Linked Fields
Look for fields that should contain identical values:
- **Pattern**: Fields with similar base names but different suffixes (e.g., `buyer_name_page1`, `buyer_name_page2`)
- **Pattern**: Fields ending in `_linked_<number>` or `_p<number>`
- **Common examples**: Names, addresses, phone numbers appearing on multiple pages

#### Continuation Fields (Text Flow)
Identify fields where text should flow from one to the next:
- **Pattern**: Fields with sequential suffixes like `_line1`, `_line2`, `_line3`
- **Pattern**: Fields with `_cont`, `_continued`, or similar suffixes
- **Common examples**: Long addresses, descriptions, explanatory text

#### Linked Date Fields
Find date fields that should auto-populate when signatures are captured:
- **Pattern**: Date fields near signature fields (within 100px vertically or horizontally)
- **Pattern**: Fields containing both "signature" and "date" in their names
- **Common examples**: `buyer_signature` → `buyer_date`, `seller_signature` → `seller_date`

### Step 3: Determine Form Type

Extract the form type from the PDF filename:
1. Take the filename without extension
2. Remove common prefixes/suffixes (like "form_", "_template", "_v1", etc.)
3. Convert to lowercase
4. Replace spaces and special characters with underscores
5. Remove multiple consecutive underscores

**Examples**:
- `Texas Realtors Residential Lease.pdf` → `texas_realtors_residential_lease`
- `Exclusive Right to Sell (Commercial).pdf` → `exclusive_right_to_sell_commercial`

### Step 4: Create Logical Field Groupings

Group fields into logical blocks based on semantic meaning:

#### Common Block Patterns:
- **Property Information**: Fields containing `property_`, `address_`, `building_`, `unit_`, `square_feet`, `lot_size`
- **Buyer Information**: Fields containing `buyer_`, `purchaser_`, `client_`
- **Seller Information**: Fields containing `seller_`, `vendor_`, `owner_`
- **Financial Details**: Fields containing `price_`, `amount_`, `deposit_`, `fee_`, `commission_`, `rent_`
- **Agent/Broker Information**: Fields containing `agent_`, `broker_`, `realtor_`, `license_`
- **Dates and Deadlines**: Fields containing `date_`, `deadline_`, `expiration_`
- **Terms and Conditions**: Fields containing `terms_`, `condition_`, `clause_`
- **Signatures**: Fields containing `signature_`, `initial_`, `sign_`

#### Block Styling Guidelines:
- **Property Information**: `color_theme: 'blue'`, icon: 'home'
- **Buyer/Seller Information**: `color_theme: 'green'`, icon: 'user'
- **Financial Details**: `color_theme: 'orange'`, icon: 'dollar-sign'
- **Agent/Broker Information**: `color_theme: 'purple'`, icon: 'briefcase'
- **Signatures**: `color_theme: 'gray'`, icon: 'pen-tool'

### Step 5: Assign Input Types

Determine the appropriate input type for each field:

- **text**: Default for most fields
- **text-area**: Fields with names containing `description`, `notes`, `comments`, `explanation`, or fields wider than 8 grid units
- **signature**: Fields containing `signature`, `sign`, `initial`
- **radio**: Fields identified as radio buttons in PDF with multiple options
- **checkbox**: Fields identified as checkboxes in PDF
- **fileUpload**: Manually added fields for document attachments (not from PDF)
- **info**: Manually added fields for instructions or headers (not from PDF)

### Step 6: Generate Display Names

Transform field names into user-friendly labels:

1. Remove technical prefixes: `txt_`, `lbl_`, `fld_`, `field_`
2. Remove technical suffixes: `_txt`, `_text`, `_field`, `_fld`
3. Replace underscores with spaces
4. Handle camelCase by adding spaces before capitals
5. Capitalize each word
6. Clean up common abbreviations:
   - `addr` → `Address`
   - `num` → `Number`
   - `qty` → `Quantity`
   - `amt` → `Amount`

### Step 7: Apply Validation Rules

#### Automatic Validation Patterns:

**Phone Numbers** (fields containing `phone`, `tel`, `mobile`):
```typescript
validation: {
  loopback: [{
    regex: "^[-()\\s\\d]{10,}$",
    message: "Must be a valid phone number"
  }]
}
```

**Email Addresses** (fields containing `email`):
```typescript
validation: {
  loopback: [{
    regex: "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$",
    message: "Must be a valid email address"
  }]
}
```

**Monetary Amounts** (fields containing `price`, `amount`, `fee`, `deposit`, `rent`, `commission`):
```typescript
validation: {
  loopback: [{
    regex: "^[\\d.,$]+$",
    message: "Must be a valid monetary amount"
  }]
}
```

**Percentages** (fields containing `percent`, `rate`, `%`):
```typescript
validation: {
  loopback: [{
    regex: "^[\\d.]+%?$",
    message: "Must be a valid percentage"
  }]
}
```

**Dates** (fields containing `date` but not partial dates):
```typescript
validation: {
  loopback: [{
    regex: "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
    message: "Must be a valid date (MM/DD/YYYY)"
  }]
}
```

#### Cross-Field Validation Logic:
- End dates should be after start dates
- Down payments should not exceed total amounts
- Percentages should not exceed 100%

### Step 8: Determine Field Widths

Assign widths based on field type and content:

- **Full width (12)**: Text areas, long descriptions, signature blocks
- **Three-quarters (8-9)**: Street addresses, company names, long text fields
- **Half width (6)**: Names, email addresses, standard signatures
- **Third width (4)**: Dates, phone numbers, ZIP codes, amounts
- **Quarter width (3)**: State abbreviations, checkboxes, radio buttons, short IDs

### Step 9: Set Placeholders

Generate helpful placeholders based on field names:

**Contact Information**:
- Phone fields → `"(555) 123-4567"`
- Email fields → `"example@email.com"`
- Work email → `"john.doe@company.com"`

**Names & Addresses**:
- First name → `"John"`
- Last name → `"Doe"`
- Street → `"123 Main Street"`
- City → `"Anytown"`
- State → `"CA"`
- ZIP → `"12345"`

**Financial**:
- Price/Amount → `"$0.00"`
- Rent → `"$2,500.00"`
- Percentage → `"3.5%"`

**Real Estate Specific**:
- MLS → `"MLS123456"`
- License → `"RE123456"`
- Square feet → `"2,500"`

### Step 10: Mark Cached Fields

Automatically set `isCached: true` for fields containing:
- `realtor_`, `agent_`, `broker_`
- `license`, `firm_name`, `company_name`
- Any professional contact information that should persist across forms

### Step 11: Handle Linked Fields and Radio Buttons

#### Linked Fields - Do NOT Create Separate Schema Items

Fields that are linked to other fields should NOT have their own individual schema items. Instead, they should be included in the `pdf_attributes` of the main field:

**Same-Value Links**: Fields that share the same value across multiple pages
- Example: `buyer_name_page1` and `buyer_name_page2` → Create ONE schema item for `buyer_name` with both fields in `pdf_attributes`

**Continuation Fields**: Fields where text flows from one to the next
- Example: `property_address` and `property_address_continued` → Create ONE schema item for `property_address` with continuation field in `linked_form_fields_text`

**Linked Dates**: Date fields that auto-populate when signatures are captured
- Example: `tenant_signature` and `tenant_signature_date` → Create ONE schema item for `tenant_signature` with date field in `linked_dates`

**Radio Button Options**: Individual radio button values within a group
- Example: `monthly_rent_value` group with `rent_price_changes` and `rent_price_remains_the_same` options → Create ONE schema item for `monthly_rent_value` with options in `linked_form_fields_radio`

#### Radio Button Handling

When the extraction reveals radio buttons with `radio_options`, create a single schema item with:

```typescript
{
  unique_id: "monthly_rent_value",
  pdf_attributes: [{
    formType: "residential_lease_extension",
    formfield: "monthly_rent_value",
    linked_form_fields_radio: [
      { radioField: "rent_price_changes", displayName: "Rent Price Changes" },
      { radioField: "rent_price_remains_the_same", displayName: "Rent Price Remains the Same" }
    ]
  }],
  display_attributes: {
    input_type: "radio",
    // ... other attributes
  }
}
```

#### Field Count Verification

After processing all relationships:
- Count the extracted fields from the JSON
- Subtract fields that are linked/continuation/radio options
- Your final schema should have fewer items than the original field count
- Document which fields were consolidated and why

### Step 12: Generate TypeScript Schema

Create a TypeScript file with the following structure:

```typescript
import { SchemaItem } from "../../../../types/realtor";

export const [formTypeInCamelCase]Schema: SchemaItem[] = [
  // ... schema items
];
```

#### Required Fields for Each SchemaItem:

```typescript
{
  unique_id: string, // Use original field name or create semantic ID
  
  pdf_attributes: [{
    formType: string, // Extracted from filename
    formfield: string, // Original PDF field name
    linked_form_fields_text?: string[], // Continuation fields
    linked_form_fields_radio?: { radioField: string; displayName: string }[],
    linked_dates?: { dateFieldName: string }[]
  }],
  
  display_attributes: {
    display_name: string, // User-friendly label
    input_type: "text" | "radio" | "checkbox" | "signature" | "fileUpload" | "info" | "text-area",
    description?: string, // Optional help text
    order: number, // Sequential starting from 1
    attribute?: string, // Simple semantic tag if applicable
    block?: string, // Group name
    block_style?: {
      title?: string,
      description?: string,
      icon?: string,
      color_theme?: 'blue' | 'green' | 'purple' | 'orange' | 'gray'
    },
    validation?: {
      loopback?: { regex: string, message: string }[],
      crossField?: { rule: string, unique_id: string, message?: string }[]
    },
    placeholder?: string,
    width?: number, // 1-12 grid system
    value: {
      type: "manual" // Always use "manual", do NOT include output field
    },
    isCached?: boolean, // true for realtor/broker info
    isRequired?: boolean, // Determine based on field importance
    breakBefore?: boolean // Use for visual separation
  }
}
```

### Step 13: Quality Assurance

Before finalizing the schema:

1. **Verify relationships**: Ensure linked fields make logical sense
2. **Check display names**: Confirm they're user-friendly and clear
3. **Validate widths**: Ensure layout will be visually appealing
4. **Review blocks**: Confirm logical grouping and appropriate styling
5. **Test validation**: Ensure rules aren't too restrictive
6. **Confirm order**: Fields should follow a logical sequence

## Step 14: Deploy Schema to Application

After generating the schema file, move it to the application's schema directory:

```bash
mv [formType]_schema.ts /Users/arvin/WebDev/onroad_full/onroad_express/src/logic/realtor/centralIntelligence/schemas/
```

This ensures the schema is properly integrated into the application structure.

## File Naming Convention

Save the generated schema as:
`[formType]_schema.ts`

Example: `texas_realtors_residential_lease_schema.ts`

## Common Pitfalls to Avoid

1. **Over-linking fields**: Not every similar field name should be linked
2. **Excessive validation**: Don't make rules so strict they prevent valid input
3. **Poor grouping**: Avoid mixing unrelated fields in the same block
4. **Inappropriate widths**: Consider content length and visual balance
5. **Missing relationships**: Look carefully for continuation and linked fields
6. **Inconsistent naming**: Maintain consistent patterns in unique_id values

## Testing the Generated Schema

After generation, verify:
1. All PDF fields are represented
2. Relationships work as expected
3. Validation rules accept valid input
4. Display names are clear and professional
5. Block grouping creates logical sections
6. Field widths create a balanced layout

## Example Workflow Commands

```bash
# Extract fields from a renamed PDF
python3 extract_pdf_fields_enhanced.py renamed-and-reviewed-forms/residential_lease_form.pdf

# Analyze the resulting JSON and generate schema
# (This is the manual analysis and TypeScript generation step)

# The output should be: residential_lease_form_schema.ts
```

Remember: The goal is to create a schema that provides an excellent user experience while maintaining all necessary PDF field mappings and relationships.