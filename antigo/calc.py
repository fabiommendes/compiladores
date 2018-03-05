"""
Implementa uma calculadora simples utilizando a biblioteca ox.
"""

import ox
import operator as op


OP_TO_FUNCTION = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

#
# Lexer
#
lexer = ox.make_lexer([
    ('NUMBER', r'[0-9]+(\.[0-9]+)?'),
    ('OP', r'[-+*/]'),
])


#
# Parser
#
binop = (lambda a, op, b: OP_TO_FUNCTION[op](a, b))
parser = ox.make_parser([
    ('term : term OP atom', binop),
    ('term : atom', lambda x: x),
    ('atom : NUMBER', float),
])


#
#
#
if __name__ == '__main__':
    st = input('expr: ')
    tokens = lexer(st)
    print('tokens:', tokens)

    value = parser(tokens)
    print('res:', value)
