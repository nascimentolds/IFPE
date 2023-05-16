# 2. Escreva uma função para imprimir o valor absoluto de um número. (obs: utilize apenas operações aritméticas).

def abs(n):
   return n * -1 if n < 0 else n

print(abs(-5))