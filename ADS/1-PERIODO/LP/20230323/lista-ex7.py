# 7. Faça um programa que receba a temperatura média de cada mês do ano e
# armazene-as em uma lista. Após isto, calcule a média anual das
# temperaturas e mostre todas as temperaturas acima da média anual, e em
# que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

temperaturas_do_ano = []
total_temperaturas = 0

# Armazenando as informações dos meses e temperaturas no array
for t in range(len(meses)):
    mes = int(input("Digite o mês: "))
    temperatura = int(input("Digite a temperatura média do mês: "))
    
    temperaturas_do_ano.append([mes, meses[t], temperatura])
    
# Somando todas as temperaturas
for t in temperaturas_do_ano:
    total_temperaturas += t[2]

# Média das temperaturas
media_temperaturas = total_temperaturas / len(meses)

# Imprimindo o resultado na tela
print()
print("-" * 20)
print(
'''TEMPERATURAS ACIMA
DA MÉDIA ANUAL'''
)
print("-" * 20)

for t in temperaturas_do_ano:
    if t[2] > media_temperaturas:
        print(f"{t[0]} - {t[1]}: {t[2]}°")
        
print()
print(f"Média anual: {media_temperaturas:.0f}°")
print("-" * 20)