# Desafio: Implemente uma função recursiva chamada reverter_string(string) 
# que receba uma string como entrada e retorne a string invertida. 
# Por exemplo, se a entrada for "Python", a função deve retornar "nohtyP".

# Seu desafio é implementar a função reverter_string utilizando recursão. 
# Pense em como você pode dividir o problema em partes menores e como a função 
# deve chamar a si mesma para lidar com essas partes menores.

def reverter_string(string):
  if len(string) <= 1:
    return string
  else:
    return reverter_string(string[1:]) + string[0]
  
print(reverter_string("Marcelo"))