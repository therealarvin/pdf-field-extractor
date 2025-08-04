# Schema Generation Instructions

This document provides step-by-step instructions for AI agents to generate TypeScript schemas from PDF forms with iterative field names (e.g., form_name_textfield_1, form_name_checkbox_1), using context analysis to determine field purposes and create meaningful schema items.

## Overview

The schema generation process converts a PDF form with programmatically generated iterative field names into a TypeScript file containing an array of `SchemaItem` objects. Since field names have no semantic meaning (they're just numbered sequences like form_name_textfield_1, form_name_textfield_2, etc.), the process relies entirely on analyzing the text context around each field (left, right, above, below) to determine its purpose and create appropriate schema items with meaningful unique_ids and display properties.

## Prerequisites

Before starting, ensure:
1. The PDF has iterative field names (e.g., `form_name_textfield_1`, `form_name_checkbox_1`)
2. Python scripts are available in the working directory, especially `extract_pdf_fields_enhanced.py`
3. You understand that field purposes will be determined from context, not field names

## Step-by-Step Process

### Step 1: Extract Field Information with Context

Extract all field information with directional context from the PDF:

```bash
python3 extract_pdf_fields_enhanced.py <pdf_filename>
```

This creates a JSON file with:
- Field names (iterative format: `form_name_textfield_1`, etc.)
- Field types (Text, RadioButton, CheckBox, etc.)
- Position coordinates
- **Directional context** (text found left, right, above, below each field)

The context information is crucial for determining field purposes since field names are generic.

### Step 2: Analyze Context to Determine Field Purpose

For each field in the extracted JSON, analyze the directional context to determine its semantic purpose. **CRITICAL: Since all field names are iterative (form_name_textfield_1, etc.), you MUST rely entirely on the context fields to understand what each field represents.**

#### Context Analysis Guidelines:

**Names and Contact Information**:
- Context containing "name", "full name", "first", "last" → Name field
- Context with "buyer", "seller", "tenant", "landlord", "agent" + "name" → Party-specific name
- Context with "phone", "tel", "mobile" → Phone number field
- Context with "email", "@" → Email field

**Address and Property**:
- Context with "address", "street", "property" → Address field
- Context with "city", "state", "zip", "postal" → Address components
- Context with "sq", "square", "feet", "ft" → Square footage
- Context with "lot", "size", "acreage" → Lot size

**Financial Fields**:
- Context with "$", "price", "amount", "fee" → Monetary field
- Context with "rent", "monthly", "deposit" → Rental amounts
- Context with "%", "percent", "rate", "commission" → Percentage field

**Dates and Signatures**:
- Context with "date", "expires", "effective" → Date field
- Context with "signature", "sign", "initial" → Signature field
- Adjacent date and signature fields → Linked signature/date pair

**Legal and Terms**:
- Context with "terms", "conditions", "clause" → Terms field
- Context with "description", "notes", "additional" → Text area field

#### Creating Semantic unique_id:
Based on the context analysis, create a descriptive unique_id that reflects the field's purpose. **Remember: The iterative field names tell you nothing about the field's purpose - you must derive meaning entirely from the context:**
- `form_name_textfield_1` with context "Buyer Name" → `buyer_name`
- `form_name_textfield_2` with context "Property Address" → `property_address`
- `form_name_checkbox_1` with context "Conventional Financing" → `financing_conventional`
- `form_name_textfield_15` with context "Monthly Rent Amount" → `monthly_rent`
- `form_name_checkbox_7` with context "Property includes pool" → `property_has_pool`

### Step 3: Analyze Field Relationships

Examine the extracted fields to identify:

#### Same-Value Linked Fields
Look for fields that should contain identical values across pages:
- **Identification**: Fields with identical or very similar context on different pages
- **Example**: Two fields with context "Buyer Name" on page 1 and page 5
- **Position check**: Often vertically aligned or in similar page locations
- **Common examples**: Party names, property addresses, key terms appearing multiple times

#### Continuation Fields (Text Flow)
Identify fields where text should flow from one to the next:
- **Identification**: Adjacent fields with context indicating continuation
- **Context clues**: "continued", "line 2", sequential numbering in context
- **Position check**: Usually horizontally or vertically adjacent
- **Common examples**: Multi-line addresses, long descriptions, terms text

#### Linked Date Fields
Find date fields that should auto-populate when signatures are captured:
- **Identification**: Date field positioned near (within 100px) a signature field
- **Context clues**: "date" context near "signature" or "initial" context
- **Common pattern**: Signature field followed by date field horizontally or below

#### Signature and Initial Grouping
**CRITICAL: Group signatures and initials by PARTY based on context:**
- **Identification**: Look for signature/initial fields with similar party context
- **Context matching**: "Buyer 1 Signature" + "Buyer 1 Initial" → Same party
- **Position check**: Party signatures/initials often appear together in signature blocks
- **WRONG**: Grouping signatures/initials with different party contexts

**Grouping Rules:**
1. **Context-based grouping**: Match party names in context (Buyer 1, Seller 2, etc.)
2. **Create semantic unique_id**: Based on party context (e.g., `buyer_1_initials_signature`)
3. **Display Name**: Use "Party X Initials & Signature" format
4. **Input Type**: Always "signature" for grouped signature+initial fields

### Step 4: Determine Form Type

Extract the form type from the PDF filename:
1. Take the filename without extension
2. Remove common prefixes/suffixes (like "form_", "_template", "_v1", etc.)
3. Convert to lowercase
4. Replace spaces and special characters with underscores
5. Remove multiple consecutive underscores

**Examples**:
- `Texas Realtors Residential Lease.pdf` → `texas_realtors_residential_lease`
- `Exclusive Right to Sell (Commercial).pdf` → `exclusive_right_to_sell_commercial`

### Step 5: Create Logical Field Groupings

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

### Step 6: Assign Input Types

**CRITICAL: Always respect the PDF field type from the extracted JSON.** Determine the appropriate input type for each field:

- **text**: Default for most fields with `"field_type": "Text"`
- **text-area**: Fields with names containing `description`, `notes`, `comments`, `explanation`, or fields wider than 8 grid units
- **signature**: Fields containing `signature`, `sign`, `initial` (note: initials are signature types)
- **checkbox**: Fields with `"field_type": "CheckBox"` in the JSON extraction - DO NOT convert to radio
- **radio**: Fields with `"field_type": "RadioButton"` in the JSON extraction that share the same group name
- **fileUpload**: Manually added fields for document attachments (not from PDF)
- **info**: Manually added fields for instructions or headers (not from PDF)

**Input Type Rules:**
1. **CheckBox → checkbox**: Individual checkboxes allow multiple selections (e.g., financing types)
2. **RadioButton → radio**: Radio groups allow single selection within a group
3. **NEVER convert CheckBox to radio** - this breaks intended functionality
4. **NEVER group individual checkboxes** into radio button groups

### Step 7: Generate Display Names

Generate user-friendly display names based on the context analysis from Step 2:

1. **Use ONLY the analyzed context** to create meaningful display names - the iterative field names provide no useful information
2. **NEVER use the iterative field name** in display names (e.g., NEVER show "Form Name Textfield 1" or "Textfield 1")
3. **Format the context** into proper display names:
   - Remove redundant words
   - Capitalize appropriately
   - Use standard terminology
   - Make it clear to users what information they should enter

**Examples**:
- Context: "Buyer Name" → Display: "Buyer Name"
- Context: "Property street address" → Display: "Property Address"
- Context: "Monthly rent amount $" → Display: "Monthly Rent"
- Context: "Tenant signature" → Display: "Tenant Signature"
- Context: "Initial here" with party context → Display: "Buyer 1 Initial"

### Step 8: Apply Validation Rules and Special Input Types

#### Automatic Validation Patterns:

**Phone Numbers** (fields containing `phone`, `tel`, `mobile`):
```typescript
validation: {
  loopback: [{
    regex: "^[-()\\s\\d]{10,}$",
    message: "Must be a valid phone number"
  }]
},
special_input: {
  text: { phone: true }
}
```

**Email Addresses** (fields containing `email`):
```typescript
validation: {
  loopback: [{
    regex: "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$",
    message: "Must be a valid email address"
  }]
},
special_input: {
  text: { email: true }
}
```

**Monetary Amounts** (fields containing `price`, `amount`, `fee`, `deposit`, `rent`, `commission`):
```typescript
validation: {
  loopback: [{
    regex: "^[\\d.,$]+$",
    message: "Must be a valid monetary amount"
  }]
},
special_input: {
  text: { currency: true }
}
```

**Percentages** (fields containing `percent`, `rate`, `%`):
```typescript
validation: {
  loopback: [{
    regex: "^[\\d.]+%?$",
    message: "Must be a valid percentage"
  }]
},
special_input: {
  text: { percentage: true }
}
```

**Dates** (fields containing `date` but not partial dates):
```typescript
validation: {
  loopback: [{
    regex: "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
    message: "Must be a valid date (MM/DD/YYYY)"
  }]
},
special_input: {
  text: { date: true }
}
```

#### Special Input Options

The `special_input` field modifies how inputs appear and behave in the form editor:

**Text Input Modifiers**:
- `percentage: true` - Adds percentage formatting
- `phone: true` - Adds phone number formatting
- `date: true` - Adds date picker/formatting
- `currency: true` - **Required for all monetary fields** (adds currency formatting)
- `number: true` - Restricts to numeric input only
- `email: true` - Adds email validation
- `url: true` - Adds URL validation

**Checkbox Modifiers**:
- `asRadio: true` - Makes checkboxes behave like radio buttons (single selection)
- `horizontal: number` - Number of columns for checkbox layout

**Info Display Styles**:
- `style: 'default' | 'subtle' | 'minimal' | 'inline' | 'compact' | 'warning' | 'success' | 'error' | 'tip'`
- `icon: true` - Shows an icon with the info
- `minimizable: true` - Allows user to collapse/expand the info block

**Radio Layout Options**:
- `layout: 'vertical' | 'horizontal' | 'grid'`
- `columns: number` - For grid layout only

**Signature Options**:
- `dateFormat: string` - Custom date format for signature timestamps
- `showInitials: true` - Shows an initials field alongside signature

**File Upload Options**:
- `accept: ".pdf,.doc,.docx"` - Restricts file types
- `maxSize: number` - Maximum file size in MB
- `multiple: true` - Allows multiple file uploads

**Text Area Options**:
- `minRows: number` - Minimum visible rows
- `maxRows: number` - Maximum rows before scrolling
- `autoResize: true` - Auto-resizes based on content

#### Cross-Field Validation Logic:
- End dates should be after start dates
- Down payments should not exceed total amounts
- Percentages should not exceed 100%

### Step 9: Determine Field Widths

Assign widths based on field type and content:

- **Full width (12)**: Text areas, long descriptions, signature blocks
- **Three-quarters (8-9)**: Street addresses, company names, long text fields
- **Half width (6)**: Names, email addresses, standard signatures
- **Third width (4)**: Dates, phone numbers, ZIP codes, amounts
- **Quarter width (3)**: State abbreviations, checkboxes, radio buttons, short IDs

### Step 10: Set Placeholders

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

### Step 11: Mark Cached Fields and Add Visibility Conditions

#### Cached Fields
Automatically set `isCached: true` for fields containing:
- `realtor_`, `agent_`, `broker_`
- `license`, `firm_name`, `company_name`
- Any professional contact information that should persist across forms

#### Visibility Conditions
Use `visibleIf` to show/hide fields based on other field values:

**For Checkbox-Linked Fields**:
```typescript
visibleIf: [{
  unique_id: "financing_options",
  operation: "contains",
  valueChecked: "FHA"  // Use the databaseStored value
}]
```

**For Radio Button Dependencies**:
```typescript
visibleIf: [{
  unique_id: "property_type",
  operation: "==",
  valueChecked: "Commercial"  // Use the display option name
}]
```

**For Numeric Comparisons**:
```typescript
visibleIf: [{
  unique_id: "purchase_price",
  operation: ">",
  valueChecked: "500000"
}]
```

**Multiple Conditions** (all must be true):
```typescript
visibleIf: [
  {
    unique_id: "property_type",
    operation: "==",
    valueChecked: "Residential"
  },
  {
    unique_id: "financing_type",
    operation: "contains",
    valueChecked: "CONVENTIONAL"
  }
]
```

**Available Operations**:
- `">"`, `">="`, `"<"`, `"<="` - Numeric comparisons
- `"=="`, `"!=="` - Exact match/not match
- `"contains"`, `"doesNotContain"` - For checkbox arrays

### Step 12: Handle Linked Fields and Radio Buttons

#### Linked Fields - Understanding Which Fields Get Separate Schema Items

**Fields that DO NOT get separate schema items** (included in pdf_attributes of main field):

**Same-Value Links**: Fields that share the same value across multiple pages or locations
- Example: `buyer_name_page1` and `buyer_name_page2` → Create ONE schema item for `buyer_name` with both fields as separate objects in `pdf_attributes` array
- Example: `property_info` and `property_info_linked_page_3` → Create ONE schema item with each field as its own `pdf_attributes` object
- Example: Fields with different names but same semantic meaning → Consolidate into ONE schema item with multiple `pdf_attributes` objects
- **For same-value radio buttons**: Use string array in `formfield` (e.g., `formfield: ["radio_option_1", "radio_option_2"]`)

**Continuation Fields**: Fields where text flows from one to the next
- Example: `property_address` and `property_address_continued` → Create ONE schema item for `property_address` with continuation field in `linked_form_fields_text`

**Linked Dates**: Date fields that auto-populate when signatures are captured
- Example: `tenant_signature` and `tenant_signature_date` → Create ONE schema item for `tenant_signature` with date field in `linked_dates`

**Radio Button Options**: Individual radio button values within a group
- Example: `monthly_rent_value` group with `rent_price_changes` and `rent_price_remains_the_same` options → Create ONE schema item for `monthly_rent_value` with options in `linked_form_fields_radio`

**Fields that DO get separate schema items**:

**Checkbox Linked Fields**: Fields that appear conditionally when a checkbox is selected
- These fields referenced in `checkbox_options.linkedFields` must have their own separate schema items
- Example: If "FHA" checkbox has `linkedFields: ["fha_case_number"]`, then `fha_case_number` needs its own schema item

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
    display_radio_options: ["Rent Price Changes", "Rent Price Remains the Same"],
    // ... other attributes
  }
}
```

#### Checkbox Handling with Nested Fields

When checkboxes have associated fields that should only appear when selected:

```typescript
{
  unique_id: "financing_options",
  pdf_attributes: [{
    formType: "purchase_agreement",
    formfield: "financing_type",
    linked_form_fields_checkbox: [
      { fromDatabase: "CONVENTIONAL", pdfAttribute: "conventional_financing" },
      { fromDatabase: "FHA", pdfAttribute: "fha_financing" },
      { fromDatabase: "VA", pdfAttribute: "va_financing" }
    ]
  }],
  display_attributes: {
    input_type: "checkbox",
    checkbox_options: {
      options: [
        { 
          display_name: "Conventional", 
          databaseStored: "CONVENTIONAL",
          linkedFields: ["conventional_loan_amount", "conventional_down_payment"]
        },
        { 
          display_name: "FHA", 
          databaseStored: "FHA",
          linkedFields: ["fha_case_number", "fha_loan_amount"]
        },
        { 
          display_name: "VA", 
          databaseStored: "VA",
          linkedFields: ["va_eligibility_number"]
        }
      ],
      maxSelected: 1,
      minSelected: 1
    },
    // ... other attributes
  }
}
```

**Important**: Fields referenced in `linkedFields` must have their own separate schema items with appropriate `visibleIf` conditions.

#### Field Count Verification

After processing all relationships:
- Count the extracted fields from the JSON
- Subtract fields that are linked/continuation/radio options
- Your final schema should have significantly fewer items than the original field count
- Document which fields were consolidated and why
- Pay special attention to fields that might semantically represent the same data value but have different names
- Ensure no duplicate schema items exist for the same semantic concept

### Step 13: Generate TypeScript Schema

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
  unique_id: string, // Semantic ID based on context analysis (e.g., "buyer_name")
  
  // For same-value fields, create separate pdf_attributes objects for each occurrence
  pdf_attributes: [{
    formType: string, // Extracted from filename
    formfield: string | string[], // Iterative field name(s) from PDF
  }, {
    formType: string, // Same form type
    formfield: string, // Another iterative field with same semantic purpose
    // Add more objects for each same-value field occurrence
  }],
  
  // OR for other field types:
  pdf_attributes: [{
    formType: string,
    formfield: string | string[],
    linked_form_fields_text?: string[], // Continuation fields
    linked_form_fields_radio?: { radioField: string; displayName: string }[],
    linked_form_fields_checkbox?: { fromDatabase: string; pdfAttribute: string }[],
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
    visibleIf?: {
      unique_id: string,
      operation: ">" | ">=" | "<" | "<=" | "==" | "!==" | "contains" | "doesNotContain",
      valueChecked: string
    }[],
    validation?: {
      loopback?: { regex: string, message: string }[],
      crossField?: { rule: ">" | ">=" | "<" | "<=" | "==" | "!==", unique_id: string, message?: string }[]
    },
    placeholder?: string,
    width?: number, // 1-12 grid system
    display_radio_options?: string[], // For radio buttons
    checkbox_options?: { // For checkboxes
      options: { display_name: string, databaseStored: string, linkedFields?: string[] }[],
      maxSelected?: number,
      minSelected?: number
    },
    value: {
      type: "manual" | "reserved",
      output?: "string" | "SignatureInput__signer", // Use SignatureInput__signer for all signatures
      reserved?: "tenant_name_csv" | "realtor_name_spaced" // For pre-filled values
    },
    special_input?: { // Modifies input appearance/behavior
      text?: {
        percentage?: boolean,
        phone?: boolean,
        date?: boolean,
        currency?: boolean, // Required for monetary fields
        number?: boolean,
        email?: boolean,
        url?: boolean
      },
      checkbox?: {
        asRadio?: boolean,
        horizontal?: number
      },
      info?: {
        style?: 'default' | 'subtle' | 'minimal' | 'inline' | 'compact' | 'warning' | 'success' | 'error' | 'tip',
        icon?: boolean,
        minimizable?: boolean
      },
      radio?: {
        layout?: 'vertical' | 'horizontal' | 'grid',
        columns?: number
      },
      signature?: {
        dateFormat?: string,
        showInitials?: boolean
      },
      fileUpload?: {
        accept?: string,
        maxSize?: number,
        multiple?: boolean
      },
      textArea?: {
        minRows?: number,
        maxRows?: number,
        autoResize?: boolean
      }
    },
    isCached?: boolean, // true for realtor/broker info
    isRequired?: boolean, // Determine based on field importance
    isHidden?: boolean, // For fields that should be hidden
    breakBefore?: boolean // Use for visual separation
  }
}
```

