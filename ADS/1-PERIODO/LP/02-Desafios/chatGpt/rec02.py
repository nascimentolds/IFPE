# Desafio: Implemente uma função recursiva chamada fibonacci(n) que retorne o 
# n-ésimo termo da sequência de Fibonacci. A sequência de Fibonacci é uma sequência 
# de números em que cada número é a soma dos dois números anteriores. Os primeiros 
# dois termos da sequência são 0 e 1. Portanto, fibonacci(0) deve retornar 0, fibonacci(1) 
# deve retornar 1 e fibonacci(n) para n > 1 deve retornar o n-ésimo termo da sequência.

# Lembre-se de considerar que a sequência de Fibonacci começa a partir do índice 0.

def fib(n):
  if n <= 1: 
    return n
  else:
    return fib(n-1) + fib(n-2)
  
print(fib(10))