# 4. Modifique o programa da questão 3 para que o usuário indique a quantidade de
# alunos que será utilizada no programa. Assim antes de começar a leitura de idades e
# alturas, o programa deve solicitar ao usuário o quantitativo de alunos.

qtde_alunos = int(input("Digite a quantidade de alunos que deseja inserir: "))
alunos = []
soma = 0
result = []

# Armazenando os alunos na lista de alunos
for x in range(qtde_alunos):
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
print(f"Média das Alturas: {media:.2f}")
print()
print("-" * 70)
print(f"{len(result)} alunos com mais de 13 anos estão com altura inferior a média")
print("-" * 70)

