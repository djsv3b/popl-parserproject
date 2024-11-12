# Generated from deliverable2.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,104,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,42,8,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,53,8,3,10,3,12,3,56,9,
        3,1,4,1,4,1,4,1,4,5,4,62,8,4,10,4,12,4,65,9,4,1,4,1,4,1,4,1,4,5,
        4,71,8,4,10,4,12,4,74,9,4,5,4,76,8,4,10,4,12,4,79,9,4,1,4,1,4,1,
        4,5,4,84,8,4,10,4,12,4,87,9,4,3,4,89,8,4,1,5,1,5,1,5,1,5,5,5,95,
        8,5,10,5,12,5,98,9,5,3,5,100,8,5,1,5,1,5,1,5,0,1,6,6,0,2,4,6,8,10,
        0,0,116,0,15,1,0,0,0,2,23,1,0,0,0,4,25,1,0,0,0,6,41,1,0,0,0,8,57,
        1,0,0,0,10,90,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,
        15,13,1,0,0,0,15,16,1,0,0,0,16,18,1,0,0,0,17,15,1,0,0,0,18,19,5,
        0,0,1,19,1,1,0,0,0,20,24,3,4,2,0,21,24,3,6,3,0,22,24,3,8,4,0,23,
        20,1,0,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,5,15,0,
        0,26,27,5,12,0,0,27,28,3,6,3,0,28,5,1,0,0,0,29,30,6,3,-1,0,30,31,
        5,1,0,0,31,42,3,6,3,7,32,42,5,15,0,0,33,42,5,16,0,0,34,42,5,17,0,
        0,35,42,5,18,0,0,36,42,3,10,5,0,37,38,5,2,0,0,38,39,3,6,3,0,39,40,
        5,3,0,0,40,42,1,0,0,0,41,29,1,0,0,0,41,32,1,0,0,0,41,33,1,0,0,0,
        41,34,1,0,0,0,41,35,1,0,0,0,41,36,1,0,0,0,41,37,1,0,0,0,42,54,1,
        0,0,0,43,44,10,10,0,0,44,45,5,11,0,0,45,53,3,6,3,11,46,47,10,9,0,
        0,47,48,5,13,0,0,48,53,3,6,3,10,49,50,10,8,0,0,50,51,5,14,0,0,51,
        53,3,6,3,9,52,43,1,0,0,0,52,46,1,0,0,0,52,49,1,0,0,0,53,56,1,0,0,
        0,54,52,1,0,0,0,54,55,1,0,0,0,55,7,1,0,0,0,56,54,1,0,0,0,57,58,5,
        4,0,0,58,59,3,6,3,0,59,63,5,5,0,0,60,62,3,2,1,0,61,60,1,0,0,0,62,
        65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,77,1,0,0,0,65,63,1,0,0,
        0,66,67,5,6,0,0,67,68,3,6,3,0,68,72,5,5,0,0,69,71,3,2,1,0,70,69,
        1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,76,1,0,0,0,
        74,72,1,0,0,0,75,66,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,
        0,0,0,78,88,1,0,0,0,79,77,1,0,0,0,80,81,5,7,0,0,81,85,5,5,0,0,82,
        84,3,2,1,0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,
        0,86,89,1,0,0,0,87,85,1,0,0,0,88,80,1,0,0,0,88,89,1,0,0,0,89,9,1,
        0,0,0,90,99,5,8,0,0,91,96,3,6,3,0,92,93,5,9,0,0,93,95,3,6,3,0,94,
        92,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,100,1,0,
        0,0,98,96,1,0,0,0,99,91,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,0,101,
        102,5,10,0,0,102,11,1,0,0,0,12,15,23,41,52,54,63,72,77,85,88,96,
        99
    ]

