import sys
from ..nodes.int_val import IntVal
from ..nodes.node_assignment import NodeAssignment
from ..nodes.node_identifier import NodeIdentifier
from ..nodes.node_if import NodeIf
from ..nodes.node_for import NodeFor
from ..nodes.node_print import NodePrint
from ..nodes.no_op import NoOp
from ..nodes.string_val import StringVal
from ..nodes.node_block import NodeBlock
from ..nodes.un_op import UnOp
from ..nodes.bin_op import BinOp
from ..nodes.node_scan import NodeScan
from ..nodes.node_vardec import NodeVarDec
from ..prepro.prepro import PrePro
from ..tokenizer.tokenizer import Tokenizer


class Parser:
    def __init__(self):
        self.tokenizer = None

    def parse_factor(self):
        if self.tokenizer.next.type == "INT":
            node = IntVal(value=self.tokenizer.next.value)
            self.tokenizer.select_next()
            if self.tokenizer.next.type == "INT":
                raise ValueError("Invalid operator")

        elif self.tokenizer.next.type == "STRING":
            node = StringVal(value=self.tokenizer.next.value)
            self.tokenizer.select_next()
            if self.tokenizer.next.type == "STRING":
                raise ValueError("Invalid operator")

        elif self.tokenizer.next.type == "IDENTIFIER":
            node = NodeIdentifier(value=self.tokenizer.next.value)
            self.tokenizer.select_next()

        elif self.tokenizer.next.type == "PLUS":
            self.tokenizer.select_next()
            node = UnOp(value="+", children=[self.parse_factor()])

        elif self.tokenizer.next.type == "MINUS":
            self.tokenizer.select_next()
            node = UnOp(value="-", children=[self.parse_factor()])

        elif self.tokenizer.next.type == "NOT_EQUAL":
            self.tokenizer.select_next()
            node = UnOp(value="!", children=[self.parse_factor()])

        elif self.tokenizer.next.type == "SCAN":
            self.tokenizer.select_next()
            if self.tokenizer.next.type != "OPEN_PAR":
                raise ValueError("Scan missing open parenthesis")
            self.tokenizer.select_next()
            if self.tokenizer.next.type != "CLOSE_PAR":
                raise ValueError("Scan missing close parenthesis")
            self.tokenizer.select_next()
            node = NodeScan(value="scan", children=[])

        elif self.tokenizer.next.type == "OPEN_PAR":
            self.tokenizer.select_next()
            node = self.parse_bool_expression()
            if self.tokenizer.next.type != "CLOSE_PAR":
                raise ValueError("Close parenthesis not found")
            self.tokenizer.select_next()

        else:
            raise ValueError("Invalid initial token")
        return node

    def parse_term(self):
        resulting_node = self.parse_factor()
        while True:
            if self.tokenizer.next.type == "MULT":
                self.tokenizer.select_next()
                resulting_node = BinOp(
                    value="*", children=[resulting_node, self.parse_factor()]
                )

            elif self.tokenizer.next.type == "DIV":
                self.tokenizer.select_next()
                resulting_node = BinOp(
                    value="//", children=[resulting_node, self.parse_factor()]
                )
            else:
                return resulting_node

    def parse_expression(self):
        resulting_node = self.parse_term()
        while True:
            if self.tokenizer.next.type == "PLUS":
                self.tokenizer.select_next()
                resulting_node = BinOp(
                    value="+", children=[resulting_node, self.parse_term()]
                )
            elif self.tokenizer.next.type == "MINUS":
                self.tokenizer.select_next()
                resulting_node = BinOp(
                    value="-", children=[resulting_node, self.parse_term()]
                )
            elif self.tokenizer.next.type == "CONCATENATE":
                self.tokenizer.select_next()
                resulting_node = BinOp(
                    value=".", children=[resulting_node, self.parse_term()]
                )
            else:
                return resulting_node

    def parse_relation_expression(self):
        resulting_node = self.parse_expression()
        while True:
            if self.tokenizer.next.type == "EQUALS":
                self.tokenizer.select_next()
                resulting_node = BinOp(
                    value="==", children=[resulting_node, self.parse_expression()]
                )
            elif self.tokenizer.next.type == "GREATER_THAN":
                self.tokenizer.select_next()
                resulting_node = BinOp(
                    value=">", children=[resulting_node, self.parse_expression()]
                )
            elif self.tokenizer.next.type == "LESS_THAN":
                self.tokenizer.select_next()
                resulting_node = BinOp(
                    value="<", children=[resulting_node, self.parse_expression()]
                )
            else:
                return resulting_node

    def parse_bool_term(self):
        resulting_node = self.parse_relation_expression()
        while True:
            if self.tokenizer.next.type == "AND":
                self.tokenizer.select_next()
                resulting_node = BinOp(
                    value="&&",
                    children=[resulting_node, self.parse_relation_expression()],
                )
            else:
                return resulting_node

    def parse_bool_expression(self):
        resulting_node = self.parse_bool_term()
        while True:
            if self.tokenizer.next.type == "OR":
                self.tokenizer.select_next()
                resulting_node = BinOp(
                    value="||", children=[resulting_node, self.parse_bool_term()]
                )
            else:
                return resulting_node

    def parse_block(self):
        if self.tokenizer.next.type != "LEFT_CURLY_BRACE":
            raise ValueError("Missing left curly brace")
        self.tokenizer.select_next()
        if self.tokenizer.next.type != "END_OF_LINE":
            raise ValueError("Identation error")
        self.tokenizer.select_next()
        children_block = []
        while (
            self.tokenizer.next.type != "RIGHT_CURLY_BRACE"
            and self.tokenizer.next.type != "EOF"
        ):
            children_block.append(self.parse_statement())
        if self.tokenizer.next.type == "EOF":
            raise ValueError("Missing right curly brace")
        self.tokenizer.select_next()

        return NodeBlock(children=children_block)

    def parse_assignment(self):
        node_id = self.tokenizer.next.value
        self.tokenizer.select_next()
        if self.tokenizer.next.type == "ASSIGNMENT":
            self.tokenizer.select_next()
            return NodeAssignment(children=[node_id, self.parse_bool_expression()])
        raise ValueError("Identifier Error")

    def parse_statement(self):
        node = NoOp()
        if self.tokenizer.next.type == "IDENTIFIER":
            node = self.parse_assignment()
        elif self.tokenizer.next.type == "PRINT":
            self.tokenizer.select_next()
            if self.tokenizer.next.type == "OPEN_PAR":
                self.tokenizer.select_next()
                node_print = self.parse_bool_expression()
                if self.tokenizer.next.type == "CLOSE_PAR":
                    self.tokenizer.select_next()
                    node = NodePrint(children=[node_print])
                else:
                    raise ValueError("Print not closed")
            else:
                raise ValueError("Print without open")
        elif self.tokenizer.next.type == "IF":
            self.tokenizer.select_next()
            children_if = []
            condition_if = self.parse_bool_expression()
            if_block = self.parse_block()
            children_if = [condition_if, if_block]
            if self.tokenizer.next.type == "ELSE":
                self.tokenizer.select_next()
                else_block = self.parse_block()
                children_if.append(else_block)
            node = NodeIf(children=children_if)
        elif self.tokenizer.next.type == "FOR":
            self.tokenizer.select_next()
            init = self.parse_assignment()
            if self.tokenizer.next.type != "SEMICOLON":
                raise ValueError("Missing semicolon")
            self.tokenizer.select_next()
            condition_for = self.parse_bool_expression()
            if self.tokenizer.next.type != "SEMICOLON":
                raise ValueError("Missing semicolon")
            self.tokenizer.select_next()
            increment = self.parse_assignment()
            block_for = self.parse_block()
            children_for = [init, condition_for, increment, block_for]
            node = NodeFor(children=children_for)
        elif self.tokenizer.next.type == "VAR":
            self.tokenizer.select_next()
            if self.tokenizer.next.type != "COLON":
                raise ValueError("Missing :")
            self.tokenizer.select_next()
            if self.tokenizer.next.type != "IDENTIFIER":
                raise ValueError("Missing name of variable")
            identifier = self.tokenizer.next.value
            self.tokenizer.select_next()
            if self.tokenizer.next.type != "COLON":
                raise ValueError("Missing :")
            self.tokenizer.select_next()
            if self.tokenizer.next.type != "TYPE":
                raise ValueError("Missing type of variable")
            type = self.tokenizer.next.value
            self.tokenizer.select_next()
            if self.tokenizer.next.type == "ASSIGNMENT":
                self.tokenizer.select_next()
                node = NodeVarDec(
                    value=type, children=[identifier, self.parse_bool_expression()]
                )
            else:
                node = NodeVarDec(value=type, children=[identifier])

        if self.tokenizer.next.type == "END_OF_LINE":
            self.tokenizer.select_next()
            return node
        elif self.tokenizer.next.type == "EOF":
            return node
        raise ValueError("Statement Error")

    def parse_program(self):
        children = []
        while True:
            children.append(self.parse_statement())
            if self.tokenizer.next.type == "EOF":
                return children

    def run(self, code, symbol_table):
        pos_code = PrePro.filter(code=code)
        self.tokenizer = Tokenizer(source=pos_code)
        self.tokenizer.select_next()
        nasm_output = ""
        for node in self.parse_program():
            node_value = node.evaluate(symbol_table)
            if isinstance(node_value, str):
                nasm_output += node_value
            elif node_value is not None:
                nasm_output += str(node_value[2])
        return nasm_output
