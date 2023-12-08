import sys
import textwrap
from compiler.parser.parser import Parser
from compiler.symbol_table.symbol_table import SymbolTable


def write_output_file(nasm_output):
    output_file_path = "output/"+sys.argv[1][:-3] + "asm"
    header = textwrap.dedent(
    """                ; constantes
                SYS_EXIT equ 1
                SYS_READ equ 3
                SYS_WRITE equ 4
                STDIN equ 0
                STDOUT equ 1
                True equ 1
                False equ 0
                
                segment .data
                
                    formatin: db "%d", 0
                    formatout: db "%d", 10, 0 ; newline, nul terminator
                    scanint: times 4 db 0 ; 32-bits integer = 4 bytes
                
                segment .bss  ; variaveis
                    res RESB 1
                    extern fflush
                    extern stdout
                
                section .text
                    global main ; linux
                    ;global _main ; windows
                    extern scanf ; linux
                    extern printf ; linux
                    ;extern _scanf ; windows
                    ;extern _printf; windows
                    extern fflush ; linux
                    ;extern _fflush ; windows
                    extern stdout ; linux
                    ;extern _stdout ; windows
                
                ; subrotinas if/while
                binop_je:
                    JE binop_true
                    JMP binop_false
                
                binop_jg:
                    JG binop_true
                    JMP binop_false
                
                binop_jl:
                    JL binop_true
                    JMP binop_false
                
                binop_false:
                    MOV EAX, False  
                    JMP binop_exit
                binop_true:
                    MOV EAX, True
                    binop_exit:
                RET
                
                main:

                    PUSH EBP ; guarda o base pointer
                    MOV EBP, ESP ; estabelece um novo base pointer

                    ; codigo gerado pelo compilador

    """
    )
    end_file = """
PUSH DWORD [stdout]
CALL fflush
ADD ESP, 4
MOV ESP, EBP
POP EBP
MOV EAX, 1
XOR EBX, EBX
INT 0x80
"""
    with open(output_file_path, "w") as output_file:
        output_file.write(header)
        output_file.write(nasm_output)
        output_file.write(end_file)


def main():
    parser = Parser()
    symbol_table = SymbolTable({})
    if sys.argv[1][-4:] != ".sep":
        raise NameError("Invalid file extension, must be .sep")
    with open(sys.argv[1], "r") as file:
        nasm_output = parser.run(code=file.read(), symbol_table=symbol_table)
    write_output_file(nasm_output)


if __name__ == "__main__":
    main()
