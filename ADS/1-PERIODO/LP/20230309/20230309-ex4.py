# 4. Escreva um programa para calcular o fatorial de um número fornecido pelo usuário.

n = int(input("Digite um número: "))
count = 1

while n > 0:
    count = count * n
    n = n - 1
print(count)