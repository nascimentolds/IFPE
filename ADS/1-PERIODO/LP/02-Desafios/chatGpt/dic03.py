# Crie um programa que permita que o usuário insira o nome e a nota de cinco alunos diferentes 
# em uma disciplina. O programa deve calcular a média das notas dos cinco alunos e exibir 
# um dicionário que mapeia o nome de cada aluno para a sua nota e se ele foi aprovado ou reprovado.

# Para resolver esse desafio, você pode começar criando um dicionário vazio para armazenar 
# as informações dos cinco alunos. Em seguida, use um loop para solicitar que o usuário insira 
# o nome e a nota de cada aluno e adicione essas informações ao dicionário.

# Depois que as informações dos cinco alunos forem armazenadas no dicionário, 
# calcule a média das notas. Em seguida, use um loop para iterar sobre as informações 
# dos alunos e determinar se cada aluno foi aprovado ou reprovado, com base em um critério 
# de nota mínima. Você pode usar uma estrutura de condicional if para atualizar a entrada 
# do dicionário correspondente para indicar se o aluno foi aprovado ou reprovado.

# Finalmente, exiba o dicionário resultante que mapeia o nome de cada aluno para a sua nota 
# e se ele foi aprovado ou reprovado.

# Espero que este desafio seja interessante e útil! Boa sorte!

alunos = {}

media = 7

for i in range(5):
    aluno = input('Digite o nome do aluno: ').upper()
    nota = int(input('Digite a nota do aluno: '))    
    alunos[aluno] = nota
    
for aluno, nota in alunos.items():
    if nota >= media:
        alunos[aluno] = [nota, 'APROVADO']
    else:
        alunos[aluno] = [nota, 'REPROVADO']
        
print(alunos)