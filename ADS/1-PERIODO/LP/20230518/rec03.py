# 3. Crie uma função recursiva que imprima o enésimo termo da sequencia de Fibonacci. 
# Ex: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584. 
# 2584 é o 18º número da sequencia.

def fib(n):
    if n <= 2: return 1
    else: return fib(n-1) + fib(n-2)

print(fib(5))