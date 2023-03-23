n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
i = 0
pares = 0

if n1 > n2: aux = n1 - n2
else: aux = n2 - n1

while i <= aux:
    i = i + 1
    if i % 2 == 0:
        pares = pares + 1
        
print(pares)
    
