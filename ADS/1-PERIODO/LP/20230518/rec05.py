# 5. Crie uma função recursiva para dado uma lista de inteiros e o seu número de elementos, 
# inverta a posição dos seus elementos.

def inverter(lista, n):
  if n <= 1:
      return lista
  else:
      lista[0], lista[n-1] = lista[n-1], lista[0]
      return [lista[0]] + inverter(lista[1:n-1], n-2) + [lista[n-1]]
  
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(inverter(lista, len(lista)))