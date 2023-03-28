# 6. Faça um programa que simule um lançamento de dados. Lance o dado 100
# vezes e armazene os resultados em uma lista. Utilize uma lista de
# contadores (1-6) e depois da execução dos sorteios, mostre quantas vezes
# cada valor foi conseguido. 
# - Dica: sorteios em python podem ser realizados através da biblioteca random, 
#   pelas funções randint() e randrange(). 
# - Documentação: https://docs.python.org/pt-br/3.8/library/random.html

import random
jogadas = 100

contadores = [0, 0, 0, 0, 0, 0]
resultados = []

for resultado in range(jogadas):
    resultado = random.randint(1, 6)
    resultados.append(resultado)
    
for resultado in resultados:
    contadores[resultado-1] += 1
    
for i in range(6):
    print(f'{i+1} - {contadores[i]} vezes')
    

# dado = [1, 2, 3, 4, 5, 6]
# sorteio = []
# jogadas = 100

# for x in range(1, jogadas+1):
#     j = random.randint(1, len(dado))
#     sorteio.append(j)
    
# for n in dado:
#     print(f"Posição {n} - {sorteio.count(n)} vezes.")

# -------------------------------------------------------
# import random

# # Define o número de lançamentos
# num_lancamentos = 100

# # Cria uma lista vazia para armazenar os resultados
# resultados = []

# # Realiza os lançamentos e armazena os resultados na lista
# for i in range(num_lancamentos):
#     resultado = random.randint(1, 6)
#     resultados.append(resultado)

# # Cria uma lista de contadores
# contadores = [0, 0, 0, 0, 0, 0]

# # Conta quantas vezes cada valor foi conseguido
# for resultado in resultados:
#     contadores[resultado - 1] += 1

# # Mostra os resultados
# for i in range(6):
#     print(f"O valor {i+1} foi conseguido {contadores[i]} vezes.")