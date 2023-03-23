# Faça um programa que peça dois números, base e expoente, calcule e
# mostre o primeiro número elevado ao segundo número. Não utilize a função
# de potência da linguagem

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
count = 1

while n2 > 0:
    count = count * n1
    n2-= 1

print(count)