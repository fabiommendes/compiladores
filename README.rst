Fundamentos de Compiladores
===========================

Este é o Git da disciplina Fundamentos de Compiladores. Aqui será compartilhado
o material produzido em sala de aula assim como tarefas, wiki e discussões.

Ementa:
1. Autômatos
2. Gramáticas
3. Analisador léxico
4. Analisador Sintático
5. Geração de Código.


Observações
-----------

Vamos tentar fazer um curso sem "moodle", operando tudo via Github. Para isto,
habilite a funcionalidade "Watch" no repositório para receber notificações sobre 
atualizações. 

O "fórum de notícias" é a lista de issues. Farei os avisos por uma issue chamada
Avisos_. Para se 
cadastrar, simplesmente habilite a função "subscrible" desta issue. 


.. _Avisos: https://github.com/fabiommendes/compiladores/issues/1


Prepare-se
----------

Este curso utilizará alguns pacotes Python que você deverá providenciar a 
instalação o mais cedo o possível. Lembre-se sempre de usar Python 3 (RIP Python 2)

* PLY (sudo apt-get install python3-ply): Port do Yacc/Bison para Python
* Ox (pip install ox-parser --user): compilador de compiladores que criaremos 
  ao longo do curso

Em qualquer curso que dependa de Python, vale a pena instalar as ferramentas:

* virtualenvwrapper: isola um ambiente Python
  para que seu ambiente de desenvolvimento não contamine o resto do sistema.
* flake8: busca erros de estilo e programação no seu código
* autopep8: tenta corrigir estes erros automaticamente
* pytest, pytest-cov: criação de testes unitários

DICA: em todos os casos, tente sempre instalar primeiro do apt-get e somente 
se o pacote não existir, instale utilizando o pip3. Se utilizar o pip, instale 
somente para o seu usuário com o comando ``pip3 install <pacote> --user`` (NUNCA 
utilize o sudo junto com --user).


Bibliografia principal
----------------------

Dragon Book: 	Alfred V. Aho, Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman, Compilers: Principles, Techniques, and Tools, Pearson, 2006. 