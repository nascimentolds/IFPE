# 4. Escreva um programa que compare duas listas e imprima:
#  - os valores comuns às duas listas;
#  - os valores que só existem na primeira lista;
#  - os valores que existem apenas na segunda lista;
#  - uma lista com os elementos não repetidos das duas listas;
#  - a primeira lista sem os elementos repetidos na segunda.

lista1 = [1, 5, 9, 11, 18, 30, 40, 12]
lista2 = [2, 5, 3, 11, 4, 30, 35, 12]
repetidos = []
lista3 = []

print()
print("Valores comuns às duas listas: ", end="")
for n in lista1:
    if n in lista2:
        print(n, end=", ")

print()

print("Valores que só existem na primeira lista: ", end="")
for n in lista1:
    if n not in lista2:
        print(n, end=", ")
        repetidos.append(n)
        lista3.append(n)

print()

print("Valores que existem apenas na segunda lista: ", end="")
for n in lista2:
    if n not in lista1:
        print(n, end=", ")
        repetidos.append(n)

print()

print(f"Uma lista com os elementos não repetidos das duas listas: {repetidos}")
print(f"A primeira lista sem os elementos repetidos na segunda: {lista3}")
print()
