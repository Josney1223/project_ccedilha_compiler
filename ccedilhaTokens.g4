lexer grammar ccedilhaTokens;
fragment SINAL: '+'|'-';

// tokens
ENDLINE: [\u00E7];
INT: SINAL?[0-9]+; // Int
STRING: '"'~[\\n]+'"'; // String
FLOAT: [0-9]+'.'[0-9]+; // Float
//CHAR: [];
BOOL: 'verdadeiro'|'falso';
ID: [a-zA-Z]+; // Id das variaveis
LKEY: '{';
RKEY: '}';
LPAREN: '(';
RPAREN: ')';
//NEWLINE:'\r'? '\n';

//Operadores Relacionais e Logicos
EQUAL: ' igual ';
IF: 'se';
ELSE: 'senao';
WHILE: 'enquanto';
AND: ' e ';
OR: ' ou ';
GREATER_EQUAL: ' maiorIgual ';
LESSER_EQUAL: ' menorIgual ';
GREATER: ' maior ';
LESSER: ' menor ';

//Operadores Matematicos
PLUS: ' mais ';
MINUS: ' menos ';
MULT: ' vezes ';
DIV: ' divide ';
REST: ' resto ';
PLUS_PLUS: ' maisMais';
MINUS_MINUS: ' menosMenos';

WS : [ \t\r\n]+ -> skip ;