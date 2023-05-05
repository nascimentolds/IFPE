# 6. Implemente um algoritmo para encontrar o par de elementos distintos
# em uma lista cuja soma seja igual a um determinado valor X fornecido
# pelo usuário. Caso a lista não contenha um par, uma mensagem deve
# ser mostrada para o usuário.

lista = [1,2,3,4,5,6,7,8,9]
n = 16

c = 0

for i in lista:
     for x in range(len(lista)):
          if i + lista[x] == n:
               print(i)
               c += 1

if c == 0:
     print('Nao existe soma na lista para esse valor!')