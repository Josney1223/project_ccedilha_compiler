import unittest
import os
from antlr4 import *
from venv.Lib.ccedilha.ccedilhaLexer import ccedilhaLexer
from venv.Lib.ccedilha.ccedilhaParser import ccedilhaParser
from venv.Lib.ccedilha.ccedilhaVisitorLogic import ccedilhaVisitorLogic


class TestCcedilhaAtt(unittest.TestCase):

    test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_files", "att")

    def test_att(self):
        path = os.path.join(self.test_dir, "tudo.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()
        c = ccedilhaVisitorLogic()
        c.visitProg(tree)

        a_value = c.local_Ids[0].dictionary['a'].value
        a_type = c.local_Ids[0].dictionary['a'].type
        a_is_list = c.local_Ids[0].dictionary['a'].isList
        self.assertEqual(10, a_value)
        self.assertEqual(int, a_type)
        self.assertEqual(False, a_is_list)

        b_value = c.local_Ids[0].dictionary['b'].value
        b_type = c.local_Ids[0].dictionary['b'].type
        b_is_list = c.local_Ids[0].dictionary['b'].isList
        self.assertEqual(True, b_value)
        self.assertEqual(bool, b_type)
        self.assertEqual(False, b_is_list)

        x_value = c.local_Ids[0].dictionary['x'].value
        x_type = c.local_Ids[0].dictionary['x'].type
        x_is_list = c.local_Ids[0].dictionary['x'].isList
        self.assertEqual('"bom-dia"', x_value)
        self.assertEqual(str, x_type)
        self.assertEqual(False, x_is_list)

        y_value = c.local_Ids[0].dictionary['y'].value
        y_type = c.local_Ids[0].dictionary['y'].type
        y_is_list = c.local_Ids[0].dictionary['y'].isList
        self.assertEqual([1, 2, 3], y_value)
        self.assertEqual(int, y_type)
        self.assertEqual(True, y_is_list)
