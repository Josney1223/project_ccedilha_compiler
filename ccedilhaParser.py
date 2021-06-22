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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\6\3\26\n\3\r\3\16\3\27\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\61\n\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\5\79\n\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7A\n")
        buf.write("\7\f\7\16\7D\13\7\3\7\2\3\f\b\2\4\6\b\n\f\2\4\3\2\34\35")
        buf.write("\3\2\32\33\2G\2\16\3\2\2\2\4\20\3\2\2\2\6\33\3\2\2\2\b")
        buf.write(" \3\2\2\2\n\60\3\2\2\2\f8\3\2\2\2\16\17\5\4\3\2\17\3\3")
        buf.write("\2\2\2\20\21\7\3\2\2\21\25\7\f\2\2\22\26\5\6\4\2\23\26")
        buf.write("\5\n\6\2\24\26\5\b\5\2\25\22\3\2\2\2\25\23\3\2\2\2\25")
        buf.write("\24\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2")
        buf.write("\30\31\3\2\2\2\31\32\7\r\2\2\32\5\3\2\2\2\33\34\5\f\7")
        buf.write("\2\34\35\7\20\2\2\35\36\5\f\7\2\36\37\7\6\2\2\37\7\3\2")
        buf.write("\2\2 !\7\13\2\2!\"\7\20\2\2\"#\5\f\7\2#$\7\6\2\2$\t\3")
        buf.write("\2\2\2%&\7\4\2\2&\'\7\16\2\2\'(\7\b\2\2()\7\17\2\2)\61")
        buf.write("\7\6\2\2*+\7\7\2\2+,\7\37\2\2,\61\7\6\2\2-.\7\7\2\2./")
        buf.write("\7 \2\2/\61\7\6\2\2\60%\3\2\2\2\60*\3\2\2\2\60-\3\2\2")
        buf.write("\2\61\13\3\2\2\2\62\63\b\7\1\2\639\7\7\2\2\64\65\7\16")
        buf.write("\2\2\65\66\5\f\7\2\66\67\7\17\2\2\679\3\2\2\28\62\3\2")
        buf.write("\2\28\64\3\2\2\29B\3\2\2\2:;\f\6\2\2;<\t\2\2\2<A\5\f\7")
        buf.write("\7=>\f\5\2\2>?\t\3\2\2?A\5\f\7\6@:\3\2\2\2@=\3\2\2\2A")
        buf.write("D\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\r\3\2\2\2DB\3\2\2\2\b\25")
        buf.write("\27\608@B")
        return buf.getvalue()


