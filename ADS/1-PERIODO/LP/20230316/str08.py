# 8. Escreva um programa que leia duas strings. Verifique se a segunda
# ocorre dentro da primeira e imprima a posição de início. 
#  1a string: AABBEFAATT
#  2a string: BE
#  Resultado: BE encontrado na posição 3 de AABBEFAATT

s1 = "AABBEFAATT"
s2 = "BE"

print(f"{s2} encontrado na posição {s1.find(s2)} de {s1}")