# Generated from ccedilha.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ccedilhaParser import ccedilhaParser
else:
    from ccedilhaParser import ccedilhaParser

# This class defines a complete generic visitor for a parse tree produced by ccedilhaParser.

class ccedilhaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ccedilhaParser#prog.
    def visitProg(self, ctx:ccedilhaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#main.
    def visitMain(self, ctx:ccedilhaParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#att.
    def visitAtt(self, ctx:ccedilhaParser.AttContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#dec.
    def visitDec(self, ctx:ccedilhaParser.DecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#basic_type.
    def visitBasic_type(self, ctx:ccedilhaParser.Basic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#funcPrint.
    def visitFuncPrint(self, ctx:ccedilhaParser.FuncPrintContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#id.
    def visitId(self, ctx:ccedilhaParser.IdContext):
        return self.visitChildren(ctx)



del ccedilhaParser