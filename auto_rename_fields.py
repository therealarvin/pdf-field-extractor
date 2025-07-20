#!/usr/bin/env python3
"""
Automated PDF Field Renamer based on FIELD_NAMING_GUIDE.md
Renames fields according to best practices without user interaction
"""

import json
import fitz  # PyMuPDF
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple


class AutoFieldRenamer:
    def __init__(self, json_path: str, pdf_path: str):
        self.json_path = json_path
        self.pdf_path = pdf_path
        self.fields_data = self.load_fields_data()
        self.renamed_fields = {}
        
    def load_fields_data(self) -> List[Dict]:
        """Load the extracted fields data from JSON"""
        with open(self.json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def determine_new_name(self, field: Dict) -> str:
        """Determine the new name for a field based on context and naming guide"""
        current_name = field['field_name']
        field_type = field['field_type']
        context_left = field.get('context_left', '').lower()
        context_right = field.get('context_right', '').lower()
        context_above = field.get('context_above', '').lower()
        context_below = field.get('context_below', '').lower()
        page = field.get('page', 0)
        
        # Skip if already well-named
        if current_name.startswith(('client_', 'broker_', 'tenant_', 'property_', 'lease_')):
            return current_name
        
        # Client fields
        if 'Client 1' == current_name:
            return 'client_name_1'
        elif 'Client 2' == current_name:
            return 'client_name_2'
        
        # Address fields for client
        elif current_name == 'Address' and page == 0 and field.get('position', [0])[1] < 200:
            return 'client_address_street'
        elif current_name == 'City State Zip' and page == 0 and field.get('position', [0])[1] < 220:
            return 'client_address_city_state_zip'
        elif current_name == 'Phone' and page == 0 and field.get('position', [0])[1] < 230:
            return 'client_phone_number'
        elif current_name == 'EmailFax' and page == 0:
            return 'client_email'
        elif current_name == 'Email Fax' and page == 0:
            return 'client_fax'
        
        # Broker fields
        elif 'Broker 1' == current_name:
            return 'broker_name_1'
        elif 'Broker 2' == current_name:
            return 'broker_name_2'
        elif current_name == 'Address_2':
            return 'broker_address_street'
        elif current_name == 'City State Zip_2':
            return 'broker_address_city_state_zip'
        elif current_name == 'Phone_2':
            return 'broker_phone_number'
        elif current_name == 'EmailFax_2':
            return 'broker_email'
        elif current_name == 'EmailFax_3':
            return 'broker_fax'
        
        # Property address fields
        elif 'property address subdivision city county zip code etc' in current_name:
            if '1' in current_name:
                return 'property_address_line_1'
            elif '2' in current_name:
                return 'property_address_line_2'
        
        # Market area field
        elif current_name == 'undefined' and page == 0 and 'means that area' in context_above:
            return 'market_area_description_1'
        elif current_name == 'D Property means any interest in real estate':
            return 'market_area_description_2'
        
        # Term/Date fields
        elif current_name == 'TERM This agreement begins on':
            return 'agreement_start_date'
        elif current_name == 'and ends at 1159 pm on':
            return 'agreement_end_date'
        
        # Initials fields (linked across pages)
        elif 'Initialed for Identification by BrokerAssociate' in current_name:
            if '_2' in current_name:
                return 'broker_initials_linked_2'
            elif '_3' in current_name:
                return 'broker_initials_linked_3'
            elif '_4' in current_name:
                return 'broker_initials_linked_4'
            else:
                return 'broker_initials_linked_1'
        
        elif 'and Client' in current_name:
            if '_2' in current_name:
                return 'client_initials_linked_2'
            elif '_3' in current_name:
                return 'client_initials_linked_3'
            elif '_4' in current_name:
                return 'client_initials_linked_4'
            else:
                return 'client_initials_linked_1'
        
        # Page number fields (these appear on each page)
        elif 'undefined' in current_name and 'page' in context_right.lower():
            page_num = page + 1
            return f'page_number_linked_{page_num}'
        
        # Agreement title fields (linked across pages)
        elif 'BuyerTenant Representation Agreement between' in current_name:
            if '_2' in current_name:
                return 'agreement_parties_linked_2'
            elif '_3' in current_name:
                return 'agreement_parties_linked_3'
            elif '_4' in current_name:
                return 'agreement_parties_linked_4'
            else:
                return 'agreement_parties_linked_1'
        
        # Commission/Fee fields
        elif '1 Purchases' == current_name:
            return 'purchase_commission_percent'
        elif 'of the sales price or a flat fee of' == current_name:
            return 'purchase_flat_fee_amount'
        elif '2 Leases' == current_name:
            return 'lease_commission_percent'
        elif 'of one months rent or' == current_name:
            return 'lease_rent_percent'
        elif 'the lease or a flat fee of' == current_name:
            return 'lease_flat_fee_amount'
        
        # Protection period
        elif 'continuing for' == current_name:
            return 'protection_period_days'
        
        # County field
        elif 'H County Amounts Payable to Broker' in current_name:
            return 'payment_county'
        
        # Referral field
        elif current_name == 'to':
            return 'referral_service_provider'
        
        # Bonus fields
        elif 'bonuses a range of compensation' in current_name:
            if '1' in current_name:
                return 'additional_compensation_1'
            elif '2' in current_name:
                return 'additional_compensation_2'
        
        # Additional info fields
        elif current_name == 'undefined_3' and 'insert amounts' in context_above:
            return 'additional_compensation_notes'
        
        # Property acquisition field
        elif 'acquiring property in the market area' == current_name:
            return 'client_financial_info'
        
        # Additional info field on page 3
        elif current_name == 'undefined_6' and page == 3:
            return 'additional_provisions'
        
        # Final signature section
        elif current_name == 'Brokers Printed Name':
            return 'broker_printed_name'
        elif current_name == 'Clients Printed Name':
            return 'client_printed_name_1'
        elif current_name == 'Clients Printed Name_2':
            return 'client_printed_name_2'
        elif current_name == 'Brokers Signature':
            return 'broker_signature'
        elif current_name == 'Clients Signature':
            return 'client_signature_1'
        elif current_name == 'Clients Signature_2':
            return 'client_signature_2'
        elif current_name == 'Brokers Associates Printed Name if applicable':
            return 'broker_associate_printed_name'
        
        # If we can't determine a better name, keep the original
        return current_name
    
    def rename_all_fields(self):
        """Automatically rename all fields based on context"""
        print("\nAutomatically renaming fields based on FIELD_NAMING_GUIDE.md...")
        print("=" * 80)
        
        renamed_count = 0
        for field in self.fields_data:
            old_name = field['field_name']
            new_name = self.determine_new_name(field)
            
            if new_name != old_name:
                self.renamed_fields[old_name] = new_name
                renamed_count += 1
                print(f"✓ '{old_name}' → '{new_name}'")
        
        print(f"\nTotal fields renamed: {renamed_count}")
        return renamed_count > 0
    
    def apply_renames_to_pdf(self, output_path: str = None):
        """Apply the field renames to the PDF"""
        if not self.renamed_fields:
            print("\nNo fields were renamed.")
            return False
        
        # Create output path if not specified
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = Path(self.pdf_path).stem + f"_renamed_{timestamp}.pdf"
        
        try:
            # Open PDF
            pdf_doc = fitz.open(self.pdf_path)
            
            # Track renamed fields
            renamed_count = 0
            
            # Iterate through pages and rename fields
            for page_num in range(len(pdf_doc)):
                page = pdf_doc[page_num]
                
                for widget in page.widgets():
                    if widget.field_name in self.renamed_fields:
                        new_name = self.renamed_fields[widget.field_name]
                        widget.field_name = new_name
                        widget.update()
                        renamed_count += 1
            
            # Save the modified PDF
            pdf_doc.save(output_path)
            pdf_doc.close()
            
            print(f"\n✓ Successfully renamed {renamed_count} fields in PDF")
            print(f"✓ Saved to: {output_path}")
            
            return True
            
        except Exception as e:
            print(f"\nError applying renames: {e}")
            return False
    
    def update_json_file(self, output_path: str = None):
        """Update the JSON file with new field names"""
        if not self.renamed_fields:
            return
        
        # Create output path if not specified
        if output_path is None:
            output_path = Path(self.json_path).stem + "_renamed.json"
        
        # Update field names in data
        updated_data = []
        for field in self.fields_data:
            field_copy = field.copy()
            if field['field_name'] in self.renamed_fields:
                field_copy['original_name'] = field['field_name']
                field_copy['field_name'] = self.renamed_fields[field['field_name']]
            updated_data.append(field_copy)
        
        # Save updated JSON
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(updated_data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Updated JSON saved to: {output_path}")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Automatically rename PDF fields based on naming guide')
    parser.add_argument('json_file', help='Path to the JSON file with extracted fields')
    parser.add_argument('pdf_file', help='Path to the original PDF file')
    parser.add_argument('-o', '--output', help='Output PDF file path')
    parser.add_argument('-j', '--json-output', help='Output JSON file path')
    
    args = parser.parse_args()
    
    # Validate files exist
    if not Path(args.json_file).exists():
        print(f"Error: JSON file '{args.json_file}' not found")
        return
    
    if not Path(args.pdf_file).exists():
        print(f"Error: PDF file '{args.pdf_file}' not found")
        return
    
    # Create renamer instance
    renamer = AutoFieldRenamer(args.json_file, args.pdf_file)
    
    # Rename all fields automatically
    if renamer.rename_all_fields():
        # Update JSON
        renamer.update_json_file(args.json_output)
        
        # Update PDF
        renamer.apply_renames_to_pdf(args.output)
        
        print("\n✓ All changes applied successfully!")
    else:
        print("\nNo changes needed.")


if __name__ == "__main__":
    main()