# Palmeirês: A Linguagem de Programação do Verdão

Palmeirês é uma linguagem de programação para todos os palmeirenses e desenvolvedores no coração. Inspirada no elenco do Palmeiras de 2023, Palmeirês une a paixão pelo maior campeão do Brasil com a lógica impecável da programação, proporcionando uma experiência única aos desenvolvedores palestrinos.

- **Elenco Estrelar**: As palavras reservadas de Palmeirês são cuidadosamente selecionadas a partir dos nomes e habilidades dos jogadores do Palmeiras em 2023. Cada palavra-chave é uma homenagem aos membros do time, trazendo a energia do Rony para o mundo da programação.

- **Sintaxe Poderosa**: A sintaxe intuitiva de Palmeirês é projetada para ser tão fluida quanto um passe do Veiga. Desenvolvedores podem criar algoritmos complexos com facilidade, enquanto celebram cada linha de código como se fosse o gol do Breno Lopes na final da Libertadores.

## EBNF

```
PROGRAM = { STATEMENT } ;
BLOCK = "{", "\n", { STATEMENT }, "}";
STATEMENT = ( λ | ASSIGNMENT | PRINT | IF | FOR | VAR), "\n" ;
ASSIGNMENT = IDENTIFIER, "=", BOOL EXPRESSION ;
IF = "mayke", BOOL EXPRESSION, BLOCK, ( λ | "marcos_rocha", BLOCK); 
VAR = "arthur", IDENTIFIER, TYPE, (λ | "abel", BOOL EXPRESSION);
TYPE = ("menino" | "gomez");
FOR = "endrick", ASSIGNMENT, ";", "BOOL EXPRESSION", ";", ASSIGNMENT, BLOCK;
PRINT = "rony", "(", EXPRESSION, ")" ;
BOOL EXPRESSION = BOOL TERM, { "richard_rios", BOOL TERM};
BOOL TERM = RELATIONAL EXPRESSION, { "breno_lopes", RELATIONAL EXPRESSION};
RELATIONAL EXPRESSION = EXPRESSION, { ("abelabel" | "palmeiras" | "dudu"), EXPRESSION};
EXPRESSION = TERM, { ("piquerez" | "ze_rafael" | "weverton"), TERM } ;
TERM = FACTOR, { ("luan" | "murilo"), FACTOR } ;
FACTOR = (("piquerez" | "ze_rafael" | "allianz_parque"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER | SCAN | STRING;
SCAN = "veiga", "(", ")";
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
STRING = '"',{ LETTER | NUMBER | SYMBOL }, '"';
SYMBOL = ("@", "!", "$", ...)
NUMBER = DIGIT, { DIGIT } ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
```

## Aviso Legal
O desenvolvedor da linguagem Palmeirês é apenas um estudante de engenharia da computação e torcedor do Palmeiras. O Palmeirês é uma expressão criativa de admiração ao time e seus jogadores, sem ligação oficial com o Palmeiras como organização.
