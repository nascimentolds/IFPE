# Escreva um programa que leia um número inteiro e calcule a soma de todos
# os divisores desse número, com exceção dele próprio. Ex: a soma dos
# divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

n = int(input("Digite um número: "))
c = 0

for x in range(1, n):
    if n % x == 0:
        c = c + x

print(f"A soma dos divisores do número {n} é: {c}")