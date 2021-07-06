// Define a grammar called Hello
grammar ccedilha;
import ccedilhaTokens;

prog: main func_dec*;

main: 'nada principal()' LKEY code RKEY; 

att: (dec | ID | list_type) EQUAL (expr | STRING | expr_bool) ENDLINE        
    ; 

code: (func | att | dec | boolean | func_call)*
    ;

dec: basic_type ID
    | basic_type ID ENDLINE
    | basic_type list_type
    | basic_type list_type ENDLINE
    ;

list_type: ID LBOX INT RBOX
    ;

basic_type: (DEINT | DESTRING | DEFLOAT | DEBOOL | DECHAR)
    ;

basic_logic: (NOT_EQUAL | EQUAL_EQUAL | GREATER | GREATER_EQUAL | LESSER_EQUAL | LESSER)
    ;

func_dec: basic_type ID LPAREN (basic_type ID)? RPAREN LKEY code RKEY
    | basic_type ID LPAREN (basic_type ID ',')+ (basic_type ID) RPAREN LKEY code RKEY
    ;

func_call: (ID LPAREN args? RPAREN | ID LPAREN (args ',')+ args RPAREN) ENDLINE
    ;
    
func: 'amostrar' LPAREN (STRING | INT | ID) RPAREN ENDLINE #funcPrint
    | ID PLUS_PLUS ENDLINE #funcPlusPlus
    | ID MINUS_MINUS ENDLINE #funcMinusMinus  
    ;

args: (expr | STRING | expr_bool | ID)
    ;
boolean: IF LPAREN expr_bool RPAREN LKEY code RKEY (ELSE boolean | ELSE LKEY code RKEY)?
    | WHILE LPAREN expr_bool RPAREN LKEY code RKEY
    ;

expr_bool: expr_bool ( AND | OR ) expr_bool #expr_boolAndOr
    | LPAREN expr_bool RPAREN #expr_boolParen
    | (expr | STRING) basic_logic (expr | STRING) #expr_boolLogic
    | BOOL #Bool
    ;

expr: expr ( MULT | DIV ) expr #exprMultDiv
    | expr ( PLUS | MINUS ) expr #exprPlusMinus
    | INT #Number
    | ID #id
    | LPAREN expr RPAREN #exprParen
    ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines