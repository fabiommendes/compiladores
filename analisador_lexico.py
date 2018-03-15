from pprint import pprint
import re 
from collections import namedtuple

Token = namedtuple('Token', ['value', 'type'])

re_number = r'(?P<NUMBER>\d+)'  
re_operator = r'(?P<OPERATOR>[-+*/])'
re_space = r'(?P<SPACE>\s+)'
re_list = [
    re_number,
    re_operator,
    re_space
]
re_full = '|'.join(re_list)
re_compiled = re.compile(re_full)


def lexer(src: str) -> list:
    """
    Analisa uma string de código e retorna a lista de 
    tokens correspondentes
    """
    tokens = []
    last_char = 0

    for m in re_compiled.finditer(src):
        i, j = m.span()
        
        # Procura por "buracos" na string de codigo
        if i > last_char:
            raise SyntaxError('invalid token: %r' % src[last_char:i])
        last_char = j

        tk_type = m.lastgroup
        tk_value = src[i:j]
        
        if tk_type != 'SPACE':
            token = Token(tk_value, tk_type)
            tokens.append(token)

    if j != len(src):
        raise SyntaxError('invalid token: %r' % src[j:])

    return tokens

pprint(lexer(input('Expr: ')))