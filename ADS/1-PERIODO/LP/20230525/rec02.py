# 2. Crie uma função recursiva para calcular a soma de todos os
# dígitos de um número.

def soma_digitos(n):
    return 0 if n == 0 else n % 10 + soma_digitos(n // 10)
        
numero = 592378
total = soma_digitos(numero)
print(f"A soma dos digitos de {numero} é {total}.")