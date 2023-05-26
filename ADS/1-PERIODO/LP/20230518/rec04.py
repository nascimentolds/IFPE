# 4. Um problema típico em ciência da computação consiste em converter um número da sua
# forma decimal para a forma binária. Crie uma função recursiva que execute essa conversão.

def binary(n):
  if n == 0:
    return 0
  else:
    return n % 2 + 10 * binary(n // 2)

print(binary(10))