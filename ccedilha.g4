// Define a grammar called Hello
grammar ccedilha;
import ccedilhaTokens;

prog: stat+;
 
stat: expr ' igual ' expr ENDLINE
    ; 

expr: expr (' vezes '|' divide ') expr
    | expr (' mais '|' menos ') expr
    | INT
    | '(' expr ')'
    ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines