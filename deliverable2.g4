// Define the grammar
grammar deliverable2;

// Entry point
program : (statement)* EOF ;

// Statements
statement : assignment                  // Variable assignments
          | expression                   // Expressions
          | conditional                  // if/elif/else statements
          ;

// Assignment statement (assigning a variable to a value or an expression)
assignment : IDENTIFIER ASSIGN_OP expression ;

// Expressions, including arithmetic and boolean logic
expression : expression ARITH_OP expression             // Arithmetic operations
           | expression COMP_OP expression              // Comparison operations
           | expression BOOL_OP expression              // Boolean operations
           | 'not' expression                           // 'not' operator
           | IDENTIFIER                                 // Variable reference
           | NUMBER                                     // Integer or float
           | STRING                                     // String literal
           | BOOLEAN                                    // Boolean values (True/False)
           | array                                      // Array/list definition
           | '(' expression ')'                         // Grouped expressions
           ;

// Conditional statement (if/elif/else blocks)
conditional : 'if' expression ':' (statement)*          // if block
            ( 'elif' expression ':' (statement)* )*     // elif blocks
            ( 'else' ':' (statement)* )?                // optional else block
            ;

// Array/list definition
array : '[' (expression (',' expression)*)? ']' ;

// Tokens for operators and other symbols
ARITH_OP : '+' | '-' | '*' | '/' | '%' ;
ASSIGN_OP : '=' | '+=' | '-=' | '*=' | '/=' ;
COMP_OP : '<' | '<=' | '>' | '>=' | '==' | '!=' ;       // Comparison operators
BOOL_OP : 'and' | 'or' ;                                // Boolean operators
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]* ;                   // Identifier rule (e.g., variable names)
NUMBER : [0-9]+ ('.' [0-9]+)? ;                         // Integer and float numbers
STRING : '"' .*? '"' ;                                  // String literal with double quotes
BOOLEAN : 'True' | 'False' ;                            // Boolean values
WS : [ \t\r\n]+ -> skip ;                               // Skip whitespace
