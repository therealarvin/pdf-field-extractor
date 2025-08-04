# Schema Workflow Orchestration Guide

This document outlines the complete two-stage agent workflow for generating and beautifying PDF form schemas. Follow this guide to orchestrate the entire schema generation process from start to finish.

## Overview

The schema generation process consists of **two specialized agents working in sequence**:
1. **Schema Generation Agent** - Creates the initial schema following technical requirements
2. **Schema Beautification Agent** - Enhances the schema for optimal user experience

## Prerequisites

Before starting, verify:
1. PDF forms are located in `/Users/arvin/WebDev/field_extraction/renamed-and-reviewed-forms/`
2. All required instruction files are present:
   - `SCHEMA_GENERATION_INSTRUCTIONS.md`
   - `SCHEMA-BEAUTIFY.md`
3. Python scripts are available in the working directory

## Workflow Steps

### Step 1: Identify Target Forms

Check the `renamed-and-reviewed-forms` folder for PDF forms that need schema generation:

```bash
ls /Users/arvin/WebDev/field_extraction/renamed-and-reviewed-forms/
```

### Step 2: Launch Schema Generation Agent

For each PDF form found, spawn the first specialized agent:

**Agent Type**: Schema Generation Agent  
**Task Description**: "Generate initial schema"  
**Instructions File**: `SCHEMA_GENERATION_INSTRUCTIONS.md`

**Agent Prompt Template**:
```
You are a specialized schema generation agent. Your task is to generate a complete TypeScript schema for the PDF form using the schema generation instructions.

**Target File:** `/Users/arvin/WebDev/field_extraction/renamed-and-reviewed-forms/[PDF_FILENAME]`

**Instructions:** Follow ALL steps in `/Users/arvin/WebDev/field_extraction/SCHEMA_GENERATION_INSTRUCTIONS.md`

**Key Requirements:**
1. Extract fields using the enhanced script
2. Properly handle linked fields (Step 11) - NO separate schema items for linked fields
3. Consolidate continuation fields, signature+date pairs, radio button groups
4. Create logical block groupings with appropriate styling
5. Apply validation rules for phone/email/date/monetary fields
6. Use manual value type without output field
7. Deploy final schema to `/Users/arvin/WebDev/onroad_full/onroad_express/src/logic/realtor/centralIntelligence/schemas/[FORM_NAME]_schema.ts`

**Critical Points:**
- Fields with `_linked_` are same-value fields (multiple pdf_attributes objects)
- Radio buttons MUST have `linked_form_fields_radio` populated
- Initials are signature types
- Consolidate semantically identical fields to avoid duplicates

Provide detailed consolidation report showing field relationships handled and final schema structure.
```

### Step 3: Wait for Schema Generation Completion

The Schema Generation Agent will:
- Extract PDF fields with enhanced context
- Identify and consolidate field relationships
- Generate initial TypeScript schema
- Deploy to application directory
- Provide consolidation report

**Expected Outputs:**
- `[form_name]_schema.ts` in application schemas directory
- Consolidation report documenting field relationships
- Field count reduction analysis

### Step 4: Launch Schema Beautification Agent

Once the initial schema is generated, spawn the second specialized agent:

**Agent Type**: Schema Beautification Agent  
**Task Description**: "Beautify and enhance schema"  
**Instructions File**: `SCHEMA-BEAUTIFY.md`

