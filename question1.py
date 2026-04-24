"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md

import sys

def main():
    try:
        total_load = float(sys.argv[1])
        num_supports = float(sys.argv[2])
        if num_supports == 0:
            print("Error: Cannot divide by zero! Supports must be greater than zero.")
        else:
            load_per_support = total_load / num_supports
            print(f"Load per support point: {load_per_support:.2f} N")
    except (ValueError, IndexError):
        print("Error: Invalid input! Enter numeric values only.")
if __name__ == "__main__":
    main()
