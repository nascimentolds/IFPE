# 11. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
# usuário. Ex.: 5! = 5.4.3.2.1=120.

n = int(input("Digite um número: "))
n1 = n
count = 1

for i in reversed(range(1, n+1)):
    count = count * n
    n = n - 1

print(f"{n1}! = ", end="")
print(n1, end="")

for i in reversed(range(1, n1)):
    print(f"*{i}", end="")

print("=", end="")
print(count, end="")