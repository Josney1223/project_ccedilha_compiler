# Generated from ccedilha.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ccedilhaParser import ccedilhaParser
else:
    from ccedilhaParser import ccedilhaParser

# This class defines a complete listener for a parse tree produced by ccedilhaParser.
class ccedilhaListener(ParseTreeListener):

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


    # Enter a parse tree produced by ccedilhaParser#att.
    def enterAtt(self, ctx:ccedilhaParser.AttContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#att.
    def exitAtt(self, ctx:ccedilhaParser.AttContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#code.
    def enterCode(self, ctx:ccedilhaParser.CodeContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#code.
    def exitCode(self, ctx:ccedilhaParser.CodeContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#dec.
    def enterDec(self, ctx:ccedilhaParser.DecContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#dec.
    def exitDec(self, ctx:ccedilhaParser.DecContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#list_type.
    def enterList_type(self, ctx:ccedilhaParser.List_typeContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#list_type.
    def exitList_type(self, ctx:ccedilhaParser.List_typeContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#basic_type.
    def enterBasic_type(self, ctx:ccedilhaParser.Basic_typeContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#basic_type.
    def exitBasic_type(self, ctx:ccedilhaParser.Basic_typeContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#basic_logic.
    def enterBasic_logic(self, ctx:ccedilhaParser.Basic_logicContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#basic_logic.
    def exitBasic_logic(self, ctx:ccedilhaParser.Basic_logicContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#funcPrint.
    def enterFuncPrint(self, ctx:ccedilhaParser.FuncPrintContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#funcPrint.
    def exitFuncPrint(self, ctx:ccedilhaParser.FuncPrintContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#funcPlusPlus.
    def enterFuncPlusPlus(self, ctx:ccedilhaParser.FuncPlusPlusContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#funcPlusPlus.
    def exitFuncPlusPlus(self, ctx:ccedilhaParser.FuncPlusPlusContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#funcMinusMinus.
    def enterFuncMinusMinus(self, ctx:ccedilhaParser.FuncMinusMinusContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#funcMinusMinus.
    def exitFuncMinusMinus(self, ctx:ccedilhaParser.FuncMinusMinusContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#boolean.
    def enterBoolean(self, ctx:ccedilhaParser.BooleanContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#boolean.
    def exitBoolean(self, ctx:ccedilhaParser.BooleanContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#expr_boolParen.
    def enterExpr_boolParen(self, ctx:ccedilhaParser.Expr_boolParenContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#expr_boolParen.
    def exitExpr_boolParen(self, ctx:ccedilhaParser.Expr_boolParenContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#Bool.
    def enterBool(self, ctx:ccedilhaParser.BoolContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#Bool.
    def exitBool(self, ctx:ccedilhaParser.BoolContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#expr_boolLogic.
    def enterExpr_boolLogic(self, ctx:ccedilhaParser.Expr_boolLogicContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#expr_boolLogic.
    def exitExpr_boolLogic(self, ctx:ccedilhaParser.Expr_boolLogicContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#expr_boolAndOr.
    def enterExpr_boolAndOr(self, ctx:ccedilhaParser.Expr_boolAndOrContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#expr_boolAndOr.
    def exitExpr_boolAndOr(self, ctx:ccedilhaParser.Expr_boolAndOrContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#exprMultDiv.
    def enterExprMultDiv(self, ctx:ccedilhaParser.ExprMultDivContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#exprMultDiv.
    def exitExprMultDiv(self, ctx:ccedilhaParser.ExprMultDivContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#exprParen.
    def enterExprParen(self, ctx:ccedilhaParser.ExprParenContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#exprParen.
    def exitExprParen(self, ctx:ccedilhaParser.ExprParenContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#exprPlusMinus.
    def enterExprPlusMinus(self, ctx:ccedilhaParser.ExprPlusMinusContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#exprPlusMinus.
    def exitExprPlusMinus(self, ctx:ccedilhaParser.ExprPlusMinusContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#Number.
    def enterNumber(self, ctx:ccedilhaParser.NumberContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#Number.
    def exitNumber(self, ctx:ccedilhaParser.NumberContext):
        pass


    # Enter a parse tree produced by ccedilhaParser#id.
    def enterId(self, ctx:ccedilhaParser.IdContext):
        pass

    # Exit a parse tree produced by ccedilhaParser#id.
    def exitId(self, ctx:ccedilhaParser.IdContext):
        pass



del ccedilhaParser