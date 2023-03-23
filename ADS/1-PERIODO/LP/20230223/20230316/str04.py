# 4. Altere o programa anterior de modo que a escada seja invertida.

nome = input("Digite seu nome: ")

for i in range(len(nome)):
    print(nome[0:len(nome)-i])