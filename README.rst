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
    01/2018
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
* Geração e otimização de código.
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
    http://classroom.google.com/ - Código de inscrição: 1byukn
Github:
    http://github.com/fabiommendes/compiladores/
Github Classroom:
    http://github.com/fga-compiladores/ - Link de inscrição: https://classroom.github.com/a/0FZLKsXp


Critérios de avaliação
======================

Cada aluno será avaliado com uma nota numérica onde a conversão entre a pontuação e a menção final é feita da forma usual: 9,0pts+: SS, 7,0pts+: MS, 5,0pts+: MM, 3,0pts+: MI e < 3,0 pts II. A distribuição de pontos ao longo do curso segue a fórmula::

    NotaFinal = 0.15 * P1 + 0.25 * P2 + 0.10 * ME + 0.50 * MT

onde P1 e P2 consistem na nota das provas 1 e 2; ME representa a média dos exercícios individuais (feitos em casa); MT representa a média dos testes realizados em sala de aula. Os testes serão resolvidos em grupos de tamanho e composição variávies e consistem em tarefas esporádicas realizadas durante a aula.

Gamificação
-----------

O aluno poderá fazer algumas tarefas opcionais que chamamos de "épicos" que ajudam na nota final do aluno. Os `épicos <epicos.rst>` são avaliados em menção (MI, MM, MS, SS), que correspondem respectivamente a (25%, 50%, 75%, 100%) de sua nota total. A nota do épico pode ser utilizada de duas maneiras:

* Como valor mínimo para a nota final do semestre
* Como complemento à nota: NF' = NF + NE / 2 * (1 - NF/10); NE = nota do épico e NF = nota final

Prova substitutiva e faltas
---------------------------

O curso não inclui prova substitutiva. Caso o aluno possua uma falta justificada no dia da primeira prova, deverá apresentar um comprovante na aula seguinte à prova ou quando terminar a licença médica. Esta justificativa não abona falta, mas dá direito ao aluno utilizar a segunda prova como prova substitutiva. 

O aluno pode faltar até 7 vezes em um semestre. Faltas com justificativa médica não serão abonadas, exceto em casos excepcionais. Os alunos reprovados por falta ficarão com uma menção igual a SR.

Código de ética e conduta
-------------------------

Algumas avaliações serão realizadas com auxílio do computador no laboratório de informática. Todas as submissões serão processadas por um programa de detecção de plágio. Qualquer atividade onde for detectada a presença de plágio será anulada sem a possibilidade de substituição. Não será feita qualquer distinção entre o aluno que forneceu a resposta para cópia e o aluno que obteve a mesma.

As mesmas considerações também se aplicam às provas teóricas que serão respondidas à mão.


Prepare-se
==========

O curso utiliza alguns pacotes Python para os quais cada estudante deverá providenciar a instalação o mais cedo o possível. O curso requer Python 3.6+ com alguns pacotes instalados:

* Pip: Gerenciador de pacotes do Python (sudo apt-get install python3-pip)
* PLY (sudo apt-get install python3-ply): Port do Yacc/Bison para Python
* Ox (pip3 install ox-parser --user): compilador de compiladores criado para esta disciplina
* Docker: cria ambientes completamente isolados para teste e validação

Já que vamos utilizar o Python, vale a pena instalar as seguintes ferramentas:

* virtualenvwrapper: isola ambientes de desenvolvimento Python para não contaminar o resto do seu sistema
* flake8: busca erros de estilo e programação no seu código
* autopep8: tenta corrigir estes erros automaticamente
* pytest, pytest-cov: criação de testes unitários
* Editores de código/IDE:
    Utilize o seu favorito. Caso precise de uma recomendação, seguem algumas:
    
 * PyCharm Educacional - IDE com ótimos recursos de introspecção e refatoração que adora memória RAM. Possui versão livre e versão profissional gratuita para estudantes.
 * VSCode - um bom meio termo entre uma IDE e um editor de código leve. Criado para Javascript, mas possui plugins para Python e várias outras linguagens.
 * Vi/Vim - herança dos anos 70 que nunca morre. Instale os plugins para Python.

DICA: em todos os casos, prefira instalar os pacotes Python utilizando o apt-get e somente se o pacote não existir, instale-o utilizando o pip. Se utilizar o pip, faça a instalação de usuário utilizando o comando ``pip3 install <pacote> --user`` (NUNCA 
utilize o sudo junto com --user e evite instalar globalmente para evitar problemas futuros com o APT).

Linux e Docker
--------------

Os comandos de instalação acima assumem uma distribuição de Linux baseada em Debian. Não é necessário instalar uma distribuição deste tipo e você pode adaptar os comandos para o gerenciador de pacotes da sua distribuição (ou o Brew, no caso do OS X). Apesar do Linux não ser necessário para executar a maior parte das tarefas, é altamente recomendável que todos instalem o Docker para compartilharmos ambientes de desenvolvimento previsíveis (por exemplo, eu testarei as submissões em containers específicos que serão compartilhados com a turma). É possível executar o Docker em ambientes não-Linux utilizando o Docker Machine ou o Vagrant. Deste modo, cada aluno deve providenciar a instalação do Docker e Docker Compose na sua máquina.


