# Teste 1

Construa um programa em Scheme que implemente uma calculadora baseada na notação
polonesa reversa. Seu programa deve executar as 4 operações fundamentais e será
avaliado segundo os critérios:

MI - solução incompleta do problema ou solução em Python.
MM - implementa uma função calc que recebe uma lista "quoted" com as operações
desejadas e retorna o resultado. Exemplo: `(calc '(10 2 * 1 + 2 *)) ==> 42`
MS - o programa lê uma string com a expressão (valores separados por espaços ou 
quebras de linha) e retorna o resultado numérico
SS - o programa implementa um REPL que pergunta cada expressão interativamente.

## Dica

A notação polonesa reversa pode ser avaliada como uma pilha de operações.
Sabendo que todas operações são binárias. Podemos avaliar o resultado retirando
elementos do topo da pilha até encontrar um operador. O operador consome os
dois últimos elementos não utilizados e retorna o resultado para o topo da 
pilha. Continuamos este processo até a pilha se exaurir.

Para implementar este processo sem loops, defina uma função calc-acc que recebe
a lista de operações e uma lista auxiliar que podemos acumular os resultados não
computados. A implementação de calc-acc provavelmente deve começar assim:

```scheme
(define (calc-acc expr numbers)
    (if (null? expr)
        ;; Se a lista de operações está vazia, numbers deve conter a resposta
        ;; como único elemento
        (car numbers)

        ;; Caso contrário, processa o primeiro elemento e decida se ele deve
        ;; consumir números ou passar o valor para a lista numbers
        (...)))
```

## Consulta

Vocês podem consultar o livro SICP e a documentação do scheme/racket em
https://docs.racket-lang.org.

## Testes

```
(calc '(1 2 +))  ==> 3
(calc '(10 5 /)) ==> 2
(calc '(2 3 * 4 +)) ==> 10 ; (2 * 3) + 4 
(calc '(2 3 4 * +)) ==> 10 ; 2 * (3 + 4)
```

