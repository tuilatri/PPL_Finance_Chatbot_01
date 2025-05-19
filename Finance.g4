grammar Finance;

// Parser rules
start: statement+ EOF;

statement
    : salaryStmt
    | categoryStmt
    | spendStmt
    | modifyCategoryStmt
    | deleteCategoryStmt
    | resetStmt
    ;

salaryStmt: 'i have' amount 'vnd' 'this month'? ;
categoryStmt: 'i want' 'to have'? categoryList ;
spendStmt: ('i spent' | 'i used') amount 'vnd' 'for' item ('in' category)? ;
modifyCategoryStmt: 'change' 'the' 'money' 'for' category 'to' amount 'vnd' ;
deleteCategoryStmt: ('delete' | 'remove') category ;
resetStmt: 'reset' ;

categoryList: categoryItem (COMMA categoryItem)* (COMMA)? ;
categoryItem: amount 'vnd' 'for' category ;

amount: NUMBER ('.' NUMBER)* ;
category: ID ;
item: ID (ID)* ;

// Lexer rules
NUMBER: [0-9]+ ;
ID: [a-zA-Z]+ ;
WS: [ \t\r\n]+ -> skip ;
COMMA: ',' ;