from enum import Enum

DATA_SIZE = 30000

class Token(Enum):
    SHIFT_RIGHT = ">"
    SHIFT_LEFT = "<"
    INCREMENT = "+"
    DECREMENT = "-"
    OUTPUT = "."
    INPUT = ","
    LOOP = "["
    END = "]"

def tokenize(code: str)-> list[Token]:
    tokenized = []
    for char in code:
        match char:
            case Token.SHIFT_RIGHT.value:
                tokenized.append(Token.SHIFT_RIGHT)
            case Token.SHIFT_LEFT.value:
                tokenized.append(Token.SHIFT_LEFT)
            case Token.INCREMENT.value:
                tokenized.append(Token.INCREMENT)
            case Token.DECREMENT.value:
                tokenized.append(Token.DECREMENT)
            case Token.OUTPUT.value:
                tokenized.append(Token.OUTPUT)
            case Token.INPUT.value:
                tokenized.append(Token.INPUT)
            case Token.LOOP.value:
                tokenized.append(Token.LOOP)
            case Token.END.value:
                tokenized.append(Token.END)
    return tokenized

class Interpreter:
    def __init__(self):
        self.data = [0] * DATA_SIZE
        self.data_pointer = 0
        self.instruction_pointer = 0

    def run(self, code: str):
        tokenized = tokenize(code)
        instruction_length = len(tokenized)

        while self.instruction_pointer < instruction_length:
            current_token = tokenized[self.instruction_pointer]
            match current_token:
                case Token.SHIFT_RIGHT:
                    self.data_pointer += 1
                    self.instruction_pointer += 1
                case Token.SHIFT_LEFT:
                    self.data_pointer -= 1
                    self.instruction_pointer += 1
                case Token.INCREMENT:
                    self.data[self.data_pointer] += 1
                    self.instruction_pointer += 1
                case Token.DECREMENT:
                    self.data[self.data_pointer] -= 1
                    self.instruction_pointer += 1
                case Token.OUTPUT:
                    print("output:",self.data[self.data_pointer])
                    self.instruction_pointer += 1
                case Token.INPUT:
                    self.data[self.data_pointer] = int(input("input : "))
                    self.instruction_pointer += 1
                case Token.LOOP:
                    if self.data[self.data_pointer] != 0:
                        self.instruction_pointer += 1
                    else:
                        while True:
                            self.instruction_pointer += 1
                            if tokenized[self.instruction_pointer] == Token.END:
                                self.instruction_pointer += 1
                                break
                case Token.END:
                    if self.data[self.data_pointer] == 0:
                        self.instruction_pointer += 1
                    else:
                        while True:
                            self.instruction_pointer -= 1
                            if tokenized[self.instruction_pointer] == Token.LOOP:
                                self.instruction_pointer += 1
                                break

        
