# 11.Escreva um programa que leia uma string e imprima quantas vezes
# cada caractere aparece nessa string. 
# - String: TTAAC
# - Formato de saída:
# - T: 2x
# - A: 2x
# - C: 1x

s1 = "TTAAC"
t = s1.count("T")
a = s1.count("A")
c = s1.count("C")

print(s1)
print(f"T: {t}x.")
print(f"A: {a}x.")
print(f"C: {c}x.")