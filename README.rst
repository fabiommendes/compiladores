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
    01/2019
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

Aulas teóricas e de exercícios: terças e quintas-feiras às 14h 
Atendimento e monitoria: a definir


Informações importantes
========================

Este curso utiliza GitHub + Github Classroom e o Google classroom para gerenciar o curso. A comunicação com a turma é feita através do Google Classroom ou por issues no repositório do Github. Habilite a funcionalidade "Watch" no repositório para receber notificações sobre atualizações.

Google Classroom:
    http://classroom.google.com/ - Código de inscrição: xsu58o9
Github:
    http://github.com/fabiommendes/compiladores/
Github Classroom:
    http://github.com/fga-compiladores/ - Link de inscrição: https://classroom.github.com/a/0FZLKsXp


Critérios de avaliação
======================

Cada aluno será avaliado com uma nota numérica onde a conversão entre a pontuação e a menção final é feita da forma usual: 9,0pts+: SS, 7,0pts+: MS, 5,0pts+: MM, 3,0pts+: MI e < 3,0 pts II. A distribuição de pontos ao longo do curso segue a fórmula:

+------------------------+-----+
| Prova 1                | 20% |
+------------------------+-----+
| Prova 2                | 20% |
+------------------------+-----+
| Exercícios individuais | 20% |
+------------------------+-----+
| Testes e trabalhos     | 40% |
+------------------------+-----+

As datas das provas estão indicadas no plano de ensino. Os testes serão resolvidos em grupos de tamanho e composição variávies (inclusive individuais) e consistem em tarefas esporádicas realizadas durante a aula. A data dos testes e o respectivo método de avaliação serão divulgados com uma aula de antecedência.


Desafios
--------

O aluno poderá fazer algumas tarefas opcionais chamados "épicos" que ajudam na nota final. Os `épicos <epicos.rst>` são avaliados em menção (MI, MM, MS, SS), que correspondem respectivamente a (25%, 50%, 75%, 100%) de sua nota total. A nota do épico pode ser utilizada de duas maneiras:

* Como valor mínimo para a nota final do semestre
* Como complemento à nota: NF' = NF + NE / 2 * (1 - NF/10); NE = nota do épico e NF = nota final


Prova substitutiva e faltas
---------------------------

O curso não inclui prova substitutiva. Caso o aluno possua uma falta justificada no dia da primeira prova, deverá apresentar um comprovante na aula seguinte à prova ou quando terminar a licença médica. Esta justificativa não abona falta, mas dá direito ao aluno utilizar a segunda prova como prova substitutiva. 

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
* DrRacket: IDE e interpretador de Scheme (e outros sabores de Lisp)

Já que vamos utilizar o Python, vale a pena instalar as seguintes ferramentas:

* virtualenvwrapper: isola ambientes de desenvolvimento para não contaminar o resto do seu sistema
* flake8: busca erros de estilo e programação no seu código
* black: corrige estes erros automaticamente
* pytest, pytest-cov: criação de testes unitários
* Editores de código/IDE:
    Utilize o seu favorito. Caso precise de uma recomendação, seguem algumas:
    
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

