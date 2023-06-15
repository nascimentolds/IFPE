# 4. Escreva um programa para sortear os próximos times da próxima maratona
# de programação. Leia um arquivo com nome de estudantes e forme grupos de 5 pessoas. 

from random import choice
arquivo = 'lista.txt'

nomes = []
grupos = []

# Copiando os nomes que estão no arquivo para a lista
with open(arquivo, 'r', encoding="utf-8") as file:
  for nome in file:
      val = nome.split()
      nomes.append(val[0])

# Criando os grupos usando o choice para escolher aleatoriamente
# em seguida remove o nome da lista principal.
# Enquanto a lista for maior ou igual a cinco, cria grupos de cinco
while len(nomes) >= 5: 
    nome1 = choice(nomes)
    nomes.remove(nome1)
    nome2 = choice(nomes)
    nomes.remove(nome2)
    nome3 = choice(nomes)
    nomes.remove(nome3)
    nome4 = choice(nomes)
    nomes.remove(nome4)
    nome5 = choice(nomes)
    nomes.remove(nome5)

    grupos.append([nome1, nome2, nome3, nome4, nome5])
   
# Adiciona os remanecentes da lista aos grupos ja existentes
# A variável i é utilizada para controlar em qual grupo o próximo 
# nome deve ser adicionado. Se todos os grupos já tiverem recebido um nome, 
# i é reiniciado para o primeiro grupo novamente.
i = 0
while nomes:
    if i == len(grupos):
        i = 0

    grupo = grupos[i]
    nome = nomes.pop(0)
    grupo.append(nome)
    i += 1

# Imprimindo em arquivo a listagem dos grupos criados.
with open("grupos2.txt", "w", encoding="utf-8") as file:
  c = 1
  for grupo in grupos:
      print('-' * 20, file=file)
      print(f'GRUPO {c}', file=file)
      print('-' * 20, file=file)

      for nome in grupo:
          print(nome, file=file)

      print(file=file)
      c += 1