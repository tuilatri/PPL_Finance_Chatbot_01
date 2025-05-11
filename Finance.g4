grammar Finance;

command             : addExpense | changeCategory | addCategory | deleteCategory | resetCommand ;
addExpense          : CATEGORY ':' DESCRIPTION '(' AMOUNT CURRENCY ')' ;
changeCategory      : 'Change' categoryChange ;
addCategory         : 'Add' categoryChange ;
deleteCategory      : 'Delete' CATEGORY ;
resetCommand        : 'Reset' ;

categoryChange      : CATEGORY '(' AMOUNT CURRENCY ')' ;

CATEGORY            : [A-Za-z][a-zA-Z0-9_]* ;
DESCRIPTION         : [a-zA-Z0-9 ]+ ;
AMOUNT              : [0-9.]+ ;
CURRENCY            : 'VND' ;
WS                  : [ \t\r\n]+ -> skip ;