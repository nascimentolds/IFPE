# 7. Faça um programa que leia uma data de nascimento no formato
# dd/mm/aaaa e imprima a data com o mês escrito por extenso. Exemplo:
# Data = 20/02/1995
# Resultado gerado pelo programa:
# Você nasceu em 20 de fevereiro de 1995

data = input("Digite sua data de nascimento: ")

data = data.replace("/", "")

dia = data[0:2]
mes = data[2:4].replace("01", "janeiro").replace("02", "fevereiro").replace("03", "março").replace("04", "abril").replace("05", "maio").replace("06", "junho").replace("07", "julho").replace("08", "agosto").replace("09", "setembro").replace("10", "outubro").replace("11", "novembro").replace("12", "dezembro")
ano = data[4:8]

print(f"Você nasceu em {dia} de {mes} de {ano}")