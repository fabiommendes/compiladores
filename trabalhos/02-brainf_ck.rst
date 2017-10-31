Compilador de Brainf_ck
=======================

Brainf_ck é uma linguagem de programação esotérica criada especialmente para ter
o poder de computação de uma linguagem tradicional, com o menor compilador 
possível (veja https://en.wikipedia.org/wiki/Brainfuck, para uma definição 
detalhada).

O seu trabalho é criar um compilador de Brainf_ck para uma linguagem de 
programação séria de sua escolha: Python, C, Javascript, Haskell, Scala, etc 
(mas não vale Java nem PHP).  

Seu compilador pode ser escrito em Python e deve operar com o comando:

    $ python3 brainf_ck.py arquivo.bf -o saida.c

(Onde o arquivo de saída deve corresponder à linguagem de destino escolhida).


Dicas:
 
* Recomendo o uso da biblioteca "click" (http://click.pocoo.org/) para tratar 
  os argumentos da linha de comando. Outra opção muito boa é o módulo argparse 
  da biblioteca padrão.
* Se o formato do programa de saída for Python, é necessário uma biblioteca
  externa para realizar a função do getchar do C. Instale uma biblioteca 
  como a getch (https://pypi.python.org/pypi/getch) a partir do pip.


Entrega:

* O trabalho deve ser feito em duplas.
* Cada dupla deve criar um repositório no Github com o compilador, um README e 
  alguns exemplos.
* Não esqueçam de escrever o nome e a matrícula no README.
* O compilador deve funcionar e produzir código válido para todos os exemplos 
  disponibilizados neste repositório.
* A avaliação é binária.
* A data de entrega é 31/10.
* O trabalho vale 7% da nota final.


Desafios que não valem ponto:

* Adicione um parâmetro --run que faça com que o compilador execute diretamente
  o código de destino
* Se o destino for uma linguagem compilada como C, chame o compilador e 
  execute o resultado (dica: veja o módulo subprocess da biblioteca padrão)
* Faça o compilador aceitar entradas em Ook! ou alguma outra variante de brainf_ck
* Invente a sua própria variante!
* Faça um "easter-egg" que realiza a compilação para Ook! (https://esolangs.org/wiki/Ook!)
