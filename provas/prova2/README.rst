JSON+
=====

O arquivo json.py implementa um parser completo de JSON. Modifique este arquivo
para incorporar as seguintes modificações à linguagem (chamamos de JSON++):

Deve aceitar comentários no formato ``// comentário``::

  {
    // comentário!
    "foo": "bar"
  }


As vírgulas são opcionais. JSON++ deve aceitar uma vírgula após o último 
elemento de um array ou objeto::

  {
    "array": [1 2 3]
    "object": {
      "name": "John",
      "band": "Beatles, 
    }
  }


As chaves dos objetos podem ser nomes de variáveis. Nomes de variávies 
começam com uma letra e seguem com uma sequência de letras, números, hífens,
e underscores::

  {
    name: "John"
    band: "Beatles"
  }  


Aceita valores do tipo data no formato AAAA-MM-DD::

  {
    name: "John"
    band: "Beatles"
    born: 1940-10-09
  }  

Dica: use a função date(year, month, day) do módulo datetime para representar
uma data. Datas que fogem deste formato são inválidas (ex: 2000-1-1 é inválida
porque tanto o mê quanto o dia precisam de 2 dígitos)


Rodando os testes
-----------------

O programa grader.py analisa os resultados e mostra a nota da prova de acordo 
com a sua submissão. 