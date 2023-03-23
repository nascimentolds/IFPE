# 9. Escreva um programa que leia duas strings e gere uma terceira com
# os caracteres comuns às duas strings lidas. 
# - 1a string: AAACTBF
# - 2a string: CBT
# - Resultado: CBT
# - A ordem dos caracteres da string gerada não é importante, mas deve
# conter todas as letras comuns a ambas.

s1 = "AAACTBF"
s2 = "CBT"

for x in s2:
    if x in s1:
        print(x, end="")