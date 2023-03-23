# 3. Escreva um programa para contar a quantidade de números pares entre dois
# números quaisquer fornecidos pelo usuário

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2: 
    maior = n1
    menor = n2
else: 
    maior = n2
    menor = n1

for i in range(menor, maior+1):
    if i % 2 == 0:
        print(i)
