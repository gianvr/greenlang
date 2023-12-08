from .node import Node, SymbolTable


class NodeIdentifier(Node):
    def __init__(self, value):
        super().__init__(value, children=None)

    def evaluate(self, symbol_table: SymbolTable):
        value = symbol_table.get(self.value)["value"]
        type = symbol_table.get(self.value)["type"]
        pointer = symbol_table.get(self.value)["pointer"]
        assembly_code = f"""
    MOV EAX, [EBP-{pointer}]
"""

        return (value, type, assembly_code)
