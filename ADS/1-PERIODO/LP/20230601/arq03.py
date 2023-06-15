# 2. Usando o arquivo texto notas_estudantes.txt, escreva um programa que
# calcula a média das notas de cada estudante e imprime o nome e a média
# de cada estudante.

with open("notas_estudantes.txt", "r") as file: 
  for line in file:
    a = line.split()
    notas = list(map(int, a[1:]))    
    media = sum(notas) / len(a[1:])
    
    print(f"{a[0]} - {media:.0f}")