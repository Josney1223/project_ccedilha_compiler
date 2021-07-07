import unittest
import os
from antlr4 import *
from venv.Lib.ccedilha.ccedilhaLexer import ccedilhaLexer
from venv.Lib.ccedilha.ccedilhaParser import ccedilhaParser
from venv.Lib.ccedilha.ccedilhaVisitorLogic import ccedilhaVisitorLogic


class TestCcedilhaFuncEnd(unittest.TestCase):

    func_test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_files", "func_dec_call_end")

    def test_func_end_sem_parametro(self):
        path = os.path.join(self.func_test_dir, "sem_parametro.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()
        c = ccedilhaVisitorLogic()
        c.visitProg(tree)

        var_value = c.local_Ids[0].dictionary['a'].value
        var_type = c.local_Ids[0].dictionary['a'].type
        self.assertEqual(10, var_value)
        self.assertEqual(int, var_type)

    def test_func_end_com_parametros(self):
        path = os.path.join(self.func_test_dir, "com_parametros.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()
        c = ccedilhaVisitorLogic()
        c.visitProg(tree)

        var_value = c.local_Ids[0].dictionary['a'].value
        var_type = c.local_Ids[0].dictionary['a'].type
        self.assertEqual(40, var_value)
        self.assertEqual(int, var_type)