### Step 14: Handle Value Types and Reserved Fields

#### Value Type Guidelines:

**Manual Input** (default for most fields):
```typescript
value: {
  type: "manual"
}
```

**Reserved Values** (for pre-filled fields):
```typescript
// For realtor full name (space-separated)
value: {
  type: "reserved",
  reserved: "realtor_name_spaced"
}

// For tenant names as CSV
value: {
  type: "reserved",
  reserved: "tenant_name_csv"
}
```

**Signature Fields**:
```typescript
value: {
  type: "manual",
  output: "SignatureInput__signer"  // Always use this for signatures
}
```

### Step 15: Quality Assurance

Before finalizing the schema:

1. **Verify relationships**: Ensure linked fields make logical sense
2. **Check display names**: Confirm they're user-friendly and clear
3. **Validate widths**: Ensure layout will be visually appealing
4. **Review blocks**: Confirm logical grouping and appropriate styling
5. **Test validation**: Ensure rules aren't too restrictive
6. **Confirm order**: Fields should follow a logical sequence
7. **Verify special_input**: Ensure currency fields have `special_input.text.currency: true`
8. **Check visibility conditions**: Confirm conditional fields have proper `visibleIf` rules

## Step 16: Deploy Schema to Application

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

## Example Workflow

### 1. Extract fields with context:
```bash
python3 extract_pdf_fields_enhanced.py purchase_agreement.pdf
```

### 2. Analyze extracted JSON:
```json
{
  "field_name": "purchase_agreement_textfield_1",
  "field_type": "Text",
  "context_left": "Buyer",
  "context_above": "Full Name",
  "context_right": "",
  "context_below": ""
}
```

### 3. Context analysis determines:
- The iterative name "purchase_agreement_textfield_1" tells us nothing - it's just the first text field
- The context "Buyer" + "Full Name" reveals this is a buyer name field
- Create semantic `unique_id: "buyer_name"` based on the context
- Keep the original `formfield: "purchase_agreement_textfield_1"` in pdf_attributes for PDF mapping

### 4. Generate schema item:
```typescript
{
  unique_id: "buyer_name",
  pdf_attributes: [{
    formType: "purchase_agreement",
    formfield: "purchase_agreement_textfield_1"
  }],
  display_attributes: {
    display_name: "Buyer Name",
    input_type: "text",
    // ... other attributes based on context
  }
}
```

Remember: The goal is to create a schema that provides an excellent user experience while maintaining all necessary PDF field mappings and relationships. Since field names are programmatically generated and carry no semantic meaning, successful schema generation depends entirely on accurate context analysis to understand each field's purpose.