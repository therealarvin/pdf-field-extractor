#!/usr/bin/env python3
"""
Batch processing script for iterative field renaming.
Processes all PDFs in forms-to-rename folder and outputs to renamed-forms folder.
"""

import os
import sys
import subprocess
import glob
from pathlib import Path
from datetime import datetime


def process_all_pdfs():
    """Process all PDFs in forms-to-rename folder."""
    # Define directories
    source_dir = "forms-to-rename"
    output_dir = "renamed-and-reviewed-forms"
    
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' not found!")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all PDF files in source directory
    pdf_pattern = os.path.join(source_dir, "*.pdf")
    pdf_files = glob.glob(pdf_pattern)
    
    if not pdf_files:
        print(f"No PDF files found in {source_dir}")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s) to process")
    print("=" * 50)
    
    # Track results
    successful = []
    failed = []
    
    # Process each PDF
    for idx, pdf_path in enumerate(pdf_files, 1):
        pdf_name = os.path.basename(pdf_path)
        print(f"\n[{idx}/{len(pdf_files)}] Processing: {pdf_name}")
        print("-" * 40)
        
        try:
            # Call iterative field mapping script with output directory
            result = subprocess.run(
                ['python3', 'iterative_field_mapping.py', pdf_path, output_dir],
                capture_output=True,
                text=True,
                check=True
            )
            
            # Print the output
            print(result.stdout)
            
            if result.stderr:
                print(f"Warnings: {result.stderr}")
            
            successful.append(pdf_name)
            
        except subprocess.CalledProcessError as e:
            print(f"ERROR processing {pdf_name}:")
            print(f"Exit code: {e.returncode}")
            print(f"Error output: {e.stderr}")
            print(f"Standard output: {e.stdout}")
            failed.append(pdf_name)
        
        except Exception as e:
            print(f"Unexpected error processing {pdf_name}: {str(e)}")
            failed.append(pdf_name)
    
    # Print summary
    print("\n" + "=" * 50)
    print("BATCH PROCESSING SUMMARY")
    print("=" * 50)
    print(f"Total PDFs processed: {len(pdf_files)}")
    print(f"Successful: {len(successful)}")
    print(f"Failed: {len(failed)}")
    
    if successful:
        print(f"\nSuccessfully processed:")
        for pdf in successful:
            form_name = Path(pdf).stem.lower().replace(' ', '_').replace('-', '_').replace('(', '').replace(')', '')
            print(f"  ✓ {pdf} → {form_name}_Fillable.pdf")
    
    if failed:
        print(f"\nFailed to process:")
        for pdf in failed:
            print(f"  ✗ {pdf}")
    
    print(f"\nAll output files are in: {output_dir}/")
    
    # Clean up any temporary files left in source directory
    cleanup_temp_files(source_dir)


def cleanup_temp_files(directory):
    """Clean up temporary mapped files from source directory."""
    # Pattern for temporary mapped files created during processing
    temp_patterns = [
        os.path.join(directory, "*_mapped_*.pdf"),
        os.path.join(directory, "*_fields_enhanced.json"),
        os.path.join(directory, "*_fields_enhanced_mapped.json")
    ]
    
    removed_count = 0
    for pattern in temp_patterns:
        temp_files = glob.glob(pattern)
        for temp_file in temp_files:
            try:
                os.remove(temp_file)
                removed_count += 1
            except Exception as e:
                print(f"Warning: Could not remove temporary file {temp_file}: {e}")
    
    if removed_count > 0:
        print(f"\nCleaned up {removed_count} temporary file(s)")


def main():
    print("Batch Iterative Field Renaming")
    print("==============================")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    process_all_pdfs()
    
    print(f"\nCompleted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()