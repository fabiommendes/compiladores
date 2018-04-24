import ox
from .lexer import tokens
from .ast import BinOp, FCall, Atom, Assign


def make_parser():
    return ox.make_parser([
    ('module : statement SEMICOLON', lambda x, _: [x]),
    ('module : statement SEMICOLON module', statements),

    ('statement : NAME EQ expr', var_def),

    ('expr : atom OP expr', op_call),
    ('expr : atom', identity),
    
    ('atom : NUMBER', lambda x: Atom(float(x))),
    ('atom : STRING', lambda x: Atom(x[1:-1])),
    ('atom : BOOL', lambda x: Atom(x == 'true')),
    ('atom : LPAR expr RPAR', lambda x, y, z: y),
    ('atom : fcall', identity),

    ('fcall : NAME LPAR RPAR', lambda x, y, z: FCall(x, [])),
    ('fcall : NAME LPAR args RPAR', fcall),
    ('args : expr COMMA args', lambda x, _, xs: [x, *xs]),
    ('args : expr', lambda x: [x]),
], tokens=tokens)


# Funçoes auxiliares
identity = (lambda x: x)
op_call = (lambda x, op, y: BinOp(op, x, y))
fcall = (lambda x, y, z, w: FCall(x, z))
statements = (lambda x, _, xs: [x, *xs])
var_def = (lambda name, eq, expr: Assign(name, expr))

# Cria parser
parser = make_parser() 
