# Crie um programa que leia um arquivo com nomes diversos 
# e gere outro arquivo com grupos de cinco pessoas escolhidas 
# aleatoriamente. Caso fiquem pessoas sobrando, alocar essas 
# pessoas nos grupos ja criados, formando assim alguns grupos 
# com 6 pessoas.

# O programa deve receber como entrada um arquivo de texto (.txt) 
# onde cada linha contém um nome de um aluno e deve distribuir 
# os participantes aleatoriamente em grupos de 5 pessoas. 
# Caso sobrem alguns alunos, estes devem ser distribuidos 
# entre os grupos formados, de forma que ao final do sorteio, 
# nenhum grupo tenha mais que 6 participantes.

from random import choice
arquivo = open('lista.txt', 'r', encoding="utf-8")

nomes = []
grupos = []

# Copiando os nomes que estão no arquivo para a lista
for nome in arquivo:
    val = nome.split()
    nomes.append(val[0])

arquivo.close()

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
lista_sorteio = open("grupos.txt", "w", encoding="utf-8")
c = 1
for grupo in grupos:
    print('-' * 20, file=lista_sorteio)
    print(f'GRUPO {c}', file=lista_sorteio)
    print('-' * 20, file=lista_sorteio)

    for nome in grupo:
        print(nome, file=lista_sorteio)

    print(file=lista_sorteio)
    c += 1

lista_sorteio.close()