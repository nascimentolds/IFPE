# 4. Reverso do número. Faça uma função que retorne o reverso de um número
# inteiro informado. Por exemplo: 127 -> 721.

def reverso(n):
    n = str(n)
    return n[::-1]

print(reverso(127))