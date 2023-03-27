# 2. Escreva um algoritmo para ler as dimensões de uma cozinha retangular
# (comprimento, largura e altura) e em seguida, calcular e escrever a
# quantidade de caixas de azulejos para se colocar em todas as suas paredes
# (considere que não será descontada a área ocupada por portas e janelas). 
# Cada caixa de azulejos possui 1,5 m2.

caixa = 1.5

comprimento = float(input("Comprimento: "))
largura = float(input("Largura: "))
altura = float(input("altura: "))

area = (comprimento * altura * 2) + (largura * altura * 2)

print(area / caixa)
