# Generated from deliverable1.g4 by ANTLR 4.13.2
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
        4,1,10,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,3,3,33,8,3,1,3,1,3,1,3,5,3,38,8,3,10,3,12,3,
        41,9,3,1,4,1,4,1,4,1,4,5,4,47,8,4,10,4,12,4,50,9,4,3,4,52,8,4,1,
        4,1,4,1,4,0,1,6,5,0,2,4,6,8,0,0,59,0,13,1,0,0,0,2,20,1,0,0,0,4,22,
        1,0,0,0,6,32,1,0,0,0,8,42,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,
        15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,
        0,16,17,5,0,0,1,17,1,1,0,0,0,18,21,3,4,2,0,19,21,3,6,3,0,20,18,1,
        0,0,0,20,19,1,0,0,0,21,3,1,0,0,0,22,23,5,6,0,0,23,24,5,5,0,0,24,
        25,3,6,3,0,25,5,1,0,0,0,26,27,6,3,-1,0,27,33,5,6,0,0,28,33,5,7,0,
        0,29,33,5,8,0,0,30,33,5,9,0,0,31,33,3,8,4,0,32,26,1,0,0,0,32,28,
        1,0,0,0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,39,1,0,0,0,
        34,35,10,6,0,0,35,36,5,4,0,0,36,38,3,6,3,7,37,34,1,0,0,0,38,41,1,
        0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,7,1,0,0,0,41,39,1,0,0,0,42,
        51,5,1,0,0,43,48,3,6,3,0,44,45,5,2,0,0,45,47,3,6,3,0,46,44,1,0,0,
        0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,52,1,0,0,0,50,48,
        1,0,0,0,51,43,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,5,3,0,0,
        54,9,1,0,0,0,6,13,20,32,39,48,51
    ]

class deliverable1Parser ( Parser ):

    grammarFileName = "deliverable1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "','", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ARITH_OP", "ASSIGN_OP", "IDENTIFIER", "NUMBER", "STRING", 
                      "BOOLEAN", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_array = 4

    ruleNames =  [ "program", "statement", "assignment", "expression", "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ARITH_OP=4
    ASSIGN_OP=5
    IDENTIFIER=6
    NUMBER=7
    STRING=8
    BOOLEAN=9
    WS=10

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
            return self.getToken(deliverable1Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliverable1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(deliverable1Parser.StatementContext,i)


        def getRuleIndex(self):
            return deliverable1Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = deliverable1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 962) != 0):
                self.state = 10
                self.statement()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(deliverable1Parser.EOF)
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
            return self.getTypedRuleContext(deliverable1Parser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(deliverable1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return deliverable1Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = deliverable1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.expression(0)
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
            return self.getToken(deliverable1Parser.IDENTIFIER, 0)

        def ASSIGN_OP(self):
            return self.getToken(deliverable1Parser.ASSIGN_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(deliverable1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return deliverable1Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = deliverable1Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(deliverable1Parser.IDENTIFIER)
            self.state = 23
            self.match(deliverable1Parser.ASSIGN_OP)
            self.state = 24
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

        def IDENTIFIER(self):
            return self.getToken(deliverable1Parser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(deliverable1Parser.NUMBER, 0)

        def STRING(self):
            return self.getToken(deliverable1Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(deliverable1Parser.BOOLEAN, 0)

        def array(self):
            return self.getTypedRuleContext(deliverable1Parser.ArrayContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliverable1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(deliverable1Parser.ExpressionContext,i)


        def ARITH_OP(self):
            return self.getToken(deliverable1Parser.ARITH_OP, 0)

        def getRuleIndex(self):
            return deliverable1Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = deliverable1Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 27
                self.match(deliverable1Parser.IDENTIFIER)
                pass
            elif token in [7]:
                self.state = 28
                self.match(deliverable1Parser.NUMBER)
                pass
            elif token in [8]:
                self.state = 29
                self.match(deliverable1Parser.STRING)
                pass
            elif token in [9]:
                self.state = 30
                self.match(deliverable1Parser.BOOLEAN)
                pass
            elif token in [1]:
                self.state = 31
                self.array()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = deliverable1Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 34
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 35
                    self.match(deliverable1Parser.ARITH_OP)
                    self.state = 36
                    self.expression(7) 
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliverable1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(deliverable1Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return deliverable1Parser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = deliverable1Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(deliverable1Parser.T__0)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 962) != 0):
                self.state = 43
                self.expression(0)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 44
                    self.match(deliverable1Parser.T__1)
                    self.state = 45
                    self.expression(0)
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 53
            self.match(deliverable1Parser.T__2)
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
                return self.precpred(self._ctx, 6)
         




