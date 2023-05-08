# 7. Utilizando funções, leia um número inteiro e retorne o seu equivalente em
# numeração romana.

romanos = {
    'unidade': {
      0: '',
      1: 'I',
      2: 'II',
      3: 'III',
      4: 'IV',
      5: 'V',
      6: 'VI',
      7: 'VII',
      8: 'VIII',
      9: 'IX'
    },
    'dezena': {
      0: '',
      10: 'X',
      20: 'XX',
      30: 'XXX',
      40: 'XL',
      50: 'L',
      60: 'LX',
      70: 'LXX',
      80: 'LXXX',
      90: 'XC'
    },
    'centena': {
      0: '',
      100: 'C',
      200: 'CC',
      300: 'CCC',
      400: 'CD',
      500: 'D',
      600: 'DC',
      700: 'DCC',
      800: 'DCCC',
      900: 'CM'
    },
    'milhar': {
      0: '',
      1000: 'M',
      2000: 'MM',
      3000: 'MMM',
      4000: 'MMMM',
      5000: 'MMMMM',
      6000: 'MMMMMM',
      7000: 'MMMMMMM',
      8000: 'MMMMMMMM',
      9000: 'MMMMMMMMM'
    }
  }

def converte_romanos(n):
    unidade = n % 10
    dezena = ((n % 100) / 10)
    centena = ((n % 1000) / 100)
    milhar = ((n % 10000) / 1000)
    numero = [int(milhar) * 1000, int(centena) * 100, int(dezena) * 10, int(unidade)]

    r = ''
    for x in numero:
        for chave, valor in romanos.items():
            for c, v in valor.items():
                if x == c and c != 0: 
                    r += v
    return r

n = int(input('Digite um numero para ser converto para Algarismo Romano: '))
print()
print('-' * 65)
print(f'O número {n} corresponde a {converte_romanos(n)} em Algarismos Romano.')
print('-' * 65)
