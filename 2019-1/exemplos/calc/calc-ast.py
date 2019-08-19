import ox
import operator as op


lexer_rules = [
    ('NUMBER', r'\d+'),
    ('ADD', r'\+'),
    ('SUB', r'\-'),
    ('MUL', r'\*'),
    ('DIV', r'\/'),
    ('LPAR', r'\('),
    ('RPAR', r'\)'),
    ('VAR', r'[a-zA-Z_]+')
]
lexer = ox.make_lexer(lexer_rules)
tokens = [x for x, _ in lexer_rules]

binop = (lambda x, op, y: (op, x, y))
parser = ox.make_parser([
    ('expr : term ADD expr', binop),
    ('expr : term SUB expr', binop),
    ('expr : term', lambda x: x),
    
    ('term : atom MUL term', binop),
    ('term : atom DIV term', binop),
    ('term : atom', lambda x: x),
    
    ('atom : NUMBER', int),
    ('atom : VAR', lambda x: ('var', x)),
    ('atom : LPAR expr RPAR', lambda x, y, z: y),
], tokens)


def find_vars(ast, vars=()):
    if not isinstance(ast, tuple):
        return set()
    head, *tail = ast
    if head == 'var':
        return {tail[0], *vars}
    
    result = set()
    for elem in tail:
        result.update(find_vars(elem))
    return result

FUNCTIONS = {'+': op.add, '-': op.sub, 
             '*': op.mul, '/': op.truediv}

def eval_ast(ast, ctx):
    if not isinstance(ast, tuple):
        return ast

    head, *tail = ast
    if head == 'var':
        return ctx[tail[0]]
    else:
        args = (eval_ast(x, ctx) for x in tail)        
        func = FUNCTIONS[head]
        return func(*args)


if __name__ == '__main__':
    ast = parser(lexer(input('expr: ')))
    free_vars = find_vars(ast)
    ctx = {x: int(input(x + ': ')) 
           for x in free_vars}

    print('result:', eval_ast(ast, ctx))
    print('ast:', ast)