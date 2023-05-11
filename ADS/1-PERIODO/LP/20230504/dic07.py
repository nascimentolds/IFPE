# 7. Desenvolva um jogo da forca. 
# - O programa deverá ter um repositório de palavras armazenadas em uma estrutura, contendo “palavra” e “dica”. 
# - O programa deverá escolher aleatoriamente cada palavra e a dica deverá ser mostrada ao usuário. 
# - O jogador poderá errar 6 vezes antes de ser enforcado.

# Importando a biblioteca random
import random
r = random

# Criando as listas que serão usadas no sistema
palavras = ['PONTE', 'CHAVE', 'MARTELO', 'ARARA', 'PSICOLOGO', 'REFRIGERANTE', 'GUITARRA', 'BRASIL', 'PERNAMBUCO', 'SERRA TALHADA']
dicas = ['POR CIMA', 'ABRE', 'BATE', 'PÁSSARO', 'PROFISSÃO', 'BEBIDA', 'INSTRUMENTO', 'PAIS', 'ESTADO', 'CIDADE']

# Lista para armazenar todas as letras corretas
letras_corretas = []

# Lista para armazenar todas as letras escolhidas
letras_escolhidas = []

# definindo o indice de pesquisa aleatório para a escolha da palavra
indice_aleatorio = r.randrange(len(palavras))

# Iniciando o contador de jogadas
c = 0
jogadas = 6

# Escolhendo a palavra para o jogo
palavra_escolhida = palavras[indice_aleatorio]

# Imprimindo a dica
print('-' * 20)
print('Dica:', dicas[indice_aleatorio])
print('-' * 20)

# Criando o tabuleiro do jogo
for p in palavra_escolhida:
    letras_corretas.append('_')
   
while True:
    print()
    # Solicitando a letra ao usuário
    palpite = input('Digite uma letra: ').upper()
    
    # Verifica se a letra ja foi digitada antes.
    # Se não foi, verifica se a letra é compativel com as letras da palavra.
    if palpite not in letras_escolhidas:  
        letras_escolhidas.append(palpite)  
        if palpite in palavra_escolhida:
            for p in range(len(palavra_escolhida)):
                if palpite == palavra_escolhida[p]:
                    letras_corretas[p] = palpite
        else:            
            c += 1
            print(f'Você errou pela {c}º vez')
            if c == jogadas - 1:
                print('Se você errar mais uma vez você perde!')
    else:
        print('Voce já digitou essa letra')
        
    # Criando a apresentação da adivinhação e a palavra
    # que será com parada com palavra escolhida aleatóriamente para adivinhação.
    palpite_final = ''.join(letras_corretas)
    mostra_palpites = ' '.join(letras_corretas)
    # for i in letras_corretas:
    #     palpite_final += i
    #     mostra_palpites += i + ' '    
    
    # Imprimindo a tentativa de adivinhação com as letras ecolhidas.
    print()
    print(f'A palavra é: {mostra_palpites}')
    print()
    
    # Verifica se a palavra final é igual a palavra escolhida.
    # Caso seja igual, o usuário ganha.
    if palpite_final == palavra_escolhida:
        print('-' * 40)
        print(f'Você ganhou! A palavra é {palavra_escolhida}!')
        print('-' * 40)
        break
    
    # Verifica a quantidade de jogadas, 
    # se zerar a quantidade de jogadas o usuário perde.
    if c == jogadas:
        print('-' * 40)
        print(f'Você perdeu! A palavra é {palavra_escolhida}!')
        print('-' * 40)
        break
