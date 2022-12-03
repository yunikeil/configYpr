from sly import Lexer
import sys
import json


class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES',
              'DIVIDE', 'ASSIGN', 'LPAREN', 'RPAREN'}

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Regular expression rules for tokens
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'


if __name__ == '__main__':
    program = []
    data = str(sys.argv[1])
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        program.append({tok.type : tok.value})
    print(json.dumps(program, sort_keys=False, indent=4))


