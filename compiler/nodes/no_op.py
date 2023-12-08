from .node import Node, SymbolTable


class NoOp(Node):
    def __init__(self):
        super().__init__(value=None, children=None)

    def evaluate(self, symbol_table: SymbolTable):
        pass
