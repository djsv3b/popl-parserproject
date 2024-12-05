// Define the grammar
grammar deliverable3;

// Entry point
program : (statement)* EOF ;

// Statements
statement : assignment                  // Variable assignments
          | expression                   // Expressions
          | conditional                  // if/elif/else statements
          | while_loop                  // while loop
          | comment                      //comment
          ;

// Assignment statement (assigning a variable to a value or an expression)
assignment : IDENTIFIER ASSIGN_OP expression ;

// Expressions, including arithmetic and boolean logic
expression : expression ARITH_OP expression             // Arithmetic operations
           | expression COMP_OP expression              // Comparison operations
           | expression BOOL_OP expression              // Boolean operations
           | 'not ' expression                           // 'not' operator
           | IDENTIFIER                                 // Variable reference
           | NUMBER                                     // Integer or float
           | STRING                                     // String literal
           | CHARACTER                                  // Character
           | BOOLEAN                                    // Boolean values (True/False)
           | array                                      // Array/list definition
           | '(' expression ')'                         // Grouped expressions
           ;

// Conditional statement (if/elif/else blocks)
conditional : 'if ' expression COLON (tab statement)*          // if block
            ( 'elif ' expression COLON (tab statement)* )*     // elif blocks
            ( 'else' COLON (tab statement)* )?                // optional else block
            ;

//While Loop
while_loop : 'while ' expression COLON (tab statement)* | 'while(' expression ')' COLON (tab statement)*;

//for loop
for_loop : 'for ' expression ' in ' expression COLON (tab statement)*;

// Array/list definition
array : '[' (expression (COMMA expression)*)? ']' ;

//comment
comment : INLINE_COMMENT | MULTI_COMMENT ;

INLINE_COMMENT : '#' ~[\r\n\f]* -> channel(HIDDEN);
MULTI_COMMENT : '\'\'\'' .*? '\'\'\'' -> channel(HIDDEN);

// Tokens for operators and other symbols
ARITH_OP : '+' | '-' | '*' | '/' | '%' | ' + ' | ' - ' | ' * ' | ' / ' | ' % ';
ASSIGN_OP : '=' | '+=' | '-=' | '*=' | '/=' | ' = ' | ' += ' | ' -= ' | ' *= ' | ' /= ' ;
COMP_OP : '<' | '<=' | '>' | '>=' | '==' | '!=' | ' < ' | ' <= ' | ' > ' | ' >= ' | ' == ' | ' != ' ;       // Comparison operators
BOOL_OP : 'and' | 'or' | ' and ' | ' or ' ;                                // Boolean operators
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]* ;                   // Identifier rule (e.g., variable names)
NUMBER : '-'? [0-9]+ ('.' [0-9]+)? ;                    // Integer and float numbers
STRING : '"' .*? '"' ;                                  // String literal with double quotes
CHARACTER : '\'' .? '\'' ;                              // Character
BOOLEAN : 'True' | 'False' ;
COLON : ':' | ' :'     ;
COMMA: ',' | ', ' ;                       // Boolean values
WS : [\r\n]+ -> skip ;                               // Skip whitespace

tab : '\t' 
    | '    '
    ;