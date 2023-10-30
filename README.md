# Palmeirês: A Linguagem de Programação do Verdão

Palmeirês é uma linguagem de programação para todos os palmeirenses e desenvolvedores no coração. Inspirada no elenco do Palmeiras de 2023, Palmeirês une a paixão pelo maior campeão do Brasil com a lógica impecável da programação, proporcionando uma experiência única aos desenvolvedores palestrinos.

As palavras reservadas de Palmeirês são selecionadas a partir dos nomes dos jogadores do Palmeiras em 2023. Cada palavra-chave é uma homenagem aos membros do time, trazendo a energia do Rony para o mundo da programação.

## EBNF

```
PROGRAM = { STATEMENT } ;
BLOCK = "{", "\n", { STATEMENT }, "}";
STATEMENT = ( λ | ASSIGNMENT | PRINT | IF | FOR | VAR), "\n" ;
ASSIGNMENT = IDENTIFIER, "=", BOOL EXPRESSION ;
IF = "mayke", BOOL EXPRESSION, BLOCK, ( λ | "marcos_rocha", BLOCK); 
VAR = "arthur", :, TYPE, :, IDENTIFIER, "abel", BOOL EXPRESSION;
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

## Operador para Palavra Reservada
| Operador  | Palavra Reservada    |
|-----------|----------------------|
| int       | gomez                |
| string    | menino               |
| if        | mayke                |
| else      | marcos_rocha         |
| for       | endrick              |
| =         | abel                 |
| <         | dudu                 |
| >         | palmeiras            |
| !         | allianz_parque       |
| ==        | abelabel             |
| scan      | veiga                |
| or        | richard_rios         |
| and       | breno_lopes          |
| +         | piquerez             |
| -         | ze_rafael            |
| *         | luan                 |
| /         | murilo               |
| print     | rony                 |
| .         | weverton             |
| var       | arthur               |


## Exemplos
- **Atribuição, condicional e print**
```
arthur:gomez:a abel 90;
arthur:gomez:b abel 70;
marcos_rocha a palmeiras b {
  rony("a maior que b")
}mayke{
  rony("b maior que a")
}
```

- **Loop, soma e atribuição**
```
arthur:gomez:a abel 90;
endrick i abel 0; i dudu a; i = i piquerez 1{
  rony(i)
}
```

## Aviso Legal
O desenvolvedor da linguagem Palmeirês é apenas um estudante de engenharia da computação e torcedor do Palmeiras. O Palmeirês é uma expressão criativa de admiração ao time e seus jogadores, sem ligação oficial com a Sociedade Esportiva Palmeiras como organização.
