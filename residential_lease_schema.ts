import { SchemaItem } from "../../../../types/realtor";

export const residentialLeaseSchema: SchemaItem[] = [
  {
    unique_id: "landlord_name",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlord_name",
      linked_form_fields_text: ["landlord_name_cont"]
    }],
    display_attributes: {
      display_name: "Landlord Name",
      input_type: "text",
      description: "Full name of the property landlord",
      order: 1,
      attribute: "landlord_info",
      block: "landlord_information",
      block_style: {
        title: "Landlord Information",
        description: "Information about the property landlord",
        icon: "user",
        color_theme: "green"
      },
      placeholder: "John Doe",
      width: 8,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "tenant_names",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_names",
      linked_form_fields_text: ["tenant_names_cont"]
    }],
    display_attributes: {
      display_name: "Tenant Names",
      input_type: "text",
      description: "Full names of all tenants",
      order: 2,
      attribute: "tenant_info",
      block: "tenant_information",
      block_style: {
        title: "Tenant Information",
        description: "Information about the tenants",
        icon: "users",
        color_theme: "blue"
      },
      placeholder: "Jane Smith, John Smith",
      width: 8,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "property_street_address",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "property_street_address"
    }],
    display_attributes: {
      display_name: "Property Street Address",
      input_type: "text",
      description: "Street address of the rental property",
      order: 3,
      attribute: "property_info",
      block: "property_information",
      block_style: {
        title: "Property Information",
        description: "Details about the rental property",
        icon: "home",
        color_theme: "purple"
      },
      placeholder: "123 Main Street",
      width: 8,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "property_legal_description",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "property_legal_description",
      linked_form_fields_text: ["property_legal_description_cont"]
    }],
    display_attributes: {
      display_name: "Property Legal Description",
      input_type: "text-area",
      description: "Legal description of the property",
      order: 4,
      attribute: "property_info",
      block: "property_information",
      placeholder: "Legal property description",
      width: 12,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "property_county",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "property_county"
    }],
    display_attributes: {
      display_name: "Property County",
      input_type: "text",
      description: "County where the property is located",
      order: 5,
      attribute: "property_info",
      block: "property_information",
      placeholder: "Harris County",
      width: 4,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "property_items",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "property_items_1"
    }, {
      formType: "residential_lease",
      formfield: "property_items_2"
    }],
    display_attributes: {
      display_name: "Property Items",
      input_type: "text-area",
      description: "Non-real property items included with rental",
      order: 6,
      attribute: "property_info",
      block: "property_information",
      placeholder: "Appliances, furniture, fixtures, etc.",
      width: 12,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "lease_start_date",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "lease_start_date"
    }],
    display_attributes: {
      display_name: "Lease Start Date",
      input_type: "text",
      description: "Date when the lease begins",
      order: 7,
      attribute: "lease_terms",
      block: "lease_terms",
      block_style: {
        title: "Lease Terms",
        description: "Key terms and dates for the lease agreement",
        icon: "calendar",
        color_theme: "orange"
      },
      validation: {
        loopback: [{
          regex: "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
          message: "Must be a valid date (MM/DD/YYYY)"
        }]
      },
      placeholder: "MM/DD/YYYY",
      width: 4,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "lease_end_date",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "lease_end_date"
    }],
    display_attributes: {
      display_name: "Lease End Date",
      input_type: "text",
      description: "Date when the lease expires",
      order: 8,
      attribute: "lease_terms",
      block: "lease_terms",
      validation: {
        loopback: [{
          regex: "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
          message: "Must be a valid date (MM/DD/YYYY)"
        }]
      },
      placeholder: "MM/DD/YYYY",
      width: 4,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "landlord_initials",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlord_initials_linked_1"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_2"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_3"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_4"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_5"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_6"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_7"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_8"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_9"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_10"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_11"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_12"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_13"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_14"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_15"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_16"
    }, {
      formType: "residential_lease",
      formfield: "landlord_initials_linked_17"
    }],
    display_attributes: {
      display_name: "Landlord Initials",
      input_type: "signature",
      description: "Landlord initials appear on all pages",
      order: 9,
      attribute: "landlord_signature",
      block: "signatures",
      block_style: {
        title: "Signatures & Initials",
        description: "Required signatures and initials for all parties",
        icon: "pen-tool",
        color_theme: "gray"
      },
      width: 3,
      value: {
        type: "manual"
      },
      isRequired: true,
      breakBefore: true
    }
  },
  {
    unique_id: "landlord_2_initials",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_1"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_2"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_3"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_4"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_5"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_6"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_7"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_8"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_9"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_10"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_11"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_12"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_13"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_14"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_15"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_16"
    }, {
      formType: "residential_lease",
      formfield: "landlord_2_initials_linked_17"
    }],
    display_attributes: {
      display_name: "Second Landlord Initials",
      input_type: "signature",
      description: "Second landlord initials (if applicable)",
      order: 10,
      attribute: "landlord_signature",
      block: "signatures",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "tenant_initials",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_initials_linked_1"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_2"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_3"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_4"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_5"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_6"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_7"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_8"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_9"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_10"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_11"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_12"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_13"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_14"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_15"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_16"
    }, {
      formType: "residential_lease",
      formfield: "tenant_initials_linked_17"
    }],
    display_attributes: {
      display_name: "Tenant Initials",
      input_type: "signature",
      description: "First tenant initials appear on all pages",
      order: 11,
      attribute: "tenant_signature",
      block: "signatures",
      width: 3,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "tenant_2_initials",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_1"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_2"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_3"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_4"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_5"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_6"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_7"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_8"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_9"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_10"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_11"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_12"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_13"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_14"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_15"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_16"
    }, {
      formType: "residential_lease",
      formfield: "tenant_2_initials_linked_17"
    }],
    display_attributes: {
      display_name: "Second Tenant Initials",
      input_type: "signature",
      description: "Second tenant initials (if applicable)",
      order: 12,
      attribute: "tenant_signature",
      block: "signatures",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "tenant_3_initials",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_1"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_2"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_3"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_4"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_5"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_6"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_7"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_8"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_9"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_10"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_11"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_12"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_13"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_14"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_15"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_16"
    }, {
      formType: "residential_lease",
      formfield: "tenant_3_initials_linked_17"
    }],
    display_attributes: {
      display_name: "Third Tenant Initials",
      input_type: "signature",
      description: "Third tenant initials (if applicable)",
      order: 13,
      attribute: "tenant_signature",
      block: "signatures",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "tenant_4_initials",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_1"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_2"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_3"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_4"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_5"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_6"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_7"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_8"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_9"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_10"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_11"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_12"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_13"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_14"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_15"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_16"
    }, {
      formType: "residential_lease",
      formfield: "tenant_4_initials_linked_17"
    }],
    display_attributes: {
      display_name: "Fourth Tenant Initials",
      input_type: "signature",
      description: "Fourth tenant initials (if applicable)",
      order: 14,
      attribute: "tenant_signature",
      block: "signatures",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "property_address",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "property_address_linked_1"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_2"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_3"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_4"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_5"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_6"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_7"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_8"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_9"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_10"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_11"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_12"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_13"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_14"
    }, {
      formType: "residential_lease",
      formfield: "property_address_linked_15"
    }],
    display_attributes: {
      display_name: "Property Address (Referenced)",
      input_type: "text",
      description: "Property address that appears on all pages",
      order: 15,
      attribute: "property_info",
      block: "property_information",
      placeholder: "123 Main St, City, State 12345",
      width: 8,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "auto_renewal_30_days_before_expiration_date",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "auto_renewal_30_days_before_expiration_date"
    }],
    display_attributes: {
      display_name: "Auto Renewal 30 Days Before Expiration",
      input_type: "checkbox",
      description: "Lease auto-renews unless terminated 30 days before expiration",
      order: 16,
      attribute: "lease_terms",
      block: "lease_terms",
      width: 6,
      value: {
        type: "manual"
      },
      breakBefore: true
    }
  },
  {
    unique_id: "auto_renewal_custom_days_before_expiration_date",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "auto_renewal_custom_days_before_expiration_date"
    }],
    display_attributes: {
      display_name: "Auto Renewal Custom Days Before Expiration",
      input_type: "checkbox",
      description: "Lease auto-renews unless terminated specified days before expiration",
      order: 17,
      attribute: "lease_terms",
      block: "lease_terms",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "auto_renewal_days_before_expiration_date",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "auto_renewal_days_before_expiration_date"
    }],
    display_attributes: {
      display_name: "Days Before Expiration for Termination Notice",
      input_type: "text",
      description: "Number of days before expiration to provide termination notice",
      order: 18,
      attribute: "lease_terms",
      block: "lease_terms",
      placeholder: "30",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "monthly_rent_amount",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "monthly_rent_amount"
    }],
    display_attributes: {
      display_name: "Monthly Rent Amount",
      input_type: "text",
      description: "Monthly rental amount",
      order: 19,
      attribute: "financial_terms",
      block: "financial_terms",
      block_style: {
        title: "Financial Terms",
        description: "Rent amounts, deposits, and payment details",
        icon: "dollar-sign",
        color_theme: "orange"
      },
      validation: {
        loopback: [{
          regex: "^[\\d.,$]+$",
          message: "Must be a valid monetary amount"
        }]
      },
      placeholder: "$2,500.00",
      width: 4,
      value: {
        type: "manual"
      },
      isRequired: true,
      breakBefore: true
    }
  },
  {
    unique_id: "rent_due_date_day",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "rent_due_date_day"
    }],
    display_attributes: {
      display_name: "Rent Due Date (Day of Month)",
      input_type: "text",
      description: "Day of the month rent is due",
      order: 20,
      attribute: "financial_terms",
      block: "financial_terms",
      placeholder: "1",
      width: 4,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "payment_payee_landlord",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "payment_payee_landlord"
    }],
    display_attributes: {
      display_name: "Payment Payee: Landlord",
      input_type: "checkbox",
      description: "Rent should be paid to the landlord",
      order: 21,
      attribute: "payment_options",
      block: "financial_terms",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "payment_payee_broker",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "payment_payee_broker"
    }],
    display_attributes: {
      display_name: "Payment Payee: Broker",
      input_type: "checkbox",
      description: "Rent should be paid to the broker",
      order: 22,
      attribute: "payment_options",
      block: "financial_terms",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "payment_payee_manager",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "payment_payee_manager"
    }],
    display_attributes: {
      display_name: "Payment Payee: Manager",
      input_type: "checkbox",
      description: "Rent should be paid to the property manager",
      order: 23,
      attribute: "payment_options",
      block: "financial_terms",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "first_month_rent_due_date",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "first_month_rent_due_date"
    }],
    display_attributes: {
      display_name: "First Month Rent Due Date",
      input_type: "text",
      description: "Due date for first month's rent",
      order: 24,
      attribute: "financial_terms",
      block: "financial_terms",
      validation: {
        loopback: [{
          regex: "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
          message: "Must be a valid date (MM/DD/YYYY)"
        }]
      },
      placeholder: "MM/DD/YYYY",
      width: 4,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "payment_method_cashier",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "payment_method_cashier"
    }],
    display_attributes: {
      display_name: "Payment Method: Cashier's Check",
      input_type: "checkbox",
      description: "Cashier's check accepted for rent payment",
      order: 25,
      attribute: "payment_methods",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "payment_method_electronic",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "payment_method_electronic"
    }],
    display_attributes: {
      display_name: "Payment Method: Electronic",
      input_type: "checkbox",
      description: "Electronic payment accepted for rent",
      order: 26,
      attribute: "payment_methods",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "payment_method_money_order",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "payment_method_money_order"
    }],
    display_attributes: {
      display_name: "Payment Method: Money Order",
      input_type: "checkbox",
      description: "Money order accepted for rent payment",
      order: 27,
      attribute: "payment_methods",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "payment_method_personal_check",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "payment_method_personal_check"
    }],
    display_attributes: {
      display_name: "Payment Method: Personal Check",
      input_type: "checkbox",
      description: "Personal check accepted for rent payment",
      order: 28,
      attribute: "payment_methods",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "payment_method_other",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "payment_method_other"
    }],
    display_attributes: {
      display_name: "Payment Method: Other",
      input_type: "text",
      description: "Other accepted payment method",
      order: 29,
      attribute: "payment_methods",
      block: "financial_terms",
      placeholder: "Specify other payment method",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "prorated_rent_amount",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "prorated_rent_amount"
    }],
    display_attributes: {
      display_name: "Prorated Rent Amount",
      input_type: "text",
      description: "Prorated rent amount for partial month",
      order: 30,
      attribute: "financial_terms",
      block: "financial_terms",
      validation: {
        loopback: [{
          regex: "^[\\d.,$]+$",
          message: "Must be a valid monetary amount"
        }]
      },
      placeholder: "$500.00",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "prorated_rent_due_date",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "prorated_rent_due_date"
    }],
    display_attributes: {
      display_name: "Prorated Rent Due Date",
      input_type: "text",
      description: "Due date for prorated rent payment",
      order: 31,
      attribute: "financial_terms",
      block: "financial_terms",
      validation: {
        loopback: [{
          regex: "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
          message: "Must be a valid date (MM/DD/YYYY)"
        }]
      },
      placeholder: "MM/DD/YYYY",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "prorated_payment_method_cashier",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "prorated_payment_method_cashier"
    }],
    display_attributes: {
      display_name: "Prorated Payment Method: Cashier's Check",
      input_type: "checkbox",
      description: "Cashier's check accepted for prorated rent",
      order: 32,
      attribute: "payment_methods",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "prorated_payment_method_electronic",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "prorated_payment_method_electronic"
    }],
    display_attributes: {
      display_name: "Prorated Payment Method: Electronic",
      input_type: "checkbox",
      description: "Electronic payment accepted for prorated rent",
      order: 33,
      attribute: "payment_methods",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "prorated_payment_method_money_order",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "prorated_payment_method_money_order"
    }],
    display_attributes: {
      display_name: "Prorated Payment Method: Money Order",
      input_type: "checkbox",
      description: "Money order accepted for prorated rent",
      order: 34,
      attribute: "payment_methods",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "prorated_payment_method_personal_check",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "prorated_payment_method_personal_check"
    }],
    display_attributes: {
      display_name: "Prorated Payment Method: Personal Check",
      input_type: "checkbox",
      description: "Personal check accepted for prorated rent",
      order: 35,
      attribute: "payment_methods",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "prorated_payment_method_other",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "prorated_payment_method_other"
    }],
    display_attributes: {
      display_name: "Prorated Payment Method: Other",
      input_type: "text",
      description: "Other accepted payment method for prorated rent",
      order: 36,
      attribute: "payment_methods",
      block: "financial_terms",
      placeholder: "Specify other payment method",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "payment_recipient_name",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "payment_recipient_name"
    }],
    display_attributes: {
      display_name: "Payment Recipient Name",
      input_type: "text",
      description: "Name of person/entity to receive rent payments",
      order: 37,
      attribute: "payment_info",
      block: "financial_terms",
      placeholder: "John Doe",
      width: 6,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "payment_address",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "payment_address",
      linked_form_fields_text: ["payment_address_continued"]
    }],
    display_attributes: {
      display_name: "Payment Address",
      input_type: "text-area",
      description: "Address where rent payments should be sent",
      order: 38,
      attribute: "payment_info",
      block: "financial_terms",
      placeholder: "123 Payment Street, City, State 12345",
      width: 8,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "accepted_payment_cashier",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "accepted_payment_cashier"
    }],
    display_attributes: {
      display_name: "Accepted Payment: Cashier's Check",
      input_type: "checkbox",
      description: "Cashier's check is an accepted payment method",
      order: 39,
      attribute: "accepted_payments",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "accepted_payment_electronic",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "accepted_payment_electronic"
    }],
    display_attributes: {
      display_name: "Accepted Payment: Electronic",
      input_type: "checkbox",
      description: "Electronic payment is accepted",
      order: 40,
      attribute: "accepted_payments",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "accepted_payment_money_order",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "accepted_payment_money_order"
    }],
    display_attributes: {
      display_name: "Accepted Payment: Money Order",
      input_type: "checkbox",
      description: "Money order is an accepted payment method",
      order: 41,
      attribute: "accepted_payments",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "accepted_payment_personal_check",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "accepted_payment_personal_check"
    }],
    display_attributes: {
      display_name: "Accepted Payment: Personal Check",
      input_type: "checkbox",
      description: "Personal check is an accepted payment method",
      order: 42,
      attribute: "accepted_payments",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "accepted_payment_other",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "accepted_payment_other"
    }],
    display_attributes: {
      display_name: "Accepted Payment: Other",
      input_type: "text",
      description: "Other accepted payment method",
      order: 43,
      attribute: "accepted_payments",
      block: "financial_terms",
      placeholder: "Specify other payment method",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "payment_fee_option",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "payment_fee_option"
    }],
    display_attributes: {
      display_name: "Payment Fee Option",
      input_type: "text",
      description: "Payment fee option details",
      order: 44,
      attribute: "fees",
      block: "financial_terms",
      placeholder: "Fee details",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "payment_fee_restriction",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "payment_fee_restriction"
    }],
    display_attributes: {
      display_name: "Payment Fee Restriction",
      input_type: "text",
      description: "Payment fee restriction details",
      order: 45,
      attribute: "fees",
      block: "financial_terms",
      placeholder: "Fee restriction details",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "fee_payment_cashier",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "fee_payment_cashier"
    }],
    display_attributes: {
      display_name: "Fee Payment: Cashier's Check",
      input_type: "checkbox",
      description: "Cashier's check accepted for fee payments",
      order: 46,
      attribute: "fee_payment_methods",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "fee_payment_electronic",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "fee_payment_electronic"
    }],
    display_attributes: {
      display_name: "Fee Payment: Electronic",
      input_type: "checkbox",
      description: "Electronic payment accepted for fees",
      order: 47,
      attribute: "fee_payment_methods",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "fee_payment_money_order",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "fee_payment_money_order"
    }],
    display_attributes: {
      display_name: "Fee Payment: Money Order",
      input_type: "checkbox",
      description: "Money order accepted for fee payments",
      order: 48,
      attribute: "fee_payment_methods",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "fee_payment_personal_check",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "fee_payment_personal_check"
    }],
    display_attributes: {
      display_name: "Fee Payment: Personal Check",
      input_type: "checkbox",
      description: "Personal check accepted for fee payments",
      order: 49,
      attribute: "fee_payment_methods",
      block: "financial_terms",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "fee_payment_other",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "fee_payment_other"
    }],
    display_attributes: {
      display_name: "Fee Payment: Other",
      input_type: "text",
      description: "Other accepted payment method for fees",
      order: 50,
      attribute: "fee_payment_methods",
      block: "financial_terms",
      placeholder: "Specify other payment method",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "single_payment_required",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "single_payment_required"
    }],
    display_attributes: {
      display_name: "Single Payment Required",
      input_type: "checkbox",
      description: "Single payment is required",
      order: 51,
      attribute: "payment_requirements",
      block: "financial_terms",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "single_payment_not_required",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "single_payment_not_required"
    }],
    display_attributes: {
      display_name: "Single Payment Not Required",
      input_type: "checkbox",
      description: "Single payment is not required",
      order: 52,
      attribute: "payment_requirements",
      block: "financial_terms",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "late_charge_day",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "late_charge_day"
    }],
    display_attributes: {
      display_name: "Late Charge Day",
      input_type: "text",
      description: "Day of month when late charges apply",
      order: 53,
      attribute: "late_fees",
      block: "fees_charges",
      block_style: {
        title: "Fees & Charges",
        description: "Late fees, deposits, and other charges",
        icon: "alert-circle",
        color_theme: "orange"
      },
      placeholder: "5",
      width: 4,
      value: {
        type: "manual"
      },
      breakBefore: true
    }
  },
  {
    unique_id: "late_charge_amount_a",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "late_charge_amount_a"
    }],
    display_attributes: {
      display_name: "Late Charge Amount A",
      input_type: "text",
      description: "Primary late charge amount",
      order: 54,
      attribute: "late_fees",
      block: "fees_charges",
      validation: {
        loopback: [{
          regex: "^[\\d.,$]+$",
          message: "Must be a valid monetary amount"
        }]
      },
      placeholder: "$50.00",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "late_charge_amount_b",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "late_charge_amount_b"
    }],
    display_attributes: {
      display_name: "Late Charge Amount B",
      input_type: "text",
      description: "Secondary late charge amount",
      order: 55,
      attribute: "late_fees",
      block: "fees_charges",
      validation: {
        loopback: [{
          regex: "^[\\d.,$]+$",
          message: "Must be a valid monetary amount"
        }]
      },
      placeholder: "$25.00",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "additional_late_charge_amount",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "additional_late_charge_amount"
    }],
    display_attributes: {
      display_name: "Additional Late Charge Amount",
      input_type: "text",
      description: "Additional late charge amount",
      order: 56,
      attribute: "late_fees",
      block: "fees_charges",
      validation: {
        loopback: [{
          regex: "^[\\d.,$]+$",
          message: "Must be a valid monetary amount"
        }]
      },
      placeholder: "$10.00",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "returned_payment_fee",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "returned_payment_fee"
    }],
    display_attributes: {
      display_name: "Returned Payment Fee",
      input_type: "text",
      description: "Fee for returned payments",
      order: 57,
      attribute: "fees",
      block: "fees_charges",
      validation: {
        loopback: [{
          regex: "^[\\d.,$]+$",
          message: "Must be a valid monetary amount"
        }]
      },
      placeholder: "$35.00",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "animal_violation_fee_initial_amount",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "animal_violation_fee_initial_amount"
    }],
    display_attributes: {
      display_name: "Animal Violation Fee (Initial)",
      input_type: "text",
      description: "Initial fee for animal policy violations",
      order: 58,
      attribute: "violation_fees",
      block: "fees_charges",
      validation: {
        loopback: [{
          regex: "^[\\d.,$]+$",
          message: "Must be a valid monetary amount"
        }]
      },
      placeholder: "$200.00",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "animal_violation_fee_additional_daily_amount",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "animal_violation_fee_additional_daily_amount"
    }],
    display_attributes: {
      display_name: "Animal Violation Fee (Daily)",
      input_type: "text",
      description: "Daily fee for ongoing animal policy violations",
      order: 59,
      attribute: "violation_fees",
      block: "fees_charges",
      validation: {
        loopback: [{
          regex: "^[\\d.,$]+$",
          message: "Must be a valid monetary amount"
        }]
      },
      placeholder: "$25.00",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "security_deposit_amount",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "security_deposit_amount"
    }],
    display_attributes: {
      display_name: "Security Deposit Amount",
      input_type: "text",
      description: "Security deposit amount",
      order: 60,
      attribute: "deposits",
      block: "fees_charges",
      validation: {
        loopback: [{
          regex: "^[\\d.,$]+$",
          message: "Must be a valid monetary amount"
        }]
      },
      placeholder: "$2,500.00",
      width: 4,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "security_deposit_method_cashier",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "security_deposit_method_cashier"
    }],
    display_attributes: {
      display_name: "Security Deposit Method: Cashier's Check",
      input_type: "checkbox",
      description: "Cashier's check accepted for security deposit",
      order: 61,
      attribute: "deposit_methods",
      block: "fees_charges",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "security_deposit_method_electronic",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "security_deposit_method_electronic"
    }],
    display_attributes: {
      display_name: "Security Deposit Method: Electronic",
      input_type: "checkbox",
      description: "Electronic payment accepted for security deposit",
      order: 62,
      attribute: "deposit_methods",
      block: "fees_charges",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "security_deposit_method_money_order",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "security_deposit_method_money_order"
    }],
    display_attributes: {
      display_name: "Security Deposit Method: Money Order",
      input_type: "checkbox",
      description: "Money order accepted for security deposit",
      order: 63,
      attribute: "deposit_methods",
      block: "fees_charges",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "security_deposit_method_personal_check",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "security_deposit_method_personal_check"
    }],
    display_attributes: {
      display_name: "Security Deposit Method: Personal Check",
      input_type: "checkbox",
      description: "Personal check accepted for security deposit",
      order: 64,
      attribute: "deposit_methods",
      block: "fees_charges",
      width: 3,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "security_deposit_method_other",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "security_deposit_method_other"
    }],
    display_attributes: {
      display_name: "Security Deposit Method: Other",
      input_type: "text",
      description: "Other accepted method for security deposit",
      order: 65,
      attribute: "deposit_methods",
      block: "fees_charges",
      placeholder: "Specify other method",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "landlord_paid_utilities",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlord_paid_utilities",
      linked_form_fields_text: ["landlord_paid_utilities_cont", "landlord_paid_utilities_cont_2"]
    }],
    display_attributes: {
      display_name: "Landlord Paid Utilities",
      input_type: "text-area",
      description: "Utilities paid by landlord",
      order: 66,
      attribute: "utility_responsibilities",
      block: "property_terms",
      block_style: {
        title: "Property Terms",
        description: "Property-specific terms and conditions",
        icon: "settings",
        color_theme: "blue"
      },
      placeholder: "Electric, gas, water, trash, etc.",
      width: 12,
      value: {
        type: "manual"
      },
      breakBefore: true
    }
  },
  {
    unique_id: "authorized_occupants",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "authorized_occupants",
      linked_form_fields_text: ["authorized_occupants_cont", "authorized_occupants_cont_2"]
    }],
    display_attributes: {
      display_name: "Authorized Occupants",
      input_type: "text-area",
      description: "List of authorized occupants besides tenants",
      order: 67,
      attribute: "occupancy",
      block: "property_terms",
      placeholder: "Names of authorized occupants",
      width: 12,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "hoa_association_name",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "hoa_association_name",
      linked_form_fields_text: ["hoa_association_name_continued"]
    }],
    display_attributes: {
      display_name: "HOA Association Name",
      input_type: "text",
      description: "Name of homeowners association (if applicable)",
      order: 68,
      attribute: "hoa_info",
      block: "property_terms",
      placeholder: "ABC Homeowners Association",
      width: 8,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "additional_restrictions",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "additional_restrictions"
    }],
    display_attributes: {
      display_name: "Additional Restrictions",
      input_type: "text-area",
      description: "Additional property restrictions",
      order: 69,
      attribute: "restrictions",
      block: "property_terms",
      placeholder: "Additional restrictions or rules",
      width: 12,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "maximum_vehicles",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "maximum_vehicles"
    }],
    display_attributes: {
      display_name: "Maximum Vehicles",
      input_type: "text",
      description: "Maximum number of vehicles allowed",
      order: 70,
      attribute: "parking",
      block: "property_terms",
      placeholder: "2",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "tenant_trip_charge_amount",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_trip_charge_amount"
    }],
    display_attributes: {
      display_name: "Tenant Trip Charge Amount",
      input_type: "text",
      description: "Amount charged for tenant service trips",
      order: 71,
      attribute: "service_charges",
      block: "property_terms",
      validation: {
        loopback: [{
          regex: "^[\\d.,$]+$",
          message: "Must be a valid monetary amount"
        }]
      },
      placeholder: "$75.00",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "condition_exception_days",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "condition_exception_days"
    }],
    display_attributes: {
      display_name: "Condition Exception Days",
      input_type: "text",
      description: "Number of days for condition exceptions",
      order: 72,
      attribute: "property_condition",
      block: "property_terms",
      placeholder: "7",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "condition_change_fee",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "condition_change_fee"
    }],
    display_attributes: {
      display_name: "Condition Change Fee",
      input_type: "text",
      description: "Fee for property condition changes",
      order: 73,
      attribute: "property_condition",
      block: "property_terms",
      validation: {
        loopback: [{
          regex: "^[\\d.,$]+$",
          message: "Must be a valid monetary amount"
        }]
      },
      placeholder: "$100.00",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "tenant_conditions_for_landlord",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_conditions_for_landlord",
      linked_form_fields_text: ["tenant_conditions_for_landlord_continued"]
    }],
    display_attributes: {
      display_name: "Tenant Conditions for Landlord",
      input_type: "text-area",
      description: "Conditions tenant requests from landlord",
      order: 74,
      attribute: "tenant_conditions",
      block: "property_terms",
      placeholder: "Conditions or requests for landlord",
      width: 12,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "inventory_return_days",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "inventory_return_days"
    }],
    display_attributes: {
      display_name: "Inventory Return Days",
      input_type: "text",
      description: "Days to return property inventory",
      order: 75,
      attribute: "inventory",
      block: "property_terms",
      placeholder: "7",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "water_access_times",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "water_access_times",
      linked_form_fields_text: ["water_access_times_continued", "water_access_times_continued_2"]
    }],
    display_attributes: {
      display_name: "Water Access Times",
      input_type: "text-area",
      description: "Times when water access may be restricted",
      order: 76,
      attribute: "utilities",
      block: "property_terms",
      placeholder: "Water access schedule or restrictions",
      width: 12,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "other_contractor_name",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "other_contractor_name"
    }],
    display_attributes: {
      display_name: "Other Contractor Name",
      input_type: "text",
      description: "Name of other contractor for property",
      order: 77,
      attribute: "contractors",
      block: "property_terms",
      placeholder: "Contractor Name",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "property_manager_phone",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "property_manager_phone"
    }],
    display_attributes: {
      display_name: "Property Manager Phone",
      input_type: "text",
      description: "Property manager phone number",
      order: 78,
      attribute: "contact_info",
      block: "management_info",
      block_style: {
        title: "Management Information",
        description: "Property management and contact details",
        icon: "phone",
        color_theme: "purple"
      },
      validation: {
        loopback: [{
          regex: "^[-()\\s\\d]{10,}$",
          message: "Must be a valid phone number"
        }]
      },
      placeholder: "(555) 123-4567",
      width: 4,
      value: {
        type: "manual"
      },
      breakBefore: true
    }
  },
  {
    unique_id: "specific_maintenance_items",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "specific_maintenance_items",
      linked_form_fields_text: ["specific_maintenance_items_cont", "specific_maintenance_items_cont_2"]
    }],
    display_attributes: {
      display_name: "Specific Maintenance Items",
      input_type: "text-area",
      description: "Specific maintenance responsibilities or items",
      order: 79,
      attribute: "maintenance",
      block: "property_terms",
      placeholder: "List specific maintenance items or responsibilities",
      width: 12,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "tenant_assignment_fee_dollar_amount",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_assignment_fee_dollar_amount"
    }],
    display_attributes: {
      display_name: "Tenant Assignment Fee (Dollar Amount)",
      input_type: "text",
      description: "Dollar amount for tenant lease assignment fee",
      order: 80,
      attribute: "assignment_fees",
      block: "fees_charges",
      validation: {
        loopback: [{
          regex: "^[\\d.,$]+$",
          message: "Must be a valid monetary amount"
        }]
      },
      placeholder: "$500.00",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "landlord_assignment_fee_dollar_amount",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlord_assignment_fee_dollar_amount"
    }],
    display_attributes: {
      display_name: "Landlord Assignment Fee (Dollar Amount)",
      input_type: "text",
      description: "Dollar amount for landlord lease assignment fee",
      order: 81,
      attribute: "assignment_fees",
      block: "fees_charges",
      validation: {
        loopback: [{
          regex: "^[\\d.,$]+$",
          message: "Must be a valid monetary amount"
        }]
      },
      placeholder: "$300.00",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "tenant_assignment_fee_percentage_amount",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_assignment_fee_percentage_amount"
    }],
    display_attributes: {
      display_name: "Tenant Assignment Fee (Percentage)",
      input_type: "text",
      description: "Percentage amount for tenant lease assignment fee",
      order: 82,
      attribute: "assignment_fees",
      block: "fees_charges",
      validation: {
        loopback: [{
          regex: "^[\\d.]+%?$",
          message: "Must be a valid percentage"
        }]
      },
      placeholder: "10%",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "landlord_assignment_fee_percentage_amount",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlord_assignment_fee_percentage_amount"
    }],
    display_attributes: {
      display_name: "Landlord Assignment Fee (Percentage)",
      input_type: "text",
      description: "Percentage amount for landlord lease assignment fee",
      order: 83,
      attribute: "assignment_fees",
      block: "fees_charges",
      validation: {
        loopback: [{
          regex: "^[\\d.]+%?$",
          message: "Must be a valid percentage"
        }]
      },
      placeholder: "5%",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "addendum_flood_disclosure",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "addendum_flood_disclosure"
    }],
    display_attributes: {
      display_name: "Addendum: Flood Disclosure",
      input_type: "checkbox",
      description: "Flood disclosure addendum included",
      order: 84,
      attribute: "addenda",
      block: "addenda",
      block_style: {
        title: "Addenda",
        description: "Additional forms and disclosures",
        icon: "file-plus",
        color_theme: "gray"
      },
      width: 6,
      value: {
        type: "manual"
      },
      breakBefore: true
    }
  },
  {
    unique_id: "addendum_lead_paint",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "addendum_lead_paint"
    }],
    display_attributes: {
      display_name: "Addendum: Lead Paint",
      input_type: "checkbox",
      description: "Lead paint disclosure addendum included",
      order: 85,
      attribute: "addenda",
      block: "addenda",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "addendum_inventory_condition",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "addendum_inventory_condition"
    }],
    display_attributes: {
      display_name: "Addendum: Inventory Condition",
      input_type: "checkbox",
      description: "Inventory condition addendum included",
      order: 86,
      attribute: "addenda",
      block: "addenda",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "addendum_parking_rules",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "addendum_parking_rules"
    }],
    display_attributes: {
      display_name: "Addendum: Parking Rules",
      input_type: "checkbox",
      description: "Parking rules addendum included",
      order: 87,
      attribute: "addenda",
      block: "addenda",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "addendum_animal_agreement",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "addendum_animal_agreement"
    }],
    display_attributes: {
      display_name: "Addendum: Animal Agreement",
      input_type: "checkbox",
      description: "Animal agreement addendum included",
      order: 88,
      attribute: "addenda",
      block: "addenda",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "addendum_mold_remediation",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "addendum_mold_remediation"
    }],
    display_attributes: {
      display_name: "Addendum: Mold Remediation",
      input_type: "checkbox",
      description: "Mold remediation addendum included",
      order: 89,
      attribute: "addenda",
      block: "addenda",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "addendum_lease_guaranty",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "addendum_lease_guaranty"
    }],
    display_attributes: {
      display_name: "Addendum: Lease Guaranty",
      input_type: "checkbox",
      description: "Lease guaranty addendum included",
      order: 90,
      attribute: "addenda",
      block: "addenda",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "addendum_broker_agreement",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "addendum_broker_agreement"
    }],
    display_attributes: {
      display_name: "Addendum: Broker Agreement",
      input_type: "checkbox",
      description: "Broker agreement addendum included",
      order: 91,
      attribute: "addenda",
      block: "addenda",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "addendum_landlord_rules",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "addendum_landlord_rules"
    }],
    display_attributes: {
      display_name: "Addendum: Landlord Rules",
      input_type: "checkbox",
      description: "Landlord rules addendum included",
      order: 92,
      attribute: "addenda",
      block: "addenda",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "addendum_hoa_rules",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "addendum_hoa_rules"
    }],
    display_attributes: {
      display_name: "Addendum: HOA Rules",
      input_type: "checkbox",
      description: "HOA rules addendum included",
      order: 93,
      attribute: "addenda",
      block: "addenda",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "addendum_pool_spa",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "addendum_pool_spa"
    }],
    display_attributes: {
      display_name: "Addendum: Pool/Spa",
      input_type: "checkbox",
      description: "Pool/spa addendum included",
      order: 94,
      attribute: "addenda",
      block: "addenda",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "addendum_lease_application",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "addendum_lease_application"
    }],
    display_attributes: {
      display_name: "Addendum: Lease Application",
      input_type: "checkbox",
      description: "Lease application addendum included",
      order: 95,
      attribute: "addenda",
      block: "addenda",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "addendum_bed_bug",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "addendum_bed_bug"
    }],
    display_attributes: {
      display_name: "Addendum: Bed Bug",
      input_type: "checkbox",
      description: "Bed bug addendum included",
      order: 96,
      attribute: "addenda",
      block: "addenda",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "other_addenda",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "other_addenda"
    }],
    display_attributes: {
      display_name: "Other Addenda 1",
      input_type: "text",
      description: "Other addendum name or description",
      order: 97,
      attribute: "addenda",
      block: "addenda",
      placeholder: "Specify other addendum",
      width: 8,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "other_addenda2",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "other_addenda2"
    }],
    display_attributes: {
      display_name: "Other Addenda 2",
      input_type: "text",
      description: "Second other addendum name or description",
      order: 98,
      attribute: "addenda",
      block: "addenda",
      placeholder: "Specify other addendum",
      width: 8,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "other_addenda3",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "other_addenda3"
    }],
    display_attributes: {
      display_name: "Other Addenda 3",
      input_type: "text",
      description: "Third other addendum name or description",
      order: 99,
      attribute: "addenda",
      block: "addenda",
      placeholder: "Specify other addendum",
      width: 8,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "other_addenda_checkbox",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "other_addenda_checkbox"
    }],
    display_attributes: {
      display_name: "Other Addenda 1 Checkbox",
      input_type: "checkbox",
      description: "Check if first other addendum is included",
      order: 100,
      attribute: "addenda",
      block: "addenda",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "other_addenda2_checkbox",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "other_addenda2_checkbox"
    }],
    display_attributes: {
      display_name: "Other Addenda 2 Checkbox",
      input_type: "checkbox",
      description: "Check if second other addendum is included",
      order: 101,
      attribute: "addenda",
      block: "addenda",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "other_addenda3_checkbox",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "other_addenda3_checkbox"
    }],
    display_attributes: {
      display_name: "Other Addenda 3 Checkbox",
      input_type: "checkbox",
      description: "Check if third other addendum is included",
      order: 102,
      attribute: "addenda",
      block: "addenda",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "tenant_notice_address",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_notice_address_1"
    }, {
      formType: "residential_lease",
      formfield: "tenant_notice_address_2"
    }, {
      formType: "residential_lease",
      formfield: "tenant_notice_address_3"
    }],
    display_attributes: {
      display_name: "Tenant Notice Address",
      input_type: "text-area",
      description: "Address for tenant notices",
      order: 103,
      attribute: "contact_info",
      block: "contact_information",
      block_style: {
        title: "Contact Information",
        description: "Notice addresses and contact details",
        icon: "mail",
        color_theme: "blue"
      },
      placeholder: "123 Main Street\nCity, State 12345",
      width: 6,
      value: {
        type: "manual"
      },
      isRequired: true,
      breakBefore: true
    }
  },
  {
    unique_id: "landlord_notice_address",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlord_notice_address_1"
    }, {
      formType: "residential_lease",
      formfield: "landlord_notice_address_2"
    }, {
      formType: "residential_lease",
      formfield: "landlord_notice_address_3"
    }],
    display_attributes: {
      display_name: "Landlord Notice Address",
      input_type: "text-area",
      description: "Address for landlord notices",
      order: 104,
      attribute: "contact_info",
      block: "contact_information",
      placeholder: "123 Main Street\nCity, State 12345",
      width: 6,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "tenant_email",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_email"
    }],
    display_attributes: {
      display_name: "Tenant Email",
      input_type: "text",
      description: "Tenant email address",
      order: 105,
      attribute: "contact_info",
      block: "contact_information",
      validation: {
        loopback: [{
          regex: "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$",
          message: "Must be a valid email address"
        }]
      },
      placeholder: "tenant@email.com",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "landlord_email",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlord_email"
    }],
    display_attributes: {
      display_name: "Landlord Email",
      input_type: "text",
      description: "Landlord email address",
      order: 106,
      attribute: "contact_info",
      block: "contact_information",
      validation: {
        loopback: [{
          regex: "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$",
          message: "Must be a valid email address"
        }]
      },
      placeholder: "landlord@email.com",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "tenant_fax",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_fax"
    }],
    display_attributes: {
      display_name: "Tenant Fax",
      input_type: "text",
      description: "Tenant fax number",
      order: 107,
      attribute: "contact_info",
      block: "contact_information",
      validation: {
        loopback: [{
          regex: "^[-()\\s\\d]{10,}$",
          message: "Must be a valid fax number"
        }]
      },
      placeholder: "(555) 123-4567",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "landlord_fax",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlord_fax"
    }],
    display_attributes: {
      display_name: "Landlord Fax",
      input_type: "text",
      description: "Landlord fax number",
      order: 108,
      attribute: "contact_info",
      block: "contact_information",
      validation: {
        loopback: [{
          regex: "^[-()\\s\\d]{10,}$",
          message: "Must be a valid fax number"
        }]
      },
      placeholder: "(555) 123-4567",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "broker_name",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "broker_name"
    }],
    display_attributes: {
      display_name: "Broker Name",
      input_type: "text",
      description: "Name of the broker",
      order: 109,
      attribute: "broker_info",
      block: "broker_information",
      block_style: {
        title: "Broker Information",
        description: "Real estate broker details",
        icon: "briefcase",
        color_theme: "purple"
      },
      placeholder: "Jane Smith",
      width: 6,
      value: {
        type: "manual"
      },
      isCached: true,
      breakBefore: true
    }
  },
  {
    unique_id: "broker_phone",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "broker_phone"
    }],
    display_attributes: {
      display_name: "Broker Phone",
      input_type: "text",
      description: "Broker phone number",
      order: 110,
      attribute: "broker_info",
      block: "broker_information",
      validation: {
        loopback: [{
          regex: "^[-()\\s\\d]{10,}$",
          message: "Must be a valid phone number"
        }]
      },
      placeholder: "(555) 123-4567",
      width: 4,
      value: {
        type: "manual"
      },
      isCached: true
    }
  },
  {
    unique_id: "broker_address",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "broker_address"
    }],
    display_attributes: {
      display_name: "Broker Address",
      input_type: "text",
      description: "Broker address",
      order: 111,
      attribute: "broker_info",
      block: "broker_information",
      placeholder: "123 Business Street, City, State 12345",
      width: 8,
      value: {
        type: "manual"
      },
      isCached: true
    }
  },
  {
    unique_id: "broker_email",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "broker_email"
    }],
    display_attributes: {
      display_name: "Broker Email",
      input_type: "text",
      description: "Broker email address",
      order: 112,
      attribute: "broker_info",
      block: "broker_information",
      validation: {
        loopback: [{
          regex: "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$",
          message: "Must be a valid email address"
        }]
      },
      placeholder: "broker@company.com",
      width: 6,
      value: {
        type: "manual"
      },
      isCached: true
    }
  },
  {
    unique_id: "insurance_recommendation",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "insurance_recommendation"
    }],
    display_attributes: {
      display_name: "Insurance Recommendation",
      input_type: "text-area",
      description: "Insurance recommendation details",
      order: 113,
      attribute: "insurance",
      block: "broker_information",
      placeholder: "Insurance recommendations",
      width: 12,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "landlords_broker_name",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlords_broker_name"
    }],
    display_attributes: {
      display_name: "Landlord's Broker Name",
      input_type: "text",
      description: "Name of landlord's broker",
      order: 114,
      attribute: "landlord_broker_info",
      block: "broker_information",
      placeholder: "John Broker",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "property_manager_name",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "property_manager_name"
    }],
    display_attributes: {
      display_name: "Property Manager Name",
      input_type: "text",
      description: "Name of property manager",
      order: 115,
      attribute: "property_manager_info",
      block: "management_info",
      placeholder: "Mary Manager",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "property_manager_phone_number",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "property_manager_phone_number"
    }],
    display_attributes: {
      display_name: "Property Manager Phone Number",
      input_type: "text",
      description: "Property manager phone number",
      order: 116,
      attribute: "property_manager_info",
      block: "management_info",
      validation: {
        loopback: [{
          regex: "^[-()\\s\\d]{10,}$",
          message: "Must be a valid phone number"
        }]
      },
      placeholder: "(555) 123-4567",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "property_manager_email",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "property_manager_email"
    }],
    display_attributes: {
      display_name: "Property Manager Email",
      input_type: "text",
      description: "Property manager email address",
      order: 117,
      attribute: "property_manager_info",
      block: "management_info",
      validation: {
        loopback: [{
          regex: "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$",
          message: "Must be a valid email address"
        }]
      },
      placeholder: "manager@company.com",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "property_manager_address",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "property_manager_address"
    }],
    display_attributes: {
      display_name: "Property Manager Address",
      input_type: "text",
      description: "Property manager address",
      order: 118,
      attribute: "property_manager_info",
      block: "management_info",
      placeholder: "123 Management Street, City, State 12345",
      width: 8,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "landlord_signature",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlord_signature_1",
      linked_dates: [{ dateFieldName: "landlord_signature_date_1" }]
    }, {
      formType: "residential_lease",
      formfield: "landlord_signature_2",
      linked_dates: [{ dateFieldName: "landlord_signature_date_2" }]
    }],
    display_attributes: {
      display_name: "Landlord Signature",
      input_type: "signature",
      description: "Landlord signature(s)",
      order: 119,
      attribute: "landlord_signature",
      block: "signatures",
      width: 6,
      value: {
        type: "manual"
      },
      isRequired: true,
      breakBefore: true
    }
  },
  {
    unique_id: "broker_associate_printed_name",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "broker_associate_printed_name"
    }],
    display_attributes: {
      display_name: "Broker Associate Printed Name",
      input_type: "text",
      description: "Printed name of broker associate",
      order: 120,
      attribute: "broker_signature",
      block: "signatures",
      placeholder: "Associate Name",
      width: 6,
      value: {
        type: "manual"
      },
      isCached: true
    }
  },
  {
    unique_id: "broker_associate_date",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "broker_associate_date"
    }],
    display_attributes: {
      display_name: "Broker Associate Date",
      input_type: "text",
      description: "Date for broker associate signature",
      order: 121,
      attribute: "broker_signature",
      block: "signatures",
      validation: {
        loopback: [{
          regex: "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
          message: "Must be a valid date (MM/DD/YYYY)"
        }]
      },
      placeholder: "MM/DD/YYYY",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "broker_printed_name",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "broker_printed_name"
    }],
    display_attributes: {
      display_name: "Broker Printed Name",
      input_type: "text",
      description: "Printed name of broker",
      order: 122,
      attribute: "broker_signature",
      block: "signatures",
      placeholder: "Broker Name",
      width: 6,
      value: {
        type: "manual"
      },
      isCached: true
    }
  },
  {
    unique_id: "broker_license_number",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "broker_license_number"
    }],
    display_attributes: {
      display_name: "Broker License Number",
      input_type: "text",
      description: "Broker license number",
      order: 123,
      attribute: "broker_license",
      block: "signatures",
      placeholder: "RE123456",
      width: 4,
      value: {
        type: "manual"
      },
      isCached: true
    }
  },
  {
    unique_id: "broker_firm_name",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "broker_firm_name"
    }],
    display_attributes: {
      display_name: "Broker Firm Name",
      input_type: "text",
      description: "Name of broker's firm",
      order: 124,
      attribute: "broker_firm",
      block: "signatures",
      placeholder: "ABC Realty",
      width: 6,
      value: {
        type: "manual"
      },
      isCached: true
    }
  },
  {
    unique_id: "tenant_signature",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_signature_1",
      linked_dates: [{ dateFieldName: "tenant_signature_date_1" }]
    }, {
      formType: "residential_lease",
      formfield: "tenant_signature_2",
      linked_dates: [{ dateFieldName: "tenant_signature_date_2" }]
    }, {
      formType: "residential_lease",
      formfield: "tenant_signature_3",
      linked_dates: [{ dateFieldName: "tenant_signature_date_3" }]
    }, {
      formType: "residential_lease",
      formfield: "tenant_signature_4",
      linked_dates: [{ dateFieldName: "tenant_signature_date_4" }]
    }],
    display_attributes: {
      display_name: "Tenant Signature",
      input_type: "signature",
      description: "Tenant signature(s)",
      order: 125,
      attribute: "tenant_signature",
      block: "signatures",
      width: 6,
      value: {
        type: "manual"
      },
      isRequired: true
    }
  },
  {
    unique_id: "lease_provided_date",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "lease_provided_date"
    }],
    display_attributes: {
      display_name: "Lease Provided Date",
      input_type: "text",
      description: "Date lease was provided",
      order: 126,
      attribute: "lease_provision",
      block: "signatures",
      validation: {
        loopback: [{
          regex: "^(0?[1-9]|1[0-2])[/](0?[1-9]|[12]\\d|3[01])[/]\\d{4}$",
          message: "Must be a valid date (MM/DD/YYYY)"
        }]
      },
      placeholder: "MM/DD/YYYY",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "lease_provision_note",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "lease_provision_note"
    }],
    display_attributes: {
      display_name: "Lease Provision Note",
      input_type: "text-area",
      description: "Note about lease provision",
      order: 127,
      attribute: "lease_provision",
      block: "signatures",
      placeholder: "Additional notes about lease provision",
      width: 12,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "monthly_rent_due_date",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "monthly_rent_due_date",
      linked_form_fields_radio: [
        { radioField: "rent_due_on_first_of_each_month", displayName: "First Day of Each Month" },
        { radioField: "Choice1", displayName: "Other Date" }
      ]
    }],
    display_attributes: {
      display_name: "Monthly Rent Due Date",
      input_type: "radio",
      description: "Monthly rent due date",
      order: 128,
      attribute: "rent_schedule",
      block: "lease_terms",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "renewal_notice_termination_date",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "renewal_notice_termination_date",
      linked_form_fields_radio: [
        { radioField: "renewal_notice_on_date_assigned", displayName: "On Date Assigned" },
        { radioField: "renewal_notice_on_last_day_of_month", displayName: "Last Day of Month" }
      ]
    }],
    display_attributes: {
      display_name: "Renewal Notice Termination Date",
      input_type: "radio",
      description: "Date for renewal notice termination",
      order: 129,
      attribute: "renewal_terms",
      block: "lease_terms",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "late_charge_fee",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "late_charge_fee",
      linked_form_fields_radio: [
        { radioField: "late_charge_fee_by_dollar_amount", displayName: "Dollar Amount" },
        { radioField: "late_charge_fee_by_percentage_amount", displayName: "Percentage Amount" }
      ]
    }],
    display_attributes: {
      display_name: "Late Charge Fee",
      input_type: "radio",
      description: "Late charge fee amount",
      order: 130,
      attribute: "late_fees",
      block: "fees_charges",
      width: 4,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "does_property_have_hoa",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "does_property_have_hoa",
      linked_form_fields_radio: [
        { radioField: "property_does_not_have_hoa", displayName: "No HOA" },
        { radioField: "property_does_have_hoa", displayName: "Has HOA" }
      ]
    }],
    display_attributes: {
      display_name: "Does Property Have HOA",
      input_type: "radio",
      description: "Does the property have a homeowners association",
      order: 131,
      attribute: "hoa_info",
      block: "property_terms",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "lawn_maintenance_responsibility",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "lawn_maintenance_responsibility",
      linked_form_fields_radio: [
        { radioField: "landlord_maintains_lawn", displayName: "Landlord Maintains" },
        { radioField: "tenant_maintains_lawn_with_contract", displayName: "Tenant Maintains with Contract" },
        { radioField: "tenant_maintains_lawn_at_tenants_expense", displayName: "Tenant Maintains at Own Expense" }
      ]
    }],
    display_attributes: {
      display_name: "Lawn Maintenance Responsibility",
      input_type: "radio",
      description: "Who is responsible for lawn maintenance",
      order: 132,
      attribute: "maintenance_responsibility",
      block: "property_terms",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "tenant_scheduled_lawn_contract",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_scheduled_lawn_contract",
      linked_form_fields_radio: [
        { radioField: "contractor_who_regularly_provides_service", displayName: "Regular Contractor" },
        { radioField: "other_contractor", displayName: "Other Contractor" }
      ]
    }],
    display_attributes: {
      display_name: "Tenant Scheduled Lawn Contract",
      input_type: "radio",
      description: "Tenant scheduled lawn maintenance contract",
      order: 133,
      attribute: "lawn_contract",
      block: "property_terms",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "smoking_rules",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "smoking_rules",
      linked_form_fields_radio: [
        { radioField: "smoking_is_not_allowed", displayName: "Smoking Not Allowed" },
        { radioField: "smoking_is_allowed", displayName: "Smoking Allowed" }
      ]
    }],
    display_attributes: {
      display_name: "Smoking Rules",
      input_type: "radio",
      description: "Property smoking rules and restrictions",
      order: 134,
      attribute: "property_rules",
      block: "property_terms",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "tenant_procures_assignee",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "tenant_procures_assignee",
      linked_form_fields_radio: [
        { radioField: "dollar_amount_tenant_pays_when_tenant_procures", displayName: "Dollar Amount" },
        { radioField: "percentage_of_rent_tenant_pays_when_tenant_procures", displayName: "Percentage of Rent" }
      ]
    }],
    display_attributes: {
      display_name: "Tenant Procures Assignee",
      input_type: "radio",
      description: "Tenant procures assignee option",
      order: 135,
      attribute: "assignment_options",
      block: "lease_terms",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "landlord_procures_assignee",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlord_procures_assignee",
      linked_form_fields_radio: [
        { radioField: "dollar_amount_tenant_pays_when_landlord_procures", displayName: "Dollar Amount" },
        { radioField: "percentage_of_rent_tenant_pays_when_landlord_procures", displayName: "Percentage of Rent" }
      ]
    }],
    display_attributes: {
      display_name: "Landlord Procures Assignee",
      input_type: "radio",
      description: "Landlord procures assignee option",
      order: 136,
      attribute: "assignment_options",
      block: "lease_terms",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "landlord_broker_role_with_property",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlord_broker_role_with_property",
      linked_form_fields_radio: [
        { radioField: "broker_is_property_manager", displayName: "Broker is Property Manager" },
        { radioField: "broker_is_not_property_manager", displayName: "Broker is Not Property Manager" }
      ]
    }],
    display_attributes: {
      display_name: "Landlord Broker Role with Property",
      input_type: "radio",
      description: "Landlord's broker role with the property",
      order: 137,
      attribute: "broker_role",
      block: "broker_information",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "who_manages_property",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "who_manages_property",
      linked_form_fields_radio: [
        { radioField: "landlord_manages_property", displayName: "Landlord Manages" },
        { radioField: "property_manager_selected_by_landlord_manages_property", displayName: "Property Manager Manages" }
      ]
    }],
    display_attributes: {
      display_name: "Who Manages Property",
      input_type: "radio",
      description: "Who manages the property",
      order: 138,
      attribute: "property_management",
      block: "management_info",
      width: 6,
      value: {
        type: "manual"
      }
    }
  },
  {
    unique_id: "landlord_lease_contact_method",
    pdf_attributes: [{
      formType: "residential_lease",
      formfield: "landlord_lease_contact_method",
      linked_form_fields_radio: [
        { radioField: "contact_via_fax", displayName: "Fax" },
        { radioField: "contact_via_email", displayName: "Email" },
        { radioField: "contact_via_mail", displayName: "Mail" },
        { radioField: "contact_via_in_person", displayName: "In Person" }
      ]
    }],
    display_attributes: {
      display_name: "Landlord Lease Contact Method",
      input_type: "radio",
      description: "Preferred method to contact landlord about lease",
      order: 139,
      attribute: "contact_preferences",
      block: "contact_information",
      width: 6,
      value: {
        type: "manual"
      }
    }
  }
];