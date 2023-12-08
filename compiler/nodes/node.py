from abc import ABC, abstractmethod
from ..symbol_table.symbol_table import SymbolTable


class Node(ABC):
    i = 0

    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = self.newId()

    @abstractmethod
    def evaluate(self, symbol_table: SymbolTable):
        pass

    @staticmethod
    def newId():
        Node.i+=1
        return Node.i