class deliverable2Parser ( Parser ):

    grammarFileName = "deliverable2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'not'", "'('", "')'", "'if'", "':'", 
                     "'elif'", "'else'", "'['", "','", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ARITH_OP", 
                      "ASSIGN_OP", "COMP_OP", "BOOL_OP", "IDENTIFIER", "NUMBER", 
                      "STRING", "BOOLEAN", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_conditional = 4
    RULE_array = 5

    ruleNames =  [ "program", "statement", "assignment", "expression", "conditional", 
                   "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    ARITH_OP=11
    ASSIGN_OP=12
    COMP_OP=13
    BOOL_OP=14
    IDENTIFIER=15
    NUMBER=16
    STRING=17
    BOOLEAN=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(deliverable2Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliverable2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(deliverable2Parser.StatementContext,i)


        def getRuleIndex(self):
            return deliverable2Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = deliverable2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 491798) != 0):
                self.state = 12
                self.statement()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(deliverable2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(deliverable2Parser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(deliverable2Parser.ExpressionContext,0)


        def conditional(self):
            return self.getTypedRuleContext(deliverable2Parser.ConditionalContext,0)


        def getRuleIndex(self):
            return deliverable2Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = deliverable2Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.conditional()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(deliverable2Parser.IDENTIFIER, 0)

        def ASSIGN_OP(self):
            return self.getToken(deliverable2Parser.ASSIGN_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(deliverable2Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return deliverable2Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = deliverable2Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(deliverable2Parser.IDENTIFIER)
            self.state = 26
            self.match(deliverable2Parser.ASSIGN_OP)
            self.state = 27
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliverable2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(deliverable2Parser.ExpressionContext,i)


        def IDENTIFIER(self):
            return self.getToken(deliverable2Parser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(deliverable2Parser.NUMBER, 0)

        def STRING(self):
            return self.getToken(deliverable2Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(deliverable2Parser.BOOLEAN, 0)

        def array(self):
            return self.getTypedRuleContext(deliverable2Parser.ArrayContext,0)


        def ARITH_OP(self):
            return self.getToken(deliverable2Parser.ARITH_OP, 0)

        def COMP_OP(self):
            return self.getToken(deliverable2Parser.COMP_OP, 0)

        def BOOL_OP(self):
            return self.getToken(deliverable2Parser.BOOL_OP, 0)

        def getRuleIndex(self):
            return deliverable2Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = deliverable2Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 30
                self.match(deliverable2Parser.T__0)
                self.state = 31
                self.expression(7)
                pass
            elif token in [15]:
                self.state = 32
                self.match(deliverable2Parser.IDENTIFIER)
                pass
            elif token in [16]:
                self.state = 33
                self.match(deliverable2Parser.NUMBER)
                pass
            elif token in [17]:
                self.state = 34
                self.match(deliverable2Parser.STRING)
                pass
            elif token in [18]:
                self.state = 35
                self.match(deliverable2Parser.BOOLEAN)
                pass
            elif token in [8]:
                self.state = 36
                self.array()
                pass
            elif token in [2]:
                self.state = 37
                self.match(deliverable2Parser.T__1)
                self.state = 38
                self.expression(0)
                self.state = 39
                self.match(deliverable2Parser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 52
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = deliverable2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 43
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 44
                        self.match(deliverable2Parser.ARITH_OP)
                        self.state = 45
                        self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = deliverable2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 46
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 47
                        self.match(deliverable2Parser.COMP_OP)
                        self.state = 48
                        self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = deliverable2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 49
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 50
                        self.match(deliverable2Parser.BOOL_OP)
                        self.state = 51
                        self.expression(9)
                        pass

             
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliverable2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(deliverable2Parser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliverable2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(deliverable2Parser.StatementContext,i)


        def getRuleIndex(self):
            return deliverable2Parser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = deliverable2Parser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(deliverable2Parser.T__3)
            self.state = 58
            self.expression(0)
            self.state = 59
            self.match(deliverable2Parser.T__4)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 60
                    self.statement() 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 66
                    self.match(deliverable2Parser.T__5)
                    self.state = 67
                    self.expression(0)
                    self.state = 68
                    self.match(deliverable2Parser.T__4)
                    self.state = 72
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 69
                            self.statement() 
                        self.state = 74
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
             
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 80
                self.match(deliverable2Parser.T__6)
                self.state = 81
                self.match(deliverable2Parser.T__4)
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 82
                        self.statement() 
                    self.state = 87
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliverable2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(deliverable2Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return deliverable2Parser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = deliverable2Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(deliverable2Parser.T__7)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 491782) != 0):
                self.state = 91
                self.expression(0)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 92
                    self.match(deliverable2Parser.T__8)
                    self.state = 93
                    self.expression(0)
                    self.state = 98
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 101
            self.match(deliverable2Parser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         




