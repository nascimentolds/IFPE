# 1. Escreva uma função que receba um número de parâmetros indefinido.
# Imprima a quantidade de parâmetros recebidos de cada tipo de dado. 
# A função também deve imprimir o maior e o menor valor numérico recebido. 
import math

def parametros(*a):
    tipo = []
    dic = {}
    val = []

    for i in a:
        if type(i) == str: 
            tipo.append('str')
        if type(i) == int: 
            tipo.append('int')
            val.append(i)
        if type(i) == float: 
            tipo.append('float')
            val.append(i)
        if type(i) == bool: 
            tipo.append('bool')
    
    for i in tipo:
        dic[i] = tipo.count(i)

    for c, v in dic.items():
        print(f'{c} - {v}')

    print(f'Maior valor: {max(val)}')
    print(f'Menor valor: {min(val)}')
        

parametros(1, 2, '3', 4.1, True, 'nada')