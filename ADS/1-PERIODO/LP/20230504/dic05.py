# 5. Escreva um programa que determine o menor número inteiro positivo
# que pode ser dividido por todos os números de 1 a 20 sem deixar
# resto.
 
def mmc(a, b):
    """
    Retorna o mínimo múltiplo comum entre dois números.
    """
    m = a * b
    while a % b != 0:
        a, b = b, a % b
    return m // b

mmc_total = 1
for i in range(1, 21):
    mmc_total = mmc(mmc_total, i)

print(mmc_total)