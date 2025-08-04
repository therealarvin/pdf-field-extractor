export const residentialRealEstateListingAgreementExclusiveRightToLeaseSchema: SchemaItem[] = [
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_1",
        "linked_form_fields_text": [
          "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_1",
          "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_2"
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Landlord Full Name",
      "description": null,
      "attribute": "landlord_full_name",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": "Enter full name of the landlord",
      "special_input": {
        "text_area": true
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_2",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_8",
        "linked_form_fields_text": [
          "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_9"
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Broker Contact Information",
      "description": null,
      "attribute": "broker_contact_info",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "text_area": {}
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text-area",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_3",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_15",
        "linked_form_fields_text": [
          "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_17"
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Property Land Description",
      "description": null,
      "attribute": "land_description",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter Lot, Block, Addition, City, County, and Address",
      "special_input": {
        "text_area": {
          "rows": 3
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text-area",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_4",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_23",
        "linked_form_fields_text": [
          "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_24"
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Non-Real Estate Items Description",
      "description": "Details regarding non-real estate items included with the property.",
      "attribute": "non_real_estate_items",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "List non-real estate items here...",
      "special_input": {
        "text_area": {
          "rows": 4
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text-area",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_5",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_25",
        "linked_form_fields_text": [
          "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_26",
          "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_27"
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Exclusions for Property Listing",
      "description": null,
      "attribute": "exclusions",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "text_area": {
          "rows": 3
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text-area",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_6",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1",
            "displayName": "Percentage of one full month's rent"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_2",
            "displayName": "Percentage of all rents"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_3",
            "displayName": "Percentage if other broker represents tenant"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Fee Payment Options",
      "description": null,
      "attribute": "broker_fee_options",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 3
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Percentage of one full month's rent",
            "databaseStored": "PERCENTAGE_OF_ONE_FULL_MONTHS_RENT"
          },
          {
            "display_name": "Percentage of all rents",
            "databaseStored": "PERCENTAGE_OF_ALL_RENTS"
          },
          {
            "display_name": "Percentage if other broker represents tenant",
            "databaseStored": "PERCENTAGE_IF_OTHER_BROKER_REPRESENTS_TENANT"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_7",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_53",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_53",
            "displayName": "Percentage of One Month's Rent"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_52",
            "displayName": "Percentage of All Rents"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_51",
            "displayName": "Flat Fee"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Broker Fee Payment Options",
      "description": null,
      "attribute": "broker_fee_options",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 3
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Percentage of One Month's Rent",
            "databaseStored": "PERCENTAGE_OF_ONE_MONTHS_RENT"
          },
          {
            "display_name": "Percentage of All Rents",
            "databaseStored": "PERCENTAGE_OF_ALL_RENTS"
          },
          {
            "display_name": "Flat Fee",
            "databaseStored": "FLAT_FEE"
          }
        ],
        "minSelected": 1
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_8",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_56",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_56",
            "displayName": "Percentage of One Month's Rent to be Paid Under a Lease"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_55",
            "displayName": "Percentage of All Rents to be Paid Under a Lease"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_54",
            "displayName": "A Flat Fee"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Broker Compensation Options",
      "description": null,
      "attribute": "broker_compensation",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Percentage of One Month's Rent to be Paid Under a Lease",
            "databaseStored": "PERCENTAGE_OF_ONE_MONTHS_RENT_TO_BE_PAID_UNDER_A_LEASE"
          },
          {
            "display_name": "Percentage of All Rents to be Paid Under a Lease",
            "databaseStored": "PERCENTAGE_OF_ALL_RENTS_TO_BE_PAID_UNDER_A_LEASE"
          },
          {
            "display_name": "A Flat Fee",
            "databaseStored": "A_FLAT_FEE"
          }
        ],
        "minSelected": 1
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_9",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_4",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_4",
            "displayName": "Percentage of One Full Month's Rent"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_5",
            "displayName": "Percentage of All Rents"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_6",
            "displayName": "Other Amount"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Fee Payment Options",
      "description": null,
      "attribute": "broker_fee_options",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 3
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Percentage of One Full Month's Rent",
            "databaseStored": "PERCENTAGE_OF_ONE_FULL_MONTHS_RENT"
          },
          {
            "display_name": "Percentage of All Rents",
            "databaseStored": "PERCENTAGE_OF_ALL_RENTS"
          },
          {
            "display_name": "Other Amount",
            "databaseStored": "OTHER_AMOUNT"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_10",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_7",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_7",
            "displayName": "Percentage of one full month's rent for renewal"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_8",
            "displayName": "Percentage of all rents for renewal"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_9",
            "displayName": "Percentage of sales price for sale"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Compensation Terms for Renewal and Sale",
      "description": null,
      "attribute": "compensation_terms",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": null,
        "color_theme": null
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 3
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Percentage of one full month's rent for renewal",
            "databaseStored": "PERCENTAGE_OF_ONE_FULL_MONTHS_RENT_FOR_RENEWAL"
          },
          {
            "display_name": "Percentage of all rents for renewal",
            "databaseStored": "PERCENTAGE_OF_ALL_RENTS_FOR_RENEWAL"
          },
          {
            "display_name": "Percentage of sales price for sale",
            "databaseStored": "PERCENTAGE_OF_SALES_PRICE_FOR_SALE"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_11",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_10",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_10",
            "displayName": "Percentage of One Full Month's Rent"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_11",
            "displayName": "Percentage of All Rents"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Broker Compensation Options for Sale",
      "description": null,
      "attribute": "broker_compensation_sale",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Percentage of One Full Month's Rent",
            "databaseStored": "PERCENTAGE_OF_ONE_FULL_MONTHS_RENT"
          },
          {
            "display_name": "Percentage of All Rents",
            "databaseStored": "PERCENTAGE_OF_ALL_RENTS"
          },
          {
            "display_name": "Percentage of Sales Price"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_12",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_66",
        "linked_form_fields_text": [
          "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_67"
        ]
      }
    ],
    "display_attributes": {
      "display_name": "County and Payment Terms for Broker",
      "description": null,
      "attribute": "county_payment_terms",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": "Enter County and Payment Terms",
      "special_input": {
        "text_area": true
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text-area",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_13",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_12",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_12",
            "displayName": "Broker will file this Listing with one or more Multiple Listing Services (MLS)"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_13",
            "displayName": "Broker will not file this Listing with any Multiple Listing Services (MLS)"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Broker Filing Instructions for Listing Services",
      "description": null,
      "attribute": "broker_filing_instructions",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Broker will file this Listing with one or more Multiple Listing Services (MLS)",
            "databaseStored": "BROKER_WILL_FILE_THIS_LISTING_WITH_ONE_OR_MORE_MULTIPLE_LISTING_SERVICES_MLS"
          },
          {
            "display_name": "Broker will not file this Listing with any Multiple Listing Services (MLS)",
            "databaseStored": "BROKER_WILL_NOT_FILE_THIS_LISTING_WITH_ANY_MULTIPLE_LISTING_SERVICES_MLS"
          }
        ],
        "minSelected": 1
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_14",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_14",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_14",
            "displayName": "Broker will file this Listing with MLS"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_15",
            "displayName": "Landlord instructs Broker not to file this Listing with MLS"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Broker Listing Filing Instructions",
      "description": null,
      "attribute": "listing_filing_instructions",
      "order": 1,
      "block": "Listing Services",
      "block_style": {
        "title": "Listing Services",
        "icon": null,
        "color_theme": null
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 1
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Broker will file this Listing with MLS",
            "databaseStored": "BROKER_WILL_FILE_THIS_LISTING_WITH_MLS"
          },
          {
            "display_name": "Landlord instructs Broker not to file this Listing with MLS",
            "databaseStored": "LANDLORD_INSTRUCTS_BROKER_NOT_TO_FILE_THIS_LISTING_WITH_MLS"
          }
        ],
        "minSelected": 1
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_15",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_73",
        "linked_form_fields_text": [
          "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_74"
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Broker Listing Filing Instructions",
      "description": "Instructions regarding the filing of the listing with Multiple Listing Services (MLS) and any restrictions on filing.",
      "attribute": "listing_filing_instructions",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": "Enter details regarding filing instructions and purposes",
      "special_input": {
        "text_area": {}
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text-area",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_16",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_16",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_16",
            "displayName": "Broker is authorized to place a keybox on the Property"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_17",
            "displayName": "Broker is not authorized to place a keybox on the Property"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Keybox Authorization Options",
      "description": null,
      "attribute": "keybox_authorization",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Broker is authorized to place a keybox on the Property",
            "databaseStored": "BROKER_IS_AUTHORIZED_TO_PLACE_A_KEYBOX_ON_THE_PROPERTY"
          },
          {
            "display_name": "Broker is not authorized to place a keybox on the Property",
            "databaseStored": "BROKER_IS_NOT_AUTHORIZED_TO_PLACE_A_KEYBOX_ON_THE_PROPERTY"
          }
        ],
        "minSelected": 1
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_17",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_18",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_18",
            "displayName": "Broker Represents Tenant"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_19",
            "displayName": "Broker Represents Buyer"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Intermediary Status Options",
      "description": null,
      "attribute": "intermediary_status",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "green",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Broker Represents Tenant",
            "databaseStored": "BROKER_REPRESENTS_TENANT"
          },
          {
            "display_name": "Broker Represents Buyer",
            "databaseStored": "BROKER_REPRESENTS_BUYER"
          }
        ],
        "minSelected": 1
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_18",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1010",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1010",
            "displayName": "Landlord does not want this Listing to be displayed on the Internet."
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1011",
            "displayName": "Landlord does not want the address of the Property to be displayed on the Internet."
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Listing Display Preferences",
      "description": null,
      "attribute": "listing_display_preferences",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Landlord does not want this Listing to be displayed on the Internet.",
            "databaseStored": "LANDLORD_DOES_NOT_WANT_THIS_LISTING_TO_BE_DISPLAYED_ON_THE_INTERNET"
          },
          {
            "display_name": "Landlord does not want the address of the Property to be displayed on the Internet.",
            "databaseStored": "LANDLORD_DOES_NOT_WANT_THE_ADDRESS_OF_THE_PROPERTY_TO_BE_DISPLAYED_ON_THE_INTERNET"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_19",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_20",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_20",
            "displayName": "Broker may not arrange for contractors to make repairs or alterations to the Property."
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_21",
            "displayName": "Broker may arrange for contractors to make repairs or alterations to the Property, with cost limitations."
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Broker Repair Authorization Options",
      "description": null,
      "attribute": "repair_authorization",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Broker may not arrange for contractors to make repairs or alterations to the Property.",
            "databaseStored": "BROKER_MAY_NOT_ARRANGE_FOR_CONTRACTORS_TO_MAKE_REPAIRS_OR_ALTERATIONS_TO_THE_PROPERTY"
          },
          {
            "display_name": "Broker may arrange for contractors to make repairs or alterations to the Property, with cost limitations.",
            "databaseStored": "BROKER_MAY_ARRANGE_FOR_CONTRACTORS_TO_MAKE_REPAIRS_OR_ALTERATIONS_TO_THE_PROPERTY_WITH_COST_LIMITATIONS"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_20",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_22",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_22",
            "displayName": "Pay the contractors directly and pay Broker a service fee upon receipt of the contractors' and Broker's invoices."
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_23",
            "displayName": "Reimburse Broker for the costs incurred for any repairs or alterations and pay Broker a service fee upon receipt of Broker's invoice."
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Broker Payment Options for Contractor Services",
      "description": null,
      "attribute": "broker_payment_options",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Pay the contractors directly and pay Broker a service fee upon receipt of the contractors' and Broker's invoices.",
            "databaseStored": "PAY_THE_CONTRACTORS_DIRECTLY_AND_PAY_BROKER_A_SERVICE_FEE_UPON_RECEIPT_OF_THE_CONTRACTORS_AND_BROKERS_INVOICES"
          },
          {
            "display_name": "Reimburse Broker for the costs incurred for any repairs or alterations and pay Broker a service fee upon receipt of Broker's invoice.",
            "databaseStored": "REIMBURSE_BROKER_FOR_THE_COSTS_INCURRED_FOR_ANY_REPAIRS_OR_ALTERATIONS_AND_PAY_BROKER_A_SERVICE_FEE_UPON_RECEIPT_OF_BROKERS_INVOICE"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_21",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_96",
        "linked_form_fields_text": [
          "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_97"
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Property Exceptions and Conditions",
      "description": null,
      "attribute": "property_exceptions_conditions",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "text_area": {}
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "text-area",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_22",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_98",
        "linked_form_fields_text": [
          "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_99",
          "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_100"
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Property Condition and Information Disclosure",
      "description": null,
      "attribute": "property_condition_info",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "text_area": {
          "rows": 4
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text-area",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_23",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_24",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_24",
            "displayName": "Information About Brokerage Services"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_25",
            "displayName": "Addendum Regarding Rental Flood Disclosure"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_26",
            "displayName": "Addendum Regarding Lead-Based Paint"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_27",
            "displayName": "Request for Information from an Owners' Association"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_28",
            "displayName": "Information about Special Flood Hazard Areas"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_29",
            "displayName": "Condominium Addendum to Listing"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_30",
            "displayName": "Keybox Authorization by Tenant"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_31",
            "displayName": "Information about On-Site Sewer Facility"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_32",
            "displayName": "IRS Forms (W-9 or W-8)"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_49",
            "displayName": "Owner's Authorization Concerning Unescorted Access to Property"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_50",
            "displayName": "General Information for Landlord Regarding Assistance Animals"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_48",
            "displayName": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_48"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Required Addenda and Documents for Landlord",
      "description": null,
      "attribute": "addenda_documents",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 3
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Information About Brokerage Services",
            "databaseStored": "INFORMATION_ABOUT_BROKERAGE_SERVICES"
          },
          {
            "display_name": "Addendum Regarding Rental Flood Disclosure",
            "databaseStored": "ADDENDUM_REGARDING_RENTAL_FLOOD_DISCLOSURE"
          },
          {
            "display_name": "Addendum Regarding Lead-Based Paint",
            "databaseStored": "ADDENDUM_REGARDING_LEAD_BASED_PAINT"
          },
          {
            "display_name": "Request for Information from an Owners' Association",
            "databaseStored": "REQUEST_FOR_INFORMATION_FROM_AN_OWNERS_ASSOCIATION"
          },
          {
            "display_name": "Information about Special Flood Hazard Areas",
            "databaseStored": "INFORMATION_ABOUT_SPECIAL_FLOOD_HAZARD_AREAS"
          },
          {
            "display_name": "Condominium Addendum to Listing",
            "databaseStored": "CONDOMINIUM_ADDENDUM_TO_LISTING"
          },
          {
            "display_name": "Keybox Authorization by Tenant",
            "databaseStored": "KEYBOX_AUTHORIZATION_BY_TENANT"
          },
          {
            "display_name": "Information about On-Site Sewer Facility",
            "databaseStored": "INFORMATION_ABOUT_ON_SITE_SEWER_FACILITY"
          },
          {
            "display_name": "IRS Forms (W-9 or W-8)",
            "databaseStored": "IRS_FORMS_W_9_OR_W_8"
          },
          {
            "display_name": "Owner's Authorization Concerning Unescorted Access to Property",
            "databaseStored": "OWNERS_AUTHORIZATION_CONCERNING_UNESCORTED_ACCESS_TO_PROPERTY"
          },
          {
            "display_name": "General Information for Landlord Regarding Assistance Animals",
            "databaseStored": "GENERAL_INFORMATION_FOR_LANDLORD_REGARDING_ASSISTANCE_ANIMALS"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_24",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_33",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_33",
            "displayName": "Monthly Rent Due on the First Day of the Month"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_34",
            "displayName": "Animals Permitted with Restrictions"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Lease Requirements by Landlord",
      "description": null,
      "attribute": "lease_requirements",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Monthly Rent Due on the First Day of the Month",
            "databaseStored": "MONTHLY_RENT_DUE_ON_THE_FIRST_DAY_OF_THE_MONTH"
          },
          {
            "display_name": "Animals Permitted with Restrictions",
            "databaseStored": "ANIMALS_PERMITTED_WITH_RESTRICTIONS"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_25",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_35",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_35",
            "displayName": "Initial Late Charge"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_36",
            "displayName": "Additional Late Charges"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Lease Terms Options",
      "description": null,
      "attribute": "lease_terms",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Initial Late Charge",
            "databaseStored": "INITIAL_LATE_CHARGE"
          },
          {
            "display_name": "Additional Late Charges",
            "databaseStored": "ADDITIONAL_LATE_CHARGES"
          },
          {
            "display_name": "Animals Not Permitted"
          },
          {
            "display_name": "Animals Permitted with Restrictions"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_26",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_37",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_37",
            "displayName": "Animals Not Permitted"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_38",
            "displayName": "Animals Permitted with Restrictions"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Animal Policy Options",
      "description": null,
      "attribute": "animal_policy",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Animals Not Permitted",
            "databaseStored": "ANIMALS_NOT_PERMITTED"
          },
          {
            "display_name": "Animals Permitted with Restrictions",
            "databaseStored": "ANIMALS_PERMITTED_WITH_RESTRICTIONS"
          }
        ],
        "minSelected": 1
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_27",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_57",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_57",
            "displayName": "Animal Deposit Required"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_59",
            "displayName": "Increased Monthly Rent"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_58",
            "displayName": "One-Time Non-Refundable Payment"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Animal Charges and Restrictions",
      "description": null,
      "attribute": "animal_charges_restrictions",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 3
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Animal Deposit Required",
            "databaseStored": "ANIMAL_DEPOSIT_REQUIRED"
          },
          {
            "display_name": "Increased Monthly Rent",
            "databaseStored": "INCREASED_MONTHLY_RENT"
          },
          {
            "display_name": "One-Time Non-Refundable Payment",
            "databaseStored": "ONE_TIME_NON_REFUNDABLE_PAYMENT"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_28",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_39",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_39",
            "displayName": "Landlord"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_40",
            "displayName": "Tenant"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_41",
            "displayName": "Contractor chosen and paid by Tenant"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1003",
            "displayName": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1003"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Maintenance Responsibilities for Property",
      "description": null,
      "attribute": "maintenance_responsibilities",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Landlord",
            "databaseStored": "LANDLORD"
          },
          {
            "display_name": "Tenant",
            "databaseStored": "TENANT"
          },
          {
            "display_name": "Contractor chosen and paid by Tenant",
            "databaseStored": "CONTRACTOR_CHOSEN_AND_PAID_BY_TENANT"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_29",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_42",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_42",
            "displayName": "Yard Maintenance by Landlord"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_43",
            "displayName": "Yard Maintenance by Tenant"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_44",
            "displayName": "Yard Maintenance by Contractor"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1001",
            "displayName": "Pool/Spa Maintenance by Landlord"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1002",
            "displayName": "Pool/Spa Maintenance by Tenant"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Maintenance Responsibilities for Property",
      "description": null,
      "attribute": "maintenance_responsibilities",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 3
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Yard Maintenance by Landlord",
            "databaseStored": "YARD_MAINTENANCE_BY_LANDLORD"
          },
          {
            "display_name": "Yard Maintenance by Tenant",
            "databaseStored": "YARD_MAINTENANCE_BY_TENANT"
          },
          {
            "display_name": "Yard Maintenance by Contractor",
            "databaseStored": "YARD_MAINTENANCE_BY_CONTRACTOR"
          },
          {
            "display_name": "Pool/Spa Maintenance by Landlord",
            "databaseStored": "POOLSPA_MAINTENANCE_BY_LANDLORD"
          },
          {
            "display_name": "Pool/Spa Maintenance by Tenant",
            "databaseStored": "POOLSPA_MAINTENANCE_BY_TENANT"
          },
          {
            "display_name": "Pool/Spa Maintenance by Contractor"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_30",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1005",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1005",
            "displayName": "Fees if procured by tenant"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1007",
            "displayName": "Fees if procured by landlord"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Tenant and Landlord Fee Responsibilities",
      "description": null,
      "attribute": "tenant_landlord_fees",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Fees if procured by tenant",
            "databaseStored": "FEES_IF_PROCURED_BY_TENANT"
          },
          {
            "display_name": "Fees if procured by landlord",
            "databaseStored": "FEES_IF_PROCURED_BY_LANDLORD"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_31",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1004",
        "linked_form_fields_checkbox": [
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1004",
            "displayName": "If procured by tenant"
          },
          {
            "checkboxField": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_1006",
            "displayName": "If procured by landlord"
          }
        ]
      }
    ],
    "display_attributes": {
      "display_name": "Tenant and Landlord Fee Responsibility Options",
      "description": null,
      "attribute": "tenant_landlord_fee_responsibility",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "If procured by tenant",
            "databaseStored": "IF_PROCURED_BY_TENANT"
          },
          {
            "display_name": "If procured by landlord",
            "databaseStored": "IF_PROCURED_BY_LANDLORD"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_32",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_36"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_58"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_71"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_78"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_83"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_89"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_104"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_108"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_131"
      },
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_161"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Compensation Amount",
      "description": "Enter the broker compensation amount for the lease agreement.",
      "attribute": "broker_compensation_amount",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter amount",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_33",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_3"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord Address Information",
      "description": null,
      "attribute": "landlord_address",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": "Enter the landlord's address",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_34",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_4"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord City, State, and Zip Code",
      "description": null,
      "attribute": "landlord_city_state_zip",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": "Enter City, State, and Zip Code",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_35",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_5"
      }
    ],
    "display_attributes": {
      "display_name": "Contact Phone Number for Parties",
      "description": null,
      "attribute": "contact_phone",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_36",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_6"
      }
    ],
    "display_attributes": {
      "display_name": "Mobile Phone Number for Parties",
      "description": null,
      "attribute": "mobile_phone",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_37",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_7"
      }
    ],
    "display_attributes": {
      "display_name": "Contact Information for Parties",
      "description": null,
      "attribute": "contact_info",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "input_options": {
        "type": "email_or_fax",
        "label": "E-Mail/Fax Number"
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_38",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_10"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Address Information",
      "description": null,
      "attribute": "broker_address",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_39",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_11"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's City, State, and Zip Code",
      "description": null,
      "attribute": "broker_city_state_zip",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_40",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_12"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Contact Phone Number",
      "description": null,
      "attribute": "broker_contact_phone",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_41",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_13"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Mobile Phone Number",
      "description": null,
      "attribute": "broker_mobile_phone",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_42",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_14"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Contact Information - E-Mail/Fax Number",
      "description": null,
      "attribute": "broker_contact_email_fax",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_43",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_16"
      }
    ],
    "display_attributes": {
      "display_name": "Property Land Lot Description",
      "description": null,
      "attribute": "land_lot_description",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter Lot, Block, Addition, City, County, and Address",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_44",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_18"
      }
    ],
    "display_attributes": {
      "display_name": "Property Land Description",
      "description": null,
      "attribute": "property_land_description",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "max_length": 500,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_45",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_19"
      }
    ],
    "display_attributes": {
      "display_name": "Property Land and Non-Real Estate Description",
      "description": null,
      "attribute": "property_description",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text-area",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_46",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_20"
      }
    ],
    "display_attributes": {
      "display_name": "Property Location and Description",
      "description": null,
      "attribute": "property_location_description",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter Lot, Block, Addition, City, County, and Address",
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 500,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_47",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_21"
      }
    ],
    "display_attributes": {
      "display_name": "Property Address and Zip Code",
      "description": null,
      "attribute": "property_address_zip",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter property address and zip code",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_48",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_22"
      }
    ],
    "display_attributes": {
      "display_name": "Property Address Identification",
      "description": null,
      "attribute": "property_address",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter property address",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_49",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_28"
      }
    ],
    "display_attributes": {
      "display_name": "Monthly Rental Price for Property Listing",
      "description": null,
      "attribute": "listing_price",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter monthly rental price",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_50",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_29"
      }
    ],
    "display_attributes": {
      "display_name": "Listing Price and Lease Term Details",
      "description": null,
      "attribute": "listing_price_and_lease_term",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "fields": [
        {
          "field_name": "listing_price",
          "display_name": "Monthly Rental Price"
        },
        {
          "field_name": "lease_term_min",
          "display_name": "Minimum Lease Term (Months)"
        },
        {
          "field_name": "lease_term_max",
          "display_name": "Maximum Lease Term (Months)"
        },
        {
          "field_name": "listing_start_date",
          "display_name": "Listing Start Date"
        },
        {
          "field_name": "listing_end_date",
          "display_name": "Listing End Date"
        }
      ],
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_51",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_30"
      }
    ],
    "display_attributes": {
      "display_name": "Lease Term Duration",
      "description": null,
      "attribute": "lease_term_duration",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 10,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_52",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_31"
      }
    ],
    "display_attributes": {
      "display_name": "Listing Term Start Date",
      "description": null,
      "attribute": "listing_term_start_date",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter start date",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_53",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_32"
      }
    ],
    "display_attributes": {
      "display_name": "Listing Price and Term Details",
      "description": null,
      "attribute": "listing_price_and_term",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "fields": [
        {
          "field_name": "listing_price",
          "display_name": "Monthly Rental Price"
        },
        {
          "field_name": "lease_term",
          "display_name": "Lease Term (Months)"
        },
        {
          "field_name": "listing_start_date",
          "display_name": "Listing Start Date"
        }
      ],
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_54",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_33"
      }
    ],
    "display_attributes": {
      "display_name": "Listing Term Start Date",
      "description": null,
      "attribute": "listing_term_start_date",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter start date",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_55",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_34"
      }
    ],
    "display_attributes": {
      "display_name": "Listing Term Start Date",
      "description": null,
      "attribute": "listing_term_start_date",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter start date",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_56",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_35"
      }
    ],
    "display_attributes": {
      "display_name": "Listing Term Start Date",
      "description": null,
      "attribute": "listing_term_start_date",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter start date",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_57",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_37"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Fee Percentage for Other Broker",
      "description": null,
      "attribute": "broker_fee_percentage",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter percentage",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_58",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_38"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Fee Percentage for Lease",
      "description": null,
      "attribute": "broker_fee_percentage",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 5,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_59",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_39"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Fee Percentage for Lease",
      "description": "Percentage of the broker's fee to be paid under the lease agreement.",
      "attribute": "broker_fee_percentage",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_60",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_41"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Compensation Structure for Tenant Representation",
      "description": null,
      "attribute": "broker_compensation_structure",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "text": {
          "maxLength": 100
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Percentage of One Month's Rent"
          },
          {
            "display_name": "Percentage of All Rents"
          },
          {
            "display_name": "Flat Fee"
          }
        ],
        "minSelected": 1
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_61",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_43"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Compensation Fee Structure",
      "description": null,
      "attribute": "broker_compensation_fee",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 10,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_62",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_45"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Compensation Fee Structure",
      "description": null,
      "attribute": "broker_compensation_fee",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "input_options": {
        "label": "Flat Fee Amount",
        "minLength": 1,
        "maxLength": 10
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_63",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_47"
      }
    ],
    "display_attributes": {
      "display_name": "Compensation Structure for Subagent Broker",
      "description": null,
      "attribute": "subagent_compensation",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 3
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "input_options": {
        "fields": [
          {
            "display_name": "Percentage of One Month's Rent"
          },
          {
            "display_name": "Percentage of All Rents"
          },
          {
            "display_name": "Flat Fee"
          }
        ]
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_64",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_49"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Compensation Structure for Other Broker",
      "description": null,
      "attribute": "broker_compensation_structure",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 100,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_65",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_51"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Compensation Structure for Other Broker Representation",
      "description": null,
      "attribute": "broker_compensation_structure",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "text": {
          "maxLength": 100
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_66",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_52"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Fee Percentage",
      "description": "Percentage of the fee to be paid to the Broker based on the rental agreement.",
      "attribute": "broker_fee_percentage",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter percentage",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_67",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_53"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Fee Percentage for Lease",
      "description": null,
      "attribute": "brokers_fee_percentage",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter percentage",
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 5,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_68",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_54"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Fee Amount",
      "description": "Amount to be paid to Broker for services rendered under the lease agreement.",
      "attribute": "broker_fee_amount",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Insert amount to be paid to Broker",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_69",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_55"
      }
    ],
    "display_attributes": {
      "display_name": "Broker and Landlord Identification",
      "description": null,
      "attribute": "broker_landlord_identification",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter names of Broker and Landlord",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_70",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_56"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Compensation Acknowledgment",
      "description": null,
      "attribute": "broker_compensation_acknowledgment",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 100,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_71",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_57"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Compensation Earned Acknowledgment",
      "description": "Acknowledgment of conditions under which the broker's compensation is considered earned.",
      "attribute": "broker_compensation_earned",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 100,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_72",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_59"
      }
    ],
    "display_attributes": {
      "display_name": "Compensation for Renewal Percentage",
      "description": "Percentage of one full month's rent to be paid under the renewal or extension of the lease.",
      "attribute": "compensation_for_renewal_percentage",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": null,
        "color_theme": null
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_73",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_60"
      }
    ],
    "display_attributes": {
      "display_name": "Percentage of Rents for Renewal Agreement",
      "description": null,
      "attribute": "percentage_of_rents_renewal",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "none",
        "color_theme": "none"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 10,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_74",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_61"
      }
    ],
    "display_attributes": {
      "display_name": "Compensation for Renewal - Rent Percentage",
      "description": null,
      "attribute": "compensation_for_renewal_rent_percentage",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": null,
        "color_theme": null
      },
      "width": 12,
      "placeholder": "Enter percentage of all rents",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_75",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_62"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Compensation Percentage for Sale",
      "description": null,
      "attribute": "broker_compensation_percentage_sale",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_76",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_63"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Compensation Percentage for Sale",
      "description": null,
      "attribute": "broker_compensation_percentage_sale",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_77",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_64"
      }
    ],
    "display_attributes": {
      "display_name": "Reimbursable Expenses Details",
      "description": null,
      "attribute": "reimbursable_expenses",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": "Enter reimbursable expenses",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_78",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_65"
      }
    ],
    "display_attributes": {
      "display_name": "Protection Period Duration",
      "description": "Duration of the protection period starting after the listing ends.",
      "attribute": "protection_period_duration",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter number of days",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_79",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_68"
      }
    ],
    "display_attributes": {
      "display_name": "County for Payment to Broker",
      "description": null,
      "attribute": "county_payment",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": "Enter County",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_80",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_69"
      }
    ],
    "display_attributes": {
      "display_name": "County for Payment to Broker",
      "description": null,
      "attribute": "county_payment",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": "Enter County",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_81",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_70"
      }
    ],
    "display_attributes": {
      "display_name": "County for Payment to Broker",
      "description": null,
      "attribute": "county_payment",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter County Name",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_82",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_72"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Listing Filing Instructions",
      "description": "Instructions regarding the filing of the listing with Multiple Listing Services (MLS) and any specific conditions set by the landlord.",
      "attribute": "listing_filing_instructions",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter number of days",
      "special_input": {
        "text": {}
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Broker will file this Listing with MLS"
          },
          {
            "display_name": "Landlord instructs Broker not to file this Listing until specified days"
          }
        ],
        "minSelected": 1
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_83",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_75"
      }
    ],
    "display_attributes": {
      "display_name": "Identification of Broker and Landlord",
      "description": null,
      "attribute": "identification",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 100,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_84",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_76"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord Identification Initials",
      "description": null,
      "attribute": "landlord_initials",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_85",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_77"
      }
    ],
    "display_attributes": {
      "display_name": "Identification Initials for Broker and Landlord",
      "description": null,
      "attribute": "identification_initials",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_86",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_79"
      }
    ],
    "display_attributes": {
      "display_name": "Authorized Scheduling Companies for Property Access",
      "description": null,
      "attribute": "scheduling_companies",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_87",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_80"
      }
    ],
    "display_attributes": {
      "display_name": "Identification of Broker/Associate and Landlord",
      "description": null,
      "attribute": "broker_associate_landlord_identification",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_88",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_81"
      }
    ],
    "display_attributes": {
      "display_name": "Identification of Broker/Associate and Landlord",
      "description": null,
      "attribute": "broker_associate_landlord_identification",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_89",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_82"
      }
    ],
    "display_attributes": {
      "display_name": "Identification of Broker/Associate and Landlord",
      "description": null,
      "attribute": "broker_associate_landlord_identification",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_90",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_86"
      }
    ],
    "display_attributes": {
      "display_name": "Broker and Landlord Identification",
      "description": null,
      "attribute": "broker_landlord_identification",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_91",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_87"
      }
    ],
    "display_attributes": {
      "display_name": "Identification for Broker and Landlord",
      "description": null,
      "attribute": "identification",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_92",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_88"
      }
    ],
    "display_attributes": {
      "display_name": "Broker and Landlord Identification",
      "description": null,
      "attribute": "broker_landlord_identification",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_93",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_90"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Service Fee for Repairs or Alterations",
      "description": null,
      "attribute": "broker_service_fee",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter service fee amount",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_94",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_91"
      }
    ],
    "display_attributes": {
      "display_name": "Payment Instructions for Contractor Services",
      "description": null,
      "attribute": "contractor_payment_instructions",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 255,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_95",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_92"
      }
    ],
    "display_attributes": {
      "display_name": "Broker Service Fee for Repairs or Alterations",
      "description": null,
      "attribute": "broker_service_fee",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter service fee amount",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_96",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_93"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Repair and Reimbursement Terms",
      "description": null,
      "attribute": "broker_repair_reimbursement",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 255,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_97",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_94"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord Financial Obligations and Liens",
      "description": null,
      "attribute": "financial_obligations_and_liens",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": "Specify any exceptions to financial obligations or liens",
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "maxLength": 500,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_98",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_95"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord's Knowledge of Liens and Encumbrances",
      "description": null,
      "attribute": "landlord_liens_encumbrances",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Specify any known liens or encumbrances",
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "maxLength": 500,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_99",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_101"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord Acknowledgment of Property Conditions",
      "description": null,
      "attribute": "landlord_conditions_acknowledgment",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 500,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_100",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_102"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord Condition Acknowledgment",
      "description": null,
      "attribute": "landlord_condition_acknowledgment",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": "Describe any known conditions affecting the property",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_101",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_103"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord's Acknowledgment of Property Conditions",
      "description": null,
      "attribute": "landlord_conditions_acknowledgment",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": "Describe any known conditions affecting the property",
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 500,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_102",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_105"
      }
    ],
    "display_attributes": {
      "display_name": "Identification of Broker and Landlord",
      "description": null,
      "attribute": "broker_landlord_identification",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter names of Broker and Landlord",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_103",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_106"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord Identification for Default Clause",
      "description": null,
      "attribute": "landlord_identification",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_104",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_107"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord Identification for Default Clause",
      "description": null,
      "attribute": "landlord_identification",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_105",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_111"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord Information Regarding Assistance Animals",
      "description": null,
      "attribute": "landlord_assistance_animals_info",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_106",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_112"
      }
    ],
    "display_attributes": {
      "display_name": "Monthly Rent Payment Details",
      "description": null,
      "attribute": "monthly_rent_details",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "validation": {
        "required": true,
        "pattern": "^[0-9]+(\\.[0-9]{1,2})?$",
        "error_message": "Please enter a valid rent amount."
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_107",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_113"
      }
    ],
    "display_attributes": {
      "display_name": "Lease Requirements by Landlord",
      "description": null,
      "attribute": "lease_requirements",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "maxLength": 500,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_108",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_114"
      }
    ],
    "display_attributes": {
      "display_name": "Initial Late Charge Amount",
      "description": null,
      "attribute": "initial_late_charge",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_109",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_115"
      }
    ],
    "display_attributes": {
      "display_name": "Late Charges and Additional Fees",
      "description": null,
      "attribute": "late_charges",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "input_options": {
        "fields": [
          {
            "label": "Initial Late Charge",
            "placeholder": "Enter amount"
          },
          {
            "label": "Additional Late Charges",
            "placeholder": "Enter amount per day"
          }
        ]
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_110",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_116"
      }
    ],
    "display_attributes": {
      "display_name": "Late Charge Percentage for Rent",
      "description": null,
      "attribute": "late_charge_percentage",
      "order": 1,
      "block": "Lease Requirements by Landlord",
      "block_style": {
        "title": "Lease Requirements by Landlord",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_111",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_117"
      }
    ],
    "display_attributes": {
      "display_name": "Animal Policy and Restrictions",
      "description": null,
      "attribute": "animal_policy",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "maxLength": 500,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_112",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_118"
      }
    ],
    "display_attributes": {
      "display_name": "Animal Policy and Restrictions",
      "description": null,
      "attribute": "animal_policy",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 2
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Not Permitted"
          },
          {
            "display_name": "Permitted with Restrictions"
          }
        ],
        "minSelected": 1
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_113",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_120"
      }
    ],
    "display_attributes": {
      "display_name": "Animal Deposit Requirements",
      "description": null,
      "attribute": "animal_deposit_requirements",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "maxLength": null,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_114",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_122"
      }
    ],
    "display_attributes": {
      "display_name": "Animal Deposit and Charges Information",
      "description": null,
      "attribute": "animal_deposit_charges",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "text": {}
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_115",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_124"
      }
    ],
    "display_attributes": {
      "display_name": "Animal Policy and Charges",
      "description": null,
      "attribute": "animal_policy",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "text": {}
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_116",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_125"
      }
    ],
    "display_attributes": {
      "display_name": "Animal Deposit and Violation Charges",
      "description": null,
      "attribute": "animal_deposit_violation_charges",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "input_options": {
        "fields": [
          {
            "label": "Animal Deposit Amount",
            "placeholder": "Enter amount"
          },
          {
            "label": "Monthly Rent Increase",
            "placeholder": "Enter amount"
          },
          {
            "label": "One-Time Non-Refundable Payment",
            "placeholder": "Enter amount"
          },
          {
            "label": "Initial Animal Violation Charge",
            "placeholder": "Enter amount"
          },
          {
            "label": "Daily Charge Thereafter",
            "placeholder": "Enter amount"
          }
        ]
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_117",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_126"
      }
    ],
    "display_attributes": {
      "display_name": "Animal Charges and Fees Information",
      "description": null,
      "attribute": "animal_charges_fees",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "input_options": {
        "fields": [
          {
            "label": "Animal Deposit Amount",
            "placeholder": "Enter amount"
          },
          {
            "label": "Monthly Rent Increase",
            "placeholder": "Enter amount"
          },
          {
            "label": "One-Time Non-Refundable Payment",
            "placeholder": "Enter amount"
          },
          {
            "label": "Initial Animal Violation Charge",
            "placeholder": "Enter amount"
          },
          {
            "label": "Daily Violation Charge",
            "placeholder": "Enter amount"
          }
        ]
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_118",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_127"
      }
    ],
    "display_attributes": {
      "display_name": "Security Deposit Amount",
      "description": null,
      "attribute": "security_deposit",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_119",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_128"
      }
    ],
    "display_attributes": {
      "display_name": "Security Deposit Amount",
      "description": null,
      "attribute": "security_deposit",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_120",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_129"
      }
    ],
    "display_attributes": {
      "display_name": "Security Deposit Amount",
      "description": null,
      "attribute": "security_deposit",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_121",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_130"
      }
    ],
    "display_attributes": {
      "display_name": "Security Deposit Amount",
      "description": null,
      "attribute": "security_deposit",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_122",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_132"
      }
    ],
    "display_attributes": {
      "display_name": "Utilities Payment Responsibilities",
      "description": null,
      "attribute": "utilities_payment",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_123",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_133"
      }
    ],
    "display_attributes": {
      "display_name": "Guest Stay Duration on Property",
      "description": null,
      "attribute": "guest_stay_duration",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter number of days",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_124",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_134"
      }
    ],
    "display_attributes": {
      "display_name": "Permitted Vehicle Count on Property",
      "description": null,
      "attribute": "vehicle_count",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter number of vehicles",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_125",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_135"
      }
    ],
    "display_attributes": {
      "display_name": "Trip Charge Information",
      "description": null,
      "attribute": "trip_charge",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "maxLength": 10,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_126",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_136"
      }
    ],
    "display_attributes": {
      "display_name": "Keybox Authorization Details",
      "description": "Information regarding keybox authorization during the lease period and associated fees.",
      "attribute": "keybox_authorization",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "maxLength": 50,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_127",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_137"
      }
    ],
    "display_attributes": {
      "display_name": "Keybox Authorization and Early Withdrawal Fee",
      "description": null,
      "attribute": "keybox_authorization",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "maxLength": 50,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_128",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_138"
      }
    ],
    "display_attributes": {
      "display_name": "Inventory and Condition Form Delivery Timeline",
      "description": null,
      "attribute": "inventory_condition_form_delivery_days",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 10,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_129",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_140"
      }
    ],
    "display_attributes": {
      "display_name": "Yard Maintenance Responsibility",
      "description": null,
      "attribute": "yard_maintenance",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Landlord"
          },
          {
            "display_name": "Tenant"
          },
          {
            "display_name": "Contractor chosen and paid by Tenant"
          }
        ],
        "minSelected": 1
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_130",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_142"
      }
    ],
    "display_attributes": {
      "display_name": "Pool/Spa Maintenance Responsibility",
      "description": null,
      "attribute": "pool_spa_maintenance",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Landlord"
          },
          {
            "display_name": "Tenant"
          },
          {
            "display_name": "Contractor chosen and paid by Tenant"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_131",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_144"
      }
    ],
    "display_attributes": {
      "display_name": "Pool/Spa Maintenance Responsibility",
      "description": null,
      "attribute": "pool_spa_maintenance",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 3
        }
      },
      "isCached": false,
      "isRequired": false,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Landlord"
          },
          {
            "display_name": "Tenant"
          },
          {
            "display_name": "Contractor (paid by Tenant)"
          }
        ],
        "minSelected": 0
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_132",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_145"
      }
    ],
    "display_attributes": {
      "display_name": "Emergency Repair Contact Information",
      "description": null,
      "attribute": "emergency_repair_contact",
      "order": 1,
      "block": "Property Details",
      "block_style": {
        "title": "Property Details",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 255,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_133",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_146"
      }
    ],
    "display_attributes": {
      "display_name": "Repair Contact Information and Exclusions",
      "description": null,
      "attribute": "repair_info",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text-area",
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_134",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_147"
      }
    ],
    "display_attributes": {
      "display_name": "Special Provisions and Additional Terms",
      "description": null,
      "attribute": "special_provisions",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter any special provisions or additional terms here",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_135",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_148"
      }
    ],
    "display_attributes": {
      "display_name": "Special Provisions for Lease Agreement",
      "description": null,
      "attribute": "special_provisions",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": "Enter any special provisions or terms here",
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_136",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_149"
      }
    ],
    "display_attributes": {
      "display_name": "Assignment and Replacement Tenant Fees",
      "description": null,
      "attribute": "tenant_fees",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "input_options": {
        "fields": [
          {
            "label": "If procured by tenant:",
            "placeholder": "Amount or percentage"
          },
          {
            "label": "If procured by landlord:",
            "placeholder": "Amount or percentage"
          }
        ]
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_137",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_151"
      }
    ],
    "display_attributes": {
      "display_name": "Assignment, Subletting, and Replacement Tenant Fees",
      "description": null,
      "attribute": "tenant_fees",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "input_options": {
        "fields": [
          {
            "label": "If procured by tenant",
            "placeholder": "Amount"
          },
          {
            "label": "If procured by landlord",
            "placeholder": "Amount"
          }
        ]
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_138",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_153"
      }
    ],
    "display_attributes": {
      "display_name": "Assignment and Subletting Tenant Fees",
      "description": null,
      "attribute": "tenant_fees",
      "order": 1,
      "block": "Lease Requirements",
      "block_style": {
        "title": "Lease Requirements",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "input_options": {
        "fields": [
          {
            "label": "If procured by tenant",
            "placeholder": "Amount"
          },
          {
            "label": "If procured by landlord",
            "placeholder": "Amount"
          }
        ]
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_139",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_155"
      }
    ],
    "display_attributes": {
      "display_name": "Assignment, Subletting and Replacement Tenant Fees",
      "description": null,
      "attribute": "assignment_subletting_replacement_fees",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "fields": [
        {
          "label": "If procured by tenant",
          "input_type": "text",
          "placeholder": "Amount or Percentage"
        },
        {
          "label": "If procured by landlord",
          "input_type": "text",
          "placeholder": "Amount or Percentage"
        }
      ],
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_140",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_156"
      }
    ],
    "display_attributes": {
      "display_name": "Additional Tenant Fees and Provisions",
      "description": null,
      "attribute": "additional_tenant_fees",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "maxLength": 500,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_141",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_157"
      }
    ],
    "display_attributes": {
      "display_name": "Other Assignment and Replacement Tenant Fees",
      "description": null,
      "attribute": "other_assignment_replacement_fees",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_142",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_158"
      }
    ],
    "display_attributes": {
      "display_name": "Identification of Broker and Landlord",
      "description": null,
      "attribute": "broker_landlord_identification",
      "order": 1,
      "block": "Additional Notices",
      "block_style": {
        "title": "Additional Notices",
        "icon": null,
        "color_theme": null
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_143",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_159"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord Identification for Broker Services",
      "description": null,
      "attribute": "landlord_identification",
      "order": 1,
      "block": "Additional Notices",
      "block_style": {
        "title": "Additional Notices",
        "icon": null,
        "color_theme": null
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_144",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_160"
      }
    ],
    "display_attributes": {
      "display_name": "Identification for Broker and Landlord",
      "description": null,
      "attribute": "identification",
      "order": 1,
      "block": "Other Compensation",
      "block_style": {
        "title": "Other Compensation",
        "icon": "None",
        "color_theme": "None"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_145",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_162"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord's Printed Name",
      "description": null,
      "attribute": "landlord_printed_name",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_146",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_163"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Printed Name",
      "description": null,
      "attribute": "brokers_printed_name",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_147",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_164"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord and Broker Signatures with Dates",
      "description": null,
      "attribute": "signatures_with_dates",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "fields": [
        {
          "field_name": "landlord_signature_date",
          "display_name": "Landlord's Signature Date"
        },
        {
          "field_name": "broker_signature_date",
          "display_name": "Broker's Signature Date"
        }
      ],
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_148",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_46"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Signature Confirmation",
      "description": null,
      "attribute": "brokers_signature",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 1
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Broker's Signature"
          }
        ],
        "minSelected": 1
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_149",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_checkbox_47"
      }
    ],
    "display_attributes": {
      "display_name": "Broker and Landlord Signatures",
      "description": null,
      "attribute": "broker_landlord_signatures",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": {
        "checkbox": {
          "horizontal": 1
        }
      },
      "isCached": false,
      "isRequired": true,
      "input_type": "checkbox",
      "checkbox_options": {
        "options": [
          {
            "display_name": "Broker's Signature"
          },
          {
            "display_name": "Broker's Associate's Signature"
          }
        ],
        "minSelected": 1
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_150",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_165"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord's Printed Name",
      "description": null,
      "attribute": "landlord_printed_name",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_151",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_166"
      }
    ],
    "display_attributes": {
      "display_name": "Broker and Landlord Signatures and Printed Names",
      "description": null,
      "attribute": "broker_landlord_signatures",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "fields": [
        {
          "field_name": "broker_printed_name",
          "display_name": "Broker's Printed Name"
        },
        {
          "field_name": "broker_signature",
          "display_name": "Broker's Signature"
        },
        {
          "field_name": "broker_associate_signature",
          "display_name": "Broker's Associate's Signature, as an authorized agent of Broker"
        },
        {
          "field_name": "broker_associate_printed_name",
          "display_name": "Broker's Associate's Printed Name, if applicable"
        },
        {
          "field_name": "landlord_printed_name",
          "display_name": "Landlord's Printed Name"
        },
        {
          "field_name": "landlord_signature",
          "display_name": "Landlord's Signature"
        }
      ],
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_152",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_167"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Printed Name for Listing Agreement",
      "description": null,
      "attribute": "brokers_printed_name",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_153",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_168"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Associate's Printed Name",
      "description": null,
      "attribute": "brokers_associates_printed_name",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_154",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_169"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord's Printed Name",
      "description": null,
      "attribute": "landlord_printed_name",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
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
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_155",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_170"
      }
    ],
    "display_attributes": {
      "display_name": "Broker License Information",
      "description": null,
      "attribute": "broker_license_info",
      "order": 1,
      "block": "Parties Information",
      "block_style": {
        "title": "Parties Information",
        "icon": "user",
        "color_theme": "green"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "maxLength": 50,
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_156",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_171"
      }
    ],
    "display_attributes": {
      "display_name": "Broker and Landlord Identification Information",
      "description": null,
      "attribute": "broker_landlord_info",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "fields": [
        {
          "field_name": "Broker's Printed Name",
          "input_type": "text"
        },
        {
          "field_name": "License No.",
          "input_type": "text"
        },
        {
          "field_name": "Landlord's Printed Name",
          "input_type": "text"
        },
        {
          "field_name": "Landlord's Signature",
          "input_type": "text"
        },
        {
          "field_name": "Date",
          "input_type": "date"
        }
      ],
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_157",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_172"
      }
    ],
    "display_attributes": {
      "display_name": "Landlord's Identification and Signature Information",
      "description": null,
      "attribute": "landlord_signature_info",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": true,
      "input_type": "text",
      "input_options": {
        "fields": [
          {
            "field_name": "Landlord's Printed Name"
          },
          {
            "field_name": "Landlord's Signature"
          }
        ]
      },
      "value": {
        "type": "manual"
      }
    }
  },
  {
    "unique_id": "estate_listing_agreement_exclusive_right_to_lease_158",
    "pdf_attributes": [
      {
        "formType": "residential_real_estate_listing_agreement_exclusive_right_to_lease",
        "formfield": "residential_real_estate_listing_agreement_exclusive_right_to_lease_textfield_173"
      }
    ],
    "display_attributes": {
      "display_name": "Broker's Associate Information",
      "description": null,
      "attribute": "broker_associate_info",
      "order": 1,
      "block": "Broker's Authority",
      "block_style": {
        "title": "Broker's Authority",
        "icon": "home",
        "color_theme": "blue"
      },
      "width": 12,
      "placeholder": null,
      "special_input": null,
      "isCached": false,
      "isRequired": false,
      "input_type": "text",
      "input_options": {
        "label": "Broker's Associate's Printed Name, if applicable",
        "license_number": "License No."
      },
      "value": {
        "type": "manual"
      }
    }
  }
];