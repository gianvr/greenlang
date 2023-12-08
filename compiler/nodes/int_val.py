from .node import Node, SymbolTable


class IntVal(Node):
    def __init__(self, value, children=None):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        assembly_code = \
    f"""    
    MOV EAX, {self.value}"""
        return (self.value, "INT", assembly_code)
