from collections import deque
from lark import Lark, InlineTransformer, Token

#
# Implementação de referência usando o Lark
#
grammar = r"""
?value : NUMBER -> number
       | BOOL   -> bool
       | "null" -> null
       | string
       | array
       | object

array  : "[" (value ("," value)*)? "]"
object : "{" (pair ("," pair)*)? "}"
pair   : string ":" value

string : STRING

STRING : /"[^"]*"/
NUMBER : /-?\d+(\.\d+)?/
BOOL   : /true|false/

%ignore /\s+/
"""


class JSONTransformer(InlineTransformer):
    number = float

    def bool(self, tk):
        return tk == "true"

    def null(self):
        return None

    def string(self, tk):
        return tk[1:-1]  # Remove as aspas

    def pair(self, key, value):
        return (key, value)

    def object(self, *pairs):
        return dict(pairs)

    def array(self, *args):
        return list(args)


grammar = Lark(grammar, start="value", transformer=JSONTransformer(), parser="lalr")
lex = grammar.lex


#
# Descida recursiva
#
JSON = object

def parse(src: str) -> JSON:
    """
    Lê uma string com JSON e retorna o objeto JSON correspondente.

    >>> parse('{"hello": "world!"}')
    {'hello': 'world!'}
    """
    
    tokens = deque(lex(src))
    tokens.append(Token("EOF", ""))
    value = parse_value(tokens)
    return value

def parse_value(tokens: deque) -> JSON:
    """
    Consome tokens e retorna
    """
    tk = tokens[0]

    if tk == "[":
        return parse_list(tokens)
    elif tk.type == "NUMBER":
        tokens.popleft()  # É necessário consumir o 1o token
        return float(tk)
    
    # Complete com as outras regras de objeto, STRING, BOOL e NULL
    # ...
    else:
        raise SyntaxError("token inesperada em lista: %r" % tk)


def parse_list(tokens: deque) -> list:
    """
    Consome tokens da lista (deque) e retorna uma lista.
    """
    # Exemplo de implementação...

    # Consome o colchete de abertura
    if tokens.popleft() != "[":
        raise SyntaxError

    # Verifica se corresponde à uma lista vazia
    elif tokens[0] == "]":
        tokens.popleft()
        return []

    # Consome os valores
    xs = []
    while True:
        # Lê valor e salva na saída
        x = parse_value(tokens)
        xs.append(x)

        # Verifica fim da lista e remove vírgula se necessário
        tk = tokens.popleft()
        if tk == "]":
            break
        elif tk != ",":
            raise SyntaxError("token inesperada em lista: %r" % tk)

    return xs


def parse_object(tokens: deque) -> dict:
    """
    Consome tokens da lista (deque) e retorna um dicionário.
    """

    ... # Provavelmente algo similar à implementação de object


def parse_pair(tokens: deque) -> (str, JSON):
    """
    Lê um par do tipo "chave": valor.

    Utilizado internamente na função parse_object
    """
    key = parse_value(tokens)
    value = ...
    return key, value


if __name__ == "__main__":
    from pprint import pprint

    src = "<not empty>"
    while src:
        src = input("JSON> ")
        if src:
            pprint(parse(src))
