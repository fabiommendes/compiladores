import ox
from datetime import date


#
# Parser
#
def make_parser(lexer, tokens):
    parser = ox.make_parser([
        ("json : object", identity),
        ("json : array", identity),
        ("json : atom", identity),

        # Objects
        ("object : LBRACE RBRACE", lambda x, y: {}),
        ("object : LBRACE pairs RBRACE", lambda x, y, z: dict(y)),
        ("pairs  : pair COMMA pairs", lambda x, _, xs: [x, *xs]),
        ("pairs  : pair", lambda x: [x]),
        ("pair   : string COLON json", lambda x, _, y: (x, y)),

        # Arrays
        ("array : LBRACK RBRACK", lambda x, y: []),
        ("array : LBRACK items RBRACK", lambda x, y, z: y),
        ("items : json COMMA items", lambda x, _, xs: [x, *xs]),
        ("items : json", lambda x: [x]),

        # Terminals
        ("string : STRING", clean_string),
        ("atom : NUMBER", float),
        ("atom : KEYWORD", lambda x: keywords[x]),
        ("atom : string", identity),
    ], tokens)

    return lambda src: parser(lexer(src))


#
# Lexer
#
def make_lexer():
    lexer_rules = [
        ('STRING', r'"[^"\n]*(\\"[^"\n]*)*"'),
        ('NUMBER', r'[+-]?\d+(\.\d+)?'),
        ('KEYWORD', r'true|false|null'),
        ('LBRACE', r'\{'),
        ('RBRACE', r'\}'),
        ('LBRACK', r'\['),
        ('RBRACK', r'\]'),
        ('COLON', r'\:'),
        ('COMMA', r'\,'),
    ]

    lexer = ox.make_lexer(lexer_rules, which='simple')
    tokens = [tk for tk, _ in lexer_rules]
    return lexer, tokens


#
# Funções úteis
#
keywords = {'true': True, 'false': False, 'null': None}
identity = (lambda x: x)


def clean_string(x):
    return x[1:-1].replace('\\"', '"')


#
# Cria o parser
#
parse_json = make_parser(*make_lexer())

# Le e processa um arquivo JSON+
if __name__ == '__main__':
    import argparse
    from pprint import pprint

    parser = argparse.ArgumentParser(description='Processa arquivo .jsonp')
    parser.add_argument('file', help='caminho para arquivo')

    args = parser.parse_args()
    with open(args.file) as F:
        data = F.read()
        pprint(parse_json(data))
