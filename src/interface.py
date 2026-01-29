import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import numpy as np
import sympy as sp
import src.logic as logic

class AdvancedMathCalculator:
    """Main application class for the Matrix Calculator GUI."""
    def __init__(self, root):
        self.root = root
        self.matrix_count = 2
        self.matrix_texts = []
        self.setup_window()
        self.setup_styles()
        self.create_widgets()
        
    def setup_window(self):
        """Configures the main application window settings."""
        self.root.title("Matrix calculator")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(True, True)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def setup_styles(self):
        """Defines custom styles for TTK widgets (buttons, tabs, etc.)."""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Title.TLabel', background='#1a1a2e', foreground='#00d4ff', font=('Arial', 24, 'bold'))
        self.style.configure('Section.TLabel', background='#16213e', foreground='#ffffff', font=('Arial', 14, 'bold'))
        self.style.configure('Custom.TButton', background='#0f3460', foreground='#ffffff', font=('Arial', 10, 'bold'), borderwidth=0)
        self.style.map('Custom.TButton', background=[('active', '#1e5f8b'), ('pressed', '#0a2744')])
        self.style.configure('Matrix.TButton', background='#e74c3c', foreground='#ffffff', font=('Arial', 10, 'bold'))
        self.style.map('Matrix.TButton', background=[('active', '#c0392b'), ('pressed', '#a93226')])
        self.style.configure('TNotebook', background='#1a1a2e', borderwidth=0)
        self.style.configure('TNotebook.Tab', background='#16213e', foreground='#ffffff', padding=[20, 10], font=('Arial', 12, 'bold'))
        self.style.map('TNotebook.Tab', background=[('selected', '#0f3460'), ('active', '#1e5f8b')])
        
    def create_widgets(self):
        """Creates the main layout components including the title and notebook tabs."""
        main_frame = tk.Frame(self.root, bg='#1a1a2e')
        main_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        title_label = ttk.Label(main_frame, text="🧮 Matrix Calculator", style='Title.TLabel')
        title_label.grid(row=0, column=0, pady=(0, 20))
        
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        
        self.create_matrix_tab()
        self.create_output_tab()
        
        # Inline Error Label at the bottom
        self.error_label = tk.Label(main_frame, text="", bg='#1a1a2e', fg='#e74c3c', font=('Arial', 12, 'bold'))
        self.error_label.grid(row=2, column=0, pady=(10, 0))
        
    def create_matrix_tab(self):
        """Builds the 'Matrix Operations' tab containing input fields and operation buttons."""
        matrix_frame = tk.Frame(self.notebook, bg='#16213e')
        self.notebook.add(matrix_frame, text='🔢 Matrix Operations')

        # Scrollable area setup
        canvas = tk.Canvas(matrix_frame, bg='#16213e', highlightthickness=0)
        scrollbar = ttk.Scrollbar(matrix_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#16213e')

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        main_container = tk.Frame(scrollable_frame, bg='#16213e')
        main_container.pack(fill='both', expand=True, padx=10, pady=5)

        # Matrix Count Spinbox
        left_frame = tk.Frame(main_container, bg='#16213e')
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))

        count_frame = tk.LabelFrame(left_frame, text="Number of Matrices", bg='#16213e', fg='#ffffff', font=('Arial', 12, 'bold'))
        count_frame.pack(fill='x', pady=5)

        count_input_frame = tk.Frame(count_frame, bg='#16213e')
        count_input_frame.pack(fill='x', padx=5, pady=5)
        tk.Label(count_input_frame, text="Count:", bg='#16213e', fg='#ffffff', font=('Arial', 10)).pack(side='left', padx=(0, 5))

        self.matrix_count_var = tk.StringVar(value="2")
        self.matrix_count_spinbox = tk.Spinbox(count_input_frame, from_=2, to=4, textvariable=self.matrix_count_var, width=5, bg='#2c3e50', fg='#ecf0f1', insertbackground='#ffffff', font=('Arial', 12), command=self.update_matrix_inputs)
        self.matrix_count_spinbox.pack(side='left', padx=(0, 10))
        tk.Label(count_input_frame, text="(Max: 4)", bg='#16213e', fg='#95a5a6', font=('Arial', 9)).pack(side='left')
    
        # Scalar & Power Inputs
        scalar_frame = tk.LabelFrame(left_frame, text="Scalar Input", bg='#16213e', fg='#ffffff', font=('Arial', 12, 'bold'))
        scalar_frame.pack(fill='x', pady=5)
        tk.Label(scalar_frame, text="Scalar value:", bg='#16213e', fg='#ffffff', font=('Arial', 10)).pack(anchor='w', padx=5, pady=2)
        scalar_input_frame = tk.Frame(scalar_frame, bg='#16213e')
        scalar_input_frame.pack(fill='x', padx=5, pady=5)
        self.scalar_entry = tk.Entry(scalar_input_frame, width=15, bg='#2c3e50', fg='#ecf0f1', insertbackground='#ffffff', font=('Arial', 12))
        self.scalar_entry.pack(side='left')
        tk.Label(scalar_input_frame, text="(for Scalar Multiply)", bg='#16213e', fg='#95a5a6', font=('Arial', 9)).pack(side='left', padx=(10, 0))

        self.matrix_input_frame = tk.LabelFrame(left_frame, text="Matrix Input", bg='#16213e', fg='#ffffff', font=('Arial', 12, 'bold'))
        self.matrix_input_frame.pack(fill='x', pady=5)
        self.create_matrix_inputs()

        power_frame = tk.LabelFrame(left_frame, text="Power Input", bg='#16213e', fg='#ffffff', font=('Arial', 12, 'bold'))
        power_frame.pack(fill='x', pady=5)
        tk.Label(power_frame, text="Power (n):", bg='#16213e', fg='#ffffff', font=('Arial', 10)).pack(anchor='w', padx=5, pady=2)
        power_input_frame = tk.Frame(power_frame, bg='#16213e')
        power_input_frame.pack(fill='x', padx=5, pady=5)
        self.power_entry = tk.Entry(power_input_frame, width=15, bg='#2c3e50', fg='#ecf0f1', insertbackground='#ffffff', font=('Arial', 12))
        self.power_entry.pack(side='left')
        tk.Label(power_input_frame, text="(for Matrix Power)", bg='#16213e', fg='#95a5a6', font=('Arial', 9)).pack(side='left', padx=(10, 0))

        # Operation Buttons
        right_frame = tk.Frame(main_container, bg='#16213e')
        right_frame.pack(side='right', fill='both', expand=True)

        basic_frame = tk.LabelFrame(right_frame, text="Basic Operations", bg='#16213e', fg='#ffffff', font=('Arial', 12, 'bold'))
        basic_frame.pack(fill='x', pady=5)
        matrix_basic_ops = [("Add Matrices", "matrix_add"), ("Subtract Matrices", "matrix_subtract"), ("Multiply Matrices", "matrix_multiply"), ("Scalar Multiply", "scalar_multiply"), ("Matrix Power", "matrix_power"), ("Element-wise Multiply", "elementwise_multiply")]
        for i, (text, command) in enumerate(matrix_basic_ops):
            row, col = i // 3, i % 3
            btn = ttk.Button(basic_frame, text=text, style='Matrix.TButton', command=lambda cmd=command: self.matrix_operation(cmd))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='ew')
        for i in range(3): basic_frame.grid_columnconfigure(i, weight=1)

        advanced_frame = tk.LabelFrame(right_frame, text="Advanced Operations", bg='#16213e', fg='#ffffff', font=('Arial', 12, 'bold'))
        advanced_frame.pack(fill='x', pady=5)
        matrix_advanced_ops = [("Determinant", "determinant"), ("Inverse", "inverse"), ("Transpose", "transpose"), ("Eigenvalues", "eigenvalues"), ("Eigenvectors", "eigenvectors"), ("Trace", "trace"), ("Characteristics", "characteristics"), ("Gauss transformation", "gauss_transformation")]
        for i, (text, command) in enumerate(matrix_advanced_ops):
            row, col = i // 4, i % 4
            btn = ttk.Button(advanced_frame, text=text, style='Matrix.TButton', command=lambda cmd=command: self.matrix_operation(cmd))
            btn.grid(row=row, column=col, padx=3, pady=3, sticky='ew')
        for i in range(4): advanced_frame.grid_columnconfigure(i, weight=1)

    def create_output_tab(self):
        """Constructs the 'Results' tab with a scrollable text area for outputs."""
        output_frame = tk.Frame(self.notebook, bg='#16213e')
        self.notebook.add(output_frame, text='📋 Results')
        output_label_frame = tk.LabelFrame(output_frame, text="Calculation Results", bg='#16213e', fg='#ffffff', font=('Arial', 12, 'bold'))
        output_label_frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.output_text = scrolledtext.ScrolledText(output_label_frame, bg='#2c3e50', fg='#ecf0f1', insertbackground='#ffffff', font=('Consolas', 11), state='disabled')
        self.output_text.pack(fill='both', expand=True, padx=5, pady=5)
        button_frame = tk.Frame(output_label_frame, bg='#16213e')
        button_frame.pack(fill='x', padx=5, pady=5)
        ttk.Button(button_frame, text="Clear Output", style='Custom.TButton', command=self.clear_output).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Copy to Clipboard", style='Custom.TButton', command=self.copy_results).pack(side='left', padx=5)
    
    def matrix_operation(self, operation):
        """Dispatches GUI requests to the mathematical logic module and handles validation."""
        self.error_label.config(text="") # Clear previous errors
        try:
            matrices = []
            for matrix_text in self.matrix_texts:
                data = self.parse_matrix(matrix_text.get("1.0", tk.END))
                if data:
                    self.validate_matrix_size(data, 6)
                    matrices.append(data)

            if not matrices: raise ValueError("At least one matrix is required")
            matrix_a = matrices[0]

            # Input validation logic
            if operation in ["matrix_multiply", "matrix_subtract", "matrix_add", "elementwise_multiply"]:
                if len(matrices) < 2: raise ValueError(f"{operation.replace('_', ' ').title()} requires at least 2 matrices")
                if operation == "matrix_multiply":
                    for i in range(len(matrices) - 1): self.validate_matrix_multiplication(matrices[i], matrices[i+1])
                else:
                    for i in range(1, len(matrices)): self.validate_matrix_sum_sub(matrices[0], matrices[i])

            # Operation mapping
            if operation == "matrix_add": result = logic.add_matrices(matrices)
            elif operation == "matrix_subtract": result = logic.subtract_matrices(matrices)
            elif operation == "matrix_multiply": result = logic.multiply_matrices(matrices)
            elif operation == "elementwise_multiply": result = logic.elementwise_multiply(matrices)
            elif operation == "determinant": result = logic.determinant(matrix_a)
            elif operation == "inverse": result = logic.inverse(matrix_a)
            elif operation == "transpose": result = logic.transpose(matrix_a)
            elif operation == "trace": result = logic.trace(matrix_a)
            elif operation == "eigenvalues": result = logic.eigenvalues(matrix_a)
            elif operation == "eigenvectors": result = logic.eigenvectors(matrix_a)
            elif operation == "characteristics": result = logic.characteristics(matrix_a)
            elif operation == "gauss_transformation": result = logic.gauss_transformation(matrix_a)
            elif operation == "matrix_power":
                power_str = self.power_entry.get().strip()
                if not power_str: raise ValueError("Enter power in Power Input field")
                power = int(power_str)
                result = logic.matrix_power(matrix_a, power)
            elif operation == "scalar_multiply":
                scalar_str = self.scalar_entry.get().strip()
                if not scalar_str: raise ValueError("Enter scalar in Scalar Input field")
                scalar = sp.sympify(scalar_str)
                if scalar == sp.zoo or scalar == sp.nan:
                    raise ValueError("Division by zero in scalar input")
                result = logic.scalar_multiply(matrix_a, scalar)
            else: raise ValueError(f"Operation {operation} not found")

            # Result formatting selection
            if operation in ["determinant", "trace"]: self.display_result(operation, result, 0)
            elif operation in ["eigenvalues", "eigenvectors"]: self.display_result(operation, result, 3)
            elif operation == "characteristics": self.display_result(operation, result, 2)
            else: self.display_result(operation, result, 1)

            self.notebook.select(1) # Auto-switch to results tab

        except ValueError as e:
            self.error_label.config(text=f"⚠️ {str(e)}")
        except Exception as e:
            self.error_label.config(text=f"❌ Error: {str(e)}")

    def parse_matrix(self, text):
        """Parses a string input into a 2D list of floats."""
        lines = text.strip().split('\n')
        matrix = []
        for line in lines:
            line = line.strip()
            if line:
                # Replace symbol √ with sqrt() for library compatibility
                import re
                line = re.sub(r'√(\d+|[a-zA-Z])', r'sqrt(\1)', line)
                # Also handle √(...) cases
                line = line.replace('√(', 'sqrt(')
                
                elements = line.split(',') if ',' in line else line.split()
                row = []
                for e in elements:
                    if e.strip():
                        val = sp.sympify(e.strip())
                        if val == sp.zoo or val == sp.nan:
                            raise ValueError("Division by zero detected in input")
                        row.append(val)
                if row: matrix.append(row)
        return matrix

    def validate_matrix_sum_sub(self, A, B):
        """Ensures matrices have matching dimensions for addition/subtraction."""
        if not A or not B: raise ValueError("Matrices empty")
        if len(A) != len(B) or len(A[0]) != len(B[0]): raise ValueError("Matrices must have same size")

    def validate_matrix_multiplication(self, A, B):
        """Validates that matrix A rows match matrix B columns for multiplication."""
        if not A or not B: raise ValueError("Matrices empty")
        if len(A[0]) != len(B): raise ValueError(f"A(cols={len(A[0])}) != B(rows={len(B)})")

    def validate_matrix_size(self, matrix, max_size=6):
        """Prevents processing of excessively large matrices."""
        if len(matrix) > max_size or (matrix and len(matrix[0]) > max_size):
            raise ValueError(f"Matrix exceeds {max_size}x{max_size}")

    def display_result(self, operation, result, k=0):
        """Renders the calculation output in the text widget with formatting."""
        self.output_text.config(state='normal')
        self.output_text.insert(tk.END, f"\n{'='*50}\nOperation: {operation.title()}\n")
        
        if k == 1: self.output_text.insert(tk.END, f"Result:\n{self.show_matrix_with_inf_check(result)}\n")
        elif k == 2:
            self.output_text.insert(tk.END, "Result:\n")
            for prop, val in result.items():
                status = "✓ Yes" if val else "✗ No"
                self.output_text.insert(tk.END, f"  {prop.replace('_',' ').title()}: {status}\n")
        elif k == 3: self.output_text.insert(tk.END, f"{result}\n")
        else: self.output_text.insert(tk.END, f"Result: {logic.format_symbolic(result)}\n")
        
        self.output_text.insert(tk.END, f"{'='*50}\n")
        self.output_text.see(tk.END)
        self.output_text.config(state='disabled')

    def show_matrix_with_inf_check(self, matrix):
        """Returns a string representation of a matrix with aligned symbols and fractions."""
        if not matrix: return "Empty matrix"
        
        # 1. Format all elements to strings first
        str_matrix = []
        for row in matrix:
            str_matrix.append([logic.format_symbolic(n) for n in row])
            
        # 2. Calculate max width for each column
        num_cols = len(str_matrix[0])
        col_widths = []
        for j in range(num_cols):
            max_w = max(len(row[j]) for row in str_matrix)
            col_widths.append(max_w)
            
        # 3. Build the formatted string
        res = ""
        for row in str_matrix:
            # Join with padding and extra space between columns
            formatted_row = "  ".join(val.ljust(col_widths[i]) for i, val in enumerate(row))
            res += f"[  {formatted_row}  ]\n"
        return res
    
    def create_matrix_inputs(self):
        """Dynamically generates matrix input text areas based on count."""
        for w in self.matrix_input_frame.winfo_children(): w.destroy()
        self.matrix_texts = []
        count = int(self.matrix_count_var.get())
        labels = ['A', 'B', 'C', 'D']
        cols = min(2, count)
        for i in range(count):
            r, c = (i // cols), (i % cols)
            tk.Label(self.matrix_input_frame, text=f"Matrix {labels[i]}:", bg='#16213e', fg='#ffffff').grid(row=r*2, column=c, sticky='w', padx=5, pady=2)
            txt = scrolledtext.ScrolledText(self.matrix_input_frame, height=4, width=30, bg='#2c3e50', fg='#ecf0f1', insertbackground='#ffffff')
            txt.grid(row=r*2+1, column=c, padx=5, pady=2)
            self.matrix_texts.append(txt)
        for i in range(cols): self.matrix_input_frame.grid_columnconfigure(i, weight=1)

    def update_matrix_inputs(self):
        """Triggers widget recreation when matrix count changes."""
        self.matrix_count = int(self.matrix_count_var.get())
        self.create_matrix_inputs()

    def clear_output(self):
        """Wipes the results terminal."""
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', tk.END)
        self.output_text.config(state='disabled')

    def copy_results(self):
        """Copies the entire output log to system clipboard."""
        try:
            content = self.output_text.get('1.0', tk.END)
            if content.strip():
                self.root.clipboard_clear()
                self.root.clipboard_append(content)
        except: pass
