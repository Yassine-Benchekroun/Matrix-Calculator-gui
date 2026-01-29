import tkinter as tk
from src.interface import AdvancedMathCalculator

# Main entry point for the Matrix Calculator application
def main():
    root = tk.Tk()
    # Initialize the primary GUI application
    app = AdvancedMathCalculator(root)
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
