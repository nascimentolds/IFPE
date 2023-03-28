# 7. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa
# sobre um crime. As perguntas são:
# - "Telefonou para a vítima?"
# - "Esteve no local do crime?"
# - "Mora perto da vítima?"
# - "Devia para a vítima?"
# - "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("Responda com 1 se sim ou 0 se não as seguintes perguntas:")
respostas = []

print()
while len(respostas) < 5:
    respostas.append(int(input("Telefonou para a vítima? ")))
    respostas.append(int(input("Esteve no local do crime? ")))
    respostas.append(int(input("Mora perto da vítima? ")))
    respostas.append(int(input("Devia para a vítima? ")))
    respostas.append(int(input("Já trabalhou com a vítima? ")))

c = respostas.count(1)
    
print()
if c > 1 and c <= 2:
    print("A pessoa é Suspeita do crime")
elif c >= 3 and c <= 4:
    print("A pessoa é Cúmplice do crime")
elif c >= 5:
    print("A pessoa é a Assassina")
else:
    print("A pessoa é Inocente")
    