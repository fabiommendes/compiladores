class CalcParser:
    def __init__(self, src):
        self.src = src

    def parse(self):
        tokens = self.src.split()
        return self.parse_expr(tokens)

    def eval(self):
        ast = self.parse()
        return eval_ast(ast)

    def parse_expr(self, tokens):
        term = self.parse_term(tokens)
        if not tokens:
            return term
        elif tokens[0] == '+':
            tokens.pop(0)
            return ['+', term, self.parse_expr(tokens)]
        elif tokens[0] == '-':
            tokens.pop(0)
            return ['-', term, self.parse_expr(tokens)]
        else:
            return term

    def parse_term(self, tokens):
        atom = self.parse_atom(tokens)
        if not tokens:
            return atom
        elif tokens[0] == '*':
            tokens.pop(0)
            return ['*', atom, self.parse_term(tokens)]
        elif tokens[0] == '/':
            tokens.pop(0)
            return ['/', atom, self.parse_term(tokens)]
        else:
            return atom

    def parse_atom(self, tokens):
        if tokens[0].isdigit():
            return int(tokens.pop(0))
        elif tokens[0] == '(':
            tokens.pop(0)
            expr = self.parse_expr(tokens)
            if tokens.pop(0) != ')':
                raise SyntaxError
            return expr


def eval_ast(ast):
    if isinstance(ast, int):
        return ast
    op, x, y = ast
    if op == '+':
        return eval_ast(x) + eval_ast(y)
    elif op == '-':
        return eval_ast(x) - eval_ast(y)
    elif op == '*':
        return eval_ast(x) * eval_ast(y)
    elif op == '/':
        return eval_ast(x) / eval_ast(y)
    else:
        raise ValueError(op)


def parse(src):
    parser = CalcParser(src)
    return parser.parse()


def eval(src):
    parser = CalcParser(src)
    return parser.eval()


if __name__ == '__main__':
    while True:
        print(eval(input('expr: ')))
