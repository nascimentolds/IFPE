# Crie um programa que simule um sistema de votação. O programa deve permitir que os usuários 
# votem em diferentes opções e, em seguida, exibir os resultados da votação.

# Para resolver esse desafio, você pode começar criando um dicionário vazio para armazenar as 
# opções de voto e suas contagens. Em seguida, use um loop para solicitar que os usuários insiram 
# seu voto. Você pode exibir as opções disponíveis e permitir que eles digitem o número 
# correspondente à opção desejada. Atualize a contagem do voto correspondente no dicionário.

# Depois que todos os votos forem registrados, você pode exibir os resultados da votação. 
# Isso pode ser feito iterando sobre as chaves do dicionário e exibindo a opção de voto 
# e o número de votos correspondente.

# Esse desafio é uma ótima oportunidade para explorar diferentes estruturas de controle, 
# como loops e condicionais, para lidar com a entrada do usuário e atualizar as contagens de votos.

votacao = {
    'Python' : 0,
    'PHP' : 0,
    'Javascript' : 0,
    'Java' : 0,
    'C#' : 0
}

c = 1
for v in votacao:
    print(f'[{c}] - {v}')
    c += 1
print('[6] - Sair da votação')
print()
while True:
    opcao = int(input('Escolha sua linguagem de programação preferida: '))
    
    if opcao == 1: votacao['Python'] += 1
    elif opcao == 2: votacao['PHP'] += 1
    elif opcao == 3: votacao['Javascript'] += 1
    elif opcao == 4: votacao['Java'] += 1
    elif opcao == 5: votacao['C#'] += 1
    else: break
    
print()
for c, v in votacao.items():
    print(f'{c} obteve {v} Votos.') 
