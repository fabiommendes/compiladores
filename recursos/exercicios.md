# Expressões regulares

1) Considere linguagens com um alfabeto formado por 0's e 1's. Excreva uma expressão
regular para as seguintes situações

a) Strings que contêm exatamente 2 dígitos 1.
b) Strings que contêm até 2 dígitos 1.
c) Strings que contêm um número par de dígitos 1.
d) Strings que contêm um número ímpar de dígitos 1.
e) Strings que correspondem a números binários ímpares
f) Strings que correspondem a números binários que são potências de 2
g) Strings que correspondem a números binários diferentes de zero

Em cada caso, desenhe um diagrama que descreve o autômato correspondente a esta
expressão regular.


2) Dado a tabela de transição para um autômato de três estados {0, 1, 2} e que atua sobre
o alfabeto {a, b}, determine o diagrama de transições e a linguagem regular associada.

 S | a | b |
---+---+---+
 0 | 1 | 2 |
 1 | 2 | 1 |
 2 | 2 | 1 |
 
 
# Gramáticas livres de contexto

1) Uma linguagem definida como uma sequência de caracteres com n a's seguida pelo mesmo
número de b's **não** pode ser descrita por uma linguagem regular. No entanto, é possível
definí-la como uma linguagem livre de contexto. (a) Crie uma gramática EBNF (notação do Lark)
que define tal linguagem. (b) Desenvolva a árvore sintática concreta para a string "aaabbb"
de acordo com a linguagem proposta. (c) Modifique a gramática para aceitar apenas strings
com 2 ou mais repetições de a's e b's.

2) Considere a gramática que gera algumas frases em inglês:

```
sentence : subject verb object
subject  : article nounphrase
object   : article nounphrase
article  : "a" | "the"
nounphrase : noun
           | adjective noun

adjective : "big" | "small"
noun : "cat" | "dog"
verb : "eats" | "plays with"
```
a) Sugira 2 frases válidas diferentes de acordo com esta gramática.
b) Desenhe a árvore sintática concreta para as frases escolhidas.
c) Esta gramática **rejeita** a frase "big cat eats dog". Explique porquê e proponha
uma alteração na gramática que tornaria a frase válida.

3) Crie uma gramática que descreva todas as expressões regulares válidas no alfabeto {a, b}.
(Considere a notação teória de expressões regulares e não o conunto completo de regex em Python).

4) Crie uma gramática que descreva todos palíndromos no alfabeto {a, b} (palíndromos são palavras lidas da mesma forma de trás para frente).

5) Crie uma gramática para expressões matemáticas que envolvam números, variáveis e 
as operações de soma, subtração, multiplicação, divisão e exponenciação. Tome cuidado com a precedência
dos operadores e as regras corretas de associatividade.


