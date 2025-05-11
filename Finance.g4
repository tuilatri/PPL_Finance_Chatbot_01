grammar Finance;

command             : addExpense | changeCategory;
addExpense          : CATEGORY ':' description '(' AMOUNT CURRENCY ')';
changeCategory      : 'Change' categoryChangeList;
categoryChangeList  : categoryChange (',' categoryChange)*;
categoryChange      : CATEGORY '(' AMOUNT CURRENCY ')';

// Parser rule for description (more flexible than lexer token)
description         : ~('(' | ',' | ':')* ;

// Lexer tokens
CATEGORY            : [A-Z][a-zA-Z0-9_]*;
AMOUNT              : [0-9.]+;
CURRENCY            : 'VND';
WS                  : [ \t\r\n]+ -> skip;
