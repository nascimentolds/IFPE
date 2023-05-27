# 4. Crie uma função recursiva para verificar se uma lista contém um
# elemento específico.

def espc(lista, el):
    if len(lista) == 0:
        return False
    elif el == lista[0]:
        return True
    else:
        return espc(lista[1:], el)
        

l = [1,2,3,4,'Marcelo', 5]
e = 'Marcelo'
print(espc(l, e))