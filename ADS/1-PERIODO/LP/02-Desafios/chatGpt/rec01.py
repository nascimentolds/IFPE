# Desafio: Implemente uma função recursiva chamada soma_recursiva(n) 
# que calcule a soma de todos os números inteiros positivos de 1 a n. 
# Por exemplo, se n for 5, a função deve retornar a soma dos números 
# de 1 a 5, ou seja, 15.

def soma_recursiva(n):
  if n == 1:
    return 1
  else:
    return n + soma_recursiva(n-1)
  
print(soma_recursiva(10))