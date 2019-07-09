# Prova 2 - Compiladores
## Data: 9/07/2019
## Gramáticas livres de contexto e LL(1)


---

### Gramática LL(1)

A gramática abaixo representa a sintaxe de uma linguagem de programação. A notação
utiliza uma sintaxe inspirada no Lark, indicando o número de linhas em cada expressão,
além da adição de produções vazias "epsilon".

```
1. expr  : OP expr expr
2.       | FN expr
3.       | N
4.       | "[" items "]"
5. items : expr tail
6. tail  : items
7.       | epsilon 

// Terminais
OP: /[-+*/]/
FN: /[a-z]+/
N: /\d+(\.\d*)/
```

1) (1pts) Calcule o conjunto First(e) para cada regra da gramática e para cada
não-terminal.
2) (1.5pts) Calcule o conjunto Follow(e) para todos os não-terminais.
3) (1.5pts) Monte a tabela de parsing para esta gramática para o algoritmo LL(1).
4) (2pts) Faça o procedimento completo de parsing da expressão segundo a
tabela de parsing do LL(1) "max [+ 1 2 3]".
Você deve mostrar a lista de regras aplicadas no processo de redução da lista de
tokens.


### Gramáticas livre de contexto

A gramática da questão anterior representa uma calculadora prefixa (o operando
aparece antes dos operadores). Os argumentos básicos podem ser números (ex.: 1, 
2, 3.14) ou vetores (ex.: [1 2], [1], [1 2 3]).

1) (1,5) Modifique a gramática para virar uma calculadora posfixa e mostre a árvore 
sintática concreta da expressão "[1 2] [2 3 * 5] +"
2) (2,5) Separe as regra de números e vetores e modifique a regra para operadores
binários para que a gramática garanta que apenas as seguintes combinações 
sejam possíveis:
```
    * Soma e adição: os dois argumentos devem ser do mesmo tipo (vetor ou escalar).
    * Multiplicação: os dois argumentos devem ser de tipos diferentes
    * Divisão: o primeiro argumento pode ser número ou vetor e o segundo um escalar.
```