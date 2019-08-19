#lang scheme


;; Retorna uma lista nos n primeiros números de Fibonacci
(define (fibs n)
  (fibs-acc n null))


;; Função auxiliar que acumula os resultados em acc utilizando recursão de cauda
(define (fibs-acc n acc)
  (cond
    ((= n 0) (reverse acc))
    ((has-less-than-one-element? acc) (fibs-acc (- n 1) (cons 1 acc)))
    (#t (let
            ((y (car acc))
             (x (car (cdr acc))))
          (fibs-acc (- n 1) (cons (+ x y) acc))))))

;; Verifica se uma lista tem mais de um elemento de forma eficient
;; (evita percorrer a lista em tempo O(n) para calcular length).
(define (has-less-than-one-element? lst)
  (cond
    ((null? lst) #t)
    ((null? (cdr lst)) #t)
    (#t #f)))