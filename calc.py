import ox

lexer = ox.make_lexer([
    ('NUMBER', r'[0-9]+(\.[0-9]+)?'),
    ('OP', r'[-+*/]'),
])


OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

def binop(a, op, b):
    return OPERATORS[op](a, b)

tokens = ['NUMBER', 'OP']

parser = ox.make_parser([
    ('term : term OP atom', binop),
    ('term : atom', lambda x: x), 
    ('atom : NUMBER', float), 
], tokens)


st = input('expr: ')
tokens = lexer(st)
print('tokens:', tokens)

res = parser(tokens)
print('res:', res)
