indice = float(input("Qual o índice de poluição? "))

if (indice >= 0.5):
    print("Todas as industrias devem paralisar suas atividades.")
elif (indice >= 0.4):
    print("As indústrias do 1º e 2º grupo devem suspender suas atividades.")
elif (indice >= 0.3):
    print("As indústrias do 1º grupo devem suspender suas atividades.")
elif (indice <= 0.29):
    print("Índice de poluição aceiável.")
