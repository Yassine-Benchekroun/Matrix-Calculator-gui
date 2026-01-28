# Matrix Calculator GUI

A powerful and elegant Matrix Calculator built with Python's Tkinter. It supports a wide range of basic and advanced matrix operations.

## Features

- **Basic Operations**: Addition, Subtraction, Multiplication, Scalar Multiplication, Matrix Power, Element-wise Multiplication.
- **Advanced Operations**: Determinant, Inverse, Transpose, Trace, Eigenvalues, Eigenvectors, Characteristics (Symmetry, etc.), Gauss Transformation.
- **Dynamic Input**: Supports up to 4 matrices (A, B, C, D).
- **Elegant UI**: Dark themed, responsive, with a scrollable interface.

## Project Structure

```
Matrix-Calculator-GUI/
├── assets/              # Icons or screenshots
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

## Development

-   **logic.py**: Contains all the mathematical logic for matrix operations.
-   **interface.py**: Handles the Tkinter GUI and user interactions.
-   **main.py**: The entry point that boots up the application.
