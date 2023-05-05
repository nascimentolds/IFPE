# 4. Dado um dicionário de palavras e suas traduções em diferentes
# idiomas (considere inglês, português, espanhol e francês), como você
# encontraria todas as palavras que começam com uma determinada
# letra(considere chaves e valores)?

dic = {
    'ingles' : ['ball', 'table', 'wallet'],
    'portugues' : ['bola', 'mesa', 'carteira'],
    'espanhol' : ['pelota', 'mesa', 'portafolio'],
    'frances' : ['balle', 'tableau', 'portefeuille']
}

l = input('Digite a letra: ')

for i in dic:
    for x in dic[i]:
        if x[0] == l:
            print(f'{i} - {x}')