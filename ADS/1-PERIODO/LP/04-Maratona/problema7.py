
pessoas = []

while True:
    e = input('Digite a entrada: ').split()
    if e[0] == '-1':
        break
    else:
        if e[0] == 'add':
            if not pessoas:
                pessoas.append([e[1], e[2], e[3], e[4], e[5]])
            else:
                for p in pessoas:
                    if e[1] == p[0]:
                        print('Pessoa ja existe!')
                    else:
                        pessoas.append([e[1], e[2], e[3], e[4], e[5]])
        
print(pessoas)