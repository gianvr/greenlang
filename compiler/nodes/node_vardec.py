from .node import Node, SymbolTable


class NodeVarDec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        if len(self.children) == 2:
            variable = self.children[0]
            value = self.children[1].evaluate(symbol_table)
            symbol_table.create(
                variable=variable,
                value=value[0],
                type=self.value
            )
            pointer = symbol_table.get(self.children[0])["pointer"]
            return f"    PUSH DWORD {value[0]} ; var {self.children[0]} int [EBP-{pointer}]\n"
        elif len(self.children) == 1:
            symbol_table.create(
                variable=self.children[0], 
                value=None, 
                type=self.value, 
            )
            pointer = symbol_table.get(self.children[0])["pointer"]
            return f"    PUSH DWORD 0 ; var {self.children[0]} int [EBP-{pointer}]\n"