**Agent Prompt Template**:
```
You are a specialized schema beautification agent. Your task is to enhance the generated schema for optimal user experience using the beautification guidelines.

**Target Schema:** `/Users/arvin/WebDev/onroad_full/onroad_express/src/logic/realtor/centralIntelligence/schemas/[FORM_NAME]_schema.ts`

**Instructions:** Follow ALL guidelines in `/Users/arvin/WebDev/field_extraction/SCHEMA-BEAUTIFY.md`

**Key Enhancements:**
1. Add comprehensive field descriptions
2. Implement intelligent `visibleIf` conditions for conditional fields
3. Optimize field ordering for logical user flow
4. Enhance validation with user-friendly error messages
5. Improve placeholders with context-specific examples
6. Add helpful icons and color themes to blocks
7. Implement progressive disclosure patterns
8. Add field dependencies and cross-field validation

**Focus Areas:**
- **User Experience**: Logical flow, clear descriptions, helpful guidance
- **Conditional Logic**: Smart field visibility based on user selections
- **Validation**: User-friendly error messages and input guidance
- **Visual Design**: Appropriate widths, spacing, and block organization
- **Progressive Disclosure**: Show fields only when relevant

**Output:** Enhanced schema file with improved UX, conditional logic, and comprehensive descriptions.

Provide enhancement report detailing UX improvements made.
```

### Step 5: Verification and Quality Assurance

After both agents complete their work:

1. **Schema Validation**: Verify TypeScript syntax and SchemaItem compliance
2. **Field Coverage**: Ensure all PDF fields are represented
3. **Conditional Logic**: Test visibleIf conditions make logical sense
4. **User Flow**: Review field ordering and block organization
5. **Validation Rules**: Confirm appropriate validation for field types

## Agent Orchestration Best Practices

### Sequential Execution
- **Always run Schema Generation Agent first**
- **Wait for completion before launching Beautification Agent**
- Each agent builds on the previous agent's work

### Error Handling
- If Schema Generation fails, debug field extraction issues
- If Beautification fails, ensure initial schema exists and is valid
- Retry with specific fixes rather than starting over

### Quality Control
- Review both agents' reports for completeness
- Verify all radio buttons have `linked_form_fields_radio`
- Confirm field consolidation was applied correctly
- Test conditional logic flows

### Performance Optimization
- Run agents for multiple forms in parallel where possible
- Cache field extraction results for similar forms
- Reuse beautification patterns across similar form types

## Expected Deliverables

### From Schema Generation Agent:
- Initial TypeScript schema file
- Field consolidation report
- PDF field mapping documentation
- Error/warning logs

### From Beautification Agent:
- Enhanced schema with UX improvements
- Conditional logic implementation
- Visual design optimizations
- Enhancement report

### Final Output:
- Production-ready schema file
- Complete documentation
- User experience optimization
- Full field coverage with relationships

## Troubleshooting

### Common Issues:
1. **Missing radio_options**: Re-run field extraction, check PDF structure
2. **Duplicate schema items**: Review same-value field consolidation logic
3. **Missing visibleIf**: Ensure beautification agent identifies conditional relationships
4. **TypeScript errors**: Verify import paths and SchemaItem compliance

### Resolution Steps:
1. Check agent reports for specific error details
2. Re-run individual agents with targeted fixes
3. Verify instruction files are up to date
4. Test schema output in development environment

## File Locations

- **Input PDFs**: `/Users/arvin/WebDev/field_extraction/renamed-and-reviewed-forms/`
- **Instructions**: `/Users/arvin/WebDev/field_extraction/SCHEMA_GENERATION_INSTRUCTIONS.md`
- **Beautification**: `/Users/arvin/WebDev/field_extraction/SCHEMA-BEAUTIFY.md`
- **Output Schemas**: `/Users/arvin/WebDev/onroad_full/onroad_express/src/logic/realtor/centralIntelligence/schemas/`
- **Working Directory**: `/Users/arvin/WebDev/field_extraction/`

## Success Criteria

A successful schema generation workflow produces:
- ✅ Complete field coverage from PDF
- ✅ Proper field relationships and consolidation
- ✅ Radio buttons with linked_form_fields_radio
- ✅ Logical block organization and styling
- ✅ Comprehensive conditional logic (visibleIf)
- ✅ User-friendly descriptions and validation
- ✅ Optimized field ordering and widths
- ✅ Production-ready TypeScript schema

This workflow ensures consistent, high-quality schema generation that provides excellent user experience while maintaining complete PDF field mapping fidelity.