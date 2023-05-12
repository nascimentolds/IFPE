# 3. Construa uma função que receba uma string como parâmetro e devolva outra 
# string com os carateres embaralhados. 
#  - Por exemplo: se função receber a palavra python, pode retornar npthyo, 
#    ophtyn ou qualquer outra combinação possível, de forma aleatória. 
#  - Padronize em sua função para que todos os caracteres sejam devolvidos em caixa alta 
#    ou caixa baixa, independentemente de como foram digitados.

import random
r = random

def embaralhar(s):
    p = [i for i in s]    
    palavra = ''
    
    for x in range(len(p)):
        a = random.choice(p)
        p.remove(a)
        palavra += a

    return palavra
    
st = input('Digite uma palavra: ').lower()
print()   
print(f'{st} - {embaralhar(st)}')