# project_ccedilha_compiler
Projeto remetente ao compilador da incrível linguagem Ç

Pré-requisitos:
- Python3 instalado
- antlr4 versão 4.9.2 instalada

Para utilizar o compilador:
- Altere o arquivo ".\venv\Lib\ccedilha\input.ç" como desejar
- Execute o arquivo no cmd o arquivo ".\venv\Scripts\activate.bat"
- Execute o comando no cmd "python test_ccedilha.py input.ç" dentro do diretório ".\venv\Lib\ccedilha\"

Caso o compilador não funcione, utilize o seguinte método:
- Delete os arquivos (caso existam): "ccedilha.tokens", "ccedilhaLexer.tokens", "ccedilhaTokens.tokens", "ccedilhaLexer.py", "ccedilhaListener.py", "ccedilhaParser.py", "ccedilhaTokens.py"
- Execute o comando "antlr4 -Dlanguage=Python3 -visitor ccedilha.g4" dentro do diretório ".\venv\Lib\ccedilha\"
- Tente utilizar o compilador novamente

Link para a documentação do projeto.

[Ccedilha.pdf](https://github.com/Josney1223/project_ccedilha_compiler/files/6777063/Ccedilha.pdf)




