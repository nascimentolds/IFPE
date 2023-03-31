import random
r = random

lista = [[], [], [], [], [], [], [], [], [], [], [], []]
for i in range(len(lista)):
    for x in range(12):
        n = r.randint(1, 12)
        lista[i].append(n)

l = int(input("Digite a linha (entre 0 e 11): "))
o = input("Digite S para soma ou M para média: ").upper()

soma = 0

for x in lista[l]:
    soma = soma + x

media = soma / len(lista[l])

if o == "S":
    print(soma)
else:
    print(f'{media:.1f}')
