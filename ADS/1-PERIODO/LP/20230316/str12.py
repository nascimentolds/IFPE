# 12. Número por extenso. Escreva um programa que solicite ao usuário a
# digitação de um número até 99 e imprima-o na tela por extenso.

n = input("Digite um número de 0 a 99: ")

if len(n) > 1:
    
    if n[-1] == "1": um = "um"
    elif n[-1] == "2": dois = "dois"
    elif n[-1] == "3": tres = "tres"
    elif n[-1] == "4": quatro = "quatro"
    elif n[-1] == "5": cinco = "cinco"
    elif n[-1] == "6": seis = "seis"
    elif n[-1] == "7": sete = "sete"
    elif n[-1] == "8": oito = "oito"
    elif n[-1] == "9": nove = "nove"
    
    if n[0] == "1": print("dez")
    if n[0] == "2": 
        vinte = "vinte"
        if n[-1] == "1": print(f'{vinte} e {um}')
        elif n[-1] == "2": print(f'{vinte} e {dois}')
        elif n[-1] == "3": print(f'{vinte} e {tres}')
        elif n[-1] == "4": print(f'{vinte} e {quatro}')
        elif n[-1] == "5": print(f'{vinte} e {cinco}')
        elif n[-1] == "6": print(f'{vinte} e {seis}')
        elif n[-1] == "7": print(f'{vinte} e {sete}')
        elif n[-1] == "8": print(f'{vinte} e {oito}')
        elif n[-1] == "9": print(f'{vinte} e {nove}')
        else: print(vinte)
else:
    if n == "1": print("um")
    elif n == "2": print("dois")
    elif n == "3": print("tres")
    elif n == "4": print("quatro")
    elif n == "5": print("cinco")
    elif n == "6": print("seis")
    elif n == "7": print("sete")
    elif n == "8": print("oito")
    elif n == "9": print("nove")
    else: print("zero")