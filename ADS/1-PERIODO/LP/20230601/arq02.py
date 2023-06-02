# 1. Usando o arquivo texto notas_estudantes.txt escreva um programa que
# imprime o nome dos alunos que têm mais de seis notas.

with open('notas_estudantes.txt', 'r') as file:
    for line in file:
        a = line.split()

        if len(a)-1 > 6:
            print(a[0])