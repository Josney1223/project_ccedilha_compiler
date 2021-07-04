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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3%")
        buf.write("Q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\6\3\32\n\3\r")
        buf.write("\3\16\3\33\3\3\3\3\3\4\3\4\5\4\"\n\4\3\4\3\4\3\4\5\4\'")
        buf.write("\n\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\5\7;\n\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\5\bD\n\b\3\b\3\b\3\b\3\b\3\b\3\b\7\bL\n\b\f\b\16")
        buf.write("\bO\13\b\3\b\2\3\16\t\2\4\6\b\n\f\16\2\6\3\2\6\n\4\2\35")
        buf.write("\36!!\3\2\27\30\3\2\25\26\2T\2\20\3\2\2\2\4\22\3\2\2\2")
        buf.write("\6!\3\2\2\2\b*\3\2\2\2\n-\3\2\2\2\f:\3\2\2\2\16C\3\2\2")
        buf.write("\2\20\21\5\4\3\2\21\3\3\2\2\2\22\23\7\3\2\2\23\31\7\"")
        buf.write("\2\2\24\32\5\f\7\2\25\32\5\6\4\2\26\27\5\b\5\2\27\30\7")
        buf.write("\34\2\2\30\32\3\2\2\2\31\24\3\2\2\2\31\25\3\2\2\2\31\26")
        buf.write("\3\2\2\2\32\33\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34")
        buf.write("\35\3\2\2\2\35\36\7#\2\2\36\5\3\2\2\2\37\"\5\b\5\2 \"")
        buf.write("\7!\2\2!\37\3\2\2\2! \3\2\2\2\"#\3\2\2\2#&\7\13\2\2$\'")
        buf.write("\5\16\b\2%\'\7\36\2\2&$\3\2\2\2&%\3\2\2\2\'(\3\2\2\2(")
        buf.write(")\7\34\2\2)\7\3\2\2\2*+\5\n\6\2+,\7!\2\2,\t\3\2\2\2-.")
        buf.write("\t\2\2\2.\13\3\2\2\2/\60\7\4\2\2\60\61\7$\2\2\61\62\t")
        buf.write("\3\2\2\62\63\7%\2\2\63;\7\34\2\2\64\65\7!\2\2\65\66\7")
        buf.write("\32\2\2\66;\7\34\2\2\678\7!\2\289\7\33\2\29;\7\34\2\2")
        buf.write(":/\3\2\2\2:\64\3\2\2\2:\67\3\2\2\2;\r\3\2\2\2<=\b\b\1")
        buf.write("\2=D\7\35\2\2>D\7!\2\2?@\7$\2\2@A\5\16\b\2AB\7%\2\2BD")
        buf.write("\3\2\2\2C<\3\2\2\2C>\3\2\2\2C?\3\2\2\2DM\3\2\2\2EF\f\7")
        buf.write("\2\2FG\t\4\2\2GL\5\16\b\bHI\f\6\2\2IJ\t\5\2\2JL\5\16\b")
        buf.write("\7KE\3\2\2\2KH\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2N")
        buf.write("\17\3\2\2\2OM\3\2\2\2\n\31\33!&:CKM")
        return buf.getvalue()


