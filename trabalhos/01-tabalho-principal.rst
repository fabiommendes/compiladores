Trabalhos em grupo
==================

Esta atividade segue até o fim do semestre e consiste em realizar um projeto
de desenvolvimento e evolução de um programa relacionado à matéria de 
compiladores. 

    * As equipes são formadas por 6-8 alunos e podem ser alteradas ao longo do 
    semestre. A pontuação total atribuída ao projeto é de 30 pontos.
    * O projeto é organizado em sprints semanais.
    * Existirão pontos de controle a cada 3 ou 4 semanas onde o progresso de cada 
    equipe será avaliado e uma parte da nota será atribuída. 
    * O professor pode determinar a troca de membros alguma equipe durante os pontos
    de controle.
    * Todos os projetos são de software livre e serão gerenciado de forma 
    transparente no Github. O professor pode determinar objetivos específicos para 
    cada equipe através de "issues" no github, mas as equipes são responsáveis por
    definir prioridades ou até mesmo levantar requisitos.
    * Espera-se que as equipes implementem um mínimo de documentação e testes.
    * No final de cada ponto de controle, será atribuída uma nota para o grupo e esta
    nota será distribuída entre cada participante de acordo com uma avaliação 
    individual por parte dos outros membros.
    * No final de cada ponto de controle, cada grupo fará uma apresentação curta no
    estilo "lightining talk" (5 min) com perguntas abertas para toda a turma.


Projetos
======== 

Ox
--

Implementar funcionalidades na biblioteca ox. Existem várias pendências: 

* Tokenizador da linguagem Python
* Parser da linguagem Python
* Módulos para emissão de código em Python, C e Javascript


Bricks
------

Bricks é uma biblioteca que implementa templates HTML como objetos Python::

    div(class_="foo")[
        h1("The title"),
        p("Hello World!"),
    ]

Queremos criar uma linguagem própria BML (Bricks Markup Language) que possa 
emitir Python, Javascript ou Elm. BML usa elementos de outras linguagens de 
template como Pug e de linguagens funcionais como Elm. O código acima se 
tornaria algo como:

    div(class="foo"):
        h1. The title
        p. Hello World

Definimos tags/comandos que extendem o HTML com recursos de programação:

    function button(name: String, state: String):
        button(class="button", class="button--" ++ state). $name

Tipos básicos: números, strings, listas, structs
Estuturas de código: função, condicional, loop

Podem ser formar até 4 grupos atacando diferentes partes da linguagem:
* Parser de bricks
* Emissão de código para Python
* Emissão de código para Javascript
* Emissão de código para Elm


Sidekick
--------

Sidekick é uma biblioteca para ajudar com programação funcional em Python. Entre
suas funcionalidades, temos o quick lambda, que é um objeto mágico chamado de 
"_" que cria funções rapidamente:: 

    from sidekick import fn, _

    increment = fn(_ + 1)
    poly = fn(1*_**2 + 2*_ + 3)

Internamente ele guarda uma árvore sintática e um objeto Python que implementa
a função correspondente. O objetivo do trabalho é criar um emissor de código 
para Javascript (para aplicações Web) ou C (para aplicações científicas).


Jarbas
------

Jarbas é um projeto que visa criar ferramentas para automatizar várias tarefas
repetitivas no ciclo de desenvolvimento. (Criar um novo projeto, adicionar 
testes, documentação, integração contínua, etc).

Jarbas criou uma linguagem que facilita a criação de módulos e a interação com
o usuário::

    Glad to see you here, $info.gender|title!

    This basic project template creates a new Python project with the bare 
    essentials. If you want to know more and understand the role of each file, 
    please go to http://rtfd.org/jarbas/help/base.html.
    
    = Author: [author=@info.author]
    = Email: [email=@info.email]
    = Project name: [name=str]
    = Project version: [version=str:0.1.0]
    = Package name: [package=str]
    =if= Use virtualenv? [use_virtualenv=bool:True]
    = Virtualenv name: [virtualenv=str:@package]
    =endif= 

Você deve implementar o parser e o intepretador desta linguagem.


Kpop
----

Kpop é um programa que realiza vários tipos de análises em genética de 
populações. Uma das funcionalidades importantes do Kpop consiste em ler arquivos
externos de outros programas consagrados na comunidade de génetica. 

Você deve implementar e evoluir o parser para alguns destes formatos. 

* Structure
* Formatos do Plink


Questions
---------

Implementar parsers para os formatos de questão do Moodle: Aiken e GIFT.

Aiken::

    What is the correct answer to this question?
    A. Is it this one?
    B. Maybe this answer?
    C. Possibly this one?
    D. Must be this one!
    ANSWER: D


GIFT::

    Who's buried in Grant's tomb?{=Grant ~no one ~Napoleon ~Churchill ~Mother Teresa }