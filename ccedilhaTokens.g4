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
//NEWLINE:'\r'? '\n';

WS : [ \t\r\n]+ -> skip ;