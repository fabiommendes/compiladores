# Gramáticas livre de contexto

Crie uma gramática livre de contexto utilizando o Lark que reconheça cada uma das
linguagens abaixo. Lembre-se que sua gramática deve aceitar todas strings válidas
da linguagem e recusar todas as strings inválidas.


## Letra minúscula envolvida por parênteses

Exemplos: `a`, `(b)`, `((((z))))`, etc
A gramática deve recusar parênteses vazios `()`, parênteses não pareados, `((a)`
ou na ordem errada, `)a(`, ou em configurações que não envolvam a letra, `(()a)`.

Esta linguagem simples é um clássico de compiladores porque se trata de uma das 
linguagens mais simples que **não** podem ser reconhecidas por expressões 
regulares.


## Conjuntos de parênteses pareados

Aceita qualquer letra minúscula, string vazia ou sequências de valores envolvidas
por parênteses pareados. Semelhante ao caso anterior, mas aceita construções como
`()`, `(()a)`, `()()`, `ab`, `a(b(c(())))`.


## Listas

Listas envolvidas por parênteses que contêm qualquer número de letras (inclusive zero)
separadas por espaços. Ex.: `()`, `(a b c)`.


## Listas dentro de listas

Semelhante ao caso anterior, mas permite a inclusão de listas dentro de listas.
Ex.: `((a (b) (c ()))`.


## Listas com separadores

Semelhante ao caso anterior, mas agora os elementos devem ser separados por vírgulas.
Os espaços em branco devem ser ignorados e não aceita um espaço em branco no final 
da lista.

Ex.: `()`, `(a, b)`, `(a , (b ,c))`



## Último separador opcional

Igual ao caso anterior, mas aceita uma vírgula após o último item da lista.

Ex.: `()`, `(a, b,)`, `(a , (b ,c,))`



## Arrays Javascript

Semelhante ao anterior, mas trocamos parênteses por colchetes e aceitamos 
qualquer número de vírgulas onde elas são aceitas. (Obs.: abra o console
do seu navegador para ver que o Javascript realmente aceita isto!)

Ex.: `[]`, `[a,,, b,]`, `[a , [b ,c,,,]]`



## Desafio: somas e subtrações em Javascript

Abra o console do Javascript no seu navegador (ctrl + shift + i) para tentar 
entender o que está acontecendo. São todas expressões válidas envolvendo
variáveis e somas e subtrações em Javascript: `x+y`, `+x`, `-x`, `x--`, `++x-y`, 
`y+++x`, `x++-y`, `x++-++y`, `x+-+-+-+-+y`. 

Talvez surpreendentemente, nem toda sequência aleatória de somas e subtrações 
é uma expressão válida, como por exemplo `x-++-y` ou `x-+++y`. Descubra o padrão 
por trás destas expressões e crie a gramática correspondente.