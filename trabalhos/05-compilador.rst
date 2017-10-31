Compilador de Lispf_ck
======================

Nesta tarefa faremos um compilador de Lispf_ck para Brainf_uck. Seu compilador
deve ler um programa em Lispf_ck, por exemplo:: 

    (do read inc (loop print (add 2)))

e produzir o programa equivalente em brainf_uck::

    .+[.++]

O parser deve ser capaz de executar a especificação de  Lispf_ck completa, 
incluindo a definição de funções.

Tarefa
------

* Seu interpretador deve ler um arquivo .lf em Lispf_ck e gravar um arquivo 
  com o código fonte brainf_uck equivalente.
* O trabalho deve ser feito em duplas.
* A avaliação é binária.
* O trabalho vale 5% da nota final.
* Os alunos podem optar por *não* implementar suport a funções, o que faz o 
  valor da tarefa cair para 3% da nota total.
  