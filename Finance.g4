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
    | analyzeStmt
    | graphStmt
    ;

salaryStmt: 'i have' amount CURRENCY 'this month'? ;
categoryStmt: 'i want' 'to have'? categoryList ;
spendStmt: ('i spent' | 'i used') amount CURRENCY 'for' item ('in' category)? ;
modifyCategoryStmt: 'change' 'the' 'money' 'for' category 'to' amount CURRENCY ;
deleteCategoryStmt: ('delete' | 'remove') category ;
resetStmt: 'reset' ;
analyzeStmt: ('analyze' | 'give advice') ;
graphStmt: ('graph' | 'show graph') ;

categoryList: categoryItem (COMMA categoryItem)* (COMMA)? ;
categoryItem: amount CURRENCY 'for' category ;

amount: NUMBER ('.' NUMBER)* ;
category: ID ;
item: ID (ID)* ;

// Lexer rules
NUMBER: [0-9]+ ;
CURRENCY: [vV][nN][dD] | [uU][sS][dD] | [eE][uU][rR] | [jJ][pP][yY] | [cC][nN][yY] ;
ID: [a-zA-Z]+ ;
WS: [ \t\r\n]+ -> skip ;
COMMA: ',' ;