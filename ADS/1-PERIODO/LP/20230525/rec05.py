# 6. Calcular o enésimo termo da sequência de números de Tribonacci. 
#  - A sequência de Tribonacci é uma extensão da sequência de Fibonacci, 
#    em que cada termo é a soma dos três termos anteriores. 
#    A sequência começa com 0, 1, 1 e, a partir daí, cada termo subsequente 
#    é a soma dos três termos anteriores. 


def fib(n):
    if n == 0 or n == 1: return 0
    elif n == 2 or n == 3: return 1
    else: return fib(n-1) + fib(n-2) + fib(n-3)

print(fib(18))