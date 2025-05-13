grammar Finance;

// Parser rules
program: (command | input)+ EOF;

input: salaryInput | categoriesInput;

salaryInput: NUMBER 'VND';

categoriesInput: category (',' category)*;
category: ID '(' NUMBER 'VND' ')';

command: spendCommand | changeCommand | addCommand | deleteCommand | resetCommand;

spendCommand: ID ':' ID '(' NUMBER 'VND' ')';
changeCommand: 'Change' ID '(' NUMBER 'VND' ')';
addCommand: 'Add' ID '(' NUMBER 'VND' ')';
deleteCommand: 'Delete' ID;
resetCommand: 'Reset';

// Lexer rules
ID: [a-zA-Z][a-zA-Z0-9]*; // Category or item names (start with letter, then letters or digits)
NUMBER: [0-9]+ ('.' [0-9]+)*; // Numbers like 10.000.000
VND: 'VND';
COLON: ':';
LPAREN: '(';
RPAREN: ')';
COMMA: ',';
WS: [ \t\r\n]+ -> skip; // Ignore whitespace