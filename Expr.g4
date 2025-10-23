grammar Expr;

prog:   expr EOF;

expr:   expr op=('*'|'/') expr
    |   expr op=('+'|'-') expr
    |   INT
    |   VAR
    |   '(' expr ')'
    ;

INT : [0-9]+ ;
VAR : [a-zA-Z]+ ;
WS  : [ \t\r\n]+ -> skip ;