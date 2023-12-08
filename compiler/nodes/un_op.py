from .node import Node, SymbolTable


class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        if self.value == "+":
            return (self.children[0].evaluate(symbol_table)[0], "INT")
        if self.value == "-":
            return (-self.children[0].evaluate(symbol_table)[0], "INT")
        if self.value == "!":
            return (not self.children[0].evaluate(symbol_table)[0], "INT")
