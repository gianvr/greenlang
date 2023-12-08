# Palmeirês: A Linguagem de Programação do Verdão

Palmeirês é uma linguagem de programação para todos os palmeirenses e desenvolvedores no coração. Inspirada no elenco do Palmeiras de 2023, Palmeirês une a paixão pelo maior campeão do Brasil com a lógica impecável da programação, proporcionando uma experiência única aos desenvolvedores palestrinos.

As palavras reservadas de Palmeirês são selecionadas a partir dos nomes dos jogadores do time do Palmeiras, campeão brasileiro em 2023. Cada palavra-chave é uma homenagem aos membros do time, trazendo a energia do Rony para o mundo da programação.

![Palmeiras campeao](./img/palmeiras_campeao.jpg)

## EBNF

```
PROGRAM = { STATEMENT } ;
BLOCK = "{", "\n", { STATEMENT }, "}";
STATEMENT = ( λ | ASSIGNMENT | PRINT | IF | FOR | VAR), "\n" ;
ASSIGNMENT = IDENTIFIER, "=", BOOL EXPRESSION ;
IF = "mayke", BOOL EXPRESSION, BLOCK, ( λ | "marcos_rocha", BLOCK); 
VAR = "arthur", :, IDENTIFIER, :, TYPE, "abel", BOOL EXPRESSION;
TYPE = ("gomez");
FOR = "endrick", ASSIGNMENT, ";", "BOOL EXPRESSION", ";", ASSIGNMENT, BLOCK;
PRINT = "rony", "(", EXPRESSION, ")" ;
BOOL EXPRESSION = BOOL TERM, { "richard_rios", BOOL TERM};
BOOL TERM = RELATIONAL EXPRESSION, { "breno_lopes", RELATIONAL EXPRESSION};
RELATIONAL EXPRESSION = EXPRESSION, { ("abelabel" | "weverton" | "dudu"), EXPRESSION};
EXPRESSION = TERM, { ("piquerez" | "ze_rafael"), TERM } ;
TERM = FACTOR, { ("luan" | "murilo"), FACTOR } ;
FACTOR = (("piquerez" | "ze_rafael" | "menino"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER | SCAN;
SCAN = "veiga", "(", ")";
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
SYMBOL = ("@", "!", "$", ...)
NUMBER = DIGIT, { DIGIT } ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
```

## Operador para Palavra Reservada
| Operador  | Palavra Reservada    |
|-----------|----------------------|
| int       | gomez                |
| if        | mayke                |
| else      | marcos_rocha         |
| for       | endrick              |
| =         | abel                 |
| <         | dudu                 |
| >         | weverton             |
| !         | menino               |
| ==        | abelabel             |
| scan      | veiga                |
| or        | richard_rios         |
| and       | breno_lopes          |
| +         | piquerez             |
| -         | ze_rafael            |
| *         | luan                 |
| /         | murilo               |
| print     | rony                 |
| var       | arthur               |


## Exemplos

- **Declaração de variáveis**
```
arthur:gomez:a //ira declarar uma variavel do tipo gomez (int) com o nome a e valor 0
arthur:gomez:b abel 10 //ira declarar uma variavel do tipo gomez (int) com o nome b e valor 10
```

- **Atribuição**
```
a abel 10 //ira atribuir o valor 10 a variavel a
```
- **Scan**
```
a abel veiga() //ira atribuir o valor digitado pelo usuario a variavel
```

- **Print**
```
rony(a) //ira printar o valor da variavel a
```

- **Condicionais**
```
mayke a weverton b { //ira executar o bloco de codigo caso a seja maior que b
  rony(a)
}

mayke a weverton b { 
  rony(a)
}marcos_rocha{ 
  rony(b)
} //ira executar o bloco de codigo caso a seja maior que b, caso contrario ira executar o bloco de codigo apos o else
```

- **Loop**
```
arthur:gomez:a; //ira declarar uma variavel do tipo gomez (int) com o nome a e valor 0 para ser usada no loop
arthur:gomez:b abel 10; //ira declarar uma variavel do tipo gomez (int) com o nome b e valor 10 para ser usada no loop

endrick a abel 0; a dudu b; a abel a piquerez 1{ //ira executar o bloco de codigo enquanto a for menor que b 
                                                // e ira incrementar a variavel a em 1 a cada loop 
  rony(a) //ira printar o valor da variavel a a cada loop
}
```

- **Exemplo de código em Palmeirês**
```
arthur:gomez:a abel 10 //ira declarar uma variavel do tipo gomez (int) com o nome a e valor 10
arthur:gomez:b abel 20 //ira declarar uma variavel do tipo gomez (int) com o nome b e valor 20
arthur:gomez:c abel 0 //ira declarar uma variavel do tipo gomez (int) com o nome c e valor 0

mayke a dudu b { //ira executar o bloco de codigo caso a seja menor que b
  rony(a) //ira printar o valor da variavel a
}marcos_rocha{ //ira executar o bloco de codigo caso a seja maior que b
  rony(b) //ira printar o valor da variavel b
}

c abel veiga() //ira atribuir o valor digitado pelo usuario a variavel c

endrick a abel 0; a dudu c; a abel a piquerez 1{ //ira executar o bloco de codigo enquanto a for menor que c 
                                                // e ira incrementar a variavel a em 1 a cada loop
  rony(a) //ira printar o valor da variavel a a cada loop
}
```

## Como executar o compilador

>[!WARNING]
>O compilador foi desenvolvido para ser executado em ambiente Linux. Não foi testado em ambiente Windows.

Para executar o compilador, crie um arquivo com a extensão .sep e execute o comando abaixo no terminal no diretório raiz do projeto:

```bash
python main.py <nome_do_arquivo>.sep
```
ou
```bash
python3 main.py <nome_do_arquivo>.sep
```

Caso tudo esteja correto irá gerar um arquivo `.asm` na pasta raiz do projeto. Para torná-lo executável, execute os comandos abaixo:

```bash 
nasm -f elf -o <nome_do_arquivo>.o <nome_do_arquivo>.asm
gcc -m32 -no-pie -o  <nome_do_arquivo> <nome_do_arquivo>.o
```
Feito isso o executável será gerado e poderá ser executado com o comando abaixo:

```bash
./<nome_do_arquivo>
```

### Como executar o flex/bison (**somente** léxico e sintático)

Para executar o flex/bison, execute o comando abaixo no terminal no diretório raiz do projeto:

```bash
./flex_bison/a.out < <nome_do_arquivo>.sep
```

>[!TIP]
>Na raiz do projeto, tem um arquivo de exemplo chamado teste.sep, que pode ser utilizado para testar o compilador e o flex/bison.

## Aviso Legal
O desenvolvedor da linguagem Palmeirês é apenas um estudante de engenharia da computação e torcedor do Palmeiras. O Palmeirês é uma expressão criativa de admiração ao time e seus jogadores, sem ligação oficial com a Sociedade Esportiva Palmeiras como organização.
