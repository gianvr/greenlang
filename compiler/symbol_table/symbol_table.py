class SymbolTable:
    def __init__(self, symbol_table: dict):
        self.symbol_table = symbol_table
        self.pointer = 0

    def get(self, variable):
        return self.symbol_table[variable]

    def set(self, variable, value):
        if variable not in self.symbol_table:
            raise ValueError("Variable not declared")
        self.symbol_table[variable]["value"] = value

    def create(self, variable, value, type):
        if variable in self.symbol_table:
            raise ValueError("Variable already exists")
        self.pointer+=4
        self.symbol_table[variable] = {"value": value, "type": type, "pointer": self.pointer}
