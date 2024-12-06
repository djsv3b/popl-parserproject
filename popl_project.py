from antlr4 import *
from popl_projectLexer import popl_projectLexer
from popl_projectParser import popl_projectParser

input_code = """
#YOUR CODE HERE
"""

lexer = popl_projectLexer(InputStream(input_code))
token_stream = CommonTokenStream(lexer)

# Parser
parser = popl_projectParser(token_stream)

# Parse starting from the 'program' rule
tree = parser.program()

# Output the parse tree
print("Parse Tree:")
print(tree.toStringTree(recog=parser))