# 10.Conta espaços e vogais. Dado uma string com uma frase informada
# pelo usuário (incluindo espaços em branco), conte: quantos espaços
# em branco existem na frase. quantas vezes aparecem as vogais a, e, i,
# o, u.

s1 = input("Digite uma frase: ")
esp = s1.count(" ")
a = s1.count("a")
e = s1.count("e")
i = s1.count("i")
o = s1.count("o")
u = s1.count("u")

print(f"Sua frase tem {esp} espaços em branco.")
print(f"Sua frase tem {a} letras a.")
print(f"Sua frase tem {e} letras e.")
print(f"Sua frase tem {i} letras i.")
print(f"Sua frase tem {o} letras o.")
print(f"Sua frase tem {u} letras u.")