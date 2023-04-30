tupla = 1, 3, 5, 2, 3, 5, 1, 1, 3

tn = ()

for i in tupla:
    if i not in tn:
        tn = tn + (i,)

print(tupla)
print(tn)
