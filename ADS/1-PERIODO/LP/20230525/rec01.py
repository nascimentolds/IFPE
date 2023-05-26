# 1. Crie uma função recursiva para verificar se uma palavra é palíndromo.
  
def palindromo(palavra):
  palavra = palavra.replace(' ', '')
  if len(palavra) <= 1:
      return True
  elif palavra[0] == palavra[-1]:
      return palindromo(palavra[1:-1])
  else:
      return False
      
print(palindromo('ai la'))
