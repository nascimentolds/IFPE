# 6. Faça uma função que computa a potência de ab para valores de a e b
# informados pelo usuário. Assuma valores de a e b como inteiros e não utilize
# o operador ** ou funções da biblioteca Math.


def potencia(a, b):
    pot = 1    
    for i in range(b):
        pot = a * a
        
    return pot

a = int(input('Digite o número base: '))
b = int(input('Digite o expoente: '))

print()
print(f'A potência de {a}^{b} é: {potencia(a, b)}')
    