# Faça um programa que peça dois números, base e expoente, calcule e
# mostre o primeiro número elevado ao segundo número. Não utilize a função
# de potência da linguagem

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
c = 1

for i in range(n2):
    c = c * n1
    # print(c)

print(f"O resulta de {n1} elevado a {n2} é: {c}")