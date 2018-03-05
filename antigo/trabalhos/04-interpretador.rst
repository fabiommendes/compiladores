Interpretador para Lispf_ck
===========================

Nesta tarefa faremos um interpretador simples de Lispf_ck. Utilizaremos a mesma
linguagem definida no trabalho anterior, mas agora faremos um interpretador em
Python para executar programas em Lispf_ck. 

Você deve reutilizar o lexer/parser do trabalho anterior (se desejar utilizar
a implementação de outro colega, atribua o crédito. O lexer/parser não será 
avaliado nesta atividade). Basicamente o parser irá retornar uma árvore 
sintática na forma de listas. Seu programa deve ser capaz de executar o código
representado por estas listas:

Exemplo
-------

Considere o programa::

    (do read inc (loop print (add 2)))

O parser deve ser capaz de retorna a seguinte estrutura de listas::

    program = ['do', 'read', 'inc', ['loop', 'print', ['add', 2]]]
  
O seu interpretador deve ser capaz de ler a lista e executar os comandos nela.
Crie uma função chamada `eval` que recebe uma lista e executa os comandos 
contidos na mesma.


Lispf_ck
--------

O modelo de execução de Lispf_ck é baseado na existência de uma lista 
potencialmente infinita para a direita que é utilizada como área de memória.
O programa começa a execução na célula mais a esquerda e utiliza os comandos 
`right` e `left` para mover o cursor na fita. 

Qualquer acesso antes da posição 0 é considerado um erro. Se tentarmos acessar 
uma célula não-existente à esquerda, ela deve criar uma nova célula (use 
list.append(0)) para isso. Os valores de cada célula iniciam em 0 e estão no 
intervalo 0-255. Utilizamos a matemática modular de forma que, por exemplo, 
255 + 1 == 0.

Comece implementando suporte aos comandos básicos, como o programa abaixo que
realiza a soma de dois números::

    (do 
        ; Inicializa os números 2 e 3
        (add 3) 
        right 
        (add 2)
        left

        ; Realiza a soma
        (loop
            dec right inc left
        )

        ; Converte para ascii e imprime
        right 
        (add 48)
        print
    )


A parte mais complicada do interpretador de Lispf_ck é permitir que novas 
funções sejam definidas. 


Tarefa
------

* Crie um interpretador que aceite os comandos básicos de brainf_uck (inc, dec, 
  right, left, print, read e loop) e os comandos adicionais do, do-after e 
  do-before. 
* Seu interpretador deve ler um arquivo .lf em Lispf_ck e executar os comandos.
* O trabalho deve ser feito em duplas.
* A avaliação é binária.
* O trabalho vale 5% da nota final.
* Se o interpretador suportar a definição e execução de funções (comando def), 
  o valor do trabalho sobe para 7%.