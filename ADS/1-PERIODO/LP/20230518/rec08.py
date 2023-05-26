# 8. Escreva um programa Python para calcular a soma harmônica de n-1. Nota: A soma
# harmônica é a soma dos recíprocos dos inteiros positivos. H(n) = 1 + 1/2 + 1/3 + 1/4 ... 1/n

def harm(n):
    if n-1 == 0: return 0
    else: return 1/n + harm(n-1)

print(harm(5))