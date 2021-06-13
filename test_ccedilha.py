# encoding: utf-8
import sys
from antlr4 import *
from ccedilhaLexer import ccedilhaLexer
from ccedilhaParser import ccedilhaParser


def main(argv):
    input = FileStream(argv[1], encoding= 'UTF-8')
    lexer = ccedilhaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ccedilhaParser(stream)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)
