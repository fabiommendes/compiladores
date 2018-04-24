from functools import singledispatch
from .ir import Atom, FCall, Symbol


def generate_python_code(ir):
    """
    Converte a representação interna para uma 
    string de código Python.
    """
    return "print('hello world!')"


@singledispatch
def emmit_expr(expr):
    raise TypeError('invalid expression: %s' % expr)

emmit_expr.register(Atom)(lambda x: repr(x.value))
emmit_expr.register(Symbol)(lambda x: x.value)
# emmit_expr.register(FCall)(lambda x: '%s(%s)')

print(emmit_expr(FCall('add', [Name('x'), Atom(1)])))


def emmit_stmt(smtm):
    pass


x = lambda x: x? fib(x -1) + fib(x-2): 1