# Desafio: Implemente uma função recursiva chamada potencia(base, expoente) 
# que calcule a potência de um número base elevado a um expoente inteiro não negativo. 
# A função deve retornar o resultado da potenciação.

# Por exemplo, se a base for 2 e o expoente for 3, a função deve retornar 8, 
# pois 2 elevado a 3 é igual a 8.

def potencia(base, expoente):
  if expoente == 0:
    return 1
  else:
    return base * potencia(base, expoente-1)
  
print(potencia(5, 0))