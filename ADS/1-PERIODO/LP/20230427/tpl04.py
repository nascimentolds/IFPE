alunos = []

while True:
    nome = input('Digite o nome: ').upper()
    idade = int(input('Digite a idade: '))
    nota = int(input('Digite a nota: '))

    alunos.append((nome, idade, nota))

    print('-' * 15)

    con = input('Deseja continuar? (S/N)').upper()

    print('-' * 15)

    if con != 'S':
        break

print('-' * 15)

see = True
while see == True:
    busca = input('Busque pelo nome: ').upper()

    print('-' * 15)

    for i in alunos:
        if busca in i[0]:
            print(i)
            see = False
        else:
            see = False

print(alunos)