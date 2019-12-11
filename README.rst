=======
Avisos!
=======

* `Avaliação 360 e envio do trabalho final <https://docs.google.com/forms/d/e/1FAIpQLSfG9lAnV84mazFPgqOi9oxvBMiaE9CWhfWrP-_fnlym8sbnaA/viewform?usp=sf_link>`_
* `Envio do trabalho de lispy <https://docs.google.com/forms/d/e/1FAIpQLSdSkhlcFpR2hRlagztN7hqRC5l1l4mz7rKhM92hqc4h9xgxBw/viewform?usp=sf_link>`_
* `Notas <https://github.com/fabiommendes/compiladores/blob/master/notas.pdf>`_

==============
Compiladores 1
==============

Este é o Git da disciplina Fundamentos de Compiladores. Aqui será compartilhado o material produzido em sala de aula assim como tarefas, wiki e discussões. Este arquivo contêm informações básicas sobre a disciplina e o plano de ensino do semestre.


Informações básicas
===================

Curso: 
    Engenharia de Software
Professor: 
    Fábio Macêdo Mendes
Disciplina: 
    Compiladores 1
Semestre/ano: 
    02/2019
Carga horária: 
    60 h
Créditos: 
    04


Ementa
======

* Introdução
* Autômatos
* Organização e estrutura de compiladores e interpretadores.
* Análise léxica.
* Expressões Regulares
* Análise sintática.
* Gramáticas Regulares e Livres de Contexto
* Estruturas de Dados e representação interna de código-fonte.
* Análise semântica.
* Geração de código.
* Máquinas abstratas e ambientes de tempo de execução.
* Projeto de Compiladores.
* Compiladores, Interpretadores e Parsers na Engenharia de Software.


Horário das aulas e atendimento
===============================

Aulas teóricas e de exercícios: segundas e sextas-feiras às 14h
Atendimento e monitoria: a definir


Informações importantes
========================

Este curso utiliza GitHub + Github Classroom e o Google classroom para gerenciar o curso. A comunicação com a turma é feita através do Google Classroom ou por issues no repositório do Github. Habilite a funcionalidade "Watch" no repositório para receber notificações sobre atualizações.

Google Classroom:
    http://classroom.google.com/ - Código de inscrição: xsu58o9
Github:
    http://github.com/fabiommendes/compiladores/


Critérios de avaliação
======================

Cada aluno será avaliado com uma nota numérica onde a conversão entre a pontuação e a menção final é feita da forma usual: 9,0pts+: SS, 7,0pts+: MS, 5,0pts+: MM, 3,0pts+: MI e < 3,0 pts II. A distribuição de pontos ao longo do curso segue a fórmula:

+---------------------+-----+
| Provas              | ??% |
+---------------------+-----+
| Exercícios e testes | ??% |
+---------------------+-----+
| Presença em aula    | ??% |
+---------------------+-----+
| Projeto final       | ??% |
+---------------------+-----+

As regras de cálculo da nota final serão definidas coletivamente.

A turma será dividida em "coaches" e "trainees", onde os primeiros são alunos matriulados que estão no final do curso e serão responsáveis por coordenar um grupo de trainees no desenvolvimento de um produto de software.


Prova substitutiva e faltas
---------------------------

As regras para prova substitutiva serão definidas coletivamente.

O aluno pode faltar até 7 vezes em um semestre. Faltas com justificativa médica não serão abonadas, exceto em casos excepcionais. Os alunos reprovados por falta ficarão com uma menção igual a SR.


Código de ética e conduta
-------------------------

Algumas avaliações serão realizadas com auxílio do computador no laboratório de informática. Todas as submissões serão processadas por um programa de detecção de plágio. Qualquer atividade onde for detectada a presença de plágio será anulada sem a possibilidade de substituição. Não será feita qualquer distinção entre o aluno que forneceu a resposta para cópia e o aluno que obteve a mesma.

As mesmas considerações também se aplicam às provas teóricas e atividades entregues no papel.


Prepare-se
==========

O curso utiliza alguns pacotes e ferramentas para os quais cada estudante deverá providenciar a instalação o mais cedo o possível. O curso requer Python 3.6+ com alguns pacotes instalados:

* Pip: Gerenciador de pacotes do Python (sudo apt-get install python3-pip)
* Jupyter notebook/nteract/Google colab: Ambiente de programação científica (https://nteract.io)
* Lark (pip3 install lark-parser --user): Biblioteca de parsing para Python. (note a **ausência** do sudo no comando!)
* Docker: cria ambientes completamente isolados para teste e validação (sudo apt-get install docker.io)

Já que vamos utilizar o Python, vale a pena instalar as seguintes ferramentas:

* virtualenvwrapper: isola ambientes de desenvolvimento para não contaminar o resto do seu sistema
* flake8: busca erros de estilo e programação no seu código
* black: corrige estes erros automaticamente
* pytest, pytest-cov: criação de testes unitários
* Editores de código/IDE: Utilize o seu favorito. Caso precise de uma recomendação, seguem algumas:
 * PyCharm Educacional - IDE com ótimos recursos de introspecção e refatoração, mas adora memória RAM. Possui uma versão livre e uma versão profissional paga, mas que é gratuita para estudantes.
 * VSCode - um bom meio termo entre uma IDE e um editor de código leve. Criado para Javascript, mas possui bons plugins para Python e várias outras linguagens.
 * Vi/Vim - herança dos anos 70 que nunca morre ;) Instale os plugins para Python.

DICA: em todos os casos, prefira instalar os pacotes Python utilizando o apt-get ou o mecanismo que sua distribuição fornece e somente se o pacote não existir, instale-o utilizando o pip. Se utilizar o pip, faça a instalação de usuário utilizando o comando ``pip3 install <pacote> --user`` (NUNCA 
utilize o sudo junto com --user e evite instalar globalmente para evitar problemas futuros com o APT). Melhor ainda é isolar o ambiente utilizado em cada disciplina utilizando uma ferramenta como o Virtualenv ou o [Poetry](https://poetry.eustace.io).


Linux e Docker
--------------

Os comandos de instalação acima assumem uma distribuição de Linux baseada em Debian. Não é necessário instalar uma distribuição deste tipo e você pode adaptar os comandos para o gerenciador de pacotes da sua distribuição (ou o Brew, no caso do OS X). Apesar do Linux não ser necessário para executar a maior parte das tarefas, é altamente recomendável que todos instalem o Docker para compartilharmos ambientes de desenvolvimento previsíveis (por exemplo, eu testarei as submissões em containers específicos que serão compartilhados com a turma). É possível executar o Docker em ambientes não-Linux utilizando o Docker Machine ou o Vagrant. Deste modo, cada aluno deve providenciar a instalação do Docker e Docker Compose na sua máquina.


Bibliografia principal
----------------------

Dragon Book: Alfred V. Aho, Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman, Compilers: Principles, Techniques, and Tools, Pearson, 2006.
Structure and Interpretation of Computer Programs, Gerald Jay Sussman and Hal Abelson, MIT Press. (https://web.mit.edu/alexmv/6.037/sicp.pdf)


Cronograma de atividades
========================

+--------+-------+-----------------------------------------------------------+
| Semana | Data  |                           Aula                            |
+========+=======+===========================================================+
| 1      | 12/08 | Início das aulas – Apresentação do curso                  |
|        |       |                                                           |
|        |       | * Estrutura de linguagens naturais                        |
|        |       | * Linguagens artificiais                                  |
|        |       | * Linguagens de programação                               |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
|        | 14/08 | Gramáticas Generativas                                    |
|        |       |                                                           |
|        |       | * Gramáticas e regras de substituição                     |
|        |       | * Léxico vs sintaxe                                       |
|        |       | * Notação EBNF                                            |
|        |       | * Gerador de lero-lero                                    |
+--------+-------+-----------------------------------------------------------+
|        | 21/03 | Autômatos                                                 |
|        |       |                                                           |
|        |       | * Autômatos simples (DFA)                                 |
|        |       | * Resolvendo problemas simples (detecção de padrões)      |
|        |       | * Generalizando autômatos                                 |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
| 3      | 26/03 | Máquinas de Turing                                        |
|        |       |                                                           |
|        |       | * Máquina de Turing                                       |
|        |       | * Modelos de Computação                                   |
|        |       | * Linguagens "Turing completas"                           |
|        |       | * Brainf*ck                                               |
+--------+-------+-----------------------------------------------------------+
|        | 28/03 | Hierarquia de Chomsky                                     |
|        |       |                                                           |
|        |       | * Gramáticas vs. autômatos                                |
|        |       | * Sintaxe de linguagens livre de contexto                 |
|        |       | * Classificação de linguagens conhecidas                  |
|        |       | * Análise semântica                                       |
+--------+-------+-----------------------------------------------------------+
|        | ...   | ??                                                        |
|        |       |                                                           |
|        |       | * ...                                                     |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+


Obs.: O cronograma está sujeito a alterações.
