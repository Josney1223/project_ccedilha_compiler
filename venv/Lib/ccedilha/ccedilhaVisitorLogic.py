# Generated from ccedilha.g4 by ANTLR 4.9.2
from att_package import att_dict
from antlr4 import *

from func_package.func_dict import funcDict
if __name__ is not None and "." in __name__:
    from .ccedilhaParser import ccedilhaParser
else:
    from ccedilhaParser import ccedilhaParser

# This class defines a complete generic visitor for a parse tree produced by ccedilhaParser.

class ccedilhaVisitorLogic(ParseTreeVisitor):
    def __init__(self):
        self.Ids = att_dict.AttDict()
        self.functions = funcDict()
        self.local_Ids = att_dict.AttDict()
        self.local_Ids_active = False       

    # Visit a parse tree produced by ccedilhaParser#prog.
    def visitProg(self, ctx:ccedilhaParser.ProgContext):
        for i in ctx.func_dec():
            self.visit(i)
        self.visit(ctx.main())

    # Visit a parse tree produced by ccedilhaParser#func_dec.
    def visitFunc_dec(self, ctx:ccedilhaParser.Func_decContext):          
        x, args = 1, []        
        while(ctx.basic_type(x) is not None):
            args.append((self.get_type(ctx.basic_type(x).getText()), ctx.ID(x).getText()))
            x += 1
        self.functions.insertFunction(ctx.ID(0).getText(), self.get_type(ctx.basic_type(0).getText()), args, ctx.code()) 
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by ccedilhaParser#func_call.
    def visitFunc_call(self, ctx:ccedilhaParser.Func_callContext):
        del self.local_Ids
        self.local_Ids_active, self.local_Ids = True, att_dict.AttDict()
        x, args = 0, self.functions.get_args(ctx.ID().getText())       
        while(ctx.args(x) is not None): 
            self.local_Ids.insert(args[x][1], ctx.args(x).getText(), args[x][0], False, 0)
            x += 1
        func_tree = self.functions.call_function(ctx.ID().getText(), args)      
        return self.visit(func_tree)
    
    # Visit a parse tree produced by ccedilhaParser#main.
    def visitMain(self, ctx:ccedilhaParser.MainContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ccedilhaParser#att.
    def visitAtt(self, ctx:ccedilhaParser.AttContext):            
        if ctx.ID() is not None:
            att_name = ctx.ID().getText()   
        elif ctx.list_type() is not None:
            att_name = ctx.list_type().ID().getText()
            index = int(ctx.list_type().INT().getText())                         
        else:
            att_name = self.visit(ctx.dec())
            
        if ctx.list_type() is None:
            if ctx.expr() is not None:
                self.Ids.setValue(att_name, self.visit(ctx.expr()), int)
            elif ctx.STRING() is not None:
                self.Ids.setValue(att_name, ctx.STRING().getText(), str)
            elif ctx.expr_bool() is not None:
                self.Ids.setValue(att_name, self.visit(ctx.expr_bool()), bool)
        else:
            if ctx.expr() is not None:
                self.Ids.insertList(att_name,index, self.visit(ctx.expr()), int)
            elif ctx.STRING() is not None:
                self.Ids.insertList(att_name,index, ctx.STRING().getText(), str)
            elif ctx.expr_bool() is not None:
                self.Ids.insertList(att_name,index, self.visit(ctx.expr_bool()), bool)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ccedilhaParser#dec.
    def visitDec(self, ctx:ccedilhaParser.DecContext): 
        t = self.get_type(ctx.basic_type().getText()) 
        if ctx.list_type() is not None:
            aux = (ctx.list_type().ID().getText(),True, int(ctx.list_type().INT().getText()))    
        else:
            aux = (ctx.ID().getText(), False, 0)       
                           
        if not self.Ids.check_exist(aux[0], t):
            self.Ids.insert(aux[0], None, t, aux[1], aux[2])        
        return aux[0]
    
    # Visit a parse tree produced by ccedilhaParser#boolean.
    def visitBoolean(self, ctx:ccedilhaParser.BooleanContext):
        if ctx.IF() is not None:
            if self.visit(ctx.expr_bool()):
                self.visit(ctx.code(0))
            elif ctx.boolean() is not None:
                self.visit(ctx.boolean())
            elif ctx.ELSE() is not None:
                self.visit(ctx.code(1))
        elif ctx.WHILE() is not None:            
            while(self.visit(ctx.expr_bool())):
                self.visit(ctx.code(0))
            
    # Visit a parse tree produced by ccedilhaParser#list_type.
    def visitList_type(self, ctx:ccedilhaParser.List_typeContext):
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
            return self.return_bool_logic(ctx, left, right)                      
        elif ctx.STRING(0) is not None and ctx.STRING(1) is not None:
            left = ctx.STRING(0).getText()
            right = ctx.STRING(1).getText()
            return self.return_bool_logic(ctx, left, right)
        else:
            raise TypeError       

    # Visit a parse tree produced by ccedilhaParser#expr_boolAndOr.
    def visitExpr_boolAndOr(self, ctx:ccedilhaParser.Expr_boolAndOrContext):
        left = self.visit(ctx.expr_bool(0))
        right = self.visit(ctx.expr_bool(1))
        if ctx.AND() is not None:
            return (left and right)
        else:
            return (left or right)        

    # Visit a parse tree produced by ccedilhaParser#funcCall.
    #def visitFuncCall(self, ctx:ccedilhaParser.FuncCallContext):
    #    return self.visitChildren(ctx)
    
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
    
    # Visit a parse tree produced by ccedilhaParser#code.
    def visitCode(self, ctx:ccedilhaParser.CodeContext):
        return self.visitChildren(ctx)

    def return_bool_logic(self, ctx, left, right):
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