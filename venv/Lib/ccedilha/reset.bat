@echo on
del "ccedilha.tokens"
del "ccedilhaLexer.py"
del "ccedilhaLexer.tokens"
del "ccedilhaListener.py"
del "ccedilhaParser.py"
del "ccedilhaTokens.py"
del "ccedilhaTokens.tokens"

cmd "antlr4 -Dlanguage=Python3 -visitor ccedilha.g4"