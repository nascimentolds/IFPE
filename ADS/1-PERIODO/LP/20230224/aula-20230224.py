# #EX 1
# print("Exercício 1")
# lados = float(input("Digite a tamanho dos lados do quadrado: "))
# area_quadrado = lados * lados
# print(f"A área do quadrado é: {area_quadrado:.2f}")
# print()

# #EX 2
# print("Exercício 2")
# base = float(input("Digite a base do triangulo: "))
# altura = float(input("Digite a altura do triangulo: "))
# area_triangulo = (base * altura) / 2
# print("A área do triangulo é: {:.2f}".format(area_triangulo))
# print()

# #EX 3
# print("Exercício 3")
# #A = pi . r²
# #C = 2 * π * r
# PI = 3.14
# raio = float(input("Digite o valor do raio do circulo: "))
# area_circulo = PI * pow(5,2)
# perimetro_circulo = 2 * PI * raio
# diametro_circulo = raio * 2
# print('''A área do circulo é {:.2f}
# O perimetro do circulo é {:.2f}
# O diametro do circulo é {:.2f} '''.format(area_circulo, perimetro_circulo, diametro_circulo))
# print()

# #EX 4
print("Exercício 4")
PRECO = 80.00
area = float(input("Digite a área em metros quadrados a ser pintada: "))
area_coberta_lata = 18 * 3
latas_necessarias = area / area_coberta_lata
latas_arredondadas = int(latas_necessarias)

if(latas_arredondadas < latas_necessarias):
    latas_arredondadas+= 1


print(f'''Qtde de latas: {latas_arredondadas}
Valor Total: {latas_arredondadas * PRECO:.2f}''')





