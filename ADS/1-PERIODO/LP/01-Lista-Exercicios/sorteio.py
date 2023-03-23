from random import choice
from time import sleep

lista = []

j1 = ['Jose', 'Bruno', 'Lucas', 'Eduardo', 'Pedro',
      'Luciano', 'Vitor', 'Diego', 'Rômulo', '*Pisca']
j2 = ['Carlinhos', 'Carlos', 'Davi', 'Thiago', 'Paulo',
      'Igor', 'Felipe', 'Marcelo', 'Matheus', 'Fabio']
j3 = ['Artur', 'Anderson', 'Gustavo', 'Rogerio', 'Marcus',
      'Nando', 'Jorge', 'Rodrigo', 'Caio', 'Jonas']

for c in range(1, 11):
    print('PROCESSANDO.....')
    sleep(2)
    print('-' * 20)
    print(f'      \033[34mEQUIPE {c}\033[m')
    print('-' * 20)
    #
    j1_player = choice(j1)
    j1.remove(j1_player)
    j2_player = choice(j2)
    j2.remove(j2_player)
    j3_player = choice(j3)
    j3.remove(j3_player)
    #
    sorteio = (f'{j1_player}\n'
               f'{j2_player}\n'
               f'{j3_player}')
    print(sorteio)
    print('-' * 20)


# import random

# arquivo = open('lista.txt', 'r', encoding="utf-8")
# nomes = arquivo.readlines()

# lista = [[] for _ in range(3)]

# for lista in range(3):
#     print(lista)

# # while len(lista) < 3:
# #     for x in lista:
# #         print("lista")

#     # sel = random.choice(nomes)

#     # if sel not in lista[0]:
#     #     lista[0].append(sel)

# # while len(lista) < 3:
# #     lista.append(l)

# # arquivo.close()

# # print(l)
# # print(lista)

# # for nome in lista:
# #     print(nome)

# # while len(lista) < 3:
# #     sel = random.choice(nomes)
# #     if sel not in lista:
# #         lista.append(sel)


# # while len(lista[0]) < 3:
# #     sel = random.choice(nomes)

# #     if sel not in lista[0]:
# #         lista[0].append(sel)
