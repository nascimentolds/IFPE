# 1. Defina a função recursiva div que recebe como argumentos dois números naturais m e n e
# devolve o resultado da divisão inteira de m por n . Neste exercício não pode recorrer às
# operações aritméticas de multiplicação, divisão e resto da divisão inteira.

def div(m, n):
    if m < n:
        return 0
    else:
        return 1 + div(m-n, n)

print(div(22, 3))

# def fat(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fat(n-1)
