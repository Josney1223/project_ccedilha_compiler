# Generated from ccedilha.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ccedilhaParser import ccedilhaParser
else:
    from ccedilhaParser import ccedilhaParser

# This class defines a complete generic visitor for a parse tree produced by ccedilhaParser.

class ccedilhaVisitor(ParseTreeVisitor):
    def __init__(self):
        self.Ids = {}

    # Visit a parse tree produced by ccedilhaParser#prog.
    def visitProg(self, ctx:ccedilhaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#main.
    def visitMain(self, ctx:ccedilhaParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#att.
    def visitAtt(self, ctx:ccedilhaParser.AttContext):
        if ctx.ID() is not None:
            self.Ids[ctx.ID().getText()] = self.visit(ctx.expr())
        return None


    # Visit a parse tree produced by ccedilhaParser#funcPrint.
    def visitFuncPrint(self, ctx:ccedilhaParser.FuncPrintContext):
        if ctx.ID() is not None:
            result = self.Ids[ctx.ID().getText()]
        elif ctx.INT() is not None:
            result = self.visit(ctx.INT())
        elif ctx.STRING() is not None:
            result = self.visit(ctx.STRING())
        print(result)
        return None


    # Visit a parse tree produced by ccedilhaParser#funcPlusPlus.
    def visitFuncPlusPlus(self, ctx:ccedilhaParser.FuncPlusPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#funcMinusMinus.
    def visitFuncMinusMinus(self, ctx:ccedilhaParser.FuncMinusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#exprMultDiv.
    def visitExprMultDiv(self, ctx:ccedilhaParser.ExprMultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#exprParen.
    def visitExprParen(self, ctx:ccedilhaParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#exprPlusMinus.
    def visitExprPlusMinus(self, ctx:ccedilhaParser.ExprPlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#Number.
    def visitNumber(self, ctx:ccedilhaParser.NumberContext):
        return int(ctx.INT().getText())


    # Visit a parse tree produced by ccedilhaParser#id.
    def visitId(self, ctx:ccedilhaParser.IdContext):
        return self.visitChildren(ctx)



del ccedilhaParser