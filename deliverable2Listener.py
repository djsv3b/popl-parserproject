# Generated from deliverable2.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .deliverable2Parser import deliverable2Parser
else:
    from deliverable2Parser import deliverable2Parser

# This class defines a complete listener for a parse tree produced by deliverable2Parser.
class deliverable2Listener(ParseTreeListener):

    # Enter a parse tree produced by deliverable2Parser#program.
    def enterProgram(self, ctx:deliverable2Parser.ProgramContext):
        pass

    # Exit a parse tree produced by deliverable2Parser#program.
    def exitProgram(self, ctx:deliverable2Parser.ProgramContext):
        pass


    # Enter a parse tree produced by deliverable2Parser#statement.
    def enterStatement(self, ctx:deliverable2Parser.StatementContext):
        pass

    # Exit a parse tree produced by deliverable2Parser#statement.
    def exitStatement(self, ctx:deliverable2Parser.StatementContext):
        pass


    # Enter a parse tree produced by deliverable2Parser#assignment.
    def enterAssignment(self, ctx:deliverable2Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by deliverable2Parser#assignment.
    def exitAssignment(self, ctx:deliverable2Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by deliverable2Parser#expression.
    def enterExpression(self, ctx:deliverable2Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by deliverable2Parser#expression.
    def exitExpression(self, ctx:deliverable2Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by deliverable2Parser#conditional.
    def enterConditional(self, ctx:deliverable2Parser.ConditionalContext):
        pass

    # Exit a parse tree produced by deliverable2Parser#conditional.
    def exitConditional(self, ctx:deliverable2Parser.ConditionalContext):
        pass


    # Enter a parse tree produced by deliverable2Parser#array.
    def enterArray(self, ctx:deliverable2Parser.ArrayContext):
        pass

    # Exit a parse tree produced by deliverable2Parser#array.
    def exitArray(self, ctx:deliverable2Parser.ArrayContext):
        pass



del deliverable2Parser