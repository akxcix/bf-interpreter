import enum

class Interpreter:
    DATA_SIZE = 30000

    class Token(enum.Enum):
        SHIFT_RIGHT = ">"
        SHIFT_LEFT = "<"
        INCREMENT = "+"
        DECREMENT = "-"
        OUTPUT = "."
        INPUT = ","
        LOOP = "["
        END = "]"

    def __init__(self):
        self.data = [0] * self.DATA_SIZE
        self.data_pointer = 0
        self.instruction_pointer = 0

    @staticmethod
    def tokenize(code: str)-> list[Token]:
        tokenized = []
        for char in code:
            match char:
                case Interpreter.Token.SHIFT_RIGHT.value:
                    tokenized.append(Interpreter.Token.SHIFT_RIGHT)
                case Interpreter.Token.SHIFT_LEFT.value:
                    tokenized.append(Interpreter.Token.SHIFT_LEFT)
                case Interpreter.Token.INCREMENT.value:
                    tokenized.append(Interpreter.Token.INCREMENT)
                case Interpreter.Token.DECREMENT.value:
                    tokenized.append(Interpreter.Token.DECREMENT)
                case Interpreter.Token.OUTPUT.value:
                    tokenized.append(Interpreter.Token.OUTPUT)
                case Interpreter.Token.INPUT.value:
                    tokenized.append(Interpreter.Token.INPUT)
                case Interpreter.Token.LOOP.value:
                    tokenized.append(Interpreter.Token.LOOP)
                case Interpreter.Token.END.value:
                    tokenized.append(Interpreter.Token.END)
        return tokenized

    def run(self, code: str):
        tokenized = self.tokenize(code)
        instruction_length = len(tokenized)

        while self.instruction_pointer < instruction_length:
            current_token = tokenized[self.instruction_pointer]
            match current_token:
                case Interpreter.Token.SHIFT_RIGHT:
                    self.data_pointer += 1
                case Interpreter.Token.SHIFT_LEFT:
                    self.data_pointer -= 1
                case Interpreter.Token.INCREMENT:
                    self.data[self.data_pointer] += 1
                case Interpreter.Token.DECREMENT:
                    self.data[self.data_pointer] -= 1
                case Interpreter.Token.OUTPUT:
                    print(self.data[self.data_pointer])
                case Interpreter.Token.INPUT:
                    self.data[self.data_pointer] = int(input())
                    if self.data[self.data_pointer] > 255:
                        self.data[self.data_pointer] = 255
                    if self.data[self.data_pointer] < 0:
                        self.data[self.data_pointer] = 0
                case Interpreter.Token.LOOP:
                    if self.data[self.data_pointer] == 0:
                        while True:
                            self.instruction_pointer += 1
                            if tokenized[self.instruction_pointer] == Interpreter.Token.END:
                                break
                case Interpreter.Token.END:
                    if self.data[self.data_pointer] != 0:
                        while True:
                            self.instruction_pointer -= 1
                            if tokenized[self.instruction_pointer] == Interpreter.Token.LOOP:
                                break
            self.instruction_pointer += 1 
