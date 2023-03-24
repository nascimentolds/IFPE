# 3. Faça um programa que armazene as idades e as alturas de 4 alunos. Seu programa
# deve exibir quantos alunos com mais de 13 anos possuem uma altura inferior à
# altura média dentre todos os alunos.

alunos = []
soma = 0
result = []

# Armazenando os alunos na lista de alunos
for x in range(4):
    idade = int(input("Idade: "))
    altura = int(input("Altura: "))

    alunos.append([idade, altura])

# Soma da altura dos alunos
for x in alunos:
    soma = soma + x[1]

# Média da Altura dos alunos
media = soma / len(alunos)

# Verificando quais alunos com idade superior a 13 anos 
# que tem altura inferior a média de alturas
for a in alunos:
    if a[0] > 13 and a[1] < media:
        result.append(a)

# Imprimindo o esultado na tela
print()
print("Média das Alturas: ", media)
print()
print("-" * 70)
print(f"{len(result)} alunos com mais de 13 anos estão com altura inferior a média")
print("-" * 70)

