// Define a grammar called Hello
grammar ccedilha;
import ccedilhaTokens;

prog: main;

main: 'nada principal()' LKEY (func | att | dec ENDLINE)+ RKEY; 

att: (dec | ID) EQUAL (expr | STRING) ENDLINE    
    ; 

dec: basic_type ID
    ;

basic_type: (DEINT | DESTRING | DEFLOAT | DEBOOL | DECHAR)
    ;

func: 'amostrar' LPAREN (STRING | INT | ID) RPAREN ENDLINE #funcPrint
    | ID PLUS_PLUS ENDLINE #funcPlusPlus
    | ID MINUS_MINUS ENDLINE #funcMinusMinus
    ;

expr: expr ( MULT | DIV ) expr #exprMultDiv
    | expr ( PLUS | MINUS ) expr #exprPlusMinus
    | INT #Number
    | ID #id
    | LPAREN expr RPAREN #exprParen
    ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines