import ox


#
# Lexer
#
lexer_rules = [
    ('COMMENT', r'\#[^\n]*'),
    ('NUMBER', r'\d+(\.\d+)?'),
    ('STRING', r'"[^"]*"'),
    ('BOOL', r'true|false'),
    ('EQ', r'='),
    ('SEMICOLON', r';'),
    ('OP', r'([-+*/<>?@&$^~%][-+*/<>?@&$^~%=]*|==)'),
    ('LPAR', r'\('),
    ('RPAR', r'\)'),
    ('NAME', r'[a-z]+'),
    ('COMMA', r'\,'),
]
lexer_raw = ox.make_lexer(lexer_rules)
tokens = [x for x, _ in lexer_rules]
del tokens[0]  # remove a token de COMMENT 


def lexer(src):
    tokens = lexer_raw(src)
    return [tk for tk in tokens if tk.type != 'COMMENT'] 
