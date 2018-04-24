import ox


#
# Lexer
#
lexer = ox.make_lexer([
    ('NUMBER', r'\d+(\.\d+)?'),
    ('STRING', r'"[^"]*"'),
    ('EQ', r'='),
    ('OP', r'([-+*/<>?@&$^~%][-+*/<>?@&$^~%=]*|==)'),
    ('COMMENT', r'\#[^\n]*'),
    ('LPAR', r'\('),
    ('RPAR', r'\)'),
    ('FNAME', r'[a-z]+'),
    ('COMMA', r'\,'),
])

tokens = ['NUMBER', 'OP', 'EQ', 'LPAR', 
          'RPAR', 'FNAME', 'COMMA']
