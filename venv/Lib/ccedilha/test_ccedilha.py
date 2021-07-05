# encoding: utf-8
import sys
from antlr4 import *
from ccedilhaLexer import ccedilhaLexer
from ccedilhaParser import ccedilhaParser
from ccedilhaVisitorLogic import ccedilhaVisitorLogic


def main(argv):
    input = FileStream(argv[1], encoding= 'UTF-8')
    lexer = ccedilhaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ccedilhaParser(stream)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))

    c = ccedilhaVisitorLogic()
    c.visitProg(tree)
    # listener = ccedilhaListener()
    # walker = ParseTreeWalker()
    # walker.walk(listener, tree)


if __name__ == '__main__':
    main(sys.argv)
