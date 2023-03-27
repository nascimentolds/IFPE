# 1. Crie um algoritmo que receba um número inteiro, conte o número total de
# dígitos e mostre o resultado. Por exemplo, se o número é 2021 , então a
# saída deve ser 4. Obs: O número não deve ser convertido para nenhum
# outro tipo, logo, todas as operações devem ser realizadas sobre o número
# inteiro.

n = int(input("Digite um número: "))
count = 1

while True:
    if n < 10:
        break
    else:
        n = n / 10
        count = count + 1

print(count)