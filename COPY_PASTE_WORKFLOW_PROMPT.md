# Copy-Paste Workflow Prompt

Use this prompt to initiate the complete schema generation workflow:

---

**PROMPT FOR SCHEMA GENERATION WORKFLOW:**

```
Please execute the complete schema generation workflow by following the SCHEMA_WORKFLOW_ORCHESTRATION.md guide located at /Users/arvin/WebDev/field_extraction/SCHEMA_WORKFLOW_ORCHESTRATION.md.

Your tasks:
1. Check /Users/arvin/WebDev/field_extraction/renamed-and-reviewed-forms/ for PDF forms that need schema generation
2. For each PDF found, spawn two sequential agents following the orchestration guide:
   - First: Schema Generation Agent using SCHEMA_GENERATION_INSTRUCTIONS.md
   - Second: Schema Beautification Agent using SCHEMA-BEAUTIFY.md
3. Oversee both agents to ensure proper completion
4. Verify final schema quality and provide summary report

Follow the exact agent prompt templates and workflow steps outlined in the orchestration guide. Ensure each agent completes successfully before proceeding to the next step.
```

---

**Alternative Short Version:**

```
Execute schema workflow per SCHEMA_WORKFLOW_ORCHESTRATION.md: check renamed-and-reviewed-forms folder, spawn Schema Generation Agent then Schema Beautification Agent for each PDF found. Follow the orchestration guide exactly.
```