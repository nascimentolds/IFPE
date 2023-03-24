# Crie um programa que leia um arquivo com nomes diversos 
# e gere outro arquivo com grupos de cinco pessoas escolhidas 
# aleatóriamente. Caso fiquem pessoas sobrando, alocar essas 
# pessoas nos grupos ja criados formando assim alguns grupos 
# de seis pessoas.

from random import choice
arquivo = open('lista.txt', 'r', encoding="utf-8")

lista = []
sorteio = []

# Copiando os nomes que estão no arquivo para a lista
for nome in arquivo:
    val = nome.split()
    lista.append(val[0])

arquivo.close()

# Criando os grupos usando o choice para escolher aleatoriamente
# em seguida remove o nome da lista principal.
# Enquanto a lista for divisilvel por cinco, cria grupos de cinco
# Se não cria grupos de seis.
for nome in lista:
    if len(lista) % 5 == 0:
        nome1 = choice(lista)
        lista.remove(nome1)
        nome2 = choice(lista)
        lista.remove(nome2)
        nome3 = choice(lista)
        lista.remove(nome3)
        nome4 = choice(lista)
        lista.remove(nome4)
        nome5 = choice(lista)
        lista.remove(nome5)

        sorteio.append([nome1, nome2, nome3, nome4, nome5])
    else:
        nome1 = choice(lista)
        lista.remove(nome1)
        nome2 = choice(lista)
        lista.remove(nome2)
        nome3 = choice(lista)
        lista.remove(nome3)
        nome4 = choice(lista)
        lista.remove(nome4)
        nome5 = choice(lista)
        lista.remove(nome5)
        nome6 = choice(lista)
        lista.remove(nome6)

        sorteio.append([nome1, nome2, nome3, nome4, nome5, nome6])

# Imprimindo em arquivo a listagem dos grupos criados.
lista_sorteio = open("sorteio.txt", "w", encoding="utf-8")
c = 1
for grupos in sorteio:
    print('-' * 20, file=lista_sorteio)
    print(f'grupo {c}', file=lista_sorteio)
    print('-' * 20, file=lista_sorteio)

    for nome in grupos:
        print(nome, file=lista_sorteio)

    print(file=lista_sorteio)
    c += 1

lista_sorteio.close()