import sidekick as sk
import ox


class Expr(sk.Union):
    Number = sk.opt(int)
    BinOp = sk.opt(op=str, left=Expr, right=Expr)
    FCall = sk.opt(name=str, fargs=list)


Number = Expr.Number
BinOp = Expr.BinOp
FCall = Expr.FCall


#
# Calc lexer
#
lexer = ox.make_lexer([
    ('NUMBER', r'\d+(\.\d+)?'),
    ('STRING', r'"[^"]*"'),
    ('OP', r'[-+*/<>=?@&$^~%]+'),
    ('COMMENT', r'\#[^\n]*'),
    ('LPAR', r'\('),
    ('RPAR', r'\)'),
    ('FNAME', r'[a-z]+'),
    ('COMMA', r'\,'),
])

tokens = ['NUMBER', 'OP', 'LPAR', 
          'RPAR', 'FNAME', 'COMMA']

#
# Calc parser
#
identity = (lambda x: x)
op_call = (lambda x, op, y: BinOp(op, x, y))
fcall = (lambda x, y, z, w: FCall(x, z))

parser = ox.make_parser([
    ('expr : atom OP expr', op_call),
    ('expr : atom', identity),
    
    ('atom : NUMBER', lambda x: Number(int(x))),
    ('atom : LPAR expr RPAR', lambda x, y, z: y),
    ('atom : fcall', identity),

    ('fcall : FNAME LPAR RPAR', lambda x, y, z: FCall(x, [])),
    ('fcall : FNAME LPAR args RPAR', fcall),
    ('args : expr COMMA args', lambda x, _, xs: [x, *xs]),
    ('args : expr', lambda x: [x]),
], tokens=tokens)


while True:
    print(parser(lexer(input('expr: '))))