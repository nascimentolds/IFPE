# 3. Escreva uma função que receba uma lista de números inteiros e
# retorne uma lista contendo apenas os números primos.

lista = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 17, 19]
primos = []

for i in lista:
    if i == 2 and i not in primos:
        primos.append(i)
    
    if i == 3 and i not in primos:
        primos.append(i)

    if i != 1 and i != 3 and i % 3 != 0 and i % 2 != 0 and i not in primos:
        primos.append(i)

print(lista)
print(primos)