# Desafio: Implemente uma função recursiva chamada contagem_regressiva(n) 
# que imprima uma contagem regressiva a partir do número n até 0. 
# Cada número deve ser impresso em uma linha separada, e a função deve 
# terminar quando atingir 0.

def contagem_regressiva(n):
  if n == 0:
    print(n)
  else:
    print(n)
    contagem_regressiva(n-1)
  
contagem_regressiva(10)