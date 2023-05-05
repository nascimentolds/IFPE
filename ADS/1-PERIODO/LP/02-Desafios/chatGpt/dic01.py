# Crie um programa que permita que o usuário insira o nome e a idade de cinco pessoas diferentes. 
# Em seguida, o programa deve exibir a média de idade das cinco pessoas, bem como o nome e a idade 
# da pessoa mais velha.

# Para resolver esse desafio, você pode começar criando um dicionário vazio para armazenar 
# as informações das cinco pessoas. Em seguida, use um loop para solicitar que o usuário insira 
# o nome e a idade de cada pessoa, e adicione essas informações ao dicionário.

# Depois que as informações das cinco pessoas forem armazenadas no dicionário, use outro loop para 
# calcular a média de idade e encontrar a pessoa mais velha. Para calcular a média de idade, você 
# pode iterar sobre os valores das idades no dicionário e dividi-los pelo número total de pessoas. 
# Para encontrar a pessoa mais velha, você pode usar o método max() do dicionário para encontrar 
# a idade máxima e, em seguida, iterar sobre as chaves do dicionário para encontrar o nome correspondente.

pessoas = {}

for i in range(2):
    print()
    print(pessoas)
    print()
    
    chave = input(f'Digite o nome da pessoa nº {i+1}: ')
    valor = int(input(f'Digite a idade da pessoa nº {i+1}: '))
    
    pessoas[chave] = valor
    
    print()
    
soma_idades = 0
    
media = sum(pessoas.values()) / len(pessoas)

idade = max(pessoas.values())
for p in pessoas:
    if idade == pessoas[p]:
        pessoa = p

print(f'A média da idade das pessoas é {media}')
print(f'A pessoa com a maior idade é {pessoa} com {idade} anos')

print()

print(pessoas)
    
# # criar dicionário vazio para armazenar informações das pessoas
# pessoas = {}

# # loop para solicitar informações das cinco pessoas
# for i in range(5):
#     nome = input("Digite o nome da pessoa: ")
#     idade = int(input("Digite a idade da pessoa: "))
#     pessoas[nome] = idade

# # calcular média de idade
# media = sum(pessoas.values()) / len(pessoas)

# # encontrar pessoa mais velha
# idade_maxima = max(pessoas.values())
# for nome, idade in pessoas.items():
#     if idade == idade_maxima:
#         pessoa_mais_velha = nome

# # exibir resultados
# print("A média de idade é:", media)
# print("A pessoa mais velha é:", pessoa_mais_velha, "com", idade_maxima, "anos")
