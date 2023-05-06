# 7. Desenvolva um jogo da forca. 
# - O programa deverá ter um repositório de palavras armazenadas em uma estrutura, contendo “palavra” e “dica”. 
# - O programa deverá escolher aleatoriamente cada palavra e a dica deverá ser mostrada ao usuário. 
# - O jogador poderá errar 6 vezes antes de ser enforcado.

# Importando a biblioteca random
import random
r = random

# Criando as listas que serão usadas no sistema
palavras = ['PONTE', 'CHAVE', 'MARTELO', 'ARARA', 'PSICOLOGO', 'REFRIGERANTE', 'GUITARRA', 'BRASIL', 'PERNAMBUCO']
dica = ['POR CIMA', 'ABRE', 'BATE', 'PÁSSARO', 'PROFISSÃO', 'BEBIDA', 'INSTRUMENTO', 'PAIS', 'ESTADO']
escolha = []
letras = []

# definindo o indice de pesquisa aleatório para a escolha da palavra
op = r.randrange(len(palavras))

# Iniciando o contador de jogadas
c = 0
jogadas = 6

# Escolhendo a palavra para o jogo
palavra = palavras[op]

# Imprimindo a dica
print('-' * 20)
print('Dica:', dica[op])
print('-' * 20)

# Criando o tabuleiro do jogo
for p in palavra:
    escolha.append('_')
   
while True:
    print()
    # Solicitando a letra ao usuário
    guess = input('Digite uma letra: ').upper()
    
    # Verifica se a letra ja foi digitada antes.
    # Se não foi, verifica se a letra é compativel com as letras da palavra.
    if guess not in letras:  
        letras.append(guess)  
        if guess in palavra:
            for p in range(len(palavra)):
                if guess == palavra[p]:
                    escolha[p] = guess
        else:            
            c += 1
            print(f'Você errou pela {c}º vez')
    else:
        print('Voce já digitou essa letra')
        
    # Criando a apresentação da adivinhação e a palavra
    # que será com parada com palavra escolhida aleatóriamente para adivinhação.
    g = ''
    s = ''
    for i in escolha:
        g += i
        s += i + ' '    
    
    # Imprimindo a tentativa de adivinhação com as letras ecolhidas.
    print()
    print(f'A palavra é: {s}')
    print()
    
    # Verifica se a palavra final é igual a palavra escolhida.
    # Caso seja igual, o usuário ganha.
    if g == palavra:
        print('-' * 40)
        print(f'Você ganhou! A palavra é {palavra}!')
        print('-' * 40)
        break
    
    # Verifica a quantidade de jogadas, 
    # se zerar a quantidade de jogadas o usuário perde.
    if c == jogadas:
        print('-' * 40)
        print(f'Você perdeu! A palavra é {palavra}!')
        print('-' * 40)
        break
