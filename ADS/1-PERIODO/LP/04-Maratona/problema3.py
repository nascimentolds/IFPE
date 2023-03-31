n = input("Digite o telefone: ")
n1 = n.replace('-', '')

if len(n1) <= 7:
    n1 = '3'+n1

n2 = n1[0:4]+'-'+n1[4:8]

print(n2)