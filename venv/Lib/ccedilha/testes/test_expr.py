import unittest
import os
from antlr4 import *
from venv.Lib.ccedilha.ccedilhaLexer import ccedilhaLexer
from venv.Lib.ccedilha.ccedilhaParser import ccedilhaParser
from venv.Lib.ccedilha.ccedilhaVisitorLogic import ccedilhaVisitorLogic


class TestCcedilhaExpr(unittest.TestCase):

    expr_test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_files", "expr")

    def test_expr_plus(self):
        path = os.path.join(self.expr_test_dir, "mais.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 90 + 10

        c = ccedilhaVisitorLogic()
        result = c.visitExprPlusMinus(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_plus_negative(self):
        path = os.path.join(self.expr_test_dir, "mais_negativo.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 1 + -10

        c = ccedilhaVisitorLogic()
        result = c.visitExprPlusMinus(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_plus_more_numbers(self):
        path = os.path.join(self.expr_test_dir, "mais_varios_numeros.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 1 + 2 + 3 + 4 + 5

        c = ccedilhaVisitorLogic()
        result = c.visitExprPlusMinus(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_minus(self):
        path = os.path.join(self.expr_test_dir, "menos.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 150 - 23

        c = ccedilhaVisitorLogic()
        result = c.visitExprPlusMinus(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_minus_negative(self):
        path = os.path.join(self.expr_test_dir, "menos_negativo.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 10 - -10

        c = ccedilhaVisitorLogic()
        result = c.visitExprPlusMinus(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_minus_more_numbers(self):
        path = os.path.join(self.expr_test_dir, "menos_varios_numeros.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 1 - 2 - 3 - 4 - 5

        c = ccedilhaVisitorLogic()
        result = c.visitExprPlusMinus(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_plus_minus(self):
        path = os.path.join(self.expr_test_dir, "mais_menos.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 1 - 2 + 3 - 4 + 5

        c = ccedilhaVisitorLogic()
        result = c.visitExprPlusMinus(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_mult(self):
        path = os.path.join(self.expr_test_dir, "vezes.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 2 * 3

        c = ccedilhaVisitorLogic()
        result = c.visitExprMultDiv(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_mult_negative(self):
        path = os.path.join(self.expr_test_dir, "vezes_negativo.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 2 * -3

        c = ccedilhaVisitorLogic()
        result = c.visitExprMultDiv(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_mult_more_numbers(self):
        path = os.path.join(self.expr_test_dir, "vezes_varios_numeros.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 2 * 3 * -5 * 1 * 9

        c = ccedilhaVisitorLogic()
        result = c.visitExprMultDiv(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_div(self):
        path = os.path.join(self.expr_test_dir, "divide.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 16 / 4

        c = ccedilhaVisitorLogic()
        result = c.visitExprMultDiv(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_div_negative(self):
        path = os.path.join(self.expr_test_dir, "divide_negativo.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 25 / -5

        c = ccedilhaVisitorLogic()
        result = c.visitExprMultDiv(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_div_more_numbers(self):
        path = os.path.join(self.expr_test_dir, "divide_varios_numeros.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 120 / 4 / 2 / 5 / 3

        c = ccedilhaVisitorLogic()
        result = c.visitExprMultDiv(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_div_mult(self):
        path = os.path.join(self.expr_test_dir, "divide_vezes.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = 16 / 4 * 6 / 2 * 3

        c = ccedilhaVisitorLogic()
        result = c.visitExprMultDiv(tree)
        self.assertEqual(equivalent_expr, result)

    def test_expr_mult_plus(self):
        path = os.path.join(self.expr_test_dir, "parentesis.ç")
        file = FileStream(path, encoding='UTF-8')
        lexer = ccedilhaLexer(file)
        stream = CommonTokenStream(lexer)
        parser = ccedilhaParser(stream)
        tree = parser.expr()

        equivalent_expr = (10 + 20) * 3

        c = ccedilhaVisitorLogic()
        result = c.visitExprMultDiv(tree)
        self.assertEqual(equivalent_expr, result)
