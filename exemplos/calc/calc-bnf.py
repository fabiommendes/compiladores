import ox
import operator as op


OPERATORS = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

lexer = ox.make_lexer([
    ('NUMBER', r'[0-9]+(\.[0-9]+)?'),
    ('OP_SUM', r'[+-]'),
    ('OP_MUL', r'[*/]'),
    ('LPAR', r'\('),
    ('RPAR', r'\)'),
])


identity = lambda x: x


def compute_operation(x, op, y):
    return OPERATORS[op](x, y)


parser = ox.make_parser([
    ('expr : term OP_SUM expr', compute_operation),
    ('expr : term', identity),
    ('term : atom OP_MUL term', compute_operation),
    ('term : atom', identity),
    ('atom : NUMBER', float),
    ('atom : LPAR expr RPAR', lambda x, y, z: y),
], ['NUMBER', 'OP_SUM', 'OP_MUL', 'LPAR', 'RPAR'])


while True:
    from pprint import pprint
    
    pprint(parser(lexer(input('expr: '))))
