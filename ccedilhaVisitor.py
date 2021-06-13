# Generated from ccedilha.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ccedilhaParser import ccedilhaParser
else:
    from ccedilhaParser import ccedilhaParser

# This class defines a complete generic visitor for a parse tree produced by ccedilhaParser.

class ccedilhaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ccedilhaParser#stat.
    def visitStat(self, ctx:ccedilhaParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#expr.
    def visitExpr(self, ctx:ccedilhaParser.ExprContext):
        return self.visitChildren(ctx)



del ccedilhaParser