import ox


# Regras para montar o lexer
token_rules = [
    ('SELECT', r'SELECT'),
    ('WHATEVER', r'.+'),
    # ...,
]


# Regras para montar o parser
parser_rules = [
    ('sql : SELECT WHATEVER', lambda x, y: {x: y}), 
    # ..., 
]


# Criamos o parser e o lexer
lexer = ox.make_lexer(token_rules)
parser = ox.make_parser(parser_rules, tokens=[x for (x, y) in token_rules])


# Testamos em algums exemplos
examples = [
    'SELECT name FROM users;',
    'SELECT * FROM users;',
    'SELECT username, password FROM users WHERE username = password;',
]

results = [
    {'SELECT': ['name'], 'FROM': 'users'},
    {'SELECT': None, 'FROM': 'users'},
    {'SELECT': ['username', 'password'], 'FROM': 'users', 'WHERE': ['=', 'username', 'password']},
]

for i, example, expected in zip(range(3), examples, results):
    print('EXEMPLO', i + 1)
    tokens = lexer(example)
    print('Tokens:', tokens)

    ast = parser(tokens)
    print('Ast:', ast)
    print('Correto?', ast == expected)
    if ast != expected:
        print('Esperado:', expected)
    print()