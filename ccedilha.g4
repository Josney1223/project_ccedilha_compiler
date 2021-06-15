// Define a grammar called Hello
grammar ccedilha;
import ccedilhaTokens;

prog: main;

main: 'nada principal()' LPAREN (stat+ | func+) RPAREN; 
 
stat: expr ' igual ' expr ENDLINE
    ; 

func: 'amostrar' LPAREN STRING RPAREN ENDLINE
    | INT PLUS_PLUS ENDLINE
    | INT MINUS_MINUS ENDLINE
    ;

expr: expr ( MULT | DIV ) expr
    | expr ( PLUS | MINUS) expr    
    | INT
    | LPAREN expr RPAREN
    ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines