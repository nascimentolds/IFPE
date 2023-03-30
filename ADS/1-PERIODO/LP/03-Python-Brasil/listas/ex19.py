# 19 .Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete 
# feita a um grande quantidade de organizações:

# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro

# Você foi contratado para desenvolver um programa que leia o resultado da enquete 
# e informe ao final o resultado da mesma. O programa deverá ler os valores até ser 
# informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores 
# além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções 
# devem ser armazenados num vetor. Após os dados terem sido completamente informados, 
# o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor 
# da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

## CÓDIGO DO SISTEMA ##
# Criada uma lista com sublistas dos sistemas operacionais, seus votos e seus percentuais
sistemas_operacionais = [
    ['Windows Server', 0, 0], 
    ['Unix', 0, 0], 
    ['Linux', 0, 0], 
    ['Netware', 0, 0], 
    ['Mac OS', 0, 0], 
    ['Outro', 0, 0]
]

print()
print('Qual o melhor Sistema Operacional para uso em servidores?')
print('-' * 57)

# Imprimindo as opções de votos na tela
for x in range(len(sistemas_operacionais)):
    print(f'{x+1} - {sistemas_operacionais[x][0]}')
    
print('-' * 57)

# Validação para verificar se os votos estão dentro dos paramentros 
# solicitados e adicionando os votos a lista
while True:
    voto = int(input('Qual a sua opção? '))
    
    if voto > 0 and voto <= 6:
        if voto == 1: sistemas_operacionais[0][1] += 1
        if voto == 2: sistemas_operacionais[1][1] += 1
        if voto == 3: sistemas_operacionais[2][1] += 1
        if voto == 4: sistemas_operacionais[3][1] += 1
        if voto == 5: sistemas_operacionais[4][1] += 1
        if voto == 6: sistemas_operacionais[5][1] += 1
    elif voto == 0:
        break
    else:
        continue

# Calculando o total de votos   
total_votos = 0
for v in range(len(sistemas_operacionais)):
    total_votos = total_votos + sistemas_operacionais[v][1]

# Calculando o percentual de votos e adicionando a lista
for p in range(len(sistemas_operacionais)):
    sistemas_operacionais[p][2] += (sistemas_operacionais[p][1] * 100) / total_votos

# Imprimindo o resultado da pesquisa
print()
print('-' * 35)
print('RESULTADO DA PESQUISA')
print('-' * 35)
print()

print('Sistema Operacional     Votos   %')
print('-------------------     -----   ---')

for sis in sistemas_operacionais:
    pct = f'{sis[2]:.0f}'
    print(sis[0], end=' ' * (29 - len(sis[0]) - len(str(sis[1]))))
    print(sis[1], end=' ' * (5 - len(str(pct))))
    print(f'{pct}%')

print('-------------------     -----')
print(' ' * (28 - len(str(total_votos))), total_votos)
print()

# Criar uma lista para recolher cada quantidade de votos
votos = []

# Adicionando os votos a lista criada antes
for a in sistemas_operacionais:
    votos.append(a[1])

# Verificando qual foi a maior quantidade de votos 
vencedor = max(votos)

# Verfica dentre todos os da lista qual foi o mais votado
# comparando com o que teve a maior quantidade de votos da lista anterior.
# Imprimindo a linha final com o resultado da pesquisa.
for m in sistemas_operacionais:
    if vencedor in m:
        print(f'O Sistema Operacional mais votado foi o {m[0]}, com {m[1]} votos, correspondendo a {m[2]:.0f}% dos votos.')