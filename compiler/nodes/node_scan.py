import textwrap
from .node import Node, SymbolTable


class NodeScan(Node):
    def __init__(self, children, value=None):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        assembly_code = """
    PUSH scanint ; endereço de memória de suporte
    PUSH formatin ; formato de entrada (int)
    call scanf
    ADD ESP, 8 ; Remove os argumentos da pilha
        
    MOV EAX, DWORD [scanint] ; retorna o valor lido em EAX
    """
        return (0, "INT", assembly_code)
