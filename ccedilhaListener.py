# Generated from ccedilha.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ccedilhaParser import ccedilhaParser
else:
    from ccedilhaParser import ccedilhaParser

# This class defines a complete listener for a parse tree produced by ccedilhaParser.
class ccedilhaListener(ParseTreeListener):
    def __init__(self):
        self.atts = {}

    # Enter a parse tree produced by ccedilhaParser#prog.
    def enterProg(self, ctx:ccedilhaParser.ProgContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#prog.
    def exitProg(self, ctx:ccedilhaParser.ProgContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#main.
    def enterMain(self, ctx:ccedilhaParser.MainContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#main.
    def exitMain(self, ctx:ccedilhaParser.MainContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#stat.
    def enterStat(self, ctx:ccedilhaParser.StatContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#stat.
    def exitStat(self, ctx:ccedilhaParser.StatContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#att.
    def enterAtt(self, ctx:ccedilhaParser.AttContext):
        if ctx.ID() not in self.atts:
            self.atts[ctx.ID()] = 

    # Exit a parse tree produced by ccedilhaParser#att.
    def exitAtt(self, ctx:ccedilhaParser.AttContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#func.
    def enterFunc(self, ctx:ccedilhaParser.FuncContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#func.
    def exitFunc(self, ctx:ccedilhaParser.FuncContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#expr.
    def enterExpr(self, ctx:ccedilhaParser.ExprContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#expr.
    def exitExpr(self, ctx:ccedilhaParser.ExprContext):
        pass



del ccedilhaParser