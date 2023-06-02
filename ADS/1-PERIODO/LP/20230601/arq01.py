arq = open('arq01.txt', 'r')

for linha in arq:
    val = linha.split()

    print('QB', val[0], val[1], 'Obteve a avaliação', val[10])

arq.close()