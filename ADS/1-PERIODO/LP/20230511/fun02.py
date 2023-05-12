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

c = 1
win = 0

while True:
    jogada = sum(dados())

    if c == 1: 
        if jogada == 7 or jogada == 11:
            # Natural
            print(f'{jogada} Você tirou um "natural" e ganhou.')
            break

        if jogada == 2 or jogada == 3 or jogada == 12:
            # Craps
            print(f'{jogada} Você tirou um "craps" e perdeu.')
            break
        else:
            c += 1
            win = jogada
            print(win)

    # elif jogada == 7:
    #     # Perde
    #     c += 1
    #     print(f'{jogada} Você perdeu na jogada numero {c}')
    #     break

    else:
        # Continue
        while True:
            jogada = sum(dados())
            print(win)
            if jogada == win:
                c += 1
                print(f'{jogada} Você ganhou na jogada numero {c}')
                break
            elif jogada == 7:
                c += 1
                print(f'{jogada} Você perdeu na jogada numero {c}')
                break
            else:
                input(f'Você tirou {jogada} aperte "ENTER" para continuar')
        break