class ccedilhaParser ( Parser ):

    grammarFileName = "ccedilha.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'nada principal()'", "'amostrar'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'{'", "'}'", "'('", "')'", 
                     "' igual '", "'se'", "'senao'", "'enquanto'", "' e '", 
                     "' ou '", "' maiorIgual '", "' menorIgual '", "' maior '", 
                     "' menor '", "' mais '", "' menos '", "' vezes '", 
                     "' divide '", "' resto '", "' maisMais'", "' menosMenos'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WS", "ENDLINE", 
                      "INT", "STRING", "FLOAT", "BOOL", "ID", "LKEY", "RKEY", 
                      "LPAREN", "RPAREN", "EQUAL", "IF", "ELSE", "WHILE", 
                      "AND", "OR", "GREATER_EQUAL", "LESSER_EQUAL", "GREATER", 
                      "LESSER", "PLUS", "MINUS", "MULT", "DIV", "REST", 
                      "PLUS_PLUS", "MINUS_MINUS" ]

    RULE_prog = 0
    RULE_main = 1
    RULE_stat = 2
    RULE_att = 3
    RULE_func = 4
    RULE_expr = 5

    ruleNames =  [ "prog", "main", "stat", "att", "func", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WS=3
    ENDLINE=4
    INT=5
    STRING=6
    FLOAT=7
    BOOL=8
    ID=9
    LKEY=10
    RKEY=11
    LPAREN=12
    RPAREN=13
    EQUAL=14
    IF=15
    ELSE=16
    WHILE=17
    AND=18
    OR=19
    GREATER_EQUAL=20
    LESSER_EQUAL=21
    GREATER=22
    LESSER=23
    PLUS=24
    MINUS=25
    MULT=26
    DIV=27
    REST=28
    PLUS_PLUS=29
    MINUS_MINUS=30

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
            self.state = 12
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

        def LKEY(self):
            return self.getToken(ccedilhaParser.LKEY, 0)

        def RKEY(self):
            return self.getToken(ccedilhaParser.RKEY, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ccedilhaParser.StatContext)
            else:
                return self.getTypedRuleContext(ccedilhaParser.StatContext,i)


        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ccedilhaParser.FuncContext)
            else:
                return self.getTypedRuleContext(ccedilhaParser.FuncContext,i)


        def att(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ccedilhaParser.AttContext)
            else:
                return self.getTypedRuleContext(ccedilhaParser.AttContext,i)


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
            self.state = 14
            self.match(ccedilhaParser.T__0)
            self.state = 15
            self.match(ccedilhaParser.LKEY)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 19
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 16
                    self.stat()
                    pass

                elif la_ == 2:
                    self.state = 17
                    self.func()
                    pass

                elif la_ == 3:
                    self.state = 18
                    self.att()
                    pass


                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ccedilhaParser.T__1) | (1 << ccedilhaParser.INT) | (1 << ccedilhaParser.ID) | (1 << ccedilhaParser.LPAREN))) != 0)):
                    break

            self.state = 23
            self.match(ccedilhaParser.RKEY)
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


        def EQUAL(self):
            return self.getToken(ccedilhaParser.EQUAL, 0)

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
            self.state = 25
            self.expr(0)
            self.state = 26
            self.match(ccedilhaParser.EQUAL)
            self.state = 27
            self.expr(0)
            self.state = 28
            self.match(ccedilhaParser.ENDLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ccedilhaParser.ID, 0)

        def EQUAL(self):
            return self.getToken(ccedilhaParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(ccedilhaParser.ExprContext,0)


        def ENDLINE(self):
            return self.getToken(ccedilhaParser.ENDLINE, 0)

        def getRuleIndex(self):
            return ccedilhaParser.RULE_att

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtt" ):
                listener.enterAtt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtt" ):
                listener.exitAtt(self)




    def att(self):

        localctx = ccedilhaParser.AttContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_att)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(ccedilhaParser.ID)
            self.state = 31
            self.match(ccedilhaParser.EQUAL)
            self.state = 32
            self.expr(0)
            self.state = 33
            self.match(ccedilhaParser.ENDLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ccedilhaParser.LPAREN, 0)

        def STRING(self):
            return self.getToken(ccedilhaParser.STRING, 0)

        def RPAREN(self):
            return self.getToken(ccedilhaParser.RPAREN, 0)

        def ENDLINE(self):
            return self.getToken(ccedilhaParser.ENDLINE, 0)

        def INT(self):
            return self.getToken(ccedilhaParser.INT, 0)

        def PLUS_PLUS(self):
            return self.getToken(ccedilhaParser.PLUS_PLUS, 0)

        def MINUS_MINUS(self):
            return self.getToken(ccedilhaParser.MINUS_MINUS, 0)

        def getRuleIndex(self):
            return ccedilhaParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = ccedilhaParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(ccedilhaParser.T__1)
                self.state = 36
                self.match(ccedilhaParser.LPAREN)
                self.state = 37
                self.match(ccedilhaParser.STRING)
                self.state = 38
                self.match(ccedilhaParser.RPAREN)
                self.state = 39
                self.match(ccedilhaParser.ENDLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(ccedilhaParser.INT)
                self.state = 41
                self.match(ccedilhaParser.PLUS_PLUS)
                self.state = 42
                self.match(ccedilhaParser.ENDLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(ccedilhaParser.INT)
                self.state = 44
                self.match(ccedilhaParser.MINUS_MINUS)
                self.state = 45
                self.match(ccedilhaParser.ENDLINE)
                pass


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

        def LPAREN(self):
            return self.getToken(ccedilhaParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ccedilhaParser.ExprContext)
            else:
                return self.getTypedRuleContext(ccedilhaParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(ccedilhaParser.RPAREN, 0)

        def MULT(self):
            return self.getToken(ccedilhaParser.MULT, 0)

        def DIV(self):
            return self.getToken(ccedilhaParser.DIV, 0)

        def PLUS(self):
            return self.getToken(ccedilhaParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ccedilhaParser.MINUS, 0)

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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ccedilhaParser.INT]:
                self.state = 49
                self.match(ccedilhaParser.INT)
                pass
            elif token in [ccedilhaParser.LPAREN]:
                self.state = 50
                self.match(ccedilhaParser.LPAREN)
                self.state = 51
                self.expr(0)
                self.state = 52
                self.match(ccedilhaParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 62
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = ccedilhaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 57
                        _la = self._input.LA(1)
                        if not(_la==ccedilhaParser.MULT or _la==ccedilhaParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 58
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ccedilhaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 60
                        _la = self._input.LA(1)
                        if not(_la==ccedilhaParser.PLUS or _la==ccedilhaParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 61
                        self.expr(4)
                        pass

             
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self._predicates[5] = self.expr_sempred
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
         




