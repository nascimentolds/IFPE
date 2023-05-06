# 5. Faça uma função que retorne a quantidade de dígitos de um determinado
# número inteiro informado pelo usuário. Não realize conversão de tipos. 

def digitos(n):
    count = 1

    while True:
        if n < 10:
            break
        else:
            n = n / 10
            count = count + 1

    return count


print(digitos(9999))