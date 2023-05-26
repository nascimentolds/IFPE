# 6. Escreva uma função recursiva que determine quantas vezes um dígito K 
# ocorre em um número natural N. Por exemplo, o dígito 2 ocorre 3 vezes em 762021192.

def digitos(n):
    # if n < 1:
    #     return 0
    # else:
    #    return 1 + digitos(n // 10)

    a = n // 10
    b = n % a
    print(b)

num = 156
print(digitos(num))
