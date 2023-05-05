# 1. Faça um programa em que dada uma lista de números inteiros,
# encontre o segundo menor e o segundo maior valor sem ordenar a
# lista.

lista = [5, 9, 7, 3, 6]

print(lista)

lista.remove(min(lista))
lista.remove(max(lista))

s_menor = min(lista)
s_maior = max(lista)

print('Segundo menor número é:', s_menor)
print('Segundo maior número é:', s_maior)

