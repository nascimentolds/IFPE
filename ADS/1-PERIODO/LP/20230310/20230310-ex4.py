# 4. Escreva um programa para calcular o fatorial de um número fornecido pelo usuário.

n = int(input("Digite um número: "))
n1 = n
count = 1

for i in range(n):
    count = count * n
    n = n - 1

print(f"{n1}!: {count}")
    


