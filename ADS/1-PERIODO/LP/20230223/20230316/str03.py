# 3. Faça um programa que solicite uma string ao usuário e
# em seguida a imprima em formato de escada.

nome = input("Digite seu nome: ")

for i in range(len(nome)):
    print(nome[0:i+1])