from .node import Node, SymbolTable


class NodeAssignment(Node):
    def __init__(self, children, value=None):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        variable = symbol_table.get(self.children[0])
        value = self.children[1].evaluate(symbol_table)
        if value[1] != variable["type"]:
            raise ValueError("The type of variable must match")

        symbol_table.set(
            variable=self.children[0], value=value[0]
        )
        assembly_code = f'''
    MOV [EBP-{variable["pointer"]}], EAX ; {self.children[0]} == {value[0]}
'''
        return value[2]+assembly_code
