# Generated from ccedilha.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3\3\3\3")
        buf.write("\6\3\20\n\3\r\3\16\3\21\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\5!\n\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\7\5)\n\5\f\5\16\5,\13\5\3\5\2\3\b\6\2\4\6\b\2\4\3\2")
        buf.write("\5\6\3\2\7\b\2-\2\n\3\2\2\2\4\f\3\2\2\2\6\25\3\2\2\2\b")
        buf.write(" \3\2\2\2\n\13\5\4\3\2\13\3\3\2\2\2\f\r\7\3\2\2\r\17\7")
        buf.write("\22\2\2\16\20\5\6\4\2\17\16\3\2\2\2\20\21\3\2\2\2\21\17")
        buf.write("\3\2\2\2\21\22\3\2\2\2\22\23\3\2\2\2\23\24\7\23\2\2\24")
        buf.write("\5\3\2\2\2\25\26\5\b\5\2\26\27\7\4\2\2\27\30\5\b\5\2\30")
        buf.write("\31\7\f\2\2\31\7\3\2\2\2\32\33\b\5\1\2\33!\7\r\2\2\34")
        buf.write("\35\7\t\2\2\35\36\5\b\5\2\36\37\7\n\2\2\37!\3\2\2\2 \32")
        buf.write("\3\2\2\2 \34\3\2\2\2!*\3\2\2\2\"#\f\6\2\2#$\t\2\2\2$)")
        buf.write("\5\b\5\7%&\f\5\2\2&\'\t\3\2\2\')\5\b\5\6(\"\3\2\2\2(%")
        buf.write("\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\t\3\2\2\2,*\3")
        buf.write("\2\2\2\6\21 (*")
        return buf.getvalue()


class ccedilhaParser ( Parser ):

    grammarFileName = "ccedilha.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'nada principal()'", "' igual '", "' vezes '", 
                     "' divide '", "' mais '", "' menos '", "'('", "')'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "ENDLINE", "INT", "STRING", "FLOAT", 
                      "BOOL", "ID", "CHAVE_ABRE", "CHAVE_FECHA" ]

    RULE_prog = 0
    RULE_main = 1
    RULE_stat = 2
    RULE_expr = 3

    ruleNames =  [ "prog", "main", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    WS=9
    ENDLINE=10
    INT=11
    STRING=12
    FLOAT=13
    BOOL=14
    ID=15
    CHAVE_ABRE=16
    CHAVE_FECHA=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(ccedilhaParser.MainContext,0)


        def getRuleIndex(self):
            return ccedilhaParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ccedilhaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAVE_ABRE(self):
            return self.getToken(ccedilhaParser.CHAVE_ABRE, 0)

        def CHAVE_FECHA(self):
            return self.getToken(ccedilhaParser.CHAVE_FECHA, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ccedilhaParser.StatContext)
            else:
                return self.getTypedRuleContext(ccedilhaParser.StatContext,i)


        def getRuleIndex(self):
            return ccedilhaParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = ccedilhaParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(ccedilhaParser.T__0)
            self.state = 11
            self.match(ccedilhaParser.CHAVE_ABRE)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.stat()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ccedilhaParser.T__6 or _la==ccedilhaParser.INT):
                    break

            self.state = 17
            self.match(ccedilhaParser.CHAVE_FECHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ccedilhaParser.ExprContext)
            else:
                return self.getTypedRuleContext(ccedilhaParser.ExprContext,i)


        def ENDLINE(self):
            return self.getToken(ccedilhaParser.ENDLINE, 0)

        def getRuleIndex(self):
            return ccedilhaParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = ccedilhaParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.expr(0)
            self.state = 20
            self.match(ccedilhaParser.T__1)
            self.state = 21
            self.expr(0)
            self.state = 22
            self.match(ccedilhaParser.ENDLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ccedilhaParser.INT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ccedilhaParser.ExprContext)
            else:
                return self.getTypedRuleContext(ccedilhaParser.ExprContext,i)


        def getRuleIndex(self):
            return ccedilhaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ccedilhaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ccedilhaParser.INT]:
                self.state = 25
                self.match(ccedilhaParser.INT)
                pass
            elif token in [ccedilhaParser.T__6]:
                self.state = 26
                self.match(ccedilhaParser.T__6)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(ccedilhaParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ccedilhaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 33
                        _la = self._input.LA(1)
                        if not(_la==ccedilhaParser.T__2 or _la==ccedilhaParser.T__3):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 34
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ccedilhaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 36
                        _la = self._input.LA(1)
                        if not(_la==ccedilhaParser.T__4 or _la==ccedilhaParser.T__5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        self.expr(4)
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




