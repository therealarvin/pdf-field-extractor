#!/usr/bin/env python3
"""
GUI Field Grouper
Visual interface for grouping PDF form fields
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
from pathlib import Path
from typing import Dict, List, Set, Optional
import base64
from io import BytesIO
from PIL import Image, ImageTk, ImageDraw
import fitz  # PyMuPDF

class FieldGrouperGUI:
    def __init__(self, pdf_path: str, fields: List[Dict]):
        self.pdf_path = pdf_path
        self.fields = fields
        self.pdf_doc = fitz.open(pdf_path)
        
        # Group fields by page
        self.fields_by_page = {}
        for field in fields:
            page = field.get('page', 0)
            if page not in self.fields_by_page:
                self.fields_by_page[page] = []
            self.fields_by_page[page].append(field)
        
        # State
        self.current_page = 0
        self.selected_fields = set()
        self.groups = []
        self.field_buttons = {}
        
        # Colors
        self.colors = {
            'unselected': '#E0E0E0',
            'selected': '#4CAF50',
            'grouped': '#2196F3',
            'hover': '#FFC107'
        }
        
        # Create GUI
        self.create_gui()
        self.load_page(0)
    
    def create_gui(self):
        """Create the main GUI window"""
        self.root = tk.Tk()
        self.root.title("PDF Field Grouper")
        self.root.geometry("1200x800")
        
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=3)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="PDF Field Grouper", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Left panel - PDF viewer
        self.create_pdf_viewer(main_frame)
        
        # Right panel - Controls and field list
        self.create_control_panel(main_frame)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
    
    def create_pdf_viewer(self, parent):
        """Create PDF viewer panel"""
        viewer_frame = ttk.LabelFrame(parent, text="PDF Preview", padding="10")
        viewer_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        
        # Canvas for PDF page
        canvas_frame = ttk.Frame(viewer_frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL)
        h_scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL)
        
        # Canvas
        self.canvas = tk.Canvas(canvas_frame, 
                               yscrollcommand=v_scrollbar.set,
                               xscrollcommand=h_scrollbar.set,
                               bg='gray')
        
        v_scrollbar.config(command=self.canvas.yview)
        h_scrollbar.config(command=self.canvas.xview)
        
        # Grid layout
        self.canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        canvas_frame.rowconfigure(0, weight=1)
        canvas_frame.columnconfigure(0, weight=1)
        
        # Page navigation
        nav_frame = ttk.Frame(viewer_frame)
        nav_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(nav_frame, text="◀ Previous", 
                  command=self.prev_page).pack(side=tk.LEFT, padx=5)
        
        self.page_var = tk.StringVar()
        self.page_label = ttk.Label(nav_frame, textvariable=self.page_var)
        self.page_label.pack(side=tk.LEFT, padx=20)
        
        ttk.Button(nav_frame, text="Next ▶", 
                  command=self.next_page).pack(side=tk.LEFT, padx=5)
    
    def create_control_panel(self, parent):
        """Create control panel"""
        control_frame = ttk.LabelFrame(parent, text="Controls", padding="10")
        control_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Field type filter
        filter_frame = ttk.LabelFrame(control_frame, text="Filter by Type", padding="5")
        filter_frame.pack(fill=tk.X, pady=5)
        
        self.show_checkboxes = tk.BooleanVar(value=True)
        self.show_text = tk.BooleanVar(value=True)
        self.show_other = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(filter_frame, text="Checkboxes", 
                       variable=self.show_checkboxes,
                       command=self.update_field_display).pack(anchor=tk.W)
        ttk.Checkbutton(filter_frame, text="Text Fields", 
                       variable=self.show_text,
                       command=self.update_field_display).pack(anchor=tk.W)
        ttk.Checkbutton(filter_frame, text="Other", 
                       variable=self.show_other,
                       command=self.update_field_display).pack(anchor=tk.W)
        
        # Selected fields
        selected_frame = ttk.LabelFrame(control_frame, text="Selected Fields", padding="5")
        selected_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Listbox with scrollbar
        list_frame = ttk.Frame(selected_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.selected_listbox = tk.Listbox(list_frame, 
                                          yscrollcommand=scrollbar.set,
                                          selectmode=tk.SINGLE)
        self.selected_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.selected_listbox.yview)
        
        # Selection buttons
        button_frame = ttk.Frame(selected_frame)
        button_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(button_frame, text="Clear Selection", 
                  command=self.clear_selection).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Remove Selected", 
                  command=self.remove_selected_field).pack(side=tk.LEFT, padx=2)
        
        # Group creation
        group_frame = ttk.LabelFrame(control_frame, text="Create Group", padding="5")
        group_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(group_frame, text="Group Type:").pack(anchor=tk.W)
        self.group_type_var = tk.StringVar(value="checkbox")
        ttk.Combobox(group_frame, textvariable=self.group_type_var,
                    values=["checkbox", "text_continuation", "radio", "same_value"],
                    state="readonly").pack(fill=tk.X, pady=2)
        
        ttk.Button(group_frame, text="Create Group from Selected", 
                  command=self.create_group,
                  style="Accent.TButton").pack(fill=tk.X, pady=5)
        
        # Groups list
        groups_frame = ttk.LabelFrame(control_frame, text="Groups", padding="5")
        groups_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Treeview for groups
        self.groups_tree = ttk.Treeview(groups_frame, columns=("type", "fields"), 
                                       show="tree headings", height=6)
        self.groups_tree.heading("type", text="Type")
        self.groups_tree.heading("fields", text="Fields")
        self.groups_tree.column("type", width=80)
        self.groups_tree.column("fields", width=120)
        self.groups_tree.pack(fill=tk.BOTH, expand=True)
        
        # Export button
        ttk.Button(control_frame, text="Export Groups", 
                  command=self.export_groups,
                  style="Accent.TButton").pack(fill=tk.X, pady=10)
    
    def load_page(self, page_num: int):
        """Load and display a PDF page"""
        if page_num < 0 or page_num >= len(self.pdf_doc):
            return
        
        self.current_page = page_num
        self.page_var.set(f"Page {page_num + 1} of {len(self.pdf_doc)}")
        
        # Render page
        page = self.pdf_doc[page_num]
        mat = fitz.Matrix(2, 2)  # 2x zoom
        pix = page.get_pixmap(matrix=mat)
        
        # Convert to PIL Image
        img_data = pix.tobytes("ppm")
        img = Image.open(BytesIO(img_data))
        
        # Draw field rectangles
        draw = ImageDraw.Draw(img)
        page_fields = self.fields_by_page.get(page_num, [])
        
        for field in page_fields:
            if not self.should_show_field(field):
                continue
            
            pos = field.get('position', [0, 0, 0, 0])
            # Scale positions by zoom factor
            rect = [p * 2 for p in pos]
            
            # Determine color
            if field['field_name'] in self.selected_fields:
                color = self.colors['selected']
            elif any(field['field_name'] in g['fields'] for g in self.groups):
                color = self.colors['grouped']
            else:
                color = self.colors['unselected']
            
            # Draw rectangle
            draw.rectangle(rect, outline=color, width=3)
            
            # Draw field name
            draw.text((rect[0], rect[1] - 20), 
                     field['field_name'].split('_')[-1],
                     fill=color)
        
        # Convert to PhotoImage
        self.photo = ImageTk.PhotoImage(img)
        
        # Update canvas
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        
        # Create clickable areas for fields
        self.create_field_buttons(page_fields)
    
    def create_field_buttons(self, fields: List[Dict]):
        """Create clickable areas for fields"""
        for field in fields:
            if not self.should_show_field(field):
                continue
            
            pos = field.get('position', [0, 0, 0, 0])
            # Scale positions by zoom factor
            rect = [p * 2 for p in pos]
            
            # Create invisible rectangle for clicking
            rect_id = self.canvas.create_rectangle(
                rect[0], rect[1], rect[2], rect[3],
                outline="", fill="", tags=field['field_name']
            )
            
            # Bind click event
            self.canvas.tag_bind(rect_id, "<Button-1>", 
                               lambda e, f=field: self.toggle_field_selection(f))
            self.canvas.tag_bind(rect_id, "<Enter>",
                               lambda e, f=field: self.on_field_hover(f, True))
            self.canvas.tag_bind(rect_id, "<Leave>",
                               lambda e, f=field: self.on_field_hover(f, False))
    
    def should_show_field(self, field: Dict) -> bool:
        """Check if field should be displayed based on filters"""
        field_type = field.get('field_type', 'Unknown')
        
        if field_type == 'CheckBox' and not self.show_checkboxes.get():
            return False
        elif field_type == 'Text' and not self.show_text.get():
            return False
        elif field_type not in ['CheckBox', 'Text'] and not self.show_other.get():
            return False
        
        return True
    
    def toggle_field_selection(self, field: Dict):
        """Toggle field selection"""
        field_name = field['field_name']
        
        if field_name in self.selected_fields:
            self.selected_fields.remove(field_name)
        else:
            self.selected_fields.add(field_name)
        
        self.update_selected_list()
        self.load_page(self.current_page)
        self.status_var.set(f"Selected: {len(self.selected_fields)} fields")
    
    def on_field_hover(self, field: Dict, entering: bool):
        """Handle field hover events"""
        if entering:
            self.status_var.set(f"{field['field_name']} - {field.get('field_type', 'Unknown')}")
        else:
            self.status_var.set(f"Selected: {len(self.selected_fields)} fields")
    
    def update_selected_list(self):
        """Update the selected fields listbox"""
        self.selected_listbox.delete(0, tk.END)
        
        for field_name in sorted(self.selected_fields):
            # Find field info
            field = next((f for f in self.fields if f['field_name'] == field_name), None)
            if field:
                display = f"{field_name} (Page {field.get('page', 0) + 1})"
                self.selected_listbox.insert(tk.END, display)
    
    def clear_selection(self):
        """Clear all selected fields"""
        self.selected_fields.clear()
        self.update_selected_list()
        self.load_page(self.current_page)
        self.status_var.set("Selection cleared")
    
    def remove_selected_field(self):
        """Remove selected field from selection"""
        selection = self.selected_listbox.curselection()
        if selection:
            idx = selection[0]
            field_name = self.selected_listbox.get(idx).split(" (")[0]
            self.selected_fields.discard(field_name)
            self.update_selected_list()
            self.load_page(self.current_page)
    
    def create_group(self):
        """Create a group from selected fields"""
        if len(self.selected_fields) < 2:
            messagebox.showwarning("Not Enough Fields", 
                                 "Please select at least 2 fields to create a group.")
            return
        
        # Create group
        group = {
            'type': self.group_type_var.get(),
            'fields': list(self.selected_fields),
            'confidence': 1.0,
            'reason': 'User-created group'
        }
        
        self.groups.append(group)
        
        # Update groups tree
        group_id = self.groups_tree.insert("", "end", 
                                         text=f"Group {len(self.groups)}",
                                         values=(group['type'], 
                                               f"{len(group['fields'])} fields"))
        
        # Add fields as children
        for field_name in group['fields']:
            self.groups_tree.insert(group_id, "end", text=field_name)
        
        # Clear selection
        self.clear_selection()
        
        messagebox.showinfo("Group Created", 
                          f"Created {group['type']} group with {len(group['fields'])} fields.")
    
    def update_field_display(self):
        """Update field display based on filters"""
        self.load_page(self.current_page)
    
    def prev_page(self):
        """Go to previous page"""
        if self.current_page > 0:
            self.load_page(self.current_page - 1)
    
    def next_page(self):
        """Go to next page"""
        if self.current_page < len(self.pdf_doc) - 1:
            self.load_page(self.current_page + 1)
    
    def export_groups(self):
        """Export groups to JSON"""
        if not self.groups:
            messagebox.showwarning("No Groups", "No groups to export.")
            return
        
        # Convert to FieldGroup format
        from pre_consolidator import FieldGroup
        
        field_groups = []
        for group in self.groups:
            # Get full field data
            fields = [f for f in self.fields if f['field_name'] in group['fields']]
            
            field_group = FieldGroup(
                group_type=group['type'],
                fields=fields,
                confidence=group['confidence'],
                reason=group['reason']
            )
            field_groups.append(field_group)
        
        # Save to file
        output_path = Path(self.pdf_path).stem + "_gui_groups.json"
        
        # Convert to serializable format
        groups_data = []
        for fg in field_groups:
            groups_data.append({
                'group_type': fg.group_type,
                'fields': fg.fields,
                'confidence': fg.confidence,
                'reason': fg.reason
            })
        
        with open(output_path, 'w') as f:
            json.dump(groups_data, f, indent=2)
        
        messagebox.showinfo("Export Complete", 
                          f"Exported {len(self.groups)} groups to {output_path}")
        
        # Close GUI
        self.root.destroy()
    
    def run(self):
        """Run the GUI"""
        self.root.mainloop()
        return self.groups


def launch_gui_grouper(pdf_path: str, fields: List[Dict]) -> Optional[List[Dict]]:
    """Launch the GUI grouper and return created groups"""
    app = FieldGrouperGUI(pdf_path, fields)
    groups = app.run()
    return groups


if __name__ == "__main__":
    # Test with sample data
    import sys
    
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
        
        # Try to load fields
        json_path = Path(pdf_path).stem + "_fields_enhanced.json"
        if Path(json_path).exists():
            with open(json_path, 'r') as f:
                fields = json.load(f)
            
            groups = launch_gui_grouper(pdf_path, fields)
            print(f"Created {len(groups) if groups else 0} groups")
        else:
            print(f"Fields file not found: {json_path}")
    else:
        print("Usage: python gui_field_grouper.py <pdf_path>")