import sys
from topsis.topsis import Topsis

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python ShrihanTayal_102203460.py <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)
    
    input_file, weights, impacts, output_file = sys.argv[1:]
    Topsis.calculate(input_file, weights, impacts, output_file)
