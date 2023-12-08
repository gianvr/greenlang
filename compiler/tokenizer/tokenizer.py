from ..token.token import Token


class Tokenizer:
    def __init__(self, source: str):
        self.source = source
        self.position = -1
        self.next = None

    def select_next(self):
        self.position += 1
        while self.position + 1 < len(self.source) and (
            self.source[self.position] == " " or self.source[self.position] == "	"
        ):
            self.position += 1

        if self.position == len(self.source):
            self.next = Token(type="EOF", value=None)
        elif self.source[self.position] == ":":
            self.next = Token(type="COLON", value=None)
        elif self.source[self.position] == "(":
            self.next = Token(type="OPEN_PAR", value=None)
        elif self.source[self.position] == ")":
            self.next = Token(type="CLOSE_PAR", value=None)
        elif self.source[self.position] == "\n":
            self.next = Token(type="END_OF_LINE", value=None)
        elif self.source[self.position] == "{":
            self.next = Token(type="LEFT_CURLY_BRACE", value=None)
        elif self.source[self.position] == "}":
            self.next = Token(type="RIGHT_CURLY_BRACE", value=None)
        elif self.source[self.position] == ";":
            self.next = Token(type="SEMICOLON", value=None)
        elif self.source[self.position] == '"':
            self.position += 1
            string = ""
            while self.source[self.position] != '"':
                if self.source[self.position] == "\n":
                    raise ValueError("Missing quotes")
                string += self.source[self.position]
                self.position += 1
            self.next = Token(type="STRING", value=string)
        else:
            value = ""
            while (
                self.position < len(self.source)
                and self.source[self.position].isnumeric()
            ):
                value += self.source[self.position]
                self.position += 1

            if value and not (
                self.source[self.position].isalpha()
                or self.source[self.position] in "(_"
            ):
                self.next = Token(type="INT", value=int(value))
            elif not value:
                while self.position < len(self.source) and (
                    self.source[self.position].isalnum()
                    or self.source[self.position] in "_"
                ):
                    value += self.source[self.position]
                    self.position += 1
                if value == "rony":
                    self.next = Token(type="PRINT", value=None)
                elif value == "endrick":
                    self.next = Token(type="FOR", value=None)
                elif value == "mayke":
                    self.next = Token(type="IF", value=None)
                elif value == "marcos_rocha":
                    self.next = Token(type="ELSE", value=None)
                elif value == "veiga":
                    self.next = Token(type="SCAN", value=None)
                elif value == "arthur":
                    self.next = Token(type="VAR", value=None)
                elif value == "gomez":
                    self.next = Token(type="TYPE", value="INT")
                elif value == "abel":
                    self.next = Token(type="ASSIGNMENT", value=None)
                elif value == "abelabel":
                    self.next = Token(type="EQUALS", value=None)
                elif value == "dudu":
                    self.next = Token(type="LESS_THAN", value=None)
                elif value == "weverton":
                    self.next = Token(type="GREATER_THAN", value=None)
                elif value == "menino":
                    self.next = Token(type="NOT_EQUAL", value=None)
                elif value == "richard_rios":
                    self.next = Token(type="OR", value=None)
                elif value == "breno_lopes":
                    self.next = Token(type="AND", value=None)
                elif value == "piquerez":
                    self.next = Token(type="PLUS", value=None)
                elif value == "ze_rafael":
                    self.next = Token(type="MINUS", value=None)
                elif value == "luan":
                    self.next = Token(type="MULT", value=None)
                elif value == "murilo":
                    self.next = Token(type="DIV", value=None)
                elif value:
                    self.next = Token(type="IDENTIFIER", value=value)

            self.position -= 1

            if len(self.source) > 0 and not value:
                raise ValueError("Invalid token")
