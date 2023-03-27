# 3. Qualquer número natural de quatro algarismos pode ser dividido em duas dezenas
# formadas pelos seus dois primeiros e dois últimos dígitos. (1297 = 12 e 97; 5314 =
# 53 e 14). Escreva um algoritmo que lê um número inteiro n (de 4 algarismos) e
# verifica se a raiz quadrada de n é igual a soma das dezenas de n. 
#  - Ex.: n = 9801, dezenas de n = 98 + 01, soma das dezenas = 99, raiz quadrada
#    de n = 99. Portanto, a raiz quadrada de 9801 é igual a soma de suas dezenas.

n = int(input("Digite um número de 4 digitos: "))
n1 = n // 100
n2 = n - (n1 * 100)

n3 = n1 + n2
r = n**0.5

print()
if n3 == r:
    print("Acertou Miseravel!")
else:
    print("Errrrroouuu!")