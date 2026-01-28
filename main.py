import tkinter as tk
from src.interface import AdvancedMathCalculator

def main():
    root = tk.Tk()
    app = AdvancedMathCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
