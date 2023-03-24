# 6. Faça um programa que leia uma data de nascimento no formato
# dd/mm/aaaa e imprima a data com o mês escrito por extenso. 
#  - Exemplo:
#  - Data = 20/02/1995
#  - Resultado gerado pelo programa:
#  - Você nasceu em 20 de fevereiro de 1995

meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

data = input("Digite sua data de nascimento: ")
dia = data[0:2]
mes = data[3:5]
mes = int(mes)
ano = data[6:]

print(f"Você nasceu em {dia} de {meses[mes-1]} de {ano}")





