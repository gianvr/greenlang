%{
  #include <stdlib.h>
%}

%union {
    int num;
    char sym;
    char* str;
}

%token ELSE IF FOR  TYPE_INT TYPE_STRING
%token EQUAL LESS_THAN LESS_OR_EQUAL NOT_EQUAL
%token GREATER_THAN GREATER_OR_EQUAL
%token NEG EQUALS SCAN OR AND
%token PLUS MINUS TIMES DIVIDE
%token PRINT CONCATENATION VAR
%token OPEN_PAREN CLOSE_PAREN 
%token OPEN_BRACE CLOSE_BRACE COLON
%token SEMICOLON  EOL
%token <num> NUMBER
%type<num> factor term exp rel_exp bool_term bool_exp assignment statement program block

%token<str> STRING IDENTIFIER


%%

program:
    | statements program
    ;

statement:
    VAR COLON IDENTIFIER COLON TYPE_INT EQUAL NUMBER EOL{/* TODO: declaracao de int */   }
    | VAR COLON IDENTIFIER COLON TYPE_STRING EQUAL STRING EOL{ /* TODO: declaracao de string */ }
    | PRINT OPEN_PAREN bool_exp CLOSE_PAREN EOL{ /* TODO: print */ }
    | IF bool_exp block EOL{ /* TODO: if sem else */}
    | IF bool_exp block ELSE block EOL{ /* TODO: if com else */   }
    | FOR assignment SEMICOLON bool_exp SEMICOLON assignment block EOL{/* TODO: for */ }
    | assignment EOL

statements:
    | statements statement
block:
    OPEN_BRACE EOL statements CLOSE_BRACE EOL{/* TODO: block */}
    ;
assignment:
    IDENTIFIER EQUAL bool_exp { /* TODO: assignment */ }
    ;
bool_exp:
    bool_term OR bool_term { /* TODO: OR bool exp */ }
    | bool_term { /* TODO: bool term */  }
    ;

bool_term:
    rel_exp AND rel_exp {/* TODO: AND bool term */}
    | rel_exp { /* TODO: relation exp */ }
    ;

rel_exp:
    exp LESS_THAN exp { /* TODO: less than relation exp */ }
    | exp GREATER_THAN exp { /* TODO: greater than relation exp */  }
    | exp LESS_OR_EQUAL exp { /* TODO: less or equal relation exp */  }
    | exp GREATER_OR_EQUAL exp { /* TODO: greater or equal relation exp */  }
    | exp NOT_EQUAL exp { /* TODO: not equal relation exp */  }
    | exp EQUALS exp {/* TODO: equals relation exp */  }
    | exp { /* TODO: expression */ }
    ;
exp:
    term PLUS term { /* TODO: plus expression */}
    | term MINUS term { /* TODO: minus expression */ }
    | term CONCATENATION term { /* TODO: concatenation expression */ }
    | term {/* TODO: term */}
    ;

term:
    factor TIMES factor {/* TODO: times term */ }
    | factor DIVIDE factor {/* TODO: divide term */  }
    | factor {/* TODO:  term */ }
    ;
factor:
     NUMBER {/* TODO: number factor */ }
     | STRING {/* TODO: string factor */}
     | IDENTIFIER {/* TODO: identifier factor */ }
     | PLUS factor {  /* TODO: plus factor */}
     | MINUS factor {/* TODO: minus factor */ }
     | NEG factor {/* TODO: neg factor */  }
     | SCAN OPEN_PAREN CLOSE_PAREN { /* TODO: scan factor */}
     | OPEN_PAREN bool_exp CLOSE_PAREN {/* TODO: bool expression factor */}
     ;
%%

yywrap() {}

int main() {
    yyparse();
    return 0;
}

int yyerror(char *s) {
    printf("\nError: %s\n", s);
    return 0;
}

