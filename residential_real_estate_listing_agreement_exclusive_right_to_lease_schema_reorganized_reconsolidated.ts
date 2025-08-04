import { SchemaItem } from "../../../../types/realtor";


export const residentialRealEstateListingAgreementExclusiveRightToLeaseSchema: SchemaItem[] = [
  {
    "unique_id": "addendum_rental_flood_disclosure",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_50",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_50",
            "displayName": "Addendum Regarding Rental Flood Disclosure"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_26",
            "displayName": "Condominium Addendum to Listing"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_49",
            "displayName": "Addendum Regarding Lead-Based Paint"
          }
        ]
      }
    ],
    "display_attributes": {
      "unique_id": "addendum_rental_flood_disclosure",
      "display_name": "Addendum Regarding",
      "description": "Select if the addendum regarding rental flood disclosure is required.",
      "attribute": "addendum",
      "order": 1,
      "block": "Addenda and Other Documents",
      "block_style": {
        "title": "Addenda and Other Documents",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Required",
            "databaseStored": "REQUIRED",
            "linkedFields": []
          },
          {
            "display_name": "Include Condominium Addendum",
            "databaseStored": "INCLUDE_CONDOMINIUM_ADDENDUM",
            "linkedFields": []
          },
          {
            "display_name": "Lead-Based Paint Addendum Required",
            "databaseStored": "LEAD_BASED_PAINT_ADDENDUM_REQUIRED",
            "linkedFields": []
          }
        ]
      }
    }
  },
  {
    "unique_id": "brokerage_services_information",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_48"
      }
    ],
    "display_attributes": {
      "unique_id": "brokerage_services_information",
      "display_name": "Information About Brokerage Services",
      "description": "Select if you need to provide information about brokerage services.",
      "attribute": "brokerage_services",
      "order": 2,
      "block": "Addenda and Other Documents",
      "block_style": {
        "title": "Addenda and Other Documents",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Information About Brokerage Services",
            "databaseStored": "INFORMATION_ABOUT_BROKERAGE_SERVICES",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "keybox_authorization_by_tenant",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_27"
      }
    ],
    "display_attributes": {
      "unique_id": "keybox_authorization_by_tenant",
      "display_name": "Keybox Authorization by Tenant",
      "description": "Authorization for the use of a keybox by the tenant",
      "attribute": "authorization",
      "order": 3,
      "block": "Addenda and Other Documents",
      "block_style": {
        "title": "Addenda and Other Documents",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Authorized",
            "databaseStored": "AUTHORIZED",
            "linkedFields": []
          },
          {
            "display_name": "Not Authorized",
            "databaseStored": "NOT_AUTHORIZED",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "request_information_owners_association",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_24"
      }
    ],
    "display_attributes": {
      "unique_id": "request_information_owners_association",
      "display_name": "Request for Information from an Owners' Association",
      "description": "Select this option if you need to request information from the owners' association.",
      "attribute": "request_information",
      "order": 4,
      "block": "Addenda and Other Documents",
      "block_style": {
        "title": "Addenda and Other Documents",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Request Information",
            "databaseStored": "REQUEST_INFORMATION",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "special_flood_hazard_information",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_25"
      }
    ],
    "display_attributes": {
      "unique_id": "special_flood_hazard_information",
      "display_name": "Information about Special Flood Hazard Areas",
      "description": "Select if information regarding special flood hazard areas is required.",
      "attribute": "flood_hazard",
      "order": 5,
      "block": "Addenda and Other Documents",
      "block_style": {
        "title": "Addenda and Other Documents",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Required",
            "databaseStored": "REQUIRED",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "additional_late_charge_percentage",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_116"
      }
    ],
    "display_attributes": {
      "unique_id": "additional_late_charge_percentage",
      "display_name": "Additional Late Charge Percentage",
      "description": "Percentage of one month's rent for additional late charges",
      "attribute": "percentage",
      "order": 6,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter percentage",
      "validation": {
        "regex": "^(100|[1-9][0-9]?)$"
      },
      "special_input": {
        "text": {
          "percentage": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "animal_deposit_amount",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_119"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_120"
      }
    ],
    "display_attributes": {
      "unique_id": "animal_deposit_amount",
      "display_name": "Animal Deposit Amount",
      "description": "Amount required as a deposit for an animal in addition to the security deposit.",
      "attribute": "amount",
      "order": 7,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "animal_restrictions",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_117"
      }
    ],
    "display_attributes": {
      "unique_id": "animal_restrictions",
      "display_name": "Animal Restrictions",
      "description": "Specify any restrictions on permitted animals, including size, weight, number, and type.",
      "attribute": "text",
      "order": 8,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter restrictions here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "animal_violation_charge_initial",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_125"
      }
    ],
    "display_attributes": {
      "unique_id": "animal_violation_charge_initial",
      "display_name": "Animal Violation Charge (Initial)",
      "description": "Initial charge for animal violations, whether the animal is permitted or not.",
      "attribute": "amount",
      "order": 9,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^\\$?\\d+(\\.\\d{2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "animal_violation_charge_per_day",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_126"
      }
    ],
    "display_attributes": {
      "unique_id": "animal_violation_charge_per_day",
      "display_name": "Animal Violation Charge Per Day",
      "description": "Charge for each day an animal violation occurs",
      "attribute": "amount",
      "order": 10,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "animals_permitted",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_34"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_37"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_38"
      }
    ],
    "display_attributes": {
      "unique_id": "animals_permitted",
      "display_name": "Animals Permitted",
      "description": "Indicate whether animals are permitted or not, along with any restrictions.",
      "attribute": "animals",
      "order": 11,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Not Permitted",
            "databaseStored": "NOT_PERMITTED",
            "linkedFields": []
          },
          {
            "display_name": "Permitted",
            "databaseStored": "PERMITTED",
            "linkedFields": []
          }
        ],
        "minSelected": 1,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "animals_permitted_restrictions",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_118"
      }
    ],
    "display_attributes": {
      "unique_id": "animals_permitted_restrictions",
      "display_name": "Animals Permitted with Restrictions",
      "description": "Specify if animals are permitted and any restrictions (size, weight, number, type)",
      "attribute": "animals",
      "order": 12,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter restrictions here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "assignment_subletting_replacement_fees",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_45"
      }
    ],
    "display_attributes": {
      "unique_id": "assignment_subletting_replacement_fees",
      "display_name": "Assignment, Subletting and Replacement Tenant Fees",
      "description": "Select if fees are applicable for assignment, subletting, or replacement of tenants.",
      "attribute": "fees",
      "order": 13,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Fees Applicable",
            "databaseStored": "FEES_APPLICABLE",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "contractor_chosen_by_tenant",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_41"
      }
    ],
    "display_attributes": {
      "unique_id": "contractor_chosen_by_tenant",
      "display_name": "Contractor Chosen by Tenant",
      "description": "Select if a contractor chosen and paid by Tenant will maintain the property.",
      "attribute": "maintenance_option",
      "order": 14,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Contractor Chosen by Tenant",
            "databaseStored": "CONTRACTOR_CHOSEN_BY_TENANT",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "initial_late_charge",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_114"
      }
    ],
    "display_attributes": {
      "unique_id": "initial_late_charge",
      "display_name": "Initial Late Charge",
      "description": "Amount charged for the first late payment",
      "attribute": "amount",
      "order": 15,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "inventory_condition_form_delivery_days",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_138"
      }
    ],
    "display_attributes": {
      "unique_id": "inventory_condition_form_delivery_days",
      "display_name": "Inventory and Condition Form Delivery Days",
      "description": "Number of days to deliver the Inventory and Condition Form",
      "attribute": "days",
      "order": 16,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter number of days",
      "validation": "^[0-9]+$",
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "irs_forms_checkbox",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_29"
      }
    ],
    "display_attributes": {
      "unique_id": "irs_forms_checkbox",
      "display_name": "IRS Forms (W-9 or W-8)",
      "description": "Select if IRS forms are required for this listing agreement.",
      "attribute": "documents",
      "order": 17,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "IRS Forms Required",
            "databaseStored": "IRS_FORMS_REQUIRED",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "landlord_assistance_animals",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_31"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_assistance_animals",
      "display_name": "General Information for Landlord Regarding Assistance Animals",
      "description": "Select if the landlord requires information regarding assistance animals.",
      "attribute": "assistance_animals",
      "order": 18,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Requires Information",
            "databaseStored": "REQUIRES_INFORMATION",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "landlord_assistance_animals_info",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_111"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_assistance_animals_info",
      "display_name": "General Information for Landlord Regarding Assistance Animals",
      "description": "Provide details regarding assistance animals as per landlord's requirements.",
      "attribute": "text",
      "order": 19,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter information regarding assistance animals",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "late_charge_day",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_113"
      }
    ],
    "display_attributes": {
      "unique_id": "late_charge_day",
      "display_name": "Late Charge Day",
      "description": "The day after the date on which rent is due when late charges are incurred.",
      "attribute": "date",
      "order": 20,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter day",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "late_charge_initial",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_35"
      }
    ],
    "display_attributes": {
      "unique_id": "late_charge_initial",
      "display_name": "Initial Late Charge",
      "description": "Select if there is an initial late charge for overdue rent",
      "attribute": "late_charge",
      "order": 21,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Yes",
            "databaseStored": "YES",
            "linkedFields": []
          },
          {
            "display_name": "No",
            "databaseStored": "NO",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "lease_requirements_first_day_of_month",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_33"
      }
    ],
    "display_attributes": {
      "unique_id": "lease_requirements_first_day_of_month",
      "display_name": "First Day of the Month",
      "description": "Select if the monthly rent is due on the first day of the month.",
      "attribute": "rent_due_date",
      "order": 22,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Due on the First Day",
            "databaseStored": "DUE_ON_FIRST_DAY",
            "linkedFields": []
          }
        ],
        "minSelected": 1,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "lease_requirements_landlord",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_32"
      }
    ],
    "display_attributes": {
      "unique_id": "lease_requirements_landlord",
      "display_name": "Lease Requirements by Landlord",
      "description": "Select if the landlord has specific lease requirements.",
      "attribute": "lease_requirements",
      "order": 23,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Monthly Rent",
            "databaseStored": "MONTHLY_RENT",
            "linkedFields": [
              "monthly_rent_due_date"
            ]
          },
          {
            "display_name": "Late Charges",
            "databaseStored": "LATE_CHARGES",
            "linkedFields": [
              "late_charge_time"
            ]
          }
        ],
        "minSelected": 0,
        "maxSelected": 2
      }
    }
  },
  {
    "unique_id": "monthly_rent_due_date",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_112"
      }
    ],
    "display_attributes": {
      "unique_id": "monthly_rent_due_date",
      "display_name": "Monthly Rent Due Date",
      "description": "Specify the date on which the monthly rent is due.",
      "attribute": "date",
      "order": 24,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "e.g., 1st",
      "validation": null,
      "special_input": {
        "text": {
          "date": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "on_site_sewer_facility_info",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_28"
      }
    ],
    "display_attributes": {
      "unique_id": "on_site_sewer_facility_info",
      "display_name": "Information About On-Site Sewer Facility",
      "description": "Select if the property has an on-site sewer facility that needs to be disclosed.",
      "attribute": "property_info",
      "order": 25,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Yes, there is an on-site sewer facility",
            "databaseStored": "ON_SITE_SEWER_FACILITY_YES",
            "linkedFields": []
          },
          {
            "display_name": "No, there is no on-site sewer facility",
            "databaseStored": "ON_SITE_SEWER_FACILITY_NO",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "owners_authorization_unsecured_access",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_30"
      }
    ],
    "display_attributes": {
      "unique_id": "owners_authorization_unsecured_access",
      "display_name": "Owner's Authorization Concerning Unsecured Access to Property",
      "description": "Authorization for allowing access to the property without prior notice.",
      "attribute": "authorization",
      "order": 26,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Authorize Unsecured Access",
            "databaseStored": "AUTHORIZE_UNSECURED_ACCESS",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "pool_spa_maintenance",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_142"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_143"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_144"
      }
    ],
    "display_attributes": {
      "unique_id": "pool_spa_maintenance",
      "display_name": "Pool/Spa Maintenance",
      "description": "Specify who will maintain the pool or spa.",
      "attribute": "maintenance",
      "order": 27,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 9,
      "placeholder": "Enter name or contractor",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "residential_lease_listing_advisory",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_161"
      }
    ],
    "display_attributes": {
      "unique_id": "residential_lease_listing_advisory",
      "display_name": "Residential Lease Listing Advisory",
      "description": "Advisory notes for landlords regarding the residential lease listing process.",
      "attribute": "text",
      "order": 28,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter advisory notes here...",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "yard_maintenance_responsibility",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_39"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_40"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_140"
      }
    ],
    "display_attributes": {
      "unique_id": "yard_maintenance_responsibility",
      "display_name": "Yard Maintenance Responsibility",
      "description": "Select who is responsible for maintaining the yard",
      "attribute": "maintenance",
      "order": 29,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Landlord",
            "databaseStored": "LANDLORD",
            "linkedFields": []
          },
          {
            "display_name": "Tenant",
            "databaseStored": "TENANT",
            "linkedFields": []
          },
          {
            "display_name": "Contractor",
            "databaseStored": "CONTRACTOR",
            "linkedFields": []
          }
        ],
        "minSelected": 1,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "additional_late_charges",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_115"
      }
    ],
    "display_attributes": {
      "unique_id": "additional_late_charges",
      "display_name": "Additional Late Charges",
      "description": "Specify the additional late charges per day after the initial late charge.",
      "attribute": "amount",
      "order": 30,
      "block": "Financial Details",
      "block_style": {
        "title": "Financial Details",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_reimbursement_agreement",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_23"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_reimbursement_agreement",
      "display_name": "Broker Reimbursement Agreement",
      "description": "Select if the landlord agrees to reimburse the broker for costs incurred for repairs or alterations.",
      "attribute": "agreement",
      "order": 31,
      "block": "Financial Details",
      "block_style": {
        "title": "Financial Details",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Reimburse Broker",
            "databaseStored": "REIMBURSE_BROKER",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "broker_reimbursement_fee",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_93"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_reimbursement_fee",
      "display_name": "Broker Reimbursement Fee",
      "description": "Amount to reimburse the Broker for costs incurred for repairs or alterations",
      "attribute": "amount",
      "order": 32,
      "block": "Financial Details",
      "block_style": {
        "title": "Financial Details",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "county_payment",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_70"
      }
    ],
    "display_attributes": {
      "unique_id": "county_payment",
      "display_name": "County",
      "description": "All amounts payable to Broker are to be paid in cash in County, Texas.",
      "attribute": "location",
      "order": 33,
      "block": "Financial Details",
      "block_style": {
        "title": "Financial Details",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 6,
      "placeholder": "Enter County Name",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "listing_delay_days",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_72"
      }
    ],
    "display_attributes": {
      "unique_id": "listing_delay_days",
      "display_name": "Days Until Filing",
      "description": "Number of days after the listing begins before the Broker can file with MLS",
      "attribute": "number",
      "order": 34,
      "block": "Financial Details",
      "block_style": {
        "title": "Financial Details",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter number of days",
      "validation": {
        "regex": "^[0-9]+$"
      },
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "listing_purpose",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_73"
      }
    ],
    "display_attributes": {
      "unique_id": "listing_purpose",
      "display_name": "Purpose for Not Filing Listing",
      "description": "Specify the purpose for which the landlord instructs the broker not to file the listing with MLS.",
      "attribute": "text",
      "order": 35,
      "block": "Financial Details",
      "block_style": {
        "title": "Financial Details",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 12,
      "placeholder": "Enter purpose here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "other_fees",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_156"
      }
    ],
    "display_attributes": {
      "unique_id": "other_fees",
      "display_name": "Other Fees",
      "description": "Specify any additional fees not covered in the previous sections.",
      "attribute": "fees",
      "order": 36,
      "block": "Financial Details",
      "block_style": {
        "title": "Financial Details",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 12,
      "placeholder": "Enter additional fees here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "replacement_tenant_fee_if_procured_by_tenant",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_149"
      }
    ],
    "display_attributes": {
      "unique_id": "replacement_tenant_fee_if_procured_by_tenant",
      "display_name": "Replacement Tenant Fee (If Procured by Tenant)",
      "description": "Fee amount for replacing a tenant if procured by the tenant.",
      "attribute": "amount",
      "order": 37,
      "block": "Financial Details",
      "block_style": {
        "title": "Financial Details",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "security_deposit_amount",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_127"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_128"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_129"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_130"
      }
    ],
    "display_attributes": {
      "unique_id": "security_deposit_amount",
      "display_name": "Security Deposit Amount",
      "description": "Enter the total amount for the security deposit",
      "attribute": "amount",
      "order": 38,
      "block": "Financial Details",
      "block_style": {
        "title": "Financial Details",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "0.00",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "animal_non_refundable_payment",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_124"
      }
    ],
    "display_attributes": {
      "unique_id": "animal_non_refundable_payment",
      "display_name": "One-Time Non-Refundable Payment for Animals",
      "description": "Amount required as a one-time, non-refundable payment if animals are permitted.",
      "attribute": "amount",
      "order": 39,
      "block": "Animals Policy",
      "block_style": {
        "title": "Animals Policy",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "animal_one_time_non_refundable_payment",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_123"
      }
    ],
    "display_attributes": {
      "unique_id": "animal_one_time_non_refundable_payment",
      "display_name": "One-Time Non-Refundable Payment",
      "description": "Specify the one-time non-refundable payment required for animals.",
      "attribute": "amount",
      "order": 40,
      "block": "Animals Policy",
      "block_style": {
        "title": "Animals Policy",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "animal_rent_increase",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_122"
      }
    ],
    "display_attributes": {
      "unique_id": "animal_rent_increase",
      "display_name": "Monthly Rent Increase for Animals",
      "description": "Amount by which the monthly rent will be increased if an animal is permitted.",
      "attribute": "amount",
      "order": 41,
      "block": "Animals Policy",
      "block_style": {
        "title": "Animals Policy",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]*(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "monthly_rent_increase",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_121"
      }
    ],
    "display_attributes": {
      "unique_id": "monthly_rent_increase",
      "display_name": "Monthly Rent Increase",
      "description": "Amount by which the monthly rent will be increased if an animal is permitted",
      "attribute": "amount",
      "order": 42,
      "block": "Animals Policy",
      "block_style": {
        "title": "Animals Policy",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_address",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_10"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_address",
      "display_name": "Broker Address",
      "description": "Address of the broker involved in the agreement",
      "attribute": "address",
      "order": 43,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "123 Main St",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_associate_initials",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_75"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_87"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_associate_initials",
      "display_name": "Broker Associate Initials",
      "description": "Initials of the Broker or Associate for identification purposes",
      "attribute": "initials",
      "order": 44,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter Initials",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_associate_name",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_168"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_associate_name",
      "display_name": "Broker's Associate's Printed Name",
      "description": "Name of the broker's associate, if applicable",
      "attribute": "name",
      "order": 45,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "John Smith",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_city_state_zip",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_11"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_city_state_zip",
      "display_name": "Broker City, State, Zip",
      "description": "City, state, and ZIP code of the broker's address",
      "attribute": "address",
      "order": 46,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "City, State, Zip",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_email_fax_number",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_14"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_email_fax_number",
      "display_name": "E-Mail/Fax Number",
      "description": "Contact email or fax number for the broker",
      "attribute": "contact",
      "order": 47,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "example@example.com or 123-456-7890",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_license_number",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_170"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_171"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_license_number",
      "display_name": "Broker License Number",
      "description": "Enter the license number of the broker",
      "attribute": "license",
      "order": 48,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "License No.",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_mobile_phone",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_13"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_mobile_phone",
      "display_name": "Broker Mobile Phone",
      "description": "Mobile phone number of the broker",
      "attribute": "phone",
      "order": 49,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "(123) 456-7890",
      "validation": {
        "regex": "^\\(\\d{3}\\) \\d{3}-\\d{4}$"
      },
      "special_input": {
        "text": {
          "phone": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_name",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_8"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_9"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_name",
      "display_name": "Broker Name",
      "description": "Name of the broker representing the landlord",
      "attribute": "name",
      "order": 50,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "Enter Broker Name",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_phone",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_12"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_phone",
      "display_name": "Broker Phone",
      "description": "Contact phone number for the broker",
      "attribute": "phone",
      "order": 51,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "(123) 456-7890",
      "validation": {
        "regex": "^\\(\\d{3}\\) \\d{3}-\\d{4}$"
      },
      "special_input": {
        "text": {
          "phone": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_printed_name",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_167"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_printed_name",
      "display_name": "Broker's Printed Name",
      "description": "Full legal name of the broker as it appears on their license",
      "attribute": "name",
      "order": 52,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "John Doe",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "brokers_associates_printed_name",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_173"
      }
    ],
    "display_attributes": {
      "unique_id": "brokers_associates_printed_name",
      "display_name": "Broker's Associate's Printed Name",
      "description": "Name of the broker's associate, if applicable",
      "attribute": "name",
      "order": 53,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "John Smith",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "brokers_printed_name",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_163"
      }
    ],
    "display_attributes": {
      "unique_id": "brokers_printed_name",
      "display_name": "Broker's Printed Name",
      "description": "Full legal name of the broker as it appears on their license",
      "attribute": "name",
      "order": 54,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "John Smith",
      "validation": null,
      "special_input": null,
      "isCached": true,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "intermediary_status",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_18"
      }
    ],
    "display_attributes": {
      "unique_id": "intermediary_status",
      "display_name": "Intermediary Status",
      "description": "Select if the broker is authorized to act as an intermediary.",
      "attribute": "broker_intermediary",
      "order": 55,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Broker Authorized as Intermediary",
            "databaseStored": "BROKER_AUTHORIZED_AS_INTERMEDIARY",
            "linkedFields": []
          }
        ],
        "minSelected": 1,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "landlord_address",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_3"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_address",
      "display_name": "Landlord Address",
      "description": "Address of the landlord for the lease agreement",
      "attribute": "address",
      "order": 56,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "123 Main St",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "landlord_city_state_zip",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_4"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_city_state_zip",
      "display_name": "City, State, Zip",
      "description": "City, state, and ZIP code of the landlord's address",
      "attribute": "address",
      "order": 57,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "Austin, TX, 73301",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "landlord_email_fax_number",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_7"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_email_fax_number",
      "display_name": "E-Mail/Fax Number",
      "description": "Contact email or fax number for the landlord",
      "attribute": "contact",
      "order": 58,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "example@example.com or 123-456-7890",
      "validation": null,
      "special_input": {
        "text": {
          "email": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "landlord_identification",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_80"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_81"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_82"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_103"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_identification",
      "display_name": "Landlord Identification",
      "description": "Enter the name of the landlord for identification purposes",
      "attribute": "name",
      "order": 59,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "Enter Landlord's Name",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "landlord_initials",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_57"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_76"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_77"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_initials",
      "display_name": "Landlord Initials",
      "description": "Initials of the landlord for identification purposes",
      "attribute": "text",
      "order": 60,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter Initials",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "landlord_mobile_phone",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_6"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_mobile_phone",
      "display_name": "Landlord Mobile Phone",
      "description": "Mobile phone number of the landlord",
      "attribute": "phone",
      "order": 61,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "(123) 456-7890",
      "validation": {
        "regex": "^\\(\\d{3}\\) \\d{3}-\\d{4}$"
      },
      "special_input": {
        "text": {
          "phone": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "landlord_name",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_1"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_2"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_name",
      "display_name": "Landlord Name",
      "description": "Name of the landlord involved in the lease agreement",
      "attribute": "name",
      "order": 62,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "Enter landlord's name",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "landlord_phone",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_5"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_phone",
      "display_name": "Landlord Phone",
      "description": "Contact phone number for the landlord",
      "attribute": "phone",
      "order": 63,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "(123) 456-7890",
      "validation": {
        "regex": "^\\(\\d{3}\\) \\d{3}-\\d{4}$"
      },
      "special_input": {
        "text": {
          "phone": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "landlord_printed_name",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_162"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_165"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_166"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_172"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_printed_name",
      "display_name": "Landlord's Printed Name",
      "description": "Legal name of the landlord as it should appear on the agreement",
      "attribute": "name",
      "order": 64,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "John Smith",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "landlord_signature",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_55"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_56"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_88"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_101"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_102"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_105"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_106"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_107"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_158"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_159"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_160"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_169"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_signature",
      "display_name": "Landlord Signature",
      "description": "Signature of the landlord to confirm agreement",
      "attribute": "signature",
      "order": 65,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "Landlord Signature",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "signature",
      "value": {
        "type": "manual",
        "output": "SignatureInput__landlord"
      }
    }
  },
  {
    "unique_id": "landlord_signature_date",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_164"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_signature_date",
      "display_name": "Landlord's Signature Date",
      "description": "Date when the landlord signs the agreement",
      "attribute": "date",
      "order": 66,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "MM/DD/YYYY",
      "validation": {
        "regex": "^\\d{1,2}/\\d{1,2}/\\d{4}$"
      },
      "special_input": {
        "text": {
          "date": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "no_intermediary_status",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_19"
      }
    ],
    "display_attributes": {
      "unique_id": "no_intermediary_status",
      "display_name": "No Intermediary Status",
      "description": "Landlord agrees that Broker will not show the Property to prospective tenants or buyers who Broker represents.",
      "attribute": "agreement",
      "order": 67,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Agree",
            "databaseStored": "AGREE",
            "linkedFields": []
          }
        ],
        "minSelected": 1,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "broker_arrangement_for_repairs",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_20"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_21"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_arrangement_for_repairs",
      "display_name": "Broker Arrangement for Repairs",
      "description": "Select if the broker may arrange for contractors to make repairs or alterations to the property.",
      "attribute": "broker_repairs",
      "order": 68,
      "block": "Make Ready",
      "block_style": {
        "title": "Make Ready",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Broker may arrange for repairs",
            "databaseStored": "BROKER_MAY_ARRANGE_FOR_REPAIRS",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "broker_payment_authorization",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_22"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_payment_authorization",
      "display_name": "Broker Payment Authorization",
      "description": "Authorize the broker to pay contractors directly and pay a service fee.",
      "attribute": "payment_authorization",
      "order": 69,
      "block": "Make Ready",
      "block_style": {
        "title": "Make Ready",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Pay Contractors Directly",
            "databaseStored": "PAY_CONTRACTORS_DIRECTLY",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "broker_service_fee",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_90"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_92"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_service_fee",
      "display_name": "Broker Service Fee",
      "description": "Enter the service fee to be paid to the Broker upon receipt of the contractor's invoices.",
      "attribute": "amount",
      "order": 70,
      "block": "Make Ready",
      "block_style": {
        "title": "Make Ready",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter fee amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "contractor_service_fee",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_91"
      }
    ],
    "display_attributes": {
      "unique_id": "contractor_service_fee",
      "display_name": "Contractor Service Fee",
      "description": "Amount to be paid to the contractors directly and the service fee to the Broker upon receipt of invoices.",
      "attribute": "amount",
      "order": 71,
      "block": "Make Ready",
      "block_style": {
        "title": "Make Ready",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "Enter service fee amount",
      "validation": null,
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_authorization_keybox",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_16"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_17"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_authorization_keybox",
      "display_name": "Broker Authorization for Keybox",
      "description": "Select if the broker is authorized to place a keybox on the property.",
      "attribute": "authorization",
      "order": 72,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Authorized",
            "databaseStored": "AUTHORIZED",
            "linkedFields": []
          },
          {
            "display_name": "Not Authorized",
            "databaseStored": "NOT_AUTHORIZED",
            "linkedFields": []
          }
        ],
        "minSelected": 1,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "county_name",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_66"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_69"
      }
    ],
    "display_attributes": {
      "unique_id": "county_name",
      "display_name": "County",
      "description": "Enter the county where the property is located",
      "attribute": "location",
      "order": 73,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "Enter County Name",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "exclusions_landlord_removal",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_26"
      }
    ],
    "display_attributes": {
      "unique_id": "exclusions_landlord_removal",
      "display_name": "Exclusions: Items to be Removed",
      "description": "List the items that the landlord will remove from the property.",
      "attribute": "text",
      "order": 74,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter items to be removed",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "financial_obligations_exceptions",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_94"
      }
    ],
    "display_attributes": {
      "unique_id": "financial_obligations_exceptions",
      "display_name": "Financial Obligations Exceptions",
      "description": "List any exceptions to the financial obligations related to the property.",
      "attribute": "text",
      "order": 75,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter exceptions here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "land_lot",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_17"
      }
    ],
    "display_attributes": {
      "unique_id": "land_lot",
      "display_name": "Land Lot",
      "description": "Specify the lot number for the property being leased",
      "attribute": "address",
      "order": 76,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "Enter Lot Number",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "landlord_exclusions",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_25"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_exclusions",
      "display_name": "Exclusions",
      "description": "Items that the landlord will remove from the property",
      "attribute": "text",
      "order": 77,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "List items to be removed",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "landlord_listing_content",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_100"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_listing_content",
      "display_name": "Landlord Listing Content",
      "description": "Details regarding the Landlord Listing Content and its rights",
      "attribute": "text",
      "order": 78,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter details about the Landlord Listing Content",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "non_real_estate_items",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_23"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_24"
      }
    ],
    "display_attributes": {
      "unique_id": "non_real_estate_items",
      "display_name": "Non-Real Estate Items",
      "description": "List any non-real estate items included in the property agreement.",
      "attribute": "items",
      "order": 79,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "e.g., appliances, furniture",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "non_real_estate_items_exclusions",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_27"
      }
    ],
    "display_attributes": {
      "unique_id": "non_real_estate_items_exclusions",
      "display_name": "Exclusions",
      "description": "Items that the landlord will remove from the property",
      "attribute": "text",
      "order": 80,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "List exclusions here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "optional_user_fees",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_96"
      }
    ],
    "display_attributes": {
      "unique_id": "optional_user_fees",
      "display_name": "Optional User Fees",
      "description": "Specify any optional user fees for the use of common areas.",
      "attribute": "fees",
      "order": 81,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter fees if applicable",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "pool_maintenance_responsibility",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_141"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_42"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_43"
      }
    ],
    "display_attributes": {
      "unique_id": "pool_maintenance_responsibility",
      "display_name": "Pool/Spa Maintenance Responsibility",
      "description": "Specify who is responsible for maintaining the pool or spa.",
      "attribute": "maintenance_responsibility",
      "order": 82,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter responsible party",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "property_addition_exceptions",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_97"
      }
    ],
    "display_attributes": {
      "unique_id": "property_addition_exceptions",
      "display_name": "Property Addition Exceptions",
      "description": "Specify any exceptions related to the property's addition.",
      "attribute": "text",
      "order": 83,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter exceptions here...",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "property_address",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_19"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_20"
      }
    ],
    "display_attributes": {
      "unique_id": "property_address",
      "display_name": "Property Address",
      "description": "Enter the address of the property being leased",
      "attribute": "address",
      "order": 84,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "123 Main St, Apt 4B",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "property_address_zip_code",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_21"
      }
    ],
    "display_attributes": {
      "unique_id": "property_address_zip_code",
      "display_name": "Property Address (Zip Code)",
      "description": "Enter the complete address including the zip code for the property.",
      "attribute": "address",
      "order": 85,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "123 Main St, Apt 4B, 12345",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "property_block",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_18"
      }
    ],
    "display_attributes": {
      "unique_id": "property_block",
      "display_name": "Property Block",
      "description": "Specify the block number of the property",
      "attribute": "property_block",
      "order": 86,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter Block Number",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "property_condition_exceptions",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_98"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_99"
      }
    ],
    "display_attributes": {
      "unique_id": "property_condition_exceptions",
      "display_name": "Property Condition Exceptions",
      "description": "Specify any conditions concerning the property that materially affect the health or safety of an ordinary tenant.",
      "attribute": "condition",
      "order": 87,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Describe any conditions here...",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "property_encumbrances",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_95"
      }
    ],
    "display_attributes": {
      "unique_id": "property_encumbrances",
      "display_name": "Property Encumbrances",
      "description": "List any liens or other encumbrances against the property, if applicable.",
      "attribute": "text",
      "order": 88,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter details here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "property_land_description",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_15"
      }
    ],
    "display_attributes": {
      "unique_id": "property_land_description",
      "display_name": "Property Land Description",
      "description": "Provide details about the land including Lot, Block, Addition, City, and County.",
      "attribute": "property_description",
      "order": 89,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Lot, Block, Addition, City, County",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "property_land_lot",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_16"
      }
    ],
    "display_attributes": {
      "unique_id": "property_land_lot",
      "display_name": "Land Lot",
      "description": "Specify the land lot details for the property",
      "attribute": "land_lot",
      "order": 90,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "Enter Lot Number",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "property_name",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_22"
      }
    ],
    "display_attributes": {
      "unique_id": "property_name",
      "display_name": "Property Name",
      "description": "Name or designation of the property being leased",
      "attribute": "name",
      "order": 91,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter property name",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "residential_lease_listing_concerning",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_78"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_83"
      }
    ],
    "display_attributes": {
      "unique_id": "residential_lease_listing_concerning",
      "display_name": "Residential Lease Listing Concerning",
      "description": "Details regarding the residential lease listing",
      "attribute": "text",
      "order": 92,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter details here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "residential_lease_terms",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_89"
      }
    ],
    "display_attributes": {
      "unique_id": "residential_lease_terms",
      "display_name": "Residential Lease Terms",
      "description": "Terms of the lease for the property being listed",
      "attribute": "lease_terms",
      "order": 93,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter lease terms here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "scheduling_companies",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_79"
      }
    ],
    "display_attributes": {
      "unique_id": "scheduling_companies",
      "display_name": "Scheduling Companies",
      "description": "List the companies authorized to schedule appointments and access the property.",
      "attribute": "text",
      "order": 94,
      "block": "Property Information",
      "block_style": {
        "title": "Property Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter company names here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_authorization_signature",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_86"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_authorization_signature",
      "display_name": "Broker Authorization Signature",
      "description": "Signature of the broker or associate for authorization purposes",
      "attribute": "signature",
      "order": 95,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "Signature",
      "validation": null,
      "special_input": null,
      "isCached": true,
      "isRequired": true,
      "input_type": "signature",
      "value": {
        "type": "manual",
        "output": "SignatureInput__broker"
      }
    }
  },
  {
    "unique_id": "brokers_signature_authorization",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_46"
      }
    ],
    "display_attributes": {
      "unique_id": "brokers_signature_authorization",
      "display_name": "Broker's Signature Authorization",
      "description": "Select to authorize the broker's signature on the listing agreement.",
      "attribute": "signature",
      "order": 96,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Authorize Broker's Signature",
            "databaseStored": "AUTHORIZE_BROKERS_SIGNATURE",
            "linkedFields": []
          }
        ],
        "minSelected": 1,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "landlord_listing_display_preference",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_85"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_listing_display_preference",
      "display_name": "Landlord Listing Display Preference",
      "description": "Indicate whether the landlord wants this listing to be displayed on the Internet.",
      "attribute": "listing_display_preference",
      "order": 97,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter your preference",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "listing_internet_display_preference",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_84"
      }
    ],
    "display_attributes": {
      "unique_id": "listing_internet_display_preference",
      "display_name": "Listing Internet Display Preference",
      "description": "Indicate whether the landlord wants this listing to be displayed on the Internet.",
      "attribute": "preference",
      "order": 98,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "user",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter preference",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_compensation_percentage",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_62"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_compensation_percentage",
      "display_name": "Broker Compensation Percentage",
      "description": "Percentage of the sales price to be paid to the Broker upon sale of the property.",
      "attribute": "percentage",
      "order": 99,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter percentage",
      "validation": "^[0-9]{1,3}(\\.[0-9]{1,2})?$",
      "special_input": {
        "text": {
          "percentage": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_compensation_tenant_representation",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_40"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_compensation_tenant_representation",
      "display_name": "Broker Compensation for Tenant Representation",
      "description": "Specify the percentage or flat fee to be paid to the other broker if they represent the tenant.",
      "attribute": "compensation",
      "order": 100,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 6,
      "placeholder": "Enter percentage or flat fee",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_compensation_terms",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_58"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_compensation_terms",
      "display_name": "Broker Compensation Terms",
      "description": "Details regarding the conditions under which the broker's compensation is payable.",
      "attribute": "text",
      "order": 101,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 12,
      "placeholder": "Enter compensation terms here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_fee_amount",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_54"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_fee_amount",
      "display_name": "Broker Fee Amount",
      "description": "Insert the amount to be paid to the Broker for the lease agreement.",
      "attribute": "amount",
      "order": 102,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_fee_compensation",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_fee_compensation",
      "display_name": "Broker Fee Compensation",
      "description": "Select the method of compensation for the broker when a tenant is procured.",
      "attribute": "broker_fee",
      "order": 103,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Percentage of One Full Month's Rent",
            "databaseStored": "PERCENTAGE_OF_ONE_FULL_MONTHS_RENT",
            "linkedFields": []
          },
          {
            "display_name": "Percentage of All Rents",
            "databaseStored": "PERCENTAGE_OF_ALL_RENTS",
            "linkedFields": []
          }
        ],
        "minSelected": 1,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "broker_fee_flat_amount",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_51"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_fee_flat_amount",
      "display_name": "Broker Fee Flat Amount",
      "description": "Specify the flat fee to be paid to the broker under the lease agreement.",
      "attribute": "amount",
      "order": 104,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter flat fee amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_fee_other_broker_representation",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_3"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_fee_other_broker_representation",
      "display_name": "If the Other Broker Represents the Tenant",
      "description": "Select if the other broker represents the tenant for the lease agreement.",
      "attribute": "broker_representation",
      "order": 105,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Represents the Tenant",
            "databaseStored": "REPRESENTS_THE_TENANT",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "broker_fee_percentage_rent",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_2"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_38"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_fee_percentage_rent",
      "display_name": "Percentage of All Rents",
      "description": "Select if the landlord agrees to pay a percentage of all rents to the broker.",
      "attribute": "broker_fee",
      "order": 106,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Percentage of All Rents",
            "databaseStored": "PERCENTAGE_OF_ALL_RENTS",
            "linkedFields": []
          }
        ],
        "minSelected": 1,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "broker_fee_without_compensation",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_6",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_6",
            "displayName": "Broker's Fee (Without Compensation)"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_4",
            "displayName": "Broker's Fee Options"
          }
        ]
      }
    ],
    "display_attributes": {
      "unique_id": "broker_fee_without_compensation",
      "display_name": "Broker's Fee",
      "description": "Select the applicable fee structure for the broker's compensation.",
      "attribute": "fee_structure",
      "order": 107,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Percentage of One Full Month's Rent",
            "databaseStored": "PERCENTAGE_OF_ONE_FULL_MONTHS_RENT",
            "linkedFields": []
          },
          {
            "display_name": "Percentage of All Rents",
            "databaseStored": "PERCENTAGE_OF_ALL_RENTS",
            "linkedFields": []
          },
          {
            "display_name": "One Full Month's Rent",
            "databaseStored": "ONE_FULL_MONTHS_RENT",
            "linkedFields": []
          }
        ]
      }
    }
  },
  {
    "unique_id": "broker_flat_fee",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_42"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_43"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_50"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_flat_fee",
      "display_name": "Broker Flat Fee",
      "description": "Flat fee to be paid to the broker for leasing the property",
      "attribute": "amount",
      "order": 108,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter flat fee amount",
      "validation": null,
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "brokers_fee",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_36"
      }
    ],
    "display_attributes": {
      "unique_id": "brokers_fee",
      "display_name": "Broker's Fee",
      "description": "Enter the fee for the broker's services, if applicable.",
      "attribute": "amount",
      "order": 109,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 6,
      "placeholder": "Enter fee amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "brokers_fee_percentage",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_53"
      }
    ],
    "display_attributes": {
      "unique_id": "brokers_fee_percentage",
      "display_name": "Broker's Fee Percentage",
      "description": "Percentage of all rents to be paid under a lease of the property",
      "attribute": "percentage",
      "order": 110,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter percentage",
      "validation": {
        "regex": "^(100|[1-9][0-9]?)$"
      },
      "special_input": {
        "text": {
          "percentage": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "flat_fee_for_broker",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_45"
      }
    ],
    "display_attributes": {
      "unique_id": "flat_fee_for_broker",
      "display_name": "Flat Fee for Broker",
      "description": "Specify the flat fee to be paid to the broker for leasing the property.",
      "attribute": "amount",
      "order": 111,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter flat fee amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "flat_fee_other_broker",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_44"
      }
    ],
    "display_attributes": {
      "unique_id": "flat_fee_other_broker",
      "display_name": "Flat Fee for Other Broker",
      "description": "Enter the flat fee to be paid to the other broker for procuring a tenant.",
      "attribute": "amount",
      "order": 112,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "flat_fee_subagent",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_48"
      }
    ],
    "display_attributes": {
      "unique_id": "flat_fee_subagent",
      "display_name": "Flat Fee for Subagent",
      "description": "Enter the flat fee to be paid to the subagent",
      "attribute": "amount",
      "order": 113,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "payment_county",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_67"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_68"
      }
    ],
    "display_attributes": {
      "unique_id": "payment_county",
      "display_name": "County",
      "description": "Enter the county where all amounts payable to Broker are to be paid in cash.",
      "attribute": "location",
      "order": 114,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 6,
      "placeholder": "Enter County Name",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "subagent_fee_flat_amount",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_46"
      }
    ],
    "display_attributes": {
      "unique_id": "subagent_fee_flat_amount",
      "display_name": "Flat Fee for Subagent",
      "description": "Enter the flat fee amount to be paid to the subagent for leasing the property.",
      "attribute": "amount",
      "order": 115,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "subagent_fee_percentage",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_47"
      }
    ],
    "display_attributes": {
      "unique_id": "subagent_fee_percentage",
      "display_name": "Subagent Fee Percentage",
      "description": "Percentage of one month's rent to be paid under a lease if the other broker is a subagent",
      "attribute": "percentage",
      "order": 116,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter percentage",
      "validation": "^(100|[1-9][0-9]?)$",
      "special_input": {
        "text": {
          "percentage": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "subagent_rent_percentage",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_49"
      }
    ],
    "display_attributes": {
      "unique_id": "subagent_rent_percentage",
      "display_name": "Subagent Rent Percentage",
      "description": "Percentage of all rents to be paid under a lease if the other broker is a subagent",
      "attribute": "percentage",
      "order": 117,
      "block": "Broker Compensation",
      "block_style": {
        "title": "Broker Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter percentage",
      "validation": "^(100|[1-9]?[0-9])$",
      "special_input": {
        "text": {
          "percentage": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "broker_fee_percentage",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_37"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_39"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_41"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_52"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_fee_percentage",
      "display_name": "Broker Fee Percentage",
      "description": "Percentage of one full month's rent to be paid under a lease of the Property.",
      "attribute": "percentage",
      "order": 118,
      "block": "Broker's Fee",
      "block_style": {
        "title": "Broker's Fee",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter percentage",
      "validation": {
        "regex": "^(100|[1-9][0-9]?)$"
      },
      "special_input": {
        "text": {
          "percentage": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "brokers_fee_all_rents",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_5"
      }
    ],
    "display_attributes": {
      "unique_id": "brokers_fee_all_rents",
      "display_name": "Percentage of All Rents",
      "description": "Select if the broker will receive a percentage of all rents to be paid under the lease of the property.",
      "attribute": "fee_percentage",
      "order": 119,
      "block": "Broker's Fee",
      "block_style": {
        "title": "Broker's Fee",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Percentage of All Rents",
            "databaseStored": "PERCENTAGE_OF_ALL_RENTS",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "broker_not_file_listing_mls",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_13"
      }
    ],
    "display_attributes": {
      "unique_id": "broker_not_file_listing_mls",
      "display_name": "Broker Will Not File Listing with MLS",
      "description": "Select this option if the Broker will not file this listing with any Multiple Listing Services (MLS) or other listing service.",
      "attribute": "listing_service",
      "order": 120,
      "block": "Listing Services",
      "block_style": {
        "title": "Listing Services",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Broker Will Not File Listing with MLS",
            "databaseStored": "BROKER_WILL_NOT_FILE_LISTING_WITH_MLS",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "listing_services_filing",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_12"
      }
    ],
    "display_attributes": {
      "unique_id": "listing_services_filing",
      "display_name": "Listing Services Filing",
      "description": "Select how the Broker will file this Listing with Multiple Listing Services (MLS). Check only one box.",
      "attribute": "filing",
      "order": 121,
      "block": "Listing Services",
      "block_style": {
        "title": "Listing Services",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 12,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Broker will file with MLS",
            "databaseStored": "BROKER_WILL_FILE_WITH_MLS",
            "linkedFields": []
          },
          {
            "display_name": "Landlord instructs not to file with MLS",
            "databaseStored": "LANDLORD_INSTRUCTS_NOT_TO_FILE_WITH_MLS",
            "linkedFields": []
          }
        ],
        "minSelected": 1,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "listing_services_instructions",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_71"
      }
    ],
    "display_attributes": {
      "unique_id": "listing_services_instructions",
      "display_name": "Listing Services Instructions",
      "description": "Instructions for the broker regarding the listing services to be used.",
      "attribute": "instructions",
      "order": 122,
      "block": "Listing Services",
      "block_style": {
        "title": "Listing Services",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 12,
      "placeholder": "Enter instructions here...",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "mls_listing_authorization",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_14"
      }
    ],
    "display_attributes": {
      "unique_id": "mls_listing_authorization",
      "display_name": "MLS Listing Authorization",
      "description": "Select if the Broker will file this Listing with MLS by the required time.",
      "attribute": "listing_authorization",
      "order": 123,
      "block": "Listing Services",
      "block_style": {
        "title": "Listing Services",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "File with MLS by required time",
            "databaseStored": "FILE_WITH_MLS_REQUIRED_TIME",
            "linkedFields": []
          }
        ],
        "minSelected": 1,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "mls_listing_delay_period",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_74"
      }
    ],
    "display_attributes": {
      "unique_id": "mls_listing_delay_period",
      "display_name": "MLS Listing Delay Period",
      "description": "Number of days after the listing begins before it can be filed with MLS",
      "attribute": "date",
      "order": 124,
      "block": "Listing Services",
      "block_style": {
        "title": "Listing Services",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter number of days",
      "validation": {
        "regex": "^[0-9]+$"
      },
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "compensation_for_renewal",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_7"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_8"
      }
    ],
    "display_attributes": {
      "unique_id": "compensation_for_renewal",
      "display_name": "Compensation for Renewal",
      "description": "Select if the landlord agrees to pay a percentage of one full month's rent under the renewal or extension.",
      "attribute": "compensation",
      "order": 125,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Percentage of One Full Month's Rent",
            "databaseStored": "PERCENTAGE_OF_ONE_FULL_MONTHS_RENT",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "compensation_for_renewal_percentage",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_59"
      }
    ],
    "display_attributes": {
      "unique_id": "compensation_for_renewal_percentage",
      "display_name": "Compensation for Renewal Percentage",
      "description": "Percentage of one full month's rent to be paid under the renewal or extension.",
      "attribute": "percentage",
      "order": 126,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "Enter percentage",
      "validation": {
        "regex": "^(100|[1-9]?[0-9])$"
      },
      "special_input": {
        "text": {
          "percentage": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "exclusive_right_to_lease",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_9"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_10"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_11"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_36"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_47"
      }
    ],
    "display_attributes": {
      "unique_id": "exclusive_right_to_lease",
      "display_name": "Exclusive Right to Lease",
      "description": "Select if the broker has the exclusive right to lease the property.",
      "attribute": "lease_rights",
      "order": 127,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Exclusive Right to Lease",
            "databaseStored": "EXCLUSIVE_RIGHT_TO_LEASE",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "reimbursable_expenses",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_64"
      }
    ],
    "display_attributes": {
      "unique_id": "reimbursable_expenses",
      "display_name": "Reimbursable Expenses",
      "description": "Enter any expenses that are reimbursable to the Broker.",
      "attribute": "expenses",
      "order": 128,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 12,
      "placeholder": "Enter reimbursable expenses here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "rental_compensation_percentage",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_61"
      }
    ],
    "display_attributes": {
      "unique_id": "rental_compensation_percentage",
      "display_name": "Percentage of All Rents",
      "description": "Enter the percentage of all rents to be paid under the renewal or extension.",
      "attribute": "percentage",
      "order": 129,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "e.g., 5%",
      "validation": {
        "regex": "^(100|[1-9][0-9]?)(\\.\\d+)?$"
      },
      "special_input": {
        "text": {
          "percentage": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "rental_percentage_compensation",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_60"
      }
    ],
    "display_attributes": {
      "unique_id": "rental_percentage_compensation",
      "display_name": "Percentage of All Rents",
      "description": "Enter the percentage of all rents to be paid under the renewal or extension.",
      "attribute": "percentage",
      "order": 130,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "e.g., 5%",
      "validation": {
        "regex": "^(100|[1-9][0-9]?)(\\.\\d+)?$"
      },
      "special_input": {
        "text": {
          "percentage": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "emergency_phone_number_repairs",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_145"
      }
    ],
    "display_attributes": {
      "unique_id": "emergency_phone_number_repairs",
      "display_name": "Emergency Phone Number for Repairs",
      "description": "Contact number for emergencies related to repairs",
      "attribute": "phone",
      "order": 131,
      "block": "Repairs Information",
      "block_style": {
        "title": "Repairs Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "(123) 456-7890",
      "validation": {
        "regex": "^\\(\\d{3}\\) \\d{3}-\\d{4}$"
      },
      "special_input": {
        "text": {
          "phone": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "repairs_exclusions",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_146"
      }
    ],
    "display_attributes": {
      "unique_id": "repairs_exclusions",
      "display_name": "Appliances or Items That Will Not Be Repaired",
      "description": "List any appliances or items that are excluded from repairs.",
      "attribute": "text",
      "order": 132,
      "block": "Repairs Information",
      "block_style": {
        "title": "Repairs Information",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "e.g., Dishwasher, Heating System",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "keybox_authorization_days",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_131"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_136"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_137"
      }
    ],
    "display_attributes": {
      "unique_id": "keybox_authorization_days",
      "display_name": "Keybox Authorization Days",
      "description": "Number of days authorized for the keybox during the lease period",
      "attribute": "number",
      "order": 133,
      "block": "Residential Lease Listing",
      "block_style": {
        "title": "Residential Lease Listing",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter number of days",
      "validation": "^[0-9]*$",
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "landlord_additional_promises",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_104"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_additional_promises",
      "display_name": "Landlord's Additional Promises",
      "description": "Details of the promises made by the landlord regarding the property lease.",
      "attribute": "text",
      "order": 134,
      "block": "Residential Lease Listing",
      "block_style": {
        "title": "Residential Lease Listing",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter additional promises here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "residential_listing_subject",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_108"
      }
    ],
    "display_attributes": {
      "unique_id": "residential_listing_subject",
      "display_name": "Residential Lease Listing Concerning",
      "description": "Specify the property or subject of the residential lease listing agreement",
      "attribute": "property_description",
      "order": 135,
      "block": "Residential Lease Listing",
      "block_style": {
        "title": "Residential Lease Listing",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter property details here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "landlord_instructions_not_to_file",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_15"
      }
    ],
    "display_attributes": {
      "unique_id": "landlord_instructions_not_to_file",
      "display_name": "Landlord Instructions Not to File",
      "description": "Select if the landlord instructs the broker not to file this listing with MLS until specified days after the listing begins.",
      "attribute": "instructions",
      "order": 136,
      "block": "Filing Instructions",
      "block_style": {
        "title": "Filing Instructions",
        "icon": "calendar",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Do Not File with MLS",
            "databaseStored": "DO_NOT_FILE_WITH_MLS",
            "linkedFields": []
          }
        ],
        "minSelected": 1,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "lease_term_duration",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_29"
      }
    ],
    "display_attributes": {
      "unique_id": "lease_term_duration",
      "display_name": "Lease Term Duration",
      "description": "Specify the duration of the lease in months",
      "attribute": "duration",
      "order": 137,
      "block": "Term Details",
      "block_style": {
        "title": "Term Details",
        "icon": "calendar",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Number of months",
      "validation": "^[0-9]+$",
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "lease_term_minimum",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_30"
      }
    ],
    "display_attributes": {
      "unique_id": "lease_term_minimum",
      "display_name": "Minimum Lease Term",
      "description": "Specify the minimum number of months for the lease term",
      "attribute": "lease_term",
      "order": 138,
      "block": "Term Details",
      "block_style": {
        "title": "Term Details",
        "icon": "calendar",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter number of months",
      "validation": "^[1-9][0-9]*$",
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "listing_start_date",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_31"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_32"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_33"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_34"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_35"
      }
    ],
    "display_attributes": {
      "unique_id": "listing_start_date",
      "display_name": "Listing Start Date",
      "description": "The date when the listing begins",
      "attribute": "date",
      "order": 139,
      "block": "Term Details",
      "block_style": {
        "title": "Term Details",
        "icon": "calendar",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "MM/DD/YYYY",
      "validation": {
        "regex": "^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\\d{4})$"
      },
      "special_input": {
        "text": {
          "date": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "monthly_rental_price",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_28"
      }
    ],
    "display_attributes": {
      "unique_id": "monthly_rental_price",
      "display_name": "Monthly Rental Price",
      "description": "Enter the monthly rental amount for the property",
      "attribute": "amount",
      "order": 140,
      "block": "Listing Price",
      "block_style": {
        "title": "Listing Price",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "e.g., 1500",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "number_of_days_guests_permitted",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_133"
      }
    ],
    "display_attributes": {
      "unique_id": "number_of_days_guests_permitted",
      "display_name": "Number of Days Guests Permitted",
      "description": "Specify the number of days guests are allowed to stay on the property.",
      "attribute": "number",
      "order": 141,
      "block": "Lease Details",
      "block_style": {
        "title": "Lease Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter number of days",
      "validation": "^[0-9]+$",
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "number_of_vehicles_permitted",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_134"
      }
    ],
    "display_attributes": {
      "unique_id": "number_of_vehicles_permitted",
      "display_name": "Number of Vehicles Permitted",
      "description": "Specify the number of vehicles allowed on the property.",
      "attribute": "number",
      "order": 142,
      "block": "Lease Details",
      "block_style": {
        "title": "Lease Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter number",
      "validation": "^[0-9]*$",
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "pool_maintenance_contractor",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_44"
      }
    ],
    "display_attributes": {
      "unique_id": "pool_maintenance_contractor",
      "display_name": "Pool/Spa Maintenance Contractor",
      "description": "Select if a contractor chosen and paid by Tenant will maintain the pool/spa.",
      "attribute": "maintenance",
      "order": 143,
      "block": "Lease Details",
      "block_style": {
        "title": "Lease Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 3,
      "placeholder": null,
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "value": {
        "type": "manual"
      },
      "checkbox_options": {
        "options": [
          {
            "display_name": "Contractor Chosen by Tenant",
            "databaseStored": "CONTRACTOR_CHOSEN_BY_TENANT",
            "linkedFields": []
          }
        ],
        "minSelected": 0,
        "maxSelected": 1
      }
    }
  },
  {
    "unique_id": "special_provisions",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_147"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_148"
      }
    ],
    "display_attributes": {
      "unique_id": "special_provisions",
      "display_name": "Special Provisions",
      "description": "Any additional terms or conditions that are specific to this lease agreement.",
      "attribute": "text",
      "order": 144,
      "block": "Lease Details",
      "block_style": {
        "title": "Lease Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter special provisions here...",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "trip_charge",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_135"
      }
    ],
    "display_attributes": {
      "unique_id": "trip_charge",
      "display_name": "Trip Charge",
      "description": "Fee charged for trips related to the lease agreement",
      "attribute": "amount",
      "order": 145,
      "block": "Lease Details",
      "block_style": {
        "title": "Lease Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "$0.00",
      "validation": {
        "regex": "^\\$?\\d+(\\.\\d{2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "utilities_paid_by_tenant",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_132"
      }
    ],
    "display_attributes": {
      "unique_id": "utilities_paid_by_tenant",
      "display_name": "Utilities Paid by Tenant",
      "description": "Specify all utilities to be paid by the tenant except for those listed.",
      "attribute": "utilities",
      "order": 146,
      "block": "Lease Details",
      "block_style": {
        "title": "Lease Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "e.g., Electricity, Water",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "yard_maintenance",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_139"
      }
    ],
    "display_attributes": {
      "unique_id": "yard_maintenance",
      "display_name": "Yard Maintenance",
      "description": "Specify who is responsible for maintaining the yard.",
      "attribute": "maintenance",
      "order": 147,
      "block": "Lease Details",
      "block_style": {
        "title": "Lease Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter maintenance details here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "other_terms_conditions",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_157"
      }
    ],
    "display_attributes": {
      "unique_id": "other_terms_conditions",
      "display_name": "Other Terms and Conditions",
      "description": "Additional terms or conditions related to the agreement",
      "attribute": "text",
      "order": 148,
      "block": "Special Provisions",
      "block_style": {
        "title": "Special Provisions",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter additional terms here",
      "validation": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "replacement_tenant_fee",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_150"
      }
    ],
    "display_attributes": {
      "unique_id": "replacement_tenant_fee",
      "display_name": "Replacement Tenant Fee",
      "description": "Fee for procuring a replacement tenant if applicable",
      "attribute": "amount",
      "order": 149,
      "block": "Special Provisions",
      "block_style": {
        "title": "Special Provisions",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 6,
      "placeholder": "Enter fee amount",
      "validation": {
        "regex": "^[0-9]+(\\.[0-9]{1,2})?$"
      },
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "protection_period_duration",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_65"
      }
    ],
    "display_attributes": {
      "unique_id": "protection_period_duration",
      "display_name": "Protection Period Duration",
      "description": "Duration of the protection period in days",
      "attribute": "duration",
      "order": 150,
      "block": "Protection Period",
      "block_style": {
        "title": "Protection Period",
        "icon": "calendar",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter number of days",
      "validation": "^[0-9]+$",
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "replacement_tenant_fee_landlord",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_152"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_153"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_154"
      }
    ],
    "display_attributes": {
      "unique_id": "replacement_tenant_fee_landlord",
      "display_name": "Replacement Tenant Fee (Landlord)",
      "description": "Fee charged by the landlord for procuring a replacement tenant",
      "attribute": "fee",
      "order": 151,
      "block": "Assignment, Subletting and Replacement Tenant Fees",
      "block_style": {
        "title": "Assignment, Subletting and Replacement Tenant Fees",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter amount or percentage",
      "validation": null,
      "special_input": {
        "text": {
          "currency": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "replacement_tenant_fee_percentage",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_151"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_155"
      }
    ],
    "display_attributes": {
      "unique_id": "replacement_tenant_fee_percentage",
      "display_name": "Replacement Tenant Fee Percentage",
      "description": "Percentage fee for procuring a replacement tenant",
      "attribute": "percentage",
      "order": 152,
      "block": "Assignment, Subletting and Replacement Tenant Fees",
      "block_style": {
        "title": "Assignment, Subletting and Replacement Tenant Fees",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 4,
      "placeholder": "Enter percentage",
      "validation": {
        "regex": "^(100|[1-9][0-9]?)$"
      },
      "special_input": {
        "text": {
          "percentage": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "sales_price_percentage",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_63"
      }
    ],
    "display_attributes": {
      "unique_id": "sales_price_percentage",
      "display_name": "Percentage of Sales Price",
      "description": "Enter the percentage of the sales price to be paid to the Broker upon sale.",
      "attribute": "percentage",
      "order": 153,
      "block": "Compensation for a Sale",
      "block_style": {
        "title": "Compensation for a Sale",
        "icon": "dollar-sign",
        "color_theme": "orange"
      },
      "width": 4,
      "placeholder": "e.g., 5%",
      "validation": {
        "regex": "^(100|[1-9][0-9]?)%?$"
      },
      "special_input": {
        "text": {
          "percentage": true
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "value": {
        "type": "manual"
      }
    }
  }
];