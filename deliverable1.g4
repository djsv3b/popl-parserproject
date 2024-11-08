// Define the grammar
grammar deliverable1;

program : (statement)* EOF ;

// Statements
statement : assignment | expression ;

// Assignment statement (assigning a variable to a value or an expression)
assignment : IDENTIFIER ASSIGN_OP expression ;

// Expressions with arithmetic operators and lists
expression : expression ARITH_OP expression             // Arithmetic operations
           | IDENTIFIER                                 // Variable reference
           | NUMBER                                     // Integer or float
           | STRING                                     // String literal
           | BOOLEAN                                    // Boolean values (True)
           | CHARACTER                                  // Characters
           | array                                      // Array/list definition
           ;

// Array/list definition
array : '[' (expression (',' expression)*)? ']' ;

// Tokens for operators and other symbols
ARITH_OP : '+' | '-' | '*' | '/' | '%' ;
ASSIGN_OP : '=' | '+=' | '-=' | '*=' | '/=' ;
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]* ;      // Identifier rule (e.g., variable names)
NUMBER : [0-9]+ ('.' [0-9]+)? ;            // Integer and float numbers
STRING : '"' .*? '"' ;                     // String literal with double quotes
BOOLEAN : 'True' | 'False' ;               // Boolean values
CHARACTER : '\'' .? '\'' ;                 // Characters
WS : [ \t\r\n]+ -> skip ;                  // Skip whitespace
