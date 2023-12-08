from .node import Node, SymbolTable


class NodeFor(Node):
    def __init__(self, children, value = None ):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        assembly_init = self.children[0].evaluate(symbol_table)
        assembly_init += f"""
    LOOP_{self.id}:
"""     
        assembly_condit = self.children[1].evaluate(symbol_table)[2]
        assembly_condit += f"""
    CMP EAX, False
    JE EXIT_{self.id}
"""
        assembly_block = ""
        assembly_increment = ""
        while self.children[1].evaluate(symbol_table)[0]:
            if assembly_block == "":
                assembly_block = self.children[3].evaluate(symbol_table)
            else:
                self.children[3].evaluate(symbol_table)
            if assembly_increment == "":
                assembly_increment = self.children[2].evaluate(symbol_table)
            else:
                self.children[2].evaluate(symbol_table)
        assembly_end = f"""
    JMP LOOP_{self.id}
    EXIT_{self.id}:
"""
        assembly_code = assembly_init + assembly_condit + assembly_block + assembly_increment + assembly_end
        return assembly_code
    