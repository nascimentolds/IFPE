# 4. Modifique a questão anterior de forma que as vogais da string
# não sejam embaralhadas, ou seja, permaneçam na mesma posição.

import random
r = random

def embaralhar(s):
    st = s.lower()
    p = [i for i in st]
    vogais = ['a','e','i','o','u']  
    palavra = ''
    
    for x in range(len(p)):
        a = random.choice(p)
        p.remove(a)
        if a not in vogais:
            palavra += a
            
    return palavra

st = input('Digite uma palavra: ')
print()   
print(f'{st} - {embaralhar(st)}')