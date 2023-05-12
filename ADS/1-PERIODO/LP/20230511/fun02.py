# 2. Faça um programa de implemente um jogo de Craps. 
# - O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
# - Se, na primeira jogada, você tirar 7 ou 11, você tirou um "natural" e ganhou. 
# - Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
# - Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". 
#   Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
#   Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

def dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    return [dado1, dado2]

jogada = dados()
print(f'Jogada - {jogada}')
print()

soma = sum(jogada)

if soma == 7 or soma == 11:
    # Natural
    print(f'{soma} - Você tirou um "natural". Você ganhou.')

elif soma == 2 or soma == 3 or soma == 12:
    # Craps
    print(f'{soma} - Você tirou um "craps". Você perdeu.')
    
else:
    print(f'Você tirou um {soma} e deve tirar o mesmo número para ganhar.')
    print(f'Mas se tirar um 7 antes disso, você perde')
    print()
    input(f'{soma} - Aperte "ENTER" para continuar jogando.')
    print()
    while True:
        jogada_nova = dados()        
        soma_nova = sum(jogada_nova)
        
        if soma_nova == soma:
            print(f'{soma_nova} - Parabéns! Você ganhou.')
            break
        elif soma_nova == 7:
            print(f'{soma_nova} - Sinto muito! Você perdeu.')
            break
        else:
            input(f'{soma_nova} - Aperte "ENTER" para continuar jogando.')
            print()