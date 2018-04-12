import ox
import operator as op
import math

OP_MAP = {
    '+': op.add, '*': op.mul, '/': op.truediv, '-': op.sub,
}

lexer = ox.make_lexer([
    ('NUMBER', r'\d+'),
    ('STRING', r'"[^"]*"'),
    ('VARNAME', r'[a-z_][a-z_0-9]*'),
    ('TYPENAME', r'[A-Z][a-z_0-9A-Z]*'),
    ('EQUAL', r'='),
    ('COMMA', r'\,'),
    ('COLON', r'\:'),
    ('LPAR', r'\('),
    ('RPAR', r'\)'),
    ('OP', r'[-+*/@!$^~|&><]+'),
])

id = lambda x: x
exec_op = lambda a, op, b: OP_MAP[op](a, b)

func_dic = {
    'lala' : (lambda x: x*'la'),
    'max' : max,
    **vars(math),
}

def call_func(name, lpar, args, rpar):
    return func_dic[name](*args)


expr_parser = ox.make_parser([
    ('expr : op_expr', id),

    ('atom : NUMBER', int),
    ('atom : STRING', id),
    ('atom : call_func', id),
    ('atom : tuple', id),
    ('atom : LPAR expr RPAR', lambda x,y,z: y),

    ('op_expr : atom OP op_expr', exec_op),
    ('op_expr : atom', id),

    ('call_func : VARNAME LPAR args RPAR', call_func),
    ('args : expr', lambda x: [x]),
    ('args : expr COMMA args', lambda x, _, y: [x,*y]),

    ('tuple : LPAR RPAR', lambda x,y : ()),
    ('tuple : LPAR expr COMMA args RPAR', lambda x,y,z,w,v : (y,) + tuple(w)),
    ],
    ['NUMBER','STRING', 'VARNAME', 'TYPENAME',
    'EQUAL', 'COMMA','COLON', 'LPAR','RPAR','OP']
)

def ast_evaluatuator(src):
    return src

def eval_expr(src):
    return ast_evaluatuator(expr_parser(lexer(src)))


print(eval_expr("(42 + sqrt(42) * sqrt(42)) / 2"))