class ccedilhaParser ( Parser ):

    grammarFileName = "ccedilha.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'nada principal()'", "'amostrar'", "<INVALID>", 
                     "'inteiro '", "'sentenca '", "'flutuante '", "'talvez '", 
                     "'letra '", "' igual '", "'se'", "'senao'", "'enquanto'", 
                     "' e '", "' ou '", "' maiorIgual '", "' menorIgual '", 
                     "' maior '", "' menor '", "' mais '", "' menos '", 
                     "' vezes '", "' divide '", "' resto '", "' maisMais'", 
                     "' menosMenos'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'{'", "'}'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WS", "DEINT", 
                      "DESTRING", "DEFLOAT", "DEBOOL", "DECHAR", "EQUAL", 
                      "IF", "ELSE", "WHILE", "AND", "OR", "GREATER_EQUAL", 
                      "LESSER_EQUAL", "GREATER", "LESSER", "PLUS", "MINUS", 
                      "MULT", "DIV", "REST", "PLUS_PLUS", "MINUS_MINUS", 
                      "ENDLINE", "INT", "STRING", "FLOAT", "BOOL", "ID", 
                      "LKEY", "RKEY", "LPAREN", "RPAREN" ]

    RULE_prog = 0
    RULE_main = 1
    RULE_att = 2
    RULE_dec = 3
    RULE_basic_type = 4
    RULE_func = 5
    RULE_expr = 6

    ruleNames =  [ "prog", "main", "att", "dec", "basic_type", "func", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WS=3
    DEINT=4
    DESTRING=5
    DEFLOAT=6
    DEBOOL=7
    DECHAR=8
    EQUAL=9
    IF=10
    ELSE=11
    WHILE=12
    AND=13
    OR=14
    GREATER_EQUAL=15
    LESSER_EQUAL=16
    GREATER=17
    LESSER=18
    PLUS=19
    MINUS=20
    MULT=21
    DIV=22
    REST=23
    PLUS_PLUS=24
    MINUS_MINUS=25
    ENDLINE=26
    INT=27
    STRING=28
    FLOAT=29
    BOOL=30
    ID=31
    LKEY=32
    RKEY=33
    LPAREN=34
    RPAREN=35

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
            self.state = 14
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


        def dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ccedilhaParser.DecContext)
            else:
                return self.getTypedRuleContext(ccedilhaParser.DecContext,i)


        def ENDLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ccedilhaParser.ENDLINE)
            else:
                return self.getToken(ccedilhaParser.ENDLINE, i)

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
            self.state = 16
            self.match(ccedilhaParser.T__0)
            self.state = 17
            self.match(ccedilhaParser.LKEY)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 23
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 18
                    self.func()
                    pass

                elif la_ == 2:
                    self.state = 19
                    self.att()
                    pass

                elif la_ == 3:
                    self.state = 20
                    self.dec()
                    self.state = 21
                    self.match(ccedilhaParser.ENDLINE)
                    pass


                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ccedilhaParser.T__1) | (1 << ccedilhaParser.DEINT) | (1 << ccedilhaParser.DESTRING) | (1 << ccedilhaParser.DEFLOAT) | (1 << ccedilhaParser.DEBOOL) | (1 << ccedilhaParser.DECHAR) | (1 << ccedilhaParser.ID))) != 0)):
                    break

            self.state = 27
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

        def EQUAL(self):
            return self.getToken(ccedilhaParser.EQUAL, 0)

        def ENDLINE(self):
            return self.getToken(ccedilhaParser.ENDLINE, 0)

        def dec(self):
            return self.getTypedRuleContext(ccedilhaParser.DecContext,0)


        def ID(self):
            return self.getToken(ccedilhaParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ccedilhaParser.ExprContext,0)


        def STRING(self):
            return self.getToken(ccedilhaParser.STRING, 0)

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
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ccedilhaParser.DEINT, ccedilhaParser.DESTRING, ccedilhaParser.DEFLOAT, ccedilhaParser.DEBOOL, ccedilhaParser.DECHAR]:
                self.state = 29
                self.dec()
                pass
            elif token in [ccedilhaParser.ID]:
                self.state = 30
                self.match(ccedilhaParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 33
            self.match(ccedilhaParser.EQUAL)
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ccedilhaParser.INT, ccedilhaParser.ID, ccedilhaParser.LPAREN]:
                self.state = 34
                self.expr(0)
                pass
            elif token in [ccedilhaParser.STRING]:
                self.state = 35
                self.match(ccedilhaParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 38
            self.match(ccedilhaParser.ENDLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_type(self):
            return self.getTypedRuleContext(ccedilhaParser.Basic_typeContext,0)


        def ID(self):
            return self.getToken(ccedilhaParser.ID, 0)

        def getRuleIndex(self):
            return ccedilhaParser.RULE_dec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec" ):
                listener.enterDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec" ):
                listener.exitDec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec" ):
                return visitor.visitDec(self)
            else:
                return visitor.visitChildren(self)




    def dec(self):

        localctx = ccedilhaParser.DecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.basic_type()
            self.state = 41
            self.match(ccedilhaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEINT(self):
            return self.getToken(ccedilhaParser.DEINT, 0)

        def DESTRING(self):
            return self.getToken(ccedilhaParser.DESTRING, 0)

        def DEFLOAT(self):
            return self.getToken(ccedilhaParser.DEFLOAT, 0)

        def DEBOOL(self):
            return self.getToken(ccedilhaParser.DEBOOL, 0)

        def DECHAR(self):
            return self.getToken(ccedilhaParser.DECHAR, 0)

        def getRuleIndex(self):
            return ccedilhaParser.RULE_basic_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasic_type" ):
                listener.enterBasic_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasic_type" ):
                listener.exitBasic_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_type" ):
                return visitor.visitBasic_type(self)
            else:
                return visitor.visitChildren(self)




    def basic_type(self):

        localctx = ccedilhaParser.Basic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_basic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ccedilhaParser.DEINT) | (1 << ccedilhaParser.DESTRING) | (1 << ccedilhaParser.DEFLOAT) | (1 << ccedilhaParser.DEBOOL) | (1 << ccedilhaParser.DECHAR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self.enterRule(localctx, 10, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ccedilhaParser.FuncPrintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(ccedilhaParser.T__1)
                self.state = 46
                self.match(ccedilhaParser.LPAREN)
                self.state = 47
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ccedilhaParser.INT) | (1 << ccedilhaParser.STRING) | (1 << ccedilhaParser.ID))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 48
                self.match(ccedilhaParser.RPAREN)
                self.state = 49
                self.match(ccedilhaParser.ENDLINE)
                pass

            elif la_ == 2:
                localctx = ccedilhaParser.FuncPlusPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(ccedilhaParser.ID)
                self.state = 51
                self.match(ccedilhaParser.PLUS_PLUS)
                self.state = 52
                self.match(ccedilhaParser.ENDLINE)
                pass

            elif la_ == 3:
                localctx = ccedilhaParser.FuncMinusMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.match(ccedilhaParser.ID)
                self.state = 54
                self.match(ccedilhaParser.MINUS_MINUS)
                self.state = 55
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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ccedilhaParser.INT]:
                localctx = ccedilhaParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 59
                self.match(ccedilhaParser.INT)
                pass
            elif token in [ccedilhaParser.ID]:
                localctx = ccedilhaParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.match(ccedilhaParser.ID)
                pass
            elif token in [ccedilhaParser.LPAREN]:
                localctx = ccedilhaParser.ExprParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(ccedilhaParser.LPAREN)
                self.state = 62
                self.expr(0)
                self.state = 63
                self.match(ccedilhaParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 73
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = ccedilhaParser.ExprMultDivContext(self, ccedilhaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 67
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 68
                        _la = self._input.LA(1)
                        if not(_la==ccedilhaParser.MULT or _la==ccedilhaParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 69
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ccedilhaParser.ExprPlusMinusContext(self, ccedilhaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 70
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 71
                        _la = self._input.LA(1)
                        if not(_la==ccedilhaParser.PLUS or _la==ccedilhaParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 72
                        self.expr(5)
                        pass

             
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self._predicates[6] = self.expr_sempred
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
         




