from .node import Node, SymbolTable


class NodeBlock(Node):
    def __init__(self, children, value=None):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        assembly_code = ""
        for child in self.children:
            assembly_statement = child.evaluate(symbol_table)
            if assembly_statement is not None:
                assembly_code += assembly_statement
        return assembly_code