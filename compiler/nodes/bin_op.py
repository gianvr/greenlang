import textwrap
from .node import Node, SymbolTable


class BinOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        assembly_code = ""
        children_1 = self.children[1].evaluate(symbol_table)
       
        assembly_code += children_1[2]
        assembly_code += """
    PUSH EAX
    """
        children_0 = self.children[0].evaluate(symbol_table)
        assembly_code += children_0[2]
        if children_0[1] == "INT" and children_1[1] == "INT":
            if self.value == "+":
                assembly_code += """    
    POP EBX
    ADD EAX, EBX"""
                return (children_0[0] + children_1[0], "INT", assembly_code)
            if self.value == "-":
                assembly_code += """    
    POP EBX
    SUB EAX, EBX"""
                return (children_0[0] - children_1[0], "INT", assembly_code)
            if self.value == "*":
                assembly_code += """    
    POP EBX
    IMUL EAX, EBX"""
                return (children_0[0] * children_1[0], "INT", assembly_code)
            if self.value == "//":
                assembly_code += """    
    POP EBX
    IDIV EAX, EBX"""
                return (children_0[0] // children_1[0], "INT", assembly_code)
            if self.value == "==":
                assembly_code += f"""
    POP EBX
    CMP EAX, EBX
    CALL binop_je
"""
                return (int(children_0[0] == children_1[0]), "INT", assembly_code)
            if self.value == ">":
                assembly_code += f"""
    POP EBX
    CMP EAX, EBX
    CALL binop_jg
"""
                return (int(children_0[0] > children_1[0]), "INT", assembly_code)
            if self.value == "<":
                assembly_code += f"""
    POP EBX
    CMP EAX, EBX
    CALL binop_jl
"""

                return (int(children_0[0] < children_1[0]), "INT", assembly_code)
            if self.value == "&&":
                return (int(children_0[0] and children_1[0]), "INT")
            if self.value == "||":
                return (int(children_0[0] or children_1[0]), "INT")

        if self.value == ".":
            return (
                str(children_0[0]) + str(children_1[0]),
                "STRING",
            )

        if children_0[1] == children_1[1]:
            if self.value == "==":
                return (int(children_0[0] == children_1[0]), "INT")
            if self.value == "<":
                return (int(children_0[0] < children_1[0]), "INT")
            if self.value == ">":
                return (int(children_0[0] > children_1[0]), "INT")

        raise ValueError("Operation between diferent types is not supported")
