from .node import Node, SymbolTable


class StringVal(Node):
    def __init__(self, value, children=None):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        return (self.value, "STRING")
