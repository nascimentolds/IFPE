# 2. Faça um programa que leia 10 números inteiros. Cada numero par deve ser
# armazenado em uma lista de pares e cada impar tem que ser armazenado em uma
# lista de impares. Ao término do programa imprima as duas listas.

par = []
impar = []

for x in range(1, 11):
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

print(par)
print(impar)