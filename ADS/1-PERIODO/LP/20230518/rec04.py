# 4. Um problema típico em ciência da computação consiste em converter um número da sua
# forma decimal para a forma binária. Crie uma função recursiva que execute essa conversão.

def binary(n):
  if n == 0:
    bi = 0
  else:
    bi = n % 2 + 10 * binary(n // 2)
  return bi

print(binary(10))