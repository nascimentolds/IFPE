from random import choice
arquivo = open('lista.txt', 'r', encoding="utf-8")

lista = []
sorteio = []

for n in arquivo:
    val = n.split()
    lista.append(val[0])

arquivo.close()

for s in lista:
    p1 = choice(lista)
    lista.remove(p1)
    p2 = choice(lista)
    lista.remove(p2)
    p3 = choice(lista)
    lista.remove(p3)
    p4 = choice(lista)
    lista.remove(p4)
    p5 = choice(lista)
    lista.remove(p5)

    sorteio.append([p1, p2, p3, p4, p5])

print(lista)
print(sorteio)

c = 1
for n in sorteio:
    print('-' * 20)
    print(f'grupo {c}')
    print('-' * 20)

    for p in n:
        print(p)

    print()
    c += 1
