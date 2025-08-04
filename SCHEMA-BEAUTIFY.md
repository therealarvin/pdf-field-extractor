# Schema Beautification Guide

This guide explains how to beautify schema items for OnRoad forms using the FormInput component patterns and design principles from the IABS form.

## ⚠️ CRITICAL RULES

### PDF Attributes - DO NOT MODIFY
- **NEVER** change `pdf_attributes` unless explicitly told "edit pdf attributes"
- PDF field names, form types, and linking must remain intact for form functionality
- **Exception**: Only modify `pdf_attributes` when explicitly instructed to link text fields or radio fields
- **Default rule**: Only modify `display_attributes` for beautification

### Required Fields and Caching
- Set `isRequired: true` in `display_attributes` if the field should be mandatory
- Set `isCached: true` for fields that won't change across deals (realtor name, firm info, etc.)

## Grid System (12-Unit Layout)

FormInput uses a 12-unit grid system where fields are arranged in rows:

```typescript
width: 1-12  // Field width in grid units
```

### Common Width Patterns:
- `width: 12` - Full width (single field per row)
- `width: 6` - Half width (two fields per row)
- `width: 4` - Third width (three fields per row)
- `width: 3` - Quarter width (four fields per row)

### Layout Control:
- `breakBefore: true` - Forces field to start a new row

## Block Organization

Group related fields using blocks with consistent styling:

```typescript
display_attributes: {
  block: "Section Name",
  block_style: {
    title: "Human Readable Title",
    description: "Brief explanation of this section's purpose",
    icon: "IconName",
    color_theme: "blue"
  }
}
```

## Color Themes

5 available themes with consistent styling:

| Theme | Use Cases |
|-------|-----------|
| `blue` | Primary information, general forms |
| `green` | Personal details, contacts, success states |
| `purple` | Financial information, calculations |
| `orange` | Agents, representatives, active roles |
| `gray` | Signatures, acknowledgments, secondary info |

## Available Icons

Choose meaningful icons that match content:

| Icon | Best For |
|------|----------|
| `Info` | Information sections, help text |
| `Home` | Property, brokerage firm details |
| `Users` | People, parties, agents |
| `FileText` | Documents, forms, signatures |
| `Calendar` | Dates, scheduling |
| `CreditCard` | Financial, payments |
| `MapPin` | Addresses, locations |
| `AlertCircle` | Warnings, important notices |

## Input Types

### Text Fields
```typescript
input_type: "text"
placeholder: "Example input text"
description: "Clear explanation of what to enter"
```

### Radio Options
```typescript
input_type: "radio"
display_radio_options: ["Option 1", "Option 2", "Option 3"]
// OR use linked_form_fields_radio for PDF mapping
```

### Checkboxes
```typescript
input_type: "checkbox"
// Returns "true"/"false" strings
```

### Signature Fields
```typescript
input_type: "signature"
// Automatically includes party selection and role dropdown
```

### Info Sections
```typescript
input_type: "info"
// Rich display with colored backgrounds and icons
// No input field, just informational content
```

### Text Areas
```typescript
input_type: "text-area"
// Multi-line text input

These are going to be the only input types, all fields will have to fit into one of these input types
```

## Field Descriptions

Descriptions appear below field labels in small, muted text:

```typescript
description: "Clear, concise explanation of what this field requires or how it's used"
```

### Good Description Patterns:
- Explain the purpose: "Primary contact email for the brokerage firm"
- Provide format hints: "Main business phone number with area code"
- Clarify requirements: "State-issued license number for the sales agent"
- Add context: "Licensed supervisor overseeing sales activities (if applicable)"

## Linked Fields

### Text Overflow Fields
For PDF forms where text might overflow to continuation boxes:
```typescript
pdf_attributes: [{
  linked_form_fields_text: ["field1", "field2", "field3"]
}]
```

