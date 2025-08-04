#!/usr/bin/env python3
"""
PDF Visual Context Extractor
Takes screenshots around form fields with visual indicators
"""

import fitz  # PyMuPDF
from pathlib import Path
import base64
from typing import Dict, List, Tuple, Optional
import io


class PDFVisualContextExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        
    def capture_field_context(
        self, 
        field_info: Dict, 
        vertical_padding: int = 200,
        zoom: float = 2.0,
        highlight_color: Tuple[float, float, float] = (1, 0, 0),
        highlight_width: int = 3
    ) -> Dict:
        """
        Capture full-width screenshot around a field with visual indicator
        
        Args:
            field_info: Dictionary containing field information including rect and page
            vertical_padding: Pixels to capture above and below the field
            zoom: Zoom factor for image clarity
            highlight_color: RGB color for field highlight (default red)
            highlight_width: Width of highlight rectangle
            
        Returns:
            Dictionary with screenshot data and metadata
        """
        page_num = field_info.get('page', 0)
        field_rect = field_info.get('position') or field_info.get('rect')
        
        if not field_rect or page_num >= len(self.doc):
            return None
            
        # Get the page
        page = self.doc[page_num]
        page_rect = page.rect
        
        # Convert field rect to fitz.Rect
        if isinstance(field_rect, list):
            field_rect = fitz.Rect(field_rect[0], field_rect[1], field_rect[2], field_rect[3])
        
        # Create full-width capture rectangle
        capture_rect = fitz.Rect(
            0,  # Full width from left edge
            max(0, field_rect.y0 - vertical_padding),  # Add padding above
            page_rect.width,  # Full width to right edge
            min(page_rect.height, field_rect.y1 + vertical_padding)  # Add padding below
        )
        
        # Create a copy of the page for drawing
        # This ensures we don't modify the original PDF
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=capture_rect)
        
        # Convert to PIL Image for drawing the highlight
        img_data = pix.tobytes("png")
        
        # Create a fresh pixmap without any modifications first
        clean_pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=capture_rect)
        
        # Convert to image and draw the rectangle using PIL or create a new document
        # We'll use a temporary document approach to avoid modifying the original
        temp_doc = fitz.open()  # Create empty document
        temp_page = temp_doc.new_page(width=page_rect.width, height=page_rect.height)
        
        # Insert the page content
        temp_page.show_pdf_page(temp_page.rect, self.doc, page_num)
        
        # Now draw the highlight on the temporary page
        temp_page.draw_rect(
            field_rect,
            color=highlight_color,
            width=highlight_width
        )
        
        # Capture with the highlight
        highlighted_pix = temp_page.get_pixmap(
            matrix=fitz.Matrix(zoom, zoom),
            clip=capture_rect
        )
        
        # Convert to base64 for API transmission
        img_buffer = io.BytesIO(highlighted_pix.tobytes("png"))
        img_buffer.seek(0)
        img_data = img_buffer.read()
        
        # Check size and compress if needed (4MB limit for base64)
        if len(img_data) > 3 * 1024 * 1024:  # If larger than 3MB (to leave room for base64 overhead)
            # Re-render at lower quality
            highlighted_pix = temp_page.get_pixmap(
                matrix=fitz.Matrix(1.5, 1.5),  # Lower zoom
                clip=capture_rect
            )
            img_buffer = io.BytesIO(highlighted_pix.tobytes("png"))
            img_buffer.seek(0)
            img_data = img_buffer.read()
            
        screenshot_base64 = base64.b64encode(img_data).decode('utf-8')
        
        # Also prepare full page capture with highlight
        full_page_pix = temp_page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        full_page_buffer = io.BytesIO(full_page_pix.tobytes("png"))
        full_page_buffer.seek(0)
        full_page_base64 = base64.b64encode(full_page_buffer.read()).decode('utf-8')
        
        # Clean up temporary document
        temp_doc.close()
        
        return {
            'field_screenshot': screenshot_base64,
            'full_page_screenshot': full_page_base64,
            'capture_rect': {
                'x0': capture_rect.x0,
                'y0': capture_rect.y0,
                'x1': capture_rect.x1,
                'y1': capture_rect.y1
            },
            'field_rect': {
                'x0': field_rect.x0,
                'y0': field_rect.y0,
                'x1': field_rect.x1,
                'y1': field_rect.y1
            },
            'page_num': page_num,
            'page_dimensions': {
                'width': page_rect.width,
                'height': page_rect.height
            }
        }
    
    def capture_fields_context(
        self, 
        fields_info: List[Dict], 
        vertical_padding: int = 200,
        zoom: float = 2.0,
        highlight_color: Tuple[float, float, float] = (1, 0, 0),
        highlight_width: int = 3
    ) -> Dict:
        """
        Capture full-width screenshot around multiple fields with visual indicators
        
        Args:
            fields_info: List of dictionaries containing field information including rect and page
            vertical_padding: Pixels to capture above and below the fields
            zoom: Zoom factor for image clarity
            highlight_color: RGB color for field highlight (default red)
            highlight_width: Width of highlight rectangle
            
        Returns:
            Dictionary with screenshot data and metadata
        """
        if not fields_info:
            return None
            
        # Group fields by page
        fields_by_page = {}
        for field_info in fields_info:
            page_num = field_info.get('page', 0)
            if page_num not in fields_by_page:
                fields_by_page[page_num] = []
            fields_by_page[page_num].append(field_info)
        
        # For now, handle the most common case: all fields on same page
        # TODO: Handle fields across multiple pages
        primary_page = list(fields_by_page.keys())[0]
        page_fields = fields_by_page[primary_page]
        
        if primary_page >= len(self.doc):
            return None
            
        # Get the page
        page = self.doc[primary_page]
        page_rect = page.rect
        
        # Collect all field rectangles and find the bounding box
        field_rects = []
        min_y = page_rect.height
        max_y = 0
        
        for field_info in page_fields:
            field_rect = field_info.get('position') or field_info.get('rect')
            if field_rect:
                # Convert field rect to fitz.Rect
                if isinstance(field_rect, list):
                    field_rect = fitz.Rect(field_rect[0], field_rect[1], field_rect[2], field_rect[3])
                field_rects.append(field_rect)
                min_y = min(min_y, field_rect.y0)
                max_y = max(max_y, field_rect.y1)
        
        if not field_rects:
            return None
        
        # Create full-width capture rectangle that includes all fields
        capture_rect = fitz.Rect(
            0,  # Full width from left edge
            max(0, min_y - vertical_padding),  # Add padding above topmost field
            page_rect.width,  # Full width to right edge
            min(page_rect.height, max_y + vertical_padding)  # Add padding below bottommost field
        )
        
        # Create a temporary document to draw highlights
        temp_doc = fitz.open()  # Create empty document
        temp_page = temp_doc.new_page(width=page_rect.width, height=page_rect.height)
        
        # Insert the page content
        temp_page.show_pdf_page(temp_page.rect, self.doc, primary_page)
        
        # Draw highlights for all fields
        for field_rect in field_rects:
            temp_page.draw_rect(
                field_rect,
                color=highlight_color,
                width=highlight_width
            )
        
        # Capture with the highlights
        highlighted_pix = temp_page.get_pixmap(
            matrix=fitz.Matrix(zoom, zoom),
            clip=capture_rect
        )
        
        # Convert to base64 for API transmission
        img_buffer = io.BytesIO(highlighted_pix.tobytes("png"))
        img_buffer.seek(0)
        img_data = img_buffer.read()
        
        # Check size and compress if needed (4MB limit for base64)
        if len(img_data) > 3 * 1024 * 1024:  # If larger than 3MB (to leave room for base64 overhead)
            # Re-render at lower quality
            highlighted_pix = temp_page.get_pixmap(
                matrix=fitz.Matrix(1.5, 1.5),  # Lower zoom
                clip=capture_rect
            )
            img_buffer = io.BytesIO(highlighted_pix.tobytes("png"))
            img_buffer.seek(0)
            img_data = img_buffer.read()
            
        screenshot_base64 = base64.b64encode(img_data).decode('utf-8')
        
        # Also prepare full page capture with highlights
        full_page_pix = temp_page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        full_page_buffer = io.BytesIO(full_page_pix.tobytes("png"))
        full_page_buffer.seek(0)
        full_page_base64 = base64.b64encode(full_page_buffer.read()).decode('utf-8')
        
        # Clean up temporary document
        temp_doc.close()
        
        # Return data with all field rectangles
        field_rects_data = []
        for rect in field_rects:
            field_rects_data.append({
                'x0': rect.x0,
                'y0': rect.y0,
                'x1': rect.x1,
                'y1': rect.y1
            })
        
        return {
            'field_screenshot': screenshot_base64,
            'full_page_screenshot': full_page_base64,
            'capture_rect': {
                'x0': capture_rect.x0,
                'y0': capture_rect.y0,
                'x1': capture_rect.x1,
                'y1': capture_rect.y1
            },
            'field_rects': field_rects_data,  # List of all field rectangles
            'page_num': primary_page,
            'page_dimensions': {
                'width': page_rect.width,
                'height': page_rect.height
            }
        }
    
    def capture_all_fields(
        self,
        fields: List[Dict],
        vertical_padding: int = 100,
        zoom: float = 2.0,
        save_preview_index: int = None
    ) -> List[Dict]:
        """
        Capture screenshots for all fields
        
        Args:
            fields: List of field dictionaries
            vertical_padding: Pixels to capture above and below each field
            zoom: Zoom factor for image clarity
            save_preview_index: If specified, save this field's screenshot as a preview (1-based index)
            
        Returns:
            List of dictionaries with field info and screenshots
        """
        results = []
        
        for i, field in enumerate(fields):
            print(f"Capturing context for field {i+1}/{len(fields)}: {field.get('field_name', 'Unknown')}")
            
            screenshot_data = self.capture_field_context(
                field,
                vertical_padding=vertical_padding,
                zoom=zoom
            )
            
            if screenshot_data:
                # Save preview if this is the requested index
                if save_preview_index and (i + 1) == save_preview_index:
                    preview_filename = f"field_{save_preview_index}_preview_{field.get('field_name', 'unknown')}.png"
                    img_data = base64.b64decode(screenshot_data['field_screenshot'])
                    with open(preview_filename, 'wb') as f:
                        f.write(img_data)
                    print(f"  ✓ Saved preview screenshot to: {preview_filename}")
                
                results.append({
                    'field': field,
                    'screenshot': screenshot_data['field_screenshot'],
                    'full_page': screenshot_data['full_page_screenshot'],
                    'metadata': {
                        'capture_rect': screenshot_data['capture_rect'],
                        'field_rect': screenshot_data['field_rect'],
                        'page_num': screenshot_data['page_num'],
                        'page_dimensions': screenshot_data['page_dimensions']
                    }
                })
            else:
                print(f"  Warning: Could not capture context for field {field.get('field_name', 'Unknown')}")
                results.append({
                    'field': field,
                    'screenshot': None,
                    'full_page': None,
                    'metadata': None
                })
        
        return results
    
    def save_screenshot_preview(
        self,
        field_info: Dict,
        output_path: str,
        vertical_padding: int = 100,
        zoom: float = 2.0
    ):
        """
        Save a screenshot preview to file for debugging
        
        Args:
            field_info: Dictionary containing field information
            output_path: Path to save the screenshot
            vertical_padding: Pixels to capture above and below the field
            zoom: Zoom factor for image clarity
        """
        screenshot_data = self.capture_field_context(
            field_info,
            vertical_padding=vertical_padding,
            zoom=zoom
        )
        
        if screenshot_data:
            # Decode base64 and save
            img_data = base64.b64decode(screenshot_data['field_screenshot'])
            with open(output_path, 'wb') as f:
                f.write(img_data)
            print(f"Screenshot saved to: {output_path}")
        else:
            print(f"Could not capture screenshot for field")
    
    def close(self):
        """Close the PDF document"""
        if self.doc:
            self.doc.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def main():
    """Test the visual context extractor"""
    import json
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python pdf_visual_context.py <pdf_path> [field_json_path]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    
    # If field JSON provided, use it; otherwise create a test field
    if len(sys.argv) > 2:
        with open(sys.argv[2], 'r') as f:
            fields = json.load(f)
            if isinstance(fields, dict):
                fields = [fields]
    else:
        # Test with a dummy field
        fields = [{
            'field_name': 'test_field',
            'field_type': 'Text',
            'page': 0,
            'position': [100, 100, 300, 120]  # x0, y0, x1, y1
        }]
    
    with PDFVisualContextExtractor(pdf_path) as extractor:
        # Capture first field as a test
        if fields:
            field = fields[0]
            output_path = f"test_screenshot_{field.get('field_name', 'field')}.png"
            extractor.save_screenshot_preview(field, output_path)
            
            # Also test batch capture
            print("\nTesting batch capture...")
            results = extractor.capture_all_fields(fields[:5])  # First 5 fields
            print(f"Captured {len(results)} field contexts")


if __name__ == "__main__":
    main()