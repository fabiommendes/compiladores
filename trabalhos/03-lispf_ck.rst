Parser para Lispf_ck
====================

Lispf_ck é uma variante de Brainf_ck+- que utiliza a sintaxe do LISP e a 
semântica do Brainf_ck com alguns recursos adicionais.

Semântica:

Lispf_ck é inspirado no LISP, que é uma linguagem funcional com uma sintaxe que
representa código como listas. Os elementos da lista são separados por 
espaços e geralmente o primeiro elemento representa uma função e os elementos 
seguintes são os argumentos aplicados a esta função. Somar dois números em LISP 
portanto seria feito pelo comando: "(+ 1 2)". Ou seja, a função "+" aplicada aos 
dois argumentos "1" e "2".

Lispf_ck é bem mais limitada e não possui todos os recursos do LISP (nem mesmo
a função "+" do exemplo. Um programa básico em Lispf_ck possui a forma

    (do read inc (loop print dec))

sendo equivalente ao programa Brainf_ck ",+[.-]". Como podemos ver, Brainf_ck é 
mais compacto, mas o Lispf_ck é mais legível.

A lista de equivalência entre os comandos é:

    [...]: (loop ...)
    >: right
    <: left
    +: inc
    -: dec
    .: print
    ,: read

A função "do" simplesmente executa linearmente cada comando na lista de 
argumentos.


Extensões
---------

add/sub:

Lispf_ck aceita incrementos/decrementos maiores que 1. Ao invés de utilizar 
"inc inc", por exemplo, use "(add 2)". 


def:

Utilizamos o comando "def" para definir uma função. A função def recebe três 
argumentos, sendo que o primeiro é um nome, o segundo é uma lista de argumentos
e o terceiro é o corpo da função. A função inc, por exemplo, poderia ser 
definida a partir de add como sendo::

    (def inc () (add 1))

do-after/do-before:

Os comandos do-after e do-before recebem um comando e uma lista de comandos e
executam a lista adicionando o primeiro comando depois ou antes de cada comando
na lista. Exemplo::

    (do-after print (foo bar))

é a mesma coisa que::

    (do (do foo print) (do bar print))

O comando do-before simplemente inverte a ordem dos argumentos internos::

    (do-before print (foo bar))
    (do (do print foo) (do print bar))

Se um programa definir funções, é necessário incluí-lo dentro de uma lista 
"do" como no exemplo abaixo::

    ; Ponto e vírgula define comentários
    (do
        ; Funções
        (def inc2 () (add 2))
        (def to-zero () (loop dec))
        (def to-number (n) (do to-zero (add n))
        
        ; Programa
        (do (to-number 97) print)  ; imprime 97 ('a' na tabela ascii)
    )

LISP não é sensível a indentação.


Tarefa
------

Sua tarefa é fazer um lexer + parser de Lispf_ck. Para realizar esta tarefa,
você pode utilizar o Ox ou o PLY ou fazer tudo em Python puro.

Entrega:

* Seu parser deve ler um arquivo .lf em Lispf_ck e imprimir a árvore sintática
  correspondente. Se você estiver utilizando listas ou tuplas para representar
  as árvores, considere utilizar a função pprint do módulo pprint para imprimir 
  as listas de uma forma legível. 
* O trabalho deve ser feito em duplas.
* A avaliação é binária.
* O trabalho vale 5% da nota final.


Notas:

* Não é necessário implementar nem um compilador nem um interpretador. Basta
  criar as árvores sintáticas.
* Talvez o modo mais natural de representar as árvores sintáticas de uma 
  linguagem como o LISP é utilizando listas ou tuplas.
