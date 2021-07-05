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
    
    # Visit a parse tree produced by ccedilhaParser#boolean.
    def visitBoolean(self, ctx:ccedilhaParser.BooleanContext):
        if self.visit(ctx.expr_bool()) == 'verdadeiro':
            return self.visitChildren(ctx)

    # Visit a parse tree produced by ccedilhaParser#basic_type.
    # def visitBasic_type(self, ctx:ccedilhaParser.Basic_typeContext):        
    #    return self.visitChildren(ctx)
    
    # Visit a parse tree produced by ccedilhaParser#basic_logic.
    def visitBasic_logic(self, ctx:ccedilhaParser.Basic_logicContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ccedilhaParser#expr_boolParen.
    def visitExpr_boolParen(self, ctx:ccedilhaParser.Expr_boolParenContext):
        return self.visit(ctx.expr_bool())

    # Visit a parse tree produced by ccedilhaParser#Bool.
    def visitBool(self, ctx:ccedilhaParser.BoolContext):
        if ctx.BOOL().getText() == 'verdadeiro':
            return True
        else:
            return False        

    # Visit a parse tree produced by ccedilhaParser#expr_boolLogic.
    def visitExpr_boolLogic(self, ctx:ccedilhaParser.Expr_boolLogicContext):
        left, right = None, None
        if ctx.expr(0) is not None and ctx.expr(1) is not None:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))                        
        elif ctx.STRING(0) is not None and ctx.STRING(1) is not None:
            left = ctx.STRING(0).getText()
            right = ctx.STRING(1).getText()
        if ctx.basic_logic().EQUAL_EQUAL() is not None:
            return (left == right)
        elif ctx.basic_logic().NOT_EQUAL() is not None:
            return (left != right)
        elif ctx.basic_logic().GREATER() is not None:
            return (left > right)
        elif ctx.basic_logic().GREATER_EQUAL() is not None:
            return (left >= right)
        elif ctx.basic_logic().LESSER_EQUAL() is not None:
            return (left <= right)
        elif ctx.basic_logic().LESSER() is not None:
            return (left < right)        

    # Visit a parse tree produced by ccedilhaParser#expr_boolAndOr.
    def visitExpr_boolAndOr(self, ctx:ccedilhaParser.Expr_boolAndOrContext):
        left = self.visit(ctx.expr_bool(0))
        right = self.visit(ctx.expr_bool(1))
        if ctx.AND() is not None:
            return (left and right)
        else:
            return (left or right)        

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
            self.Ids.setValue(att_name, valor + 1, int)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ccedilhaParser#funcMinusMinus.
    def visitFuncMinusMinus(self, ctx:ccedilhaParser.FuncMinusMinusContext):
        if ctx.ID() is not None:
            att_name = ctx.ID().getText()
            valor = self.Ids.getValue(att_name, int)
            self.Ids.setValue(att_name, valor - 1, int)
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