# 2. Implemente uma função recursiva que, dados dois números inteiros x e n, 
# calcula o valor de x^n.

def pot(x, n):
    if n == 0:
        return 1
    else:
        return x * pot(x, n-1)

print(pot(5, 3))