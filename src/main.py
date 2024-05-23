import bfi
import sys

# takes two number as input, adds them, and prints the result

def main(filename: str):
    code = open(filename, "r").read()
    interpreter = bfi.Interpreter()
    interpreter.run(code)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        main(filename)
    else:
        print("Please provide a filename as a command line argument.")
