# 3. Crie uma função recursiva para verificar se uma lista está
# ordenada em ordem crescente. 

def ordem(lista):
    if len(lista) == 1:
        return True
    elif lista[0] < lista[1]:
        return ordem(lista[1:])
    else:
        return False


l = [1,2,3,4,5]
print(ordem(l))