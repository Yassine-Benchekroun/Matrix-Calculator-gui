# Matrix Calculator GUI

A powerful and elegant Matrix Calculator built with Python's Tkinter. It supports a wide range of basic and advanced matrix operations.

## Features

- **Basic Operations**: Addition, Subtraction, Multiplication, Scalar Multiplication, Matrix Power, Element-wise Multiplication.
- **Advanced Operations**: Determinant, Inverse, Transpose, Trace, Eigenvalues, Eigenvectors, Characteristics (Symmetry, etc.), Gauss Transformation.
- **Dynamic Input**: Supports up to 4 matrices (A, B, C, D).
- **Elegant UI**: Dark themed, responsive, with a scrollable interface.

## Computational Power

The computational power of this application relies on a strategic integration of **NumPy** and **SymPy**:

- **SymPy (Symbolic Mathematics)**: This library is the backbone of the "Advanced Operations" module. It allows the calculator to provide exact results (e.g., keeping fractions like $1/3$ or radicals like $\sqrt{2}$) rather than decimal approximations. This is essential for operations like Eigenvalue decomposition and Matrix Inversion where mathematical precision is a priority.
- **NumPy (Numerical Computing)**: For high-performance calculations and large-scale data handling, the program leverages NumPy. By converting matrices into float-based arrays (`dtype=float`), the application can execute rapid numerical linear algebra, ensuring the GUI remains responsive even when processing complex 4x4 matrices.

## Project Structure

```
Matrix-Calculator-GUI/
├── src/                 # Source code
│   ├── logic.py         # Matrix math functions
│   └── interface.py     # GUI layout code
├── requirements.txt     # List of dependencies
├── .gitignore           # Files Git should ignore
├── main.py              # Entry point of the app
└── README.md            # Project documentation
```

## How to Run

1.  **Clone the repository** (or download the source).
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application**:
    ```bash
    python main.py
    ```

## Application Overview & Demos

**1. Main Dashboard**
The interface features a responsive, dark-themed layout that supports dynamic input for up to four matrices simultaneously.
![Main Dashboard](./Screenshots/Main_window.jpg)

**2. Supported Operations**
A comprehensive dropdown menu provides instant access to both basic arithmetic and advanced linear algebra functions (Determinant, Inverse, etc.).
![List of Operations](./Screenshots/matrix_operations.jpg)

**3. Symbolic Precision (SymPy Engine)**
Unlike standard calculators, the application preserves exact mathematical forms. Notice how the eigenvalues are displayed as exact roots rather than rounded decimals.
![SymPy Exact Results](./Screenshots/Result_eigenvalue-sympy.jpg)

**4. Complex Number Support**
The calculator is robust enough to handle complex number arithmetic, essential for advanced engineering computations.
![Complex Numbers](./Screenshots/Handling_complex_numbers.jpg)

**5. Robust Error Handling**
The application includes input validation to prevent crashes, such as automatically detecting and flagging division by zero errors.
![Error Handling](./Screenshots/Handling_Division_by_0.jpg)
