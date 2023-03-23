# # EX 1
# print("Exercício 1")
# horas_trabalhadas = int(input("Quantas horas trabalhadas? "))
# valor_hora = 50.00
# salario = horas_trabalhadas * valor_hora
# print("Seu salário esse mês é", salario)
# print()

# # EX 2
# print("Exercício 2")
# hora = int(input("Quantas horas estudadas? "))
# minutos = int(input("Quantos minutos estudadas? "))
# total = (hora * 60) + minutos
# print("Você estudou", total, "minutos.")
# print("Você estudou", total * 60, "segundos.")
# print()

# #EX 3
# print("Exercício 3")
# CENTIMETROS = 100
# metros = int(input("Quantos metros? "))
# total_centimetros = metros * CENTIMETROS
# print(metros, "metros é igual a", total_centimetros, "centimetros.")
# print()

# #EX 1
# print("Exercício 1")
# nota1 = float(input("Digite a nota 1: "))
# nota2 = float(input("Digite a nota 2: "))
# nota3 = float(input("Digite a nota 3: "))
# nota4 = float(input("Digite a nota 4: "))

# media = (nota1 + nota2 + nota3 + nota4) / 4
# print("A média bimestral é", media)
# print()

# #EX 2
# print("Exercício 2")
# #A = pi . r²
# PI = 3.14
# area_circulo = PI * pow(5,2)
# print(area_circulo)
# print()

# #EX 3
# print("Exercício 3")
# lados = float(input("Digite a tamanho dos lados do quadrado: "))
# area_quadrado = lados * lados
# print("O dobro da área do quadrado é:", area_quadrado * 2)
# print()

# #EX 4
# print("Exercício 4")
id1 = 10
id2 = 12
id3 = 15
id4 = 17
id5 = 16

media_idades = (id1 + id2 + id3 + id4) / 4
media_idades_nova = (id1 + id2 + id3 + id4 + id5) / 5
percentual = ((media_idades_nova - media_idades) / media_idades) * 100

if(id5 == 16):
    print(media_idades)
    print(f'{percentual:.2f}')
else:
    print(media_idades)  

print('''duas
linhas
outra linha''')