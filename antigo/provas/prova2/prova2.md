Prova 2
=======

## Q1. Expressões regulares

Você deve criar expressões regulares que passem em todos os testes fornecidos
no arquivo regex.py


## Q2. Parser de SQL

Faça um parser para um subconjunto da sintaxe do SQL. Seu parser deve ser capaz
de lidar com os seguintes comandos:

    SELECT <columns> FROM <table>;
    SELECT <columns> FROM <table> WHERE <condition>;

Nos comandos acima, <columns> pode ser qualquer sequência nomes de variáveis 
separada por vírgulas ou um asterisco (no SQL, isto significa selecionar todas
as colunas). Para simplificar, assuma que os nomes das variáveis contêm apenas 
letras minúsculas e o underscore.

<table> também é o nome de uma variável e <condition> é uma expressão que 
envolve duas variáveis e um operador (ex.: var_a > var_b). O SQL aceita os
seguintes operadores: =, <>, <, >, >=, <=.

Exemplos:

    SELECT name FROM users;
    
    SELECT * FROM users;
    
    SELECT username, password FROM users WHERE username = password; 


Você deve retornar a informação em um dicionário (resultado esperado para cada
comando):

    {'SELECT': ['name'], 'FROM': 'users'}

    {'SELECT': None, 'FROM': 'users'}
    
    {'SELECT': ['username', 'password'], 'FROM': 'users', 'WHERE': ['=', 'username', 'password']}
    