Bibliografia principal
----------------------

Dragon Book: Alfred V. Aho, Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman, Compilers: Principles, Techniques, and Tools, Pearson, 2006. 


Cronograma de atividades
========================

+--------+-------+--------------------------------------------------------+
| Semana | Data  |                          Aula                          |
+========+=======+========================================================+
| 1      | 06/03 | Início das aulas – Apresentação do curso               |
|        |       |                                                        |
|        |       | * Estrutura de linguagens naturais                     |
|        |       | * Linguagens artificiais                               |
|        |       | * Linguagens de programação                            |
+--------+-------+--------------------------------------------------------+
|        | 08/03 | Expressões regulares                                   |
|        |       |                                                        |
|        |       | * Ortografia e léxico de uma linguagem                 |
|        |       | * Linguagens regulares                                 |
|        |       | * Expressões regulares em Python                       |
+--------+-------+--------------------------------------------------------+
| 2      | 13/03 | Laboratório de regex: chatbot                          |
|        |       |                                                        |
|        |       | * Detecção de padrões                                  |
|        |       | * Resposta a padrões                                   |
|        |       | * Usos de expressões regulares e API Python            |
+--------+-------+--------------------------------------------------------+
|        | 15/03 | Análise léxica                                         |
|        |       |                                                        |
|        |       | * Tokens                                               |
|        |       | * Implementando um analizador léxico                   |
|        |       | * Analizador léxico no Ox                              |
+--------+-------+--------------------------------------------------------+
| 3      | 20/03 | Léxico de linguagens de programação                    |
|        |       |                                                        |
|        |       | * Exemplos em Python                                   |
|        |       | * Definição de tokens                                  |
|        |       | * Precedência de expressões regulares                  |
|        |       | * Inventando uma linguagem de programação              |
+--------+-------+--------------------------------------------------------+
|        | 22/03 | **Avaliação: Expressões regulares**                    |
|        |       |                                                        |
+--------+-------+--------------------------------------------------------+
| 4      | 27/03 | Análise sintática                                      |
|        |       |                                                        |
|        |       | * Gramática                                            |
|        |       | * Especificação de regras gramaticais                  |
|        |       | * Hierarquia de linguagens                             |
|        |       | * Sintaxe vs semântica                                 |
+--------+-------+--------------------------------------------------------+
|        | 29/03 | Laboratório de análise sintática: Gerador de lero lero |
|        |       |                                                        |
|        |       | * Formalização de uma gramática                        |
|        |       | * Produções válidas                                    |
|        |       | * Gerador de textos aleatórios                         |
+--------+-------+--------------------------------------------------------+
| 5      | 03/04 | Gramáticas livres de contexto                          |
|        |       |                                                        |
|        |       | * Regras de produção                                   |
|        |       | * Sintaxe do Ox                                        |
|        |       | * Calculadora                                          |
+--------+-------+--------------------------------------------------------+
|        | 05/04 | Árvores sintáticas e representação de código           |
|        |       |                                                        |
|        |       | * S-expressions                                        |
|        |       | * ADTs                                                 |
|        |       | * Classes                                              |
+--------+-------+--------------------------------------------------------+
| 6      | 10/04 | Laboratório: Calculadora avançada                      |
|        |       |                                                        |
|        |       | * Operadores e expressões                              |
|        |       | * Representação intermediária                          |
|        |       | * Precedência                                          |
|        |       | * Análise semântica                                    |
+--------+-------+--------------------------------------------------------+
|        | 12/04 | Emissão de código                                      |
|        |       |                                                        |
|        |       | * Representação intermediária                          |
|        |       | * Geração de código                                    |
|        |       | * Controle de formatação e indentação                  |
|        |       | * Funções auxiliares para emissão de código no Ox      |
+--------+-------+--------------------------------------------------------+
| 7      | 17/04 | Gramática do Python                                    |
|        |       |                                                        |
|        |       | * Tokenizador                                          |
|        |       | * Arquivo de gramática                                 |
|        |       | * Árvore sintática de um código “vivo”                 |
|        |       | * Gramática do Python no Ox                            |
+--------+-------+--------------------------------------------------------+
|        | 19/04 | Desenho de linguagens de programação                   |
|        |       | * Expressões e declarações                             |
|        |       | * Mutabilidade                                         |
|        |       | * Escopo                                               |
|        |       | * Sistema de tipos                                     |
|        |       | * Estruturas de controle                               |
+--------+-------+--------------------------------------------------------+
| 8      | 24/04 | Projeto: Linguagem funcional                           |
|        |       |                                                        |
|        |       | * Sintaxe, semântica e sistema de tipos                |
|        |       | * Integração com o Python                              |
|        |       | * Estruturas de controle básicas                       |
|        |       | * Recursos para programação funcional                  |
|        |       | * Exemplos de programas                                |
+--------+-------+--------------------------------------------------------+
|        | 26/04 | **Avaliação: Lexer e parser**                          |
|        |       |                                                        |
+--------+-------+--------------------------------------------------------+
| 9      | 01/05 | *Feriado - Dia do Trabalho*                            |
|        |       |                                                        |
+--------+-------+--------------------------------------------------------+
|        | 03/05 | Autômatos                                              |
|        |       |                                                        |
|        |       | * Introdução a autômatos                               |
|        |       | * Autômato determinístico finito                       |
|        |       | * Autômatos para linguagens regulares                  |
+--------+-------+--------------------------------------------------------+
| 10     | 08/05 | Hierarquia de Chomsky                                  |
|        |       |                                                        |
|        |       | * Modelos de computação                                |
|        |       | * Tipos de autômatos                                   |
|        |       | * Hierarquia de linguagens formais                     |
|        |       | * Máquina de Turing                                    |
+--------+-------+--------------------------------------------------------+
|        | 10/05 | Laboratório: JSON                                      |
|        |       |                                                        |
|        |       | * Gramática como autômato                              |
|        |       | * Separação entre a análise léxica e sintática         |
|        |       | * Implementação do JSON em Ox                          |
+--------+-------+--------------------------------------------------------+
| 11     | 17/05 | Cremilda: Lexer                                        |
|        |       |                                                        |
|        |       | * Tipos atômicos (numerais, strings, etc)              |
|        |       | * Símbolos                                             |
|        |       | * Operadores e delimitadores                           |
+--------+-------+--------------------------------------------------------+
|        | 19/05 | Cremilda: Expressões e declarações simples             |
|        |       |                                                        |
|        |       | * Chamada de função                                    |
|        |       | * Tradução para Python                                 |
|        |       | * Aninhamento                                          |
|        |       | * Declarações                                          |
+--------+-------+--------------------------------------------------------+
| 12     | 22/05 | Cremilda: Estruturas condicionais simples              |
|        |       |                                                        |
|        |       | * Linguagem baseada em expressões                      |
|        |       | * Palavras reservadas                                  |
|        |       | * Operadores booleanos "curto-circuito"                |
|        |       | * Condicional if/else                                  |
+--------+-------+--------------------------------------------------------+
|        | 24/05 | **Avaliação: gramáticas livres de contexto**           |
|        |       |                                                        |
+--------+-------+--------------------------------------------------------+
| 13     | 29/05 | Checagem de tipos                                      |
|        |       |                                                        |
|        |       | * Sistemas de tipos                                    |
|        |       | * Coerções                                             |
|        |       | * Polimorfismo                                         |
|        |       | * Type dispatch                                        |
+--------+-------+--------------------------------------------------------+
|        | 31/05 | *Feriado - Corpus Christi*                             |
|        |       |                                                        |
+--------+-------+--------------------------------------------------------+
| 14     | 05/06 | Cremilda: declaração de tipos                          |
|        |       |                                                        |
|        |       | * Aliases                                              |
|        |       | * Union types                                          |
|        |       | * Tuplas                                               |
+--------+-------+--------------------------------------------------------+
|        | 07/06 | Cremilda: Criação de tipos dinâmica                    |
|        |       |                                                        |
|        |       | * Classes dinâmicas                                    |
|        |       | * Dicionário de tipos                                  |
|        |       | * Tipos na biblioteca Sidekick                         |
+--------+-------+--------------------------------------------------------+
| 15     | 12/06 | Cremilda: declaração de módulos                        |
|        |       |                                                        |
|        |       | * Símbolos públicos                                    |
|        |       | * Imports                                              |
|        |       | * Integração com o Python                              |
+--------+-------+--------------------------------------------------------+
|        | 14/06 | Cremilda: runtime                                      |
|        |       |                                                        |
|        |       | * Tipos e funções nativas                              |
|        |       | * Módulos padrão                                       |
|        |       | * Compilação para Python                               |
+--------+-------+--------------------------------------------------------+
| 16     | 19/06 | Máquinas virtuais                                      |
|        |       |                                                        |
|        |       | * Objetivos de compilação                              |
|        |       | * Máquina virtual Python                               |
|        |       | * Leitura de Bytcodes                                  |
|        |       | * Manipulação de Bytcodes                              |
+--------+-------+--------------------------------------------------------+
|        | 21/06 | Cremilda: blocos let                                   |
|        |       |                                                        |
|        |       | * Atribuição de variáveis                              |
|        |       | * Controle de escopo                                   |
|        |       | * Forma SSA                                            |
|        |       | * Descontrutores                                       |
+--------+-------+--------------------------------------------------------+
| 17     | 26/06 | Cremilda: blocos case                                  |
|        |       |                                                        |
|        |       | * Despacho por tipo e sub-tipo                         |
|        |       | * Switch/case                                          |
|        |       | * Desconstrutores                                      |
+--------+-------+--------------------------------------------------------+
|        | 28/06 | **Avaliação Final**                                    |
|        |       |                                                        |
+--------+-------+--------------------------------------------------------+
| 18     | 03/07 | Livre                                                  |
|        |       |                                                        |
+--------+-------+--------------------------------------------------------+
|        | 05/07 | Revisão de nota                                        |
|        |       |                                                        |
+--------+-------+--------------------------------------------------------+

Obs.: O cronograma está sujeito a alterações.
