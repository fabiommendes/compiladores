import ox
from pprint import pprint


RULES = dict(
    NUMBER=r'\d+',
    STRING=r'".*"',
    LPAREN=r'\(',
    RPAREN=r'\)',
    SYMBOL=r'\w+',
    EQUAL=r'=',
    OP=r'[-+*/?^~<>!@$%&]+',
    COMMENT=r'\#[^\n]*',
)


lexer = ox.make_lexer(RULES.items())


pprint(lexer('x = 42 # comentario!'))
pprint(lexer('fib(x) = if x < 1 then 1 else fib(x - 1) + fib(x - 2)'))