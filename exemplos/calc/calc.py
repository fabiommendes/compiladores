import ox
import operator as op


OP_TO_FUNC = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}


lexer = ox.make_lexer([
    ('NUMBER', r'\d+(\.\d*)?'),
    ('TERM_OP', r'[*/]'),
    ('EXP_OP', r'[-+]'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)')
])


parser = ox.make_parser([
    ('expr : expr EXP_OP term', lambda x, op, y: (op, x, y)),
    ('term : term TERM_OP value', lambda x, op, y: (op, x, y)),
    ('expr : term', lambda x: x),
    ('term : value', lambda x: x),
    ('value : NUMBER', lambda x: ('atom', x)),
], ['NUMBER', 'TERM_OP', 'EXP_OP'])


def eval(ast):
    head, *tail = ast
    if head == 'atom':
        return float(tail[0])
    else:
        x, y = tail
        return OP_TO_FUNC[head](eval(x), eval(y))


if __name__ == '__main__':
    ox.parser.main(lexer, parser, eval)
