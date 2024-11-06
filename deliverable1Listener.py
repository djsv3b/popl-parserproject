# Generated from deliverable1.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .deliverable1Parser import deliverable1Parser
else:
    from deliverable1Parser import deliverable1Parser

# This class defines a complete listener for a parse tree produced by deliverable1Parser.
class deliverable1Listener(ParseTreeListener):

    # Enter a parse tree produced by deliverable1Parser#program.
    def enterProgram(self, ctx:deliverable1Parser.ProgramContext):
        pass

    # Exit a parse tree produced by deliverable1Parser#program.
    def exitProgram(self, ctx:deliverable1Parser.ProgramContext):
        pass


    # Enter a parse tree produced by deliverable1Parser#statement.
    def enterStatement(self, ctx:deliverable1Parser.StatementContext):
        pass

    # Exit a parse tree produced by deliverable1Parser#statement.
    def exitStatement(self, ctx:deliverable1Parser.StatementContext):
        pass


    # Enter a parse tree produced by deliverable1Parser#assignment.
    def enterAssignment(self, ctx:deliverable1Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by deliverable1Parser#assignment.
    def exitAssignment(self, ctx:deliverable1Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by deliverable1Parser#expression.
    def enterExpression(self, ctx:deliverable1Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by deliverable1Parser#expression.
    def exitExpression(self, ctx:deliverable1Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by deliverable1Parser#array.
    def enterArray(self, ctx:deliverable1Parser.ArrayContext):
        pass

    # Exit a parse tree produced by deliverable1Parser#array.
    def exitArray(self, ctx:deliverable1Parser.ArrayContext):
        pass



del deliverable1Parser