import ox
from .lexer import tokens
from .ast import BinOp, FCall, Number


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