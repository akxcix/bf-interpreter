import bfi
import sys
import argparse
import bfi

def main(filename: str, data_size: int, print_end: str):
    code = open(filename, "r").read()
    interpreter = bfi.Interpreter(data_size, print_end)
    interpreter.run(code)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs='?', help="the name of the file to interpret")
    parser.add_argument("--data-size", type=int, default=30000, help="the size of the data array")
    parser.add_argument("--print-end", default="\n", help="the character to print at the end of each output")
    args = parser.parse_args()

    main(args.filename, args.data_size, args.print_end)
