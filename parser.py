from lark import Lark, InlineTransformer
from  pprint import pprint

grammar = r"""
programa : (atrib | expr)* 

atrib : NOME "=" expr

?expr  : expr /[+-]/ termo  -> binop
       | termo

?termo : termo /[*\/]/ pow  -> binop
       | pow

?pow   : atom "^" pow       -> binop
       | atom
      
      
?atom  : NUMERO        -> numero
       | NOME          -> nome
       | "(" expr ")"
      
      
NUMERO : /\d+(\.\d+)?/ 
NOME   : /[a-zA-Z]\w*/
%ignore /\s+/
""" 

lark = Lark(grammar, start="programa")


class CalcTransformer(InlineTransformer):
    def numero(self, tk):
        return float(tk)

    def nome(self, tk):
        return str(tk)

    def binop(self, left, op, right):
        return (str(op), left, right)

    def atrib(self, nome, valor):
        return ("=", str(nome), valor)

    def programa(self, *args):
        return ("!", *args)


def parse(src):
    tree = lark.parse(src)
    calc_transformer = CalcTransformer()
    return calc_transformer.transform(tree)

    
def eval_ast(ast, contexto):
    if isinstance(ast, float):
        return ast
    elif isinstance(ast, str):
        return contexto[ast]
    
    raiz, *args = ast
    if raiz ==  '+':
        x, y = args
        return eval_ast(x, contexto) + eval_ast(y, contexto)
    elif raiz ==  '-':
        x, y = args
        return eval_ast(x, contexto) - eval_ast(y, contexto)
    elif raiz ==  '*':
        x, y = args
        return eval_ast(x, contexto) * eval_ast(y, contexto)
    elif raiz ==  '/':
        x, y = args
        return eval_ast(x, contexto) / eval_ast(y, contexto)
    elif raiz ==  '^':
        x, y = args
        return eval_ast(x, contexto) ** eval_ast(y, contexto)
    elif raiz == '=':
        x, y =  args
        value = eval_ast(y, contexto)
        contexto[x] = value
        return value
    elif raiz ==  '!':
        value = None
        for expr in  args:
            value = eval_ast(expr, contexto)
        return value
    else:
        raise RuntimeError(f'expressão inválida: {raiz!r}')


src = """
x = 40
y = 2
x + z * (y + 1)
"""
ast = parse(src)
pprint(ast)
print(eval_ast(ast, {'z': 2.0, 'pi': 3.14, 'e': 2.71}))