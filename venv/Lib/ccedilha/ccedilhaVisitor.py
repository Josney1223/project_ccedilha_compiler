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


    # Visit a parse tree produced by ccedilhaParser#code.
    def visitCode(self, ctx:ccedilhaParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#dec.
    def visitDec(self, ctx:ccedilhaParser.DecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#list_type.
    def visitList_type(self, ctx:ccedilhaParser.List_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#basic_type.
    def visitBasic_type(self, ctx:ccedilhaParser.Basic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#basic_logic.
    def visitBasic_logic(self, ctx:ccedilhaParser.Basic_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#func_dec.
    def visitFunc_dec(self, ctx:ccedilhaParser.Func_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#func_call.
    def visitFunc_call(self, ctx:ccedilhaParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#func_end.
    def visitFunc_end(self, ctx:ccedilhaParser.Func_endContext):
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


    # Visit a parse tree produced by ccedilhaParser#args.
    def visitArgs(self, ctx:ccedilhaParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#boolean.
    def visitBoolean(self, ctx:ccedilhaParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#expr_boolParen.
    def visitExpr_boolParen(self, ctx:ccedilhaParser.Expr_boolParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#Bool.
    def visitBool(self, ctx:ccedilhaParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#expr_boolLogic.
    def visitExpr_boolLogic(self, ctx:ccedilhaParser.Expr_boolLogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ccedilhaParser#expr_boolAndOr.
    def visitExpr_boolAndOr(self, ctx:ccedilhaParser.Expr_boolAndOrContext):
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


    # Visit a parse tree produced by ccedilhaParser#exprFuncCall.
    def visitExprFuncCall(self, ctx:ccedilhaParser.ExprFuncCallContext):
        return self.visitChildren(ctx)



del ccedilhaParser