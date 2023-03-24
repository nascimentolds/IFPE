# 8. Em uma competição de salto em distância cada atleta tem direito a cinco
# saltos. O resultado do atleta será determinado pela média dos cinco valores
# restantes. Você deve fazer um programa que receba o nome e as cinco
# distâncias alcançadas pelo atleta em seus saltos e depois informe o nome,
# os saltos e a média dos saltos. O programa deve ser encerrado quando não
# for informado o nome do atleta. A saída do programa deve ser conforme o
# exemplo abaixo:

atletas = []
x = 0

while x == 0:
    nome = input("Nome do atleta: ")
    
    if nome == "":
        print("Programa encerrado")
        print()
        break
    
    s1 = float(input("Nota do primeiro salto: "))
    s2 = float(input("Nota do segundo salto: "))
    s3 = float(input("Nota do terceiro salto: "))
    s4 = float(input("Nota do quarto salto: "))
    s5 = float(input("Nota do quinto salto: "))
    
    media = (s1+s2+s3+s4+s5) / 5
    
    atletas.append([nome, s1, s2, s3, s4, s4, media])    
    print()
    
for a in atletas:
    print("-" * 30)
    print(f"Atleta: {a[0]}")
    print()    
    print(f"Primeiro Salto: {a[1]:.1f} m")
    print(f"Segundo Salto: {a[2]:.1f} m")
    print(f"Terceiro Salto: {a[3]:.1f} m")
    print(f"Quarto Salto: {a[4]:.1f} m")
    print(f"Quinto Salto: {a[5]:.1f} m")
    print()
    print("Resultado Final:")
    print(f"Atleta: {a[0]}")
    print(f"Saltos: {a[1]:.1f} - {a[2]:.1f} - {a[3]:.1f} - {a[4]:.1f} - {a[5]:.1f}")
    print(f"Média dos saltos: {a[6]:.1f} m")
    print()
    
print(atletas)