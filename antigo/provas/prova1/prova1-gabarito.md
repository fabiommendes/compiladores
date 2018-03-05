Compiladores - Prova 1, gabarito
================================

5/10/2017 - Prof. Fábio Macêdo Mendes


## Q1-jedi (2.0 pts): Gramáticas simples 

a) (0.5) Não, pois as expressões que possuem apenas 1 "b" possuem pelo menos 4 
caracteres segundo as 2 primeiras regras de derivação.

b) (0.75) Em s-exprs:

    (E_1 
        a 
        (E_2 
            b 
            (E_3 a) 
            a 
            (E_3 a) 
        ) 
        b 
        (E_3 a)
    )

Onde distinguimos os três ramos da definição de E na gramática associados a cada
uma das regras.

c) (0.75) Sabendo que apenas `E_1`  e `E_2` introduzem b's na gramática, basta provar que 
se expr1 e expr2 possuem um número de a's maior que b's, o mesmo vale
para as expressões derivadas.

Seja a1 e b1 o número de a's e b's em expr1 e a2 e b2 para expr2. A análise 
para E1 e E2 é a mesma, já que ambas introduzem um valor de a e outro de b:

    a_final = a1 + a2 + 1
    b_final = b1 + b2 + 1

uma vez que a1 > b1, então a_final > b1 + a2 + 1. Sabendo que a2 > b2, 
também temos que `a_final > b1 + b2 + 1 = b_final`, QED.


## Q1-padawan (1.5pts): Gramáticas simples

a) A expressão pode ser derivada como `(a * a) * a` ou `a * (a * a)`, fazendo a 
associatividade tanto à esquerda quanto à direita:

Derivação 1: 

    E -> E * E -> E * a -> E * E * a 
      -> a * E * a -> a * a * a

Derivação 2: 

    E -> E * E -> a * E -> a * E * E 
      -> a * E * a -> a * a * a

b) Uma gramática não ambígua seria: `E = E * a | a` que só permite 
associatividade à esquerda pois o novo elemento é sempre um átomo `a` colocado 
à direita. 

----


## Q2-jedi (3.0 pts): Linguagens regulares

a) Tabela de valores:

---------------  -------------  -------------
[V] `42`         [V] `+42.`     [V] `-42`   
[V] `3.1415`     [F] `.15`      [F] `1.2e10`
[F] `--1.5`      [V] `1.2.3`    [V] `1..10` 
---------------  -------------  -------------

b) Expressão regular:

    N -> (-|+|e)
         (dd*)
         (.d*|e)

c) Expressão regular:

    N -> (-|+|e)
         (
           dd*
           |
           (d|dd|ddd)(_ddd)*
         )
         (.d*|e)


## Q2-padawan (2.0 pts): Linguagens regulares

Linguagem regular:

    N -> (d|dd|ddd)(_ddd)*

----


## Q3-jedi (3.0 pts) Análize de código 

a) Tokens (eles estão identados somente para facilitar a visualização):

    KEYWORD(DEF) NAME(say_hi) LPAR NAME(x) RPAR COLON
        INDENT NAME(print) LPAR STRING("Hello ") OP(+) NAME(x) RPAR

Assumi que o tokenizador introduz os tokens de indentação, mas isto é um detalhe
de implementação. Os tokens LPAR, RPAR, COLON possuem valores fixos `(`, `)` e `:`

b) Com s-exprs:

    (DEF
        NAME(say_hi)
        (ARGS
            NAME(x)
        )
        (BLOCK
            (CALL
                NAME(print)
                (PLUS
                    STRING("Hello ")
                    NAME(x)
                )
            )
        )
    )


## Q3-padawan (2.0 pts) Análize de código 

a) Tokens
    
    NAME(X) EQ(=) NUMBER(10) OP(+) NAME(b) OP(*) NUMBER(42)

b) Com s-exprs:
    
    (ASSIGN
        NAME(x)
        (PLUS 
            (TIMES 
                NUMBER(10) 
                NAME(b)
            ) 
            NUMBER(42)
        )
        
    )


---


## Q4-jedi (3.5 pts) Gramática para o JSON

Gramática BNF:

    expr 
        : atom
        | list
        | object  
    
    list 
        : [ list_args ]
    
    list_args 
        : args , expr
        | expr
       
    object
        : { pairs }
        
    pairs 
        : pairs , pair
        | pair

    pair 
        : STRING : expr 

    atom 
        : true 
        | false 
        | null 
        | NUMBER 
        | STRING
         


## Q4-padawan (2.5 pts) Gramática dos dicionários

Gramática BNF:

    dictionary
        : { pairs }

    pairs
        : pairs, pair
        | pair

    pair
        : STRING : atom

    atom
        : STRING
        | NUMBER
