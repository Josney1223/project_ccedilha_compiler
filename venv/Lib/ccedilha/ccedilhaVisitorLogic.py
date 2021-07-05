# Generated from ccedilha.g4 by ANTLR 4.9.2
from att_package import att_dict
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ccedilhaParser import ccedilhaParser
else:
    from ccedilhaParser import ccedilhaParser

# This class defines a complete generic visitor for a parse tree produced by ccedilhaParser.

class ccedilhaVisitorLogic(ParseTreeVisitor):
    def __init__(self):
        self.Ids = att_dict.AttDict()

    # Visit a parse tree produced by ccedilhaParser#prog.
    def visitProg(self, ctx:ccedilhaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#main.
    def visitMain(self, ctx:ccedilhaParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#att.
    def visitAtt(self, ctx:ccedilhaParser.AttContext):        
        if ctx.ID() is not None:
            att_name = ctx.ID().getText()
            if ctx.expr() is not None:
                self.Ids.setValue(att_name, self.visit(ctx.expr()), int)
            elif ctx.STRING() is not None:
                self.Ids.setValue(att_name, ctx.STRING().getText(), str)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#dec.
    def visitDec(self, ctx:ccedilhaParser.DecContext):        
        t = self.get_type(ctx.basic_type().getText())
        if not self.Ids.check_exist(ctx.ID().getText(), t) and t is not None:
            self.Ids.insert(ctx.ID().getText(), None, t)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#basic_type.
    def visitBasic_type(self, ctx:ccedilhaParser.Basic_typeContext):        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#funcPrint.
    def visitFuncPrint(self, ctx:ccedilhaParser.FuncPrintContext):    
        if ctx.ID() is not None:
            print(self.Ids.getValue(ctx.ID().getText(), "wildcard"))
        elif ctx.INT() is not None:
            print(ctx.INT().getText())
        elif ctx.STRING() is not None:
            print(ctx.STRING().getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#funcPlusPlus.
    def visitFuncPlusPlus(self, ctx:ccedilhaParser.FuncPlusPlusContext):
        if ctx.ID() is not None:
            att_name = ctx.ID().getText()
            valor = self.Ids.getValue(att_name, int)
            if valor is not None:
                self.Ids.setValue(att_name, valor + 1, int)
            else:
                raise TypeError
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#funcMinusMinus.
    def visitFuncMinusMinus(self, ctx:ccedilhaParser.FuncMinusMinusContext):
        if ctx.ID() is not None:
            att_name = ctx.ID().getText()
            valor = self.Ids.getValue(att_name, int)
            if valor is not None:
                self.Ids.setValue(att_name, valor - 1, int)
            else:
                raise TypeError
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#exprMultDiv.
    def visitExprMultDiv(self, ctx:ccedilhaParser.ExprMultDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.MULT() is not None:
            return left * right
        else:
            return left / right       


    # Visit a parse tree produced by ccedilhaParser#exprParen.
    def visitExprParen(self, ctx:ccedilhaParser.ExprParenContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by ccedilhaParser#exprPlusMinus.
    def visitExprPlusMinus(self, ctx:ccedilhaParser.ExprPlusMinusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.PLUS() is not None:
            return left + right
        else:
            return left - right        


    # Visit a parse tree produced by ccedilhaParser#Number.
    def visitNumber(self, ctx:ccedilhaParser.NumberContext):
        return int(ctx.INT().getText())


    # Visit a parse tree produced by ccedilhaParser#id.
    def visitId(self, ctx:ccedilhaParser.IdContext):
        return int(self.Ids.getValue(ctx.ID().getText(), int))

    def get_type(self, s: str) -> type:
        if s.strip() == "inteiro":
            return int
        elif s.strip() == "sentenca":
            return str
        elif s.strip() == "flutuante":
            return float
        elif s.strip() == "talvez":
            return bool
        return None


del ccedilhaParser