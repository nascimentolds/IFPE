# 5. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita
# da direita para esquerda ou vice-versa. Por exemplo: OSSO e OVO são
# palíndromos. Em textos mais complexos os espaços e pontuação são
# ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma
# onde os espaços foram ignorados. Faça um programa que leia uma
# seqüência de caracteres, mostre-a e diga se é um palíndromo ou não.

pal = input("Digite um PALINDROMO: ")
pal2 = pal.replace(" ", "")

if pal2.startswith(pal2[::-1]): 
   res =  "É um PALÍNDROMO"
else:
   res =  "Não é um PALÍNDROMO"

print(f"{pal} {res}")