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
        buf.write("?\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\6\3\23\n\3\r\3\16\3\24\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5)\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\62\n\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\7\6:\n\6\f\6\16\6=\13\6\3\6\2\3\n\7")
        buf.write("\2\4\6\b\n\2\5\4\2\7\b\13\13\3\2\34\35\3\2\32\33\2A\2")
        buf.write("\f\3\2\2\2\4\16\3\2\2\2\6\30\3\2\2\2\b(\3\2\2\2\n\61\3")
        buf.write("\2\2\2\f\r\5\4\3\2\r\3\3\2\2\2\16\17\7\3\2\2\17\22\7\f")
        buf.write("\2\2\20\23\5\b\5\2\21\23\5\6\4\2\22\20\3\2\2\2\22\21\3")
        buf.write("\2\2\2\23\24\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25\26")
        buf.write("\3\2\2\2\26\27\7\r\2\2\27\5\3\2\2\2\30\31\7\13\2\2\31")
        buf.write("\32\7\20\2\2\32\33\5\n\6\2\33\34\7\6\2\2\34\7\3\2\2\2")
        buf.write("\35\36\7\4\2\2\36\37\7\16\2\2\37 \t\2\2\2 !\7\17\2\2!")
        buf.write(")\7\6\2\2\"#\7\13\2\2#$\7\37\2\2$)\7\6\2\2%&\7\13\2\2")
        buf.write("&\'\7 \2\2\')\7\6\2\2(\35\3\2\2\2(\"\3\2\2\2(%\3\2\2\2")
        buf.write(")\t\3\2\2\2*+\b\6\1\2+\62\7\7\2\2,\62\7\13\2\2-.\7\16")
        buf.write("\2\2./\5\n\6\2/\60\7\17\2\2\60\62\3\2\2\2\61*\3\2\2\2")
        buf.write("\61,\3\2\2\2\61-\3\2\2\2\62;\3\2\2\2\63\64\f\7\2\2\64")
        buf.write("\65\t\3\2\2\65:\5\n\6\b\66\67\f\6\2\2\678\t\4\2\28:\5")
        buf.write("\n\6\79\63\3\2\2\29\66\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3")
        buf.write("\2\2\2<\13\3\2\2\2=;\3\2\2\2\b\22\24(\619;")
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
    RULE_att = 2
    RULE_func = 3
    RULE_expr = 4

    ruleNames =  [ "prog", "main", "att", "func", "expr" ]

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ccedilhaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = ccedilhaParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(ccedilhaParser.T__0)
            self.state = 13
            self.match(ccedilhaParser.LKEY)
            self.state = 16 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 14
                    self.func()
                    pass

                elif la_ == 2:
                    self.state = 15
                    self.att()
                    pass


                self.state = 18 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ccedilhaParser.T__1 or _la==ccedilhaParser.ID):
                    break

            self.state = 20
            self.match(ccedilhaParser.RKEY)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt" ):
                return visitor.visitAtt(self)
            else:
                return visitor.visitChildren(self)




    def att(self):

        localctx = ccedilhaParser.AttContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_att)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(ccedilhaParser.ID)
            self.state = 23
            self.match(ccedilhaParser.EQUAL)
            self.state = 24
            self.expr(0)
            self.state = 25
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


        def getRuleIndex(self):
            return ccedilhaParser.RULE_func

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FuncMinusMinusContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ccedilhaParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ccedilhaParser.ID, 0)
        def MINUS_MINUS(self):
            return self.getToken(ccedilhaParser.MINUS_MINUS, 0)
        def ENDLINE(self):
            return self.getToken(ccedilhaParser.ENDLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncMinusMinus" ):
                listener.enterFuncMinusMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncMinusMinus" ):
                listener.exitFuncMinusMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncMinusMinus" ):
                return visitor.visitFuncMinusMinus(self)
            else:
                return visitor.visitChildren(self)


    class FuncPlusPlusContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ccedilhaParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ccedilhaParser.ID, 0)
        def PLUS_PLUS(self):
            return self.getToken(ccedilhaParser.PLUS_PLUS, 0)
        def ENDLINE(self):
            return self.getToken(ccedilhaParser.ENDLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncPlusPlus" ):
                listener.enterFuncPlusPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncPlusPlus" ):
                listener.exitFuncPlusPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncPlusPlus" ):
                return visitor.visitFuncPlusPlus(self)
            else:
                return visitor.visitChildren(self)


    class FuncPrintContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ccedilhaParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ccedilhaParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(ccedilhaParser.RPAREN, 0)
        def ENDLINE(self):
            return self.getToken(ccedilhaParser.ENDLINE, 0)
        def STRING(self):
            return self.getToken(ccedilhaParser.STRING, 0)
        def INT(self):
            return self.getToken(ccedilhaParser.INT, 0)
        def ID(self):
            return self.getToken(ccedilhaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncPrint" ):
                listener.enterFuncPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncPrint" ):
                listener.exitFuncPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncPrint" ):
                return visitor.visitFuncPrint(self)
            else:
                return visitor.visitChildren(self)



    def func(self):

        localctx = ccedilhaParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ccedilhaParser.FuncPrintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(ccedilhaParser.T__1)
                self.state = 28
                self.match(ccedilhaParser.LPAREN)
                self.state = 29
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ccedilhaParser.INT) | (1 << ccedilhaParser.STRING) | (1 << ccedilhaParser.ID))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 30
                self.match(ccedilhaParser.RPAREN)
                self.state = 31
                self.match(ccedilhaParser.ENDLINE)
                pass

            elif la_ == 2:
                localctx = ccedilhaParser.FuncPlusPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(ccedilhaParser.ID)
                self.state = 33
                self.match(ccedilhaParser.PLUS_PLUS)
                self.state = 34
                self.match(ccedilhaParser.ENDLINE)
                pass

            elif la_ == 3:
                localctx = ccedilhaParser.FuncMinusMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(ccedilhaParser.ID)
                self.state = 36
                self.match(ccedilhaParser.MINUS_MINUS)
                self.state = 37
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


        def getRuleIndex(self):
            return ccedilhaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprMultDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ccedilhaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ccedilhaParser.ExprContext)
            else:
                return self.getTypedRuleContext(ccedilhaParser.ExprContext,i)

        def MULT(self):
            return self.getToken(ccedilhaParser.MULT, 0)
        def DIV(self):
            return self.getToken(ccedilhaParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMultDiv" ):
                listener.enterExprMultDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMultDiv" ):
                listener.exitExprMultDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMultDiv" ):
                return visitor.visitExprMultDiv(self)
            else:
                return visitor.visitChildren(self)


    class ExprParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ccedilhaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ccedilhaParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(ccedilhaParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(ccedilhaParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprParen" ):
                listener.enterExprParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprParen" ):
                listener.exitExprParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParen" ):
                return visitor.visitExprParen(self)
            else:
                return visitor.visitChildren(self)


    class ExprPlusMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ccedilhaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ccedilhaParser.ExprContext)
            else:
                return self.getTypedRuleContext(ccedilhaParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(ccedilhaParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(ccedilhaParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPlusMinus" ):
                listener.enterExprPlusMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPlusMinus" ):
                listener.exitExprPlusMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPlusMinus" ):
                return visitor.visitExprPlusMinus(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ccedilhaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ccedilhaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ccedilhaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ccedilhaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ccedilhaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ccedilhaParser.INT]:
                localctx = ccedilhaParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 41
                self.match(ccedilhaParser.INT)
                pass
            elif token in [ccedilhaParser.ID]:
                localctx = ccedilhaParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(ccedilhaParser.ID)
                pass
            elif token in [ccedilhaParser.LPAREN]:
                localctx = ccedilhaParser.ExprParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(ccedilhaParser.LPAREN)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(ccedilhaParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 55
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = ccedilhaParser.ExprMultDivContext(self, ccedilhaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 50
                        _la = self._input.LA(1)
                        if not(_la==ccedilhaParser.MULT or _la==ccedilhaParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ccedilhaParser.ExprPlusMinusContext(self, ccedilhaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 53
                        _la = self._input.LA(1)
                        if not(_la==ccedilhaParser.PLUS or _la==ccedilhaParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.expr(5)
                        pass

             
                self.state = 59
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
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




