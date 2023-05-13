# 2. Escreva uma função para imprimir o valor absoluto de um número. (obs: utilize apenas operações aritméticas).

def abs(n):
    if n < 0: return n * -1
    else: return n

print(abs(5))