### Radio Button Mapping
Maps display names to PDF radio field names:
```typescript
pdf_attributes: [{
  linked_form_fields_radio: [
    { displayName: "User-Friendly Name", radioField: "pdf_field_name" }
  ]
}]
```

### Linked Dates for Signature Fields
Links date fields to signature fields so dates auto-populate when signatures are completed:
```typescript
pdf_attributes: [{
  formType: "FORM_TYPE",
  formfield: "signature_field_name",
  linked_dates: [
    {
      dateFieldName: "date_field_unique_id"
    }
  ]
}]
```

**Important Principles:**
- Each signature field should link to its own corresponding date field
- The `dateFieldName` should match the `unique_id` of the date field (NOT the PDF field name)
- Date fields should use `visibleIf` to only show when their corresponding signature is NOT blank
- Multiple signature fields should NOT share the same date field unless they truly represent the same signing event

## IABS Design Patterns

### Section Structure
The IABS form demonstrates excellent organization:

1. **Info Section** (width: 12, blue theme, Info icon)
2. **Broker Firm Information** (width: 6 fields, blue theme, Home icon)
3. **Designated Firm Broker** (width: 6 fields, green theme, Users icon)
4. **Sales Supervisor** (width: 6 fields, purple theme, CreditCard icon)
5. **Sales Agent** (width: 6 fields, orange theme, Users icon)
6. **Acknowledgment & Signatures** (width: 6 fields, gray theme, FileText icon)

### Visual Flow Principles:
- Start with info section explaining the form
- Group related information in themed blocks
- Use consistent field widths within blocks
- Strategic use of `breakBefore` for visual breaks
- End with signature/acknowledgment sections

### Field Layout Patterns:
- **Name fields**: Usually width: 6
- **Contact info** (email/phone): width: 6 
- **License numbers**: width: 6
- **Full-width info**: width: 12
- **Signature fields**: width: 6
- **Dates**: width: 3

## Value Field Configuration

The `value` field determines how form fields get their data - either manual entry or automatic resolution from database:

### Manual Entry (User Input Required)
```typescript
value: { 
  type: "manual" 
}
```
Use when users must manually enter information.

### Resolved Fields (Automatic Population)
```typescript
value: {
  type: "resolved",
  output: "string" | "SignatureInput__signer" | "SignatureInput__delegator",
  supabase: [
    {
      table: "table_name",
      column: "column_to_retrieve", 
      eqBy: [
        {
          columnName: "field_to_match",
          variable: "dealId" | "dealOptionId",     // Dynamic variables
          hardCodedValue: "static_value"           // OR static values
        }
      ]
    }
    // Additional fallback queries...
  ]
}
```

### Output Types:
- **`"string"`** - Returns plain text value
- **`"SignatureInput__signer"`** - Creates signature field with actionAs: "signer" 
- **`"SignatureInput__delegator"`** - Creates signature field with actionAs: "delegator"

### Supabase Query Array (Fallback System):
The `supabase` array tries queries in order until one returns data:

```typescript
// Example from IABS.ts - tries buyer first, then tenant
supabase: [
  {
    table: "deals_parties",
    column: "party_email",
    eqBy: [
      { columnName: "deal_id", variable: "dealId" },
      { columnName: "partyNumber", hardCodedValue: "1" },
      { columnName: "party_role", hardCodedValue: "buyer" }
    ]
  },
  {
    table: "deals_parties", 
    column: "party_email",
    eqBy: [
      { columnName: "deal_id", variable: "dealId" },
      { columnName: "partyNumber", hardCodedValue: "1" },
      { columnName: "party_role", hardCodedValue: "tenant" }  // Fallback
    ]
  }
]
```

### Signature Field Patterns:

**From the IABS schema, signature fields use this pattern:**
1. **Query deals_parties table** for party email
2. **Filter by dealId + partyNumber + party_role** 
3. **Fallback between roles** (buyer→tenant, seller→landlord)
4. **Auto-populate signature field** with found email

