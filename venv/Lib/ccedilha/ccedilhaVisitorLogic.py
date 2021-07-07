# Generated from ccedilha.g4 by ANTLR 4.9.2
if __name__ is not None and "." in __name__:
    from att_package import att_dict
else:
    from att_package import att_dict
from antlr4 import *
from ccedilhaParser import ccedilhaParser
from func_package.func_dict import funcDict

# This class defines a complete generic visitor for a parse tree produced by ccedilhaParser.


class ccedilhaVisitorLogic(ParseTreeVisitor):
    def __init__(self):
        self.functions = funcDict()
        self.local_Ids = []
        self.local_Ids.append(att_dict.AttDict())
        self.actual_context = 0
        self.func_return = None

    # Visit a parse tree produced by ccedilhaParser#prog.
    def visitProg(self, ctx:ccedilhaParser.ProgContext):
        for i in ctx.func_dec():
            self.visit(i)
        self.visit(ctx.main())        

    # Visit a parse tree produced by ccedilhaParser#func_dec.
    def visitFunc_dec(self, ctx:ccedilhaParser.Func_decContext):          
        x, args = 1, []        
        while(ctx.basic_type(x)):
            args.append((self.get_type(ctx.basic_type(x).getText()), ctx.ID(x).getText()))
            x += 1
        self.functions.insertFunction(ctx.ID(0).getText(), self.get_type(ctx.basic_type(0).getText()), args, ctx.code())

    # Visit a parse tree produced by ccedilhaParser#func_call.
    def visitFunc_call(self, ctx:ccedilhaParser.Func_callContext):
        x, args = 0, []
        while(ctx.args(x)):
            if ctx.args(x).expr():
                args.append(self.visit(ctx.args(x).expr()))
            elif ctx.args(x).expr_bool():
                args.append(self.visit(ctx.args(x).expr_bool()))
            elif ctx.args(x).STRING():
                args.append(ctx.args(x).STRING().getText())
            elif ctx.args(x).ID():
                args.append(self.visit(ctx.args(x).ID()))                         
            x += 1
        self.actual_context += 1
        self.local_Ids.append(att_dict.AttDict())
        
        x, args_dec = 0, self.functions.get_args(ctx.ID().getText())   
        while(ctx.args(x)):
            if self.local_Ids[self.actual_context-1].check_exist(ctx.args(x).getText(),"wildcard"): 
                self.local_Ids[self.actual_context].insert(args_dec[x][1], self.local_Ids[self.actual_context-1].getValue(ctx.args(x).getText(),"wildcard"), args_dec[x][0], False, 0)                
            else:                
                self.local_Ids[self.actual_context].insert(args_dec[x][1], args[x], args_dec[x][0], False, 0)
            x += 1
        func_tree = self.functions.call_function(ctx.ID().getText(), args)
        self.visit(func_tree)
        r = self.func_return

        self.local_Ids.pop(self.actual_context)
        self.func_return = None
        self.actual_context -= 1
        return r

    # Visit a parse tree produced by ccedilhaParser#func_end.
    def visitFunc_end(self, ctx:ccedilhaParser.Func_endContext):
        if ctx.expr():
            self.func_return = self.visit(ctx.expr())
        elif ctx.STRING():
            self.func_return = self.visit(ctx.STRING())
        elif ctx.expr_bool():
            self.func_return = self.visit(ctx.expr_bool())
        elif ctx.ID():
            self.func_return = self.visit(ctx.ID())
        elif ctx.func_call():
            self.func_return = self.visit(ctx.func_call())           
    
    # Visit a parse tree produced by ccedilhaParser#main.
    def visitMain(self, ctx:ccedilhaParser.MainContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ccedilhaParser#att.
    def visitAtt(self, ctx:ccedilhaParser.AttContext):
        if self.func_return is None:            
            if ctx.ID(0):
                att_name = ctx.ID(0).getText()
            elif ctx.list_type():
                att_name = ctx.list_type().ID().getText()
                index = int(ctx.list_type().INT().getText())
            else:
                att_name = self.visit(ctx.dec())

            if ctx.list_type() is None:
                if ctx.expr():
                    self.local_Ids[self.actual_context].setValue(att_name, self.visit(ctx.expr()), int)
                elif ctx.STRING():
                    self.local_Ids[self.actual_context].setValue(att_name, ctx.STRING().getText(), str)
                elif ctx.expr_bool():
                    self.local_Ids[self.actual_context].setValue(att_name, self.visit(ctx.expr_bool()), bool)
                elif ctx.func_call():
                    self.local_Ids[self.actual_context].setValue(att_name, self.visit(ctx.func_call()), self.functions.get_type(ctx.func_call().ID().getText()))
            else:
                if ctx.expr():
                    self.local_Ids[self.actual_context].insertList(att_name,index, self.visit(ctx.expr()), int)
                elif ctx.STRING():
                    self.local_Ids[self.actual_context].insertList(att_name,index, ctx.STRING().getText(), str)
                elif ctx.expr_bool():
                    self.local_Ids[self.actual_context].insertList(att_name,index, self.visit(ctx.expr_bool()), bool)
                elif ctx.func_call():
                    self.local_Ids[self.actual_context].setValue(att_name, index, self.visit(ctx.func_call()), self.functions.get_type(ctx.func_call().ID().getText()))
            return self.visitChildren(ctx)

    # Visit a parse tree produced by ccedilhaParser#dec.
    def visitDec(self, ctx:ccedilhaParser.DecContext):
        if self.func_return is None:  
            t = self.get_type(ctx.basic_type().getText()) 
            if ctx.list_type():
                aux = (ctx.list_type().ID().getText(),True, int(ctx.list_type().INT().getText()))    
            else:
                aux = (ctx.ID().getText(), False, 0)

            if not self.local_Ids[self.actual_context].check_exist(aux[0], t):
                self.local_Ids[self.actual_context].insert(aux[0], None, t, aux[1], aux[2])
            return aux[0]
    
    # Visit a parse tree produced by ccedilhaParser#boolean.
    def visitBoolean(self, ctx:ccedilhaParser.BooleanContext):
        if self.func_return is None: 
            if ctx.IF():
                if self.visit(ctx.expr_bool()):
                    self.visit(ctx.code(0))
                elif ctx.boolean():
                    self.visit(ctx.boolean())
                elif ctx.ELSE():
                    self.visit(ctx.code(1))
            elif ctx.WHILE():
                while(self.visit(ctx.expr_bool())):
                    self.visit(ctx.code(0))
            
    # Visit a parse tree produced by ccedilhaParser#list_type.
    def visitList_type(self, ctx:ccedilhaParser.List_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ccedilhaParser#basic_logic.
    def visitBasic_logic(self, ctx:ccedilhaParser.Basic_logicContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ccedilhaParser#expr_boolParen.
    def visitExpr_boolParen(self, ctx:ccedilhaParser.Expr_boolParenContext):
        return self.visit(ctx.expr_bool())

    # Visit a parse tree produced by ccedilhaParser#Bool.
    def visitBool(self, ctx:ccedilhaParser.BoolContext):
        n = True if ctx.NOT() else False
        if ctx.BOOL().getText() == 'verdadeiro':
            return True if not n else False
        else:
            return False if not n else True

    # Visit a parse tree produced by ccedilhaParser#expr_boolLogic.
    def visitExpr_boolLogic(self, ctx:ccedilhaParser.Expr_boolLogicContext):
        left, right = None, None
        n = True if ctx.NOT() else False
        if ctx.expr(0) and ctx.expr(1):
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))  
            return self.return_bool_logic(ctx, left, right) if not n else (not self.return_bool_logic(ctx, left, right))
        elif ctx.STRING(0) and ctx.STRING(1):
            left = ctx.STRING(0).getText()
            right = ctx.STRING(1).getText()
            return self.return_bool_logic(ctx, left, right) if not n else (not self.return_bool_logic(ctx, left, right))
        else:
            raise TypeError       

    # Visit a parse tree produced by ccedilhaParser#expr_boolAndOr.
    def visitExpr_boolAndOr(self, ctx:ccedilhaParser.Expr_boolAndOrContext):
        left = self.visit(ctx.expr_bool(0))
        right = self.visit(ctx.expr_bool(1))
        if ctx.AND():
            return (left and right)
        else:
            return (left or right)        

    # Visit a parse tree produced by ccedilhaParser#funcPrint.
    def visitFuncPrint(self, ctx:ccedilhaParser.FuncPrintContext):
        if self.func_return is None:     
            if ctx.ID():
                print(self.local_Ids[self.actual_context].getValue(ctx.ID().getText(), "wildcard"))
            elif ctx.expr():
                print(self.visit(ctx.expr()))
            elif ctx.STRING():
                print(ctx.STRING().getText())        
            return self.visitChildren(ctx)

    # Visit a parse tree produced by ccedilhaParser#funcPlusPlus.
    def visitFuncPlusPlus(self, ctx:ccedilhaParser.FuncPlusPlusContext):
        if self.func_return is None: 
            if ctx.ID():
                att_name = ctx.ID().getText()
            valor = self.local_Ids[self.actual_context].getValue(att_name, int)
            if valor is not None:
                self.local_Ids[self.actual_context].setValue(att_name, valor + 1, int)
            else:
                raise TypeError
            return self.visitChildren(ctx)

    # Visit a parse tree produced by ccedilhaParser#funcMinusMinus.
    def visitFuncMinusMinus(self, ctx:ccedilhaParser.FuncMinusMinusContext):
        if self.func_return is None: 
            if ctx.ID():
                att_name = ctx.ID().getText()
            valor = self.local_Ids[self.actual_context].getValue(att_name, int)
            if valor is not None:
                self.local_Ids[self.actual_context].setValue(att_name, valor - 1, int)
            else:
                raise TypeError
            return self.visitChildren(ctx)

    # Visit a parse tree produced by ccedilhaParser#exprMultDiv.
    def visitExprMultDiv(self, ctx:ccedilhaParser.ExprMultDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.MULT():
            return left * right
        elif ctx.DIV():
            return left / right       
        else:
            return left % right

    # Visit a parse tree produced by ccedilhaParser#exprParen.
    def visitExprParen(self, ctx:ccedilhaParser.ExprParenContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by ccedilhaParser#exprPlusMinus.
    def visitExprPlusMinus(self, ctx:ccedilhaParser.ExprPlusMinusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.PLUS():
            return left + right
        else:
            return left - right        

    # Visit a parse tree produced by ccedilhaParser#Number.
    def visitNumber(self, ctx:ccedilhaParser.NumberContext):
        return int(ctx.INT().getText())

    # Visit a parse tree produced by ccedilhaParser#id.
    def visitId(self, ctx:ccedilhaParser.IdContext):
        return int(self.local_Ids[self.actual_context].getValue(ctx.ID().getText(), int))
    
    # Visit a parse tree produced by ccedilhaParser#code.
    def visitCode(self, ctx:ccedilhaParser.CodeContext):
        return self.visitChildren(ctx)

    def visitExprFuncCall(self, ctx:ccedilhaParser.ExprFuncCallContext):
        return self.visitFunc_call(ctx.func_call())

    # Visit a parse tree produced by ccedilhaParser#args.
    def visitArgs(self, ctx:ccedilhaParser.ArgsContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.expr_bool():
            return self.visit(ctx.expr_bool())
        elif ctx.ID():
            return self.visit(ctx.ID())

    def return_bool_logic(self, ctx, left, right):
        if ctx.basic_logic().EQUAL_EQUAL():
            return (left == right)
        elif ctx.basic_logic().NOT_EQUAL():
            return (left != right)
        elif ctx.basic_logic().GREATER():
            return (left > right)
        elif ctx.basic_logic().GREATER_EQUAL():
            return (left >= right)
        elif ctx.basic_logic().LESSER_EQUAL():
            return (left <= right)
        elif ctx.basic_logic().LESSER():
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