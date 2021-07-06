import unittest
import os
from antlr4 import *
from venv.Lib.ccedilha.ccedilhaLexer import ccedilhaLexer
from venv.Lib.ccedilha.ccedilhaParser import ccedilhaParser
from venv.Lib.ccedilha.ccedilhaVisitorLogic import ccedilhaVisitorLogic


class TestCcedilhaBoolean(unittest.TestCase):

    test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_files", "boolean")

    def test_boolean_se_verdadeiro(self):
        path = os.path.join(self.test_dir, "se_verdadeiro.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()
        c = ccedilhaVisitorLogic()
        c.visitProg(tree)

        a_value = c.local_Ids[0].dictionary['a'].value
        a_type = c.local_Ids[0].dictionary['a'].type
        self.assertEqual(a_value, True)
        self.assertEqual(a_type, bool)

    def test_boolean_se_falso(self):
        path = os.path.join(self.test_dir, "se_falso.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()
        c = ccedilhaVisitorLogic()
        c.visitProg(tree)

        a_value = c.local_Ids[0].dictionary['a'].value
        a_type = c.local_Ids[0].dictionary['a'].type
        self.assertEqual(a_value, False)
        self.assertEqual(a_type, bool)

    def test_boolean_se_senao_se_verdadeiro(self):
        path = os.path.join(self.test_dir, "se_senao_se_verdadeiro.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()
        c = ccedilhaVisitorLogic()
        c.visitProg(tree)

        a_value = c.local_Ids[0].dictionary['a'].value
        a_type = c.local_Ids[0].dictionary['a'].type
        self.assertEqual(a_value, 2)
        self.assertEqual(a_type, int)

    def test_boolean_se_senao_se_falso(self):
        path = os.path.join(self.test_dir, "se_senao_se_falso.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()
        c = ccedilhaVisitorLogic()
        c.visitProg(tree)

        a_value = c.local_Ids[0].dictionary['a'].value
        a_type = c.local_Ids[0].dictionary['a'].type
        self.assertEqual(a_value, 3)
        self.assertEqual(a_type, int)

    def test_boolean_enquanto(self):
        path = os.path.join(self.test_dir, "enquanto.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.prog()
        c = ccedilhaVisitorLogic()
        c.visitProg(tree)

        a_value = c.local_Ids[0].dictionary['a'].value
        a_type = c.local_Ids[0].dictionary['a'].type
        self.assertEqual(a_value, 10)
        self.assertEqual(a_type, int)
