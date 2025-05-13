grammar Finance;

command             : addExpense | changeCategory | addCategory | deleteCategory | resetCommand ;
addExpense          : CATEGORY ':' DESCRIPTION '(' AMOUNT CURRENCY ')' ;
changeCategory      : CHANGE CATEGORY '(' AMOUNT CURRENCY ')' ;
addCategory         : ADD CATEGORY '(' AMOUNT CURRENCY ')' ;
deleteCategory      : DELETE CATEGORY ;
resetCommand        : RESET ;

CHANGE              : 'Change' ; // Keyword for changing category
ADD                 : 'Add' ;    // Keyword for adding category
DELETE              : 'Delete' ; // Keyword for deleting category
RESET               : 'Reset' ;  // Keyword for resetting data
CATEGORY            : [A-Za-z][a-zA-Z0-9_]* ; // Category names like Food, Renting
DESCRIPTION         : [a-zA-Z0-9 ]+ ;        // Descriptions like Milktea, New Shoes
AMOUNT              : [0-9]+ ('.' [0-9][0-9][0-9])* ; // Strict VND format: 50.000, 1.000.000
CURRENCY            : 'VND' ;                 // Currency token
WS                  : [ \t\r\n]+ -> skip ;    // Skip whitespace