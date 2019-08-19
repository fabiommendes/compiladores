#lang scheme
;; GABARITO


;; RESOLUÇÃO MM
;; Calcula valor da expressão
(define (calc expr)

  ;; Versão com acumulador. O acumulador guarda os números não utilizados ainda.
  (define (calc-acc expr numbers)
    (if (null? expr)
        ;; Se a lista de operações está vazia, numbers deve conter a resposta
        ;; como único elemento
        (car numbers)

        ;; Caso contrário, processa o primeiro elemento e decide se ele deve
        ;; consumir números ou passar o valor para a lista numbers
        (if (number? (car expr))
            (calc-acc (cdr expr) (cons (car expr) numbers))
            (calc-acc (cdr expr) (consume-stack (car expr) numbers)))))

  ;; Chamamos a função interna com acumulador
  (calc-acc expr null))


;; Roda o operador op consumindo os dois primeiros elementos da lista
;; de números. Retorna a lista de números adicionando o resultado ao
;; topo da pilha.
(define (consume-stack op nums)
  (begin
    (define x (list-ref nums 1))
    (define y (list-ref nums 0))
     
    (cons
     ;; Processa operação 
     (case op
       ('+ (+ x y))
       ('- (- x y))
       ('* (* x y))
       ('/ (/ x y)))

     ;; Remove os dois números utilizados da pilha
     (drop nums 2))))


;; RESOLUÇÃO MS - Lê resultado de uma string
(define (calc-str st)
  (calc (map token-value (string-split st))))

;; Converte string de token para valor
(define (token-value st)
  (let
      ((n (string->number st)))
    (if n
        n
        (string->symbol st))))


;; RESOLUÇÃO SS - REPL
(define (repl)
  (begin
    ;; Mostra prompt para usuário
    (display "\n> ")
    (define in (read-line))
    (if (empty? in)
        null
        (begin
          (display (calc-str in))
          (repl)))))


;; RESOLUÇÃO SS+ - REPL correto
(define (repl++)
  (begin

    ;; Pede uma entrada para o usuário e converte para token
    (define (prompt)
      (begin (display "> ") (read)))

    ;; Lê valor e pede para processar
    (define (repl-step numbers)
      (begin
        (let ((tk (prompt)))
          (if tk
              (process-tk tk numbers)
              null))))

    ;; Processa valor de token
    (define (process-tk tk numbers)
      (cond
        ;; Sai quando o usuário solicitar
        ((eq? tk 'exit) null)

        ;; Realiza operação se o usuário digitar um símbolo
        ((symbol? tk)
         (begin
           (define out (consume-stack tk numbers))
           (define value (car out))
           (display value)
           (display "\n")
           (repl-step (cons value (cdr out)))))

        ;; Caso seja um número, adiciona ao stack
        ((number? tk) (repl-step (cons tk numbers)))))

    (repl-step null)))
                    
;; Executa
(repl++)