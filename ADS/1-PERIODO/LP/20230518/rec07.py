# 7. Considere a seguinte fórmula para calcular o mdc (máximo divisor comum) 
# de dois números inteiros positivos: 
#   – mdc(a, b) = b, se b divide a (ou seja, a%b == 0) 
#   – mdc(a, b) = mdc(b, a%b), 
# caso contrário. Escreva uma função em Python que, dados dois números, 
# retorne o máximo divisor comum entre eles. Usar recursividade.

def mdc(a, b):
  if a % b == 0:
    return b
  else:
    return mdc(b, a%b)
  
  
print(mdc(50, 18))