%{
    #include "parser.tab.h"
%}

%%

"//".*                    { }
";"                       { return SEMICOLON; }
"gomez"                   { return TYPE_INT; }
"mayke"                   { return IF; }
"marcos_rocha"            { return ELSE; }
"endrick"                 { return FOR; }
"abelabel"                { return EQUALS; }
"abel"                    { return EQUAL; }
"dudu"                    { return LESS_THAN; }
"weverton"                { return GREATER_THAN; }
"menino"                  { return NEG; }
"veiga"                   { return SCAN; }
"richard_rios"            { return OR; }
"breno_lopes"             { return AND; }
"piquerez"                { return PLUS; }
"ze_rafael"               { return MINUS; }
"luan"                    { return TIMES; }
"murilo"                  { return DIVIDE; }
"rony"                    { return PRINT; }
"arthur"                  { return VAR; }
"("                       { return OPEN_PAREN; }
")"                       { return CLOSE_PAREN; }
"{"                       { return OPEN_BRACE; }
"}"                       { return CLOSE_BRACE; }
":"                       { return COLON; }
[0-9]+                    { yylval.num = atoi(yytext); return NUMBER;}
[a-zA-Z_][a-zA-Z0-9_]*    { yylval.str = yytext; return IDENTIFIER;}
\n                        { return EOL; }
[ \t]                     { } 
%%