**Important Role Mapping Rules:**
- **Landlord fields** → Query `party_role: "landlord"` (NOT "seller")
- **Seller fields** → Query `party_role: "seller"`
- **Buyer fields** → Query `party_role: "buyer"`  
- **Tenant fields** → Query `party_role: "tenant"`
- **Always match display names to database roles**

**Initials vs Full Signatures:**
- **Both initials AND full signatures** should use `input_type: "signature"`
- **Both should be resolved from database** when possible (not manual)
- **Initials are just shorter signature fields** - treat them the same way

## Example Implementation

```typescript
{
  unique_id: "broker_firm_name",
  pdf_attributes: [
    {
      formType: "EXAMPLE_FORM", 
      formfield: "broker_firm_name" // DO NOT CHANGE
    }
  ],
  display_attributes: {
    display_name: "Broker Firm Name",
    description: "The legal name of the real estate brokerage firm as registered with the state licensing authority",
    input_type: "text",
    placeholder: "ABC Real Estate Brokerage",
    block: "Broker Firm Information",
    block_style: {
      title: "Broker Firm Information",
      description: "Primary brokerage firm details and licensing information",
      icon: "Home",
      color_theme: "blue"
    },
    width: 6,
    order: 2, // Sequential numbering
    isRequired: true,
    isCached: true, // Firm info doesn't change per deal
    value: { type: "manual" }
  }
}
```

## Field Reordering for Better UX

You can and should reorder fields to improve user experience and form flow:

### Reordering Process:
1. **Change the `order` attribute** for each field (sequential numbering: 1, 2, 3...)
2. **Physically reorder fields** in the schema array to match ascending order
3. **Maintain logical grouping** - keep related fields together

### Good Reordering Principles:
- **Start with context** (info sections, property details)
- **Group related information** (all contact info together)
- **Progressive disclosure** (basic info before detailed info)
- **End with signatures** (acknowledgments and sign-off)

```typescript
// Example of reordering - change both order attribute AND physical position
{
  unique_id: "intro_info",
  display_attributes: {
    order: 1, // First field
    // ...
  }
},
{
  unique_id: "property_address", 
  display_attributes: {
    order: 2, // Second field
    // ...
  }
}
// Physical order in array should match order attribute!
```

## Conditional Visibility with visibleIf

Use `visibleIf` conditions sparingly but effectively for dynamic forms:

### Basic Structure:
```typescript
visibleIf: [
  {
    unique_id: "controlling_field_id",
    operation: ">=" | ">" | "<=" | "<" | "==" | "!==",
    valueChecked: "comparison_value"
  }
]
```

### Available Operations:
- `"=="` - Exact match
- `"!=="` - Does not match  
- `">="` - Greater than or equal (useful for numbers)
- `">"` - Greater than
- `"<="` - Less than or equal
- `"<"` - Less than

### Helper Question Pattern

**Best Practice**: Create helper questions without PDF attributes to control visibility:

```typescript
// Helper question - no PDF attributes needed
{
  unique_id: "number_of_animals_question",
  display_attributes: {
    display_name: "How Many Animals Are You Moving In?",
    input_type: "radio",
    order: 5,
    block: "Animal Count",
    display_radio_options: ["0", "1", "2", "3", "4"],
    value: { type: "manual" }
  }
},

// Dependent fields that show based on answer
{
  unique_id: "animal_1_type",
  pdf_attributes: [/*...existing PDF mapping...*/],
  display_attributes: {
    display_name: "Animal 1 - Type",
    input_type: "text",
    order: 6,
    block: "Animal 1 Details",
    visibleIf: [
      {
        unique_id: "number_of_animals_question",
        operation: ">=",
        valueChecked: "1"
      }
    ]
  }
}
```

### Animal Agreement Pattern Example

From the Animal Agreement schema, this pattern is used effectively:

