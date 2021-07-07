import unittest
import os
from antlr4 import *
from venv.Lib.ccedilha.ccedilhaLexer import ccedilhaLexer
from venv.Lib.ccedilha.ccedilhaParser import ccedilhaParser
from venv.Lib.ccedilha.ccedilhaVisitorLogic import ccedilhaVisitorLogic


class TestCcedilhaDec(unittest.TestCase):

    test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_files", "dec")

    def test_dec(self):
        path = os.path.join(self.test_dir, "tipos_basico.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()
        c = ccedilhaVisitorLogic()
        c.visitProg(tree)

        a_type = c.local_Ids[0].dictionary['a'].type
        a_is_list = c.local_Ids[0].dictionary['a'].isList
        self.assertEqual(bool, a_type)
        self.assertEqual(False, a_is_list)

        b_type = c.local_Ids[0].dictionary['b'].type
        b_is_list = c.local_Ids[0].dictionary['b'].isList
        self.assertEqual(int, b_type)
        self.assertEqual(False, b_is_list)

        x_type = c.local_Ids[0].dictionary['x'].type
        x_is_list = c.local_Ids[0].dictionary['x'].isList
        self.assertEqual(str, x_type)
        self.assertEqual(False, x_is_list)

        y_type = c.local_Ids[0].dictionary['y'].type
        y_is_list = c.local_Ids[0].dictionary['y'].isList
        self.assertEqual(bool, y_type)
        self.assertEqual(True, y_is_list)
