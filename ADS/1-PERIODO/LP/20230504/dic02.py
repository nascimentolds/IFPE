# 2. Escreva um programa que receba uma lista de palavras como
# argumento e retorne um dicionário onde as chaves são as palavras
# únicas e os valores são a contagem de ocorrências de cada palavra.

teste = "Escreva um programa que receba uma lista de palavras como argumento e retorne um dicionário onde as chaves são as palavras únicas e os valores são a contagem de ocorrências de cada palavra."
lista1 = teste.split()

lista = ['guitarra', 'guitarra', 'guitarra', 'baixo', 'baixo', 'baixo', 'baixo', 'bateria', 'bateria']
dic = {}

for i in lista1:
    dic[i] = lista1.count(i)

print(dic)