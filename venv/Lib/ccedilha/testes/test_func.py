import unittest
import os
from antlr4 import *
from venv.Lib.ccedilha.ccedilhaLexer import ccedilhaLexer
from venv.Lib.ccedilha.ccedilhaParser import ccedilhaParser
from venv.Lib.ccedilha.ccedilhaVisitorLogic import ccedilhaVisitorLogic


class TestCcedilhaFunc(unittest.TestCase):

    func_test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_files", "func")

    def test_func_plusplus(self):
        path = os.path.join(self.func_test_dir, "maisMais.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()

        equivalent_tree_as_str = '(prog (main nada principal() { (code (att (dec (basic_type inteiro ) a)  igual  ' \
                                 '(expr 10) ç) (func a  maisMais ç)) }))'

        c = ccedilhaVisitorLogic()
        c.visitProg(tree)
        self.assertEqual(equivalent_tree_as_str, tree.toStringTree(recog=parser))

        a = 10
        a += 1
        equivalent_value = a

        var_value = c.local_Ids[0].dictionary['a'].value
        var_type = c.local_Ids[0].dictionary['a'].type
        self.assertEqual(equivalent_value, var_value)
        self.assertEqual(var_type, int)

    def test_func_minusminus(self):
        path = os.path.join(self.func_test_dir, "menosMenos.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()

        equivalent_tree_as_str = '(prog (main nada principal() { (code (att (dec (basic_type inteiro ) a)  igual  ' \
                                 '(expr 10) ç) (func a  menosMenos ç)) }))'

        c = ccedilhaVisitorLogic()
        c.visitProg(tree)
        self.assertEqual(equivalent_tree_as_str, tree.toStringTree(recog=parser))

        a = 10
        a -= 1
        equivalent_value = a

        var_value = c.local_Ids[0].dictionary['a'].value
        var_type = c.local_Ids[0].dictionary['a'].type
        self.assertEqual(equivalent_value, var_value)
        self.assertEqual(var_type, int)

    def test_func_print(self):
        path = os.path.join(self.func_test_dir, "amostrar.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()

        equivalent_tree_as_str = '(prog (main nada principal() { (code (att (dec (basic_type inteiro ) a)  igual  ' \
                                 '(expr 20) ç) (func amostrar ( a ) ç)) }))'

        c = ccedilhaVisitorLogic()
        c.visitProg(tree)
        self.assertEqual(equivalent_tree_as_str, tree.toStringTree(recog=parser))