1. **Master Control**: "How many animals?" (0-4 options)
2. **Progressive Sections**: 
   - Animal 1 fields show when `>= "1"`
   - Animal 2 fields show when `>= "2"`  
   - Animal 3 fields show when `>= "3"`
   - Animal 4 fields show when `>= "4"`

### Date Field Visibility Pattern

Date fields linked to signatures should only appear when their corresponding signature is NOT blank:

```typescript
// Date field with conditional visibility
{
  unique_id: "signature_date_field",
  pdf_attributes: [{ formType: "FORM_TYPE", formfield: "date_pdf_field" }],
  display_attributes: {
    display_name: "Date Signed",
    input_type: "text",
    order: X,
    visibleIf: [
      {
        unique_id: "corresponding_signature_field",
        operation: "!==", 
        valueChecked: ""
      }
    ]
  }
}
```

**Key Points:**
- Use `operation: "!=="` and `valueChecked: ""` to show when signature is NOT blank
- The `unique_id` in `visibleIf` should match the signature field's unique_id
- This prevents empty date fields from cluttering the form

### When to Use Conditional Visibility:

✅ **Good Use Cases:**
- **Repetitive sections** (multiple animals, parties, properties)
- **Optional details** (additional contact info if needed)
- **Branching logic** (different fields for different property types)
- **Progressive disclosure** (advanced options after basic selection)
- **Date fields linked to signatures** (only show when signature exists)

❌ **Avoid Using For:**
- **Core required fields** (always show essential information)
- **Simple yes/no splits** (consider separate forms instead)
- **Complex nested conditions** (can confuse users)

### Multiple Conditions:

You can have multiple conditions (ALL must be true):

```typescript
visibleIf: [
  {
    unique_id: "property_type",
    operation: "==",
    valueChecked: "rental"
  },
  {
    unique_id: "lease_duration", 
    operation: ">=",
    valueChecked: "12"
  }
]
```

## Form Beautification Checklist

### Before Starting:
- [ ] Read existing PDF attributes - DO NOT CHANGE unless explicitly told
- [ ] Understand the form's purpose and user flow
- [ ] Identify logical field groupings
- [ ] Consider if field reordering would improve UX
- [ ] Analyze existing `value` fields (manual vs resolved)

### During Beautification:
- [ ] Create meaningful block names with appropriate themes
- [ ] Add clear, helpful descriptions to all fields
- [ ] Choose appropriate field widths for visual balance
- [ ] Select relevant icons for each block
- [ ] Use consistent patterns within the form
- [ ] Set appropriate `isRequired` flags
- [ ] Set `isCached: true` for realtor/firm information
- [ ] Reorder fields logically and update order attributes
- [ ] Consider helper questions for complex conditional sections
- [ ] Add visibleIf conditions where they improve UX
- [ ] Preserve existing `value` configurations (keep resolved fields intact)

### After Beautification:
- [ ] Verify no PDF attributes were modified (unless explicitly instructed)
- [ ] Check visual flow and grouping makes sense
- [ ] Ensure all fields have appropriate descriptions
- [ ] Confirm required flags are properly set
- [ ] Verify order attributes match physical field order
- [ ] Test conditional visibility logic makes sense
- [ ] Confirm resolved fields maintain their database connections

## Questions to Consider

When beautifying schemas, ask yourself:

1. **Organization**: How can fields be logically grouped and ordered?
2. **User Experience**: What information helps users complete fields correctly?
3. **Visual Hierarchy**: Which sections are most important?
4. **Data Consistency**: What fields should be cached across deals?
5. **Requirements**: Which fields are mandatory for form completion?
6. **Progressive Flow**: Would reordering fields create a more intuitive sequence?
7. **Conditional Logic**: Are there repetitive sections that could use helper questions?

Remember: The goal is to create forms that are intuitive, visually appealing, and functionally complete while maintaining PDF form compatibility.