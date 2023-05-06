# 3. Faça um programa para imprimir de acordo com a imagem abaixo para um n
# informado pelo usuário. Use uma função que receba um valor n inteiro e
# imprima até a n-ésima linha.

#     1
#     2   2
#     3   3   3
#     n   n   n   n

def triangulo(i):
    c = 1
    for x in range(1, i+1):
        print(f'{x}  ' * c)
        c += 1

n = int(input('Digite um número: '))

triangulo(n)