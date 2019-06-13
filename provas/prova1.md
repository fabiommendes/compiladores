# Prova de Compiladores
## Data: 13/06/2019
## Expressões regulares e gramáticas livres de contexto

---

### Expressões regulares I (2,0)

Considere a tabela de transição para um autômato de três estados {S0, S1, S2, SE} 
que atua sobre um alfabeto de apenas dois símbolos {a, b}. 

| Estado | a  | b  |
|--------|----|----|
| S0     | S1 | S2 |
| S1     | SE | S2 |
| S2     | S1 | SE | 
| SE     | SE | SE |

Consideramos que apenas S2 é um estado terminal válido, responda às questões:

a) Desenhe o diagrama de transições para a linguagem
b) Escreva qual/quais é a menor expressão válida para esta linguagem e construa mais 3 exemplos válidos.
c) Generalize a partir destes exemplos e apresente uma expressão regular que descreva esta linguagem.


### Expressões regulares II (2,0)

Repita as mesmas considerações da questão anterior, mas agora considerando que 
S1 e S2 são estados terminais válidos.


### Gramáticas livres de contexto (2,5)

Considere uma gramática que gera previsões de horóscopo:

```
frase    : sujeito VERBO objeto
sujeito  : ASTRO "em" SIGNO
objeto   : acontecimento CONTEXTO
acontecimento : INTENSIFICADOR_F? ACONTECIMENTO_F
              | INTENSIFICADOR_M? ACONTECIMENTO_M
         
ASTRO : /Mercúrio|Vênus|Lua|Marte|Júpiter|.../
SIGNO : /Capricórnio|Libra|Touro|Aquário|.../ 
VERBO : /indica|sugere|aponta/
ACONTECIMENTO_F : /novidades|alegrias/
ACONTECIMENTO_M : /problemas|bons presságios/
INTENSIFICADOR_F : /muitas|poucas/
INTENSIFICADOR_M : /muitos|poucos/
LUGAR : /no trabalho|na vida amorosa|nas relações familiares/
```
a) Sugira 2 frases válidas diferentes de acordo com esta gramática.
b) Desenhe a árvore sintática concreta para uma das frases escolhidas.
c) Esta gramática descreve uma linguagem regular? Explique.


### Gramáticas livres de contexto (programação) (3,5)

Crie uma gramática utilizando o Lark que identifica expressões regulares para
um alfabeto de apenas três letras a, b e c. Não é necessário suportar nenhuma
extensão às expressões regulares tradicionais como os operadores `+`, `?`, `[]`, etc. 
A gramática também pode ser insensível a espaços.

Seguem alguns exemplos de expressões válidas que contemplam todas as operações 
necessárias:

```
abc
a(bc)*
a(a|c)(bb*)
```

Lembre-se de implementar a procedência corretamente: o operador de produto estrela 
`*` possui a maior precedência, seguido do operador concatenação e, por último,
o operador de alternativas `|`. Assim, a interpretação correta de `ab*|c` é 
dada por `(a(b*))|c`.

Scaffold:

```python
from lark import Lark, InlineTransformer
from pprint import pprint

#
# Gramática para expressões regulares
#
grammar = r"""
?start : expr

?expr  : rule

?rule  : single

?single : atom

?atom   : letter

letter  : LETTER

LETTER  : /a|b|c/

%ignore /\s+/
"""
parser = Lark(grammar, parser='lalr')

#
# Transforma para S-expressions
#
class Transformer(InlineTransformer):
    def alt(self, a, b):
        if isinstance(b, tuple) and b[0] == 'alt':
            return ('alt', a, *b[1:])
        return ('alt', a, b)

    def concat(self, a, b):
        if isinstance(b, tuple) and b[0] == 'concat':
            return ('concat', a, *b[1:])
        return ('concat', a, b)

    def power(self, a):
        return ('power', a)

    def letter(self, c):
        return str(c)


transformer = Transformer()

#
# Testes
#
examples = {
    'a': 'a',
    'a|b': ('alt', 'a', 'b'),
    'ab': ('concat', 'a', 'b'),
    'abc': ('concat', 'a', 'b', 'c'),
    'a*': ('power', 'a'),
    'ab*': ('concat', 'a', ('power', 'b')),
    'a|bc*': ('alt', 'a', ('concat', 'b', ('power', 'c'))),
    'ab|c(ab*)*|a': ('alt',
        ('concat', 'a', 'b'),
        ('concat', 'c', ('power', ('concat', 'a', ('power', 'b')))),
        'a'),
}

for expr, sexpr_ in examples.items():
    print('\n', '-' * 40, sep='')
    
    print('Expressão:', expr)
    
    print('\nLark:')
    print(parser.parse(expr).pretty())
    
    print('S-Expr')
    sexpr = transformer.transform(parser.parse(expr))
    pprint(sexpr)
    
    assert sexpr == sexpr_, 'esperado ' + str(sexpr_)

print('\n\nTodos testes passaram. PARABÉNS!')
```