import bfi

# takes two number as input, adds them, and prints the result
bf_code = ",>,<[->+<]>."


def main():
    interpreter = bfi.Interpreter()
    interpreter.run(bf_code)

if __name__ == "__main__":
    main()
