import sys
from antlr4 import *
from deliverable2Lexer import deliverable2Lexer
from deliverable2Parser import deliverable2Parser

input_code = """
assign1 = "20"
assign2 = 123
assign3 = 1.23
assign4 = assign1

arith_op1 = 1 + 2
arith_op2 = 13 - 3
arith_op3 = 10 / arith_op1
arith_op4 = 4.2 * 10
arith_op5 = arith_op1 % arith_op2

arith_op1 += arith_op2
arith_op2 -= arith_op3
arith_op3 *= arith_op4
arith_op4 /= arith_op5

array1 = [1, 2, 3, 4, 5]
array2 = ['a', 'b', 'c']
array3 = [1.6, 2.7, 3.8, 4.9, 5.0]

var1 = 10
var2 = var1/2 + 5
var3 = var2 % 2
var4 = 1

flag = True

assign1 = ""

if var1 > var2:
	arith_op1 = 1 + 2
	assign1 = "text data"

if var1 <= var2 and var3 == var4:
	arith_op1 = 1 + 2
	assign1 = "text data"
else:
	arith_op4 = 4.2 * 10
	arith_op3 *= arith_op4
	
data = 0

if var1 != var2 or var3 >= var4:
	flag = True
elif (not flag) and var3 > 10:
	flag = False
else:
	data = -1
"""

lexer = deliverable2Lexer(InputStream(input_code))
token_stream = CommonTokenStream(lexer)

# Parser
parser = deliverable2Parser(token_stream)

# Parse starting from the 'program' rule
tree = parser.program()

# Output the parse tree
print("Parse Tree:")
print(tree.toStringTree(recog=parser))