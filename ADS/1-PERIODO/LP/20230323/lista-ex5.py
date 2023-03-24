# 5. Modifique o programa da questão 3 para que o programa funcione para qualquer
# quantidade de alunos. Assim, durante a leitura das idades e alturas o usuário poderá
# inserir um valor negativo para indicar que deseja interromper a leitura dos dados.

alunos = []
soma = 0
result = []
x = 0


# Armazenando os alunos na lista de alunos
while x >= 0:
    idade = int(input("Idade: "))
    
    if idade < 0:
        break
    
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
print(alunos)
print()
print("-" * 70)
print(f"{len(result)} alunos com mais de 13 anos estão com altura inferior a média")
print("-" * 70)

