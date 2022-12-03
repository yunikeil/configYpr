from sly import Lexer
import sys
import json


class CalcLexer(Lexer):
    tokens = {'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES',
              'DIVIDE', 'ASSIGN', 'LPAREN', 'RPAREN'}
    ignore = ' \t'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'


#if __name__ == '__main__':
def calc(data: str):
    program = []
    #data = str(sys.argv[1])
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        program.append({tok.type : tok.value})
    return program

