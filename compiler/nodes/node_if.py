from .node import Node, SymbolTable


class NodeIf(Node):
    def __init__(self, children, value = None ):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        condition_value = self.children[0].evaluate(symbol_table)[2]
        assembly_condit = f"""
    CMP EAX, True
    JE IF_{self.id}
"""     
        assembly_else = ""
        assembly_if = f"""
    IF_{self.id}:
"""
        assembly_if += self.children[1].evaluate(symbol_table)
        if len(self.children) == 3:
            assembly_else += f"""
    ELSE_{self.id}:
"""
            assembly_else += self.children[2].evaluate(symbol_table)
            assembly_else += f"""
    JMP ENDIF_{self.id}
"""
        else:
            assembly_else += f"""
    JMP ENDIF_{self.id}
"""
        assembly_endif = f"""
    ENDIF_{self.id}:
"""
        assembly_code = condition_value + assembly_condit + assembly_else + assembly_if + assembly_endif
        return assembly_code