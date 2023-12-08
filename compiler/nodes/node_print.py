from .node import Node, SymbolTable


class NodePrint(Node):
    def __init__(self, children, value = None):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        value = self.children[0].evaluate(symbol_table)
        assembly_code = value[2]
        assembly_code+= """    
    PUSH EAX 
    PUSH formatout 
    CALL printf 
    ADD ESP, 8
"""
        return assembly_code
