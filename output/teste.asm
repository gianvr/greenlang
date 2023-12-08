; constantes
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

    PUSH DWORD 22 ; var a int [EBP-4]
    PUSH DWORD 0 ; var b int [EBP-8]
    PUSH DWORD 0 ; var i int [EBP-12]
    
    MOV EAX, 11
    MOV [EBP-8], EAX ; b == 11
    
    MOV EAX, 80
    MOV [EBP-12], EAX ; i == 80
    
    MOV EAX, 0
    MOV [EBP-12], EAX ; i == 0

    LOOP_30:

    MOV EAX, [EBP-4]

    PUSH EAX
    
    MOV EAX, [EBP-12]

    POP EBX
    CMP EAX, EBX
    CALL binop_jl

    CMP EAX, False
    JE EXIT_30

    MOV EAX, [EBP-12]
    
    PUSH EAX 
    PUSH formatout 
    CALL printf 
    ADD ESP, 8
    
    MOV EAX, 1
    PUSH EAX
    
    MOV EAX, [EBP-12]
    
    POP EBX
    ADD EAX, EBX
    MOV [EBP-12], EAX ; i == 1

    JMP LOOP_30
    EXIT_30:

    MOV EAX, [EBP-4]

    PUSH EAX
    
    MOV EAX, [EBP-8]

    POP EBX
    CMP EAX, EBX
    CALL binop_jl

    CMP EAX, True
    JE IF_40

    JMP ENDIF_40

    IF_40:

    MOV EAX, [EBP-8]
    
    PUSH EAX 
    PUSH formatout 
    CALL printf 
    ADD ESP, 8

    ENDIF_40:

    PUSH scanint ; endere�o de mem�ria de suporte
    PUSH formatin ; formato de entrada (int)
    call scanf
    ADD ESP, 8 ; Remove os argumentos da pilha
        
    MOV EAX, DWORD [scanint] ; retorna o valor lido em EAX
    
    MOV [EBP-8], EAX ; b == 0

    MOV EAX, [EBP-8]
    
    PUSH EAX 
    PUSH formatout 
    CALL printf 
    ADD ESP, 8

    MOV EAX, [EBP-12]

    PUSH EAX
    
    MOV EAX, [EBP-4]

    POP EBX
    CMP EAX, EBX
    CALL binop_jl

    CMP EAX, True
    JE IF_62

    ELSE_62:

    MOV EAX, [EBP-4]
    
    PUSH EAX 
    PUSH formatout 
    CALL printf 
    ADD ESP, 8

    JMP ENDIF_62

    IF_62:

    MOV EAX, [EBP-12]
    
    PUSH EAX 
    PUSH formatout 
    CALL printf 
    ADD ESP, 8

    ENDIF_62:

PUSH DWORD [stdout]
CALL fflush
ADD ESP, 4
MOV ESP, EBP
POP EBP
MOV EAX, 1
XOR EBX, EBX
INT 0x80
