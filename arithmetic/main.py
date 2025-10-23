from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser

def main():
    input_stream = InputStream("3+5")
    lexer = ArithmeticLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ArithmeticParser(stream)
    tree = parser.expr()
    print(tree.toStringTree(recog=parser))

if _name_ == "_main_":
    main()
