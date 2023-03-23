# 8. Em Matemática, o número harmônico designado por H(n) define-se como
# sendo a soma da série harmónica: H(n) = 1 + 1/2 + 1/3 + 1/4 ... 1/n
# Faça um programa que leia um valor n inteiro e positivo e apresente o valor
# de H(n):

n = int(input("Digite um número: "))
c = 1
y = 0
t = 0

for x in range(1, n+1):
    y = c/x
    t = t + y

print(f"H(n) de {n} é igual a: {t:.2f}")