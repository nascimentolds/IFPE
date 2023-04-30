lista = [1, 2, 3, 5]
tupla = []

for x in lista:
    tupla.append((x, pow(x, 3)))

print(tupla)