Structure and Interpretation of Computer Programs, Gerald Jay Sussman and Hal Abelson, MIT Press. (https://web.mit.edu/alexmv/6.037/sicp.pdf)
Dragon Book: Alfred V. Aho, Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman, Compilers: Principles, Techniques, and Tools, Pearson, 2006. 


Cronograma de atividades
========================

+--------+-------+-----------------------------------------------------------+
| Semana | Data  |                           Aula                            |
+========+=======+===========================================================+
| 1      | 14/03 | Início das aulas – Apresentação do curso                  |
|        |       |                                                           |
|        |       | * Estrutura de linguagens naturais                        |
|        |       | * Linguagens artificiais                                  |
|        |       | * Linguagens de programação                               |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
| 2      | 19/03 | Lispy                                                     |
|        |       |                                                           |
|        |       | * Introdução ao Scheme (http://norvig.com/lispy.html)     |
|        |       | * Etapas da compilação                                    |
|        |       | * Interpretadores                                         |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
|        | 21/03 | Introdução ao Scheme                                      |
|        |       |                                                           |
|        |       | * Sintaxe e ferramentas da linguagem                      |
|        |       | * Procedimentos e abstrações                              |
|        |       | * Resolvendo problemas simples                            |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
| 3      | 26/03 | Iteração, recursão e funções de alta ordem                |
|        |       |                                                           |
|        |       | * Iteração vs. recursão                                   |
|        |       | * Recursão de cauda                                       |
|        |       | * Funções como valores                                    |
|        |       | * Lambdas e closures                                      |
+--------+-------+-----------------------------------------------------------+
|        | 28/03 | Estruturas de dados e listas                              |
|        |       |                                                           |
|        |       | * Função "cons"                                           |
|        |       | * Criando novas estruturas de dados com cons              |
|        |       | * Listas em Lisp                                          |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
| 4      | 02/04 | Revisitando Lispy                                         |
|        |       |                                                           |
|        |       | * Sintaxe adicional: booleanos, strings                   |
|        |       | * Análise semântica                                       |
|        |       | * Recursão de cauda                                       |
|        |       | * Macros                                                  |
+--------+-------+-----------------------------------------------------------+
|        | 04/04 | **Avaliação: Scheme**                                     |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
| 5      | 09/04 | Expressões regulares                                      |
|        |       |                                                           |
|        |       | * Ortografia e léxico de uma linguagem                    |
|        |       | * Linguagens regulares                                    |
|        |       | * Expressões regulares em Python                          |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
|        | 11/04 | Laboratório de regex: chatbot                             |
|        |       |                                                           |
|        |       | * Detecção de padrões                                     |
|        |       | * Resposta a padrões                                      |
|        |       | * Usos de expressões regulares e API Python               |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
| 6      | 16/04 | Análise léxica                                            |
|        |       |                                                           |
|        |       | * Tokens                                                  |
|        |       | * Implementando um analizador léxico                      |
|        |       | * Analizador léxico                                       |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
|        | 18/04 | Léxico de linguagens de programação                       |
|        |       |                                                           |
|        |       | * Exemplos em Python e Scheme                             |
|        |       | * Definição de tokens                                     |
|        |       | * Precedência de expressões regulares no tokenizador      |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
| 7      | 23/04 | Limites de expressões regulares                           |
|        |       |                                                           |
|        |       | * Aninhamento e recursividade                             |
|        |       | * Análise de estado                                       |
|        |       | * Expressão regular como autômato                         |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
|        | 25/04 | **Avaliação: Expressões regulares**                       |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
| 8      | 30/04 | Análise sintática                                         |
|        |       |                                                           |
|        |       | * Gramática                                               |
|        |       | * Especificação de regras gramaticais                     |
|        |       | * Hierarquia de linguagens                                |
|        |       | * Sintaxe vs semântica                                    |
+--------+-------+-----------------------------------------------------------+
|        | 02/05 | Laboratório de análise sintática: Gerador de lero lero    |
|        |       |                                                           |
|        |       | * Formalização de uma gramática                           |
|        |       | * Produções válidas                                       |
|        |       | * Gerador de textos aleatórios                            |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
| 9      | 07/05 | Gramáticas livres de contexto                             |
|        |       |                                                           |
|        |       | * Regras de produção                                      |
|        |       | * Lark                                                    |
|        |       | * Calculadora                                             |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
|        | 09/05 | Laboratório: JSON                                         |
|        |       |                                                           |
|        |       |                                                           |
|        |       | * Gramática como autômato                                 |
|        |       | * Separação entre a análise léxica e sintática            |
|        |       | * Implementação do JSON em Ox                             |
+--------+-------+-----------------------------------------------------------+
| 10     | 14/05 | Árvores sintáticas e representação de código              |
|        |       |                                                           |
|        |       | * Árvores concretas e abstratas                           |
|        |       | * S-expressions                                           |
|        |       | * Classes                                                 |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
|        | 16/05 | Laboratório: Calculadora avançada                         |
|        |       |                                                           |
|        |       | * Operadores e expressões                                 |
|        |       | * Representação intermediária                             |
|        |       | * Precedência                                             |
|        |       | * Análise semântica                                       |
+--------+-------+-----------------------------------------------------------+
| 11     | 21/05 | Emissão de código                                         |
|        |       |                                                           |
|        |       | * Representação intermediária                             |
|        |       | * Geração de código                                       |
|        |       | * Controle de formatação e indentação                     |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
|        | 23/05 | Autômatos                                                 |
|        |       |                                                           |
|        |       |                                                           |
|        |       | * Introdução a autômatos                                  |
|        |       | * Autômato determinístico finito                          |
|        |       | * Autômatos para linguagens regulares                     |
+--------+-------+-----------------------------------------------------------+
| 12     | 28/05 | *Não haverá aula*                                         |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
|        | 30/05 | **PROVA: Análise sintática e léxica**                     |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
| 13     | 04/06 | Descida recursiva                                         |
|        |       |                                                           |
|        |       | * Tipos atômicos (numerais, strings, etc)                 |
|        |       | * Símbolos                                                |
|        |       | * Operadores e delimitadores                              |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
|        | 06/06 | Parser LL                                                 |
|        |       |                                                           |
|        |       | * Chamada de função                                       |
|        |       | * Tradução para Python                                    |
|        |       | * Aninhamento                                             |
|        |       | * Declarações                                             |
+--------+-------+-----------------------------------------------------------+
| 14     | 11/06 | Hierarquia de Chomsky                                     |
|        |       |                                                           |
|        |       | * Modelos de computação                                   |
|        |       | * Tipos de autômatos                                      |
|        |       | * Hierarquia de linguagens formais                        |
|        |       | * Máquina de Turing                                       |
+--------+-------+-----------------------------------------------------------+
|        | 13/06 | Gramática do Python                                       |
|        |       |                                                           |
|        |       | * Tokenizador e projeto Transpyler                        |
|        |       | * Arquivo de gramática                                    |
|        |       | * Árvore sintática de um código “vivo”                    |
|        |       | * Meta programação                                        |
+--------+-------+-----------------------------------------------------------+
| 15     | 18/06 | Parser de Scheme                                          |
|        |       |                                                           |
|        |       | * Tokens da linguagem                                     |
|        |       | * Expressões comuns                                       |
|        |       | * Formas especiais                                        |
|        |       | * Percorrendo a árvore sintática                          |
+--------+-------+-----------------------------------------------------------+
|        | 20/06 | **Avaliação: gramáticas livres de contexto**              |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
| 16     | 25/06 | Avaliador metacircular                                    |
|        |       |                                                           |
|        |       | * Interpretação como um programa e avaliação metacircular |
|        |       | * Código como estrutura de dados                          |
|        |       | * Função eval()                                           |
|        |       | * Implementação de eval()                                 |
+--------+-------+-----------------------------------------------------------+
|        | 27/06 | Avaliador metacircular II                                 |
|        |       |                                                           |
|        |       | * Análise semântica                                       |
|        |       | * "Compilação" como aplicação parcial                     |
|        |       | * Modelo de avaliação e extensões semânticas              |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
| 17     | 02/07 | Máquinas virtuais                                         |
|        |       |                                                           |
|        |       | * Objetivos de compilação                                 |
|        |       | * Máquina virtual Python                                  |
|        |       | * Inspeção de Bytcodes                                    |
|        |       | * Máquina de pilha                                        |
+--------+-------+-----------------------------------------------------------+
|        | 04/07 | Emissão de bytecode                                       |
|        |       |                                                           |
|        |       | * Manipulação de Bytcodes                                 |
|        |       | * Compilação de funções                                   |
|        |       | * Loops e condicionais como GOTOs                         |
|        |       | * Escopo e ambiente local vs global                       |
+--------+-------+-----------------------------------------------------------+
| 18     | 09/07 | **PROVA Final**                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+
|        | 11/07 | Revisão de nota                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
|        |       |                                                           |
+--------+-------+-----------------------------------------------------------+


Obs.: O cronograma está sujeito a alterações.
