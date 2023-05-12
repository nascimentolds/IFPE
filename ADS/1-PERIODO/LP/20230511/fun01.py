# 1. Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
# - Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# - A entrada é dada em dois inteiros. 
# - Deve haver pelo menos duas funções: uma para fazer a conversão
#   e uma para a saída. 
# - Inclua um loop que permita que o usuário repita esse cálculo para
#   novos valores de entrada todas as vezes que desejar.


def converte_hora(hora, minutos):
    hora_convertida = 0
    meridiem = ''

    if hora > 12:
        hora_convertida = hora - 12
        meridiem = 'P.M.'
    elif hora == 12:
        hora_convertida = hora
        meridiem = 'P.M.'
    elif hora == 00:
        hora_convertida = 12
        meridiem = 'A.M.'
    else:
        hora_convertida = hora
        meridiem = 'A.M.'

    return [hora_convertida, minutos, meridiem]

def imprime_hora(c):
    return f'{c[0]}:{c[1]} {c[2]}'

while True:
    hora = int(input('Digite a hora: '))
    minutos = int(input('Digite os minutos: '))

    if hora > 24 or minutos > 59:
        print()
        print('Hora inválida! Digite uma hora Válida.')
        print()
    else:
        print()
        print(f'A hora {hora}:{minutos} convertida é {imprime_hora(converte_hora(hora, minutos))}')
        print()
        opcao = input('Deseja converter outra hora? S/N: ').upper()
        print()
        
        if opcao != 'S':
            break