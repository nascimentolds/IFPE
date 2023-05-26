# 6. Escreva uma função recursiva que determine quantas vezes um dígito K 
# ocorre em um número natural N. Por exemplo, o dígito 2 ocorre 3 vezes em 762021192.

def digitos(n, k):
    if n == 0:  # Caso base: número zero, não há mais dígitos para verificar
        return 0
    elif n % 10 == k:  # Se o último dígito for igual a k
        return 1 + digitos(n // 10, k)  # Incrementa 1 e continua verificando o restante do número
    else:
        return digitos(n // 10, k)  # Caso contrário, continua verificando o restante do número

# Exemplo de uso
numero = 7620211920
digito = 0
ocorrencias = digitos(numero, digito)
print(f"O dígito {digito} ocorre {ocorrencias} vezes no número {numero}.")
