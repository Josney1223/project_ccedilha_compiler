import unittest
import os
from antlr4 import *
from venv.Lib.ccedilha.ccedilhaLexer import ccedilhaLexer
from venv.Lib.ccedilha.ccedilhaParser import ccedilhaParser
from venv.Lib.ccedilha.ccedilhaVisitorLogic import ccedilhaVisitorLogic


class TestCcedilhaExprBool(unittest.TestCase):

    test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_files", "expr_bool")

    def test_expr_bool_and(self):
        path = os.path.join(self.test_dir, "e.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()
        c = ccedilhaVisitorLogic()
        c.visitProg(tree)

        a = True and True
        b = True and False
        ce = False and True
        d = False and False

        a_value = c.local_Ids[0].dictionary['a'].value
        a_type = c.local_Ids[0].dictionary['a'].type
        self.assertEqual(a, a_value)
        self.assertEqual(a_type, bool)

        b_value = c.local_Ids[0].dictionary['b'].value
        b_type = c.local_Ids[0].dictionary['b'].type
        self.assertEqual(b, b_value)
        self.assertEqual(b_type, bool)

        ce_value = c.local_Ids[0].dictionary['c'].value
        ce_type = c.local_Ids[0].dictionary['c'].type
        self.assertEqual(ce, ce_value)
        self.assertEqual(ce_type, bool)

        d_value = c.local_Ids[0].dictionary['d'].value
        d_type = c.local_Ids[0].dictionary['d'].type
        self.assertEqual(d, d_value)
        self.assertEqual(d_type, bool)

    def test_expr_bool_or(self):
        path = os.path.join(self.test_dir, "ou.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()
        c = ccedilhaVisitorLogic()
        c.visitProg(tree)

        a = True or True
        b = True or False
        ce = False or True
        d = False or False

        a_value = c.local_Ids[0].dictionary['a'].value
        a_type = c.local_Ids[0].dictionary['a'].type
        self.assertEqual(a, a_value)
        self.assertEqual(a_type, bool)

        b_value = c.local_Ids[0].dictionary['b'].value
        b_type = c.local_Ids[0].dictionary['b'].type
        self.assertEqual(b, b_value)
        self.assertEqual(b_type, bool)

        ce_value = c.local_Ids[0].dictionary['c'].value
        ce_type = c.local_Ids[0].dictionary['c'].type
        self.assertEqual(ce, ce_value)
        self.assertEqual(ce_type, bool)

        d_value = c.local_Ids[0].dictionary['d'].value
        d_type = c.local_Ids[0].dictionary['d'].type
        self.assertEqual(d, d_value)
        self.assertEqual(d_type, bool)

    def test_expr_bool(self):
        path = os.path.join(self.test_dir, "tudo.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()
        c = ccedilhaVisitorLogic()
        c.visitProg(tree)

        a = 10 == 5 and (4 >= 4 or 6 <= 0) or (1 != 2) or 3 > 5 and 1 < 4 and True

        a_value = c.local_Ids[0].dictionary['a'].value
        a_type = c.local_Ids[0].dictionary['a'].type
        self.assertEqual(a, a_value)
        self.assertEqual(a_type, bool)
