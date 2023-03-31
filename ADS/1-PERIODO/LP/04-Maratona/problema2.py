n = input("Digite os numeros: ").split()

n1 = int(n[0])
n2 = int(n[1])
c = 0

for x in range(n1, n2+1):
    if x == 2:
        print(x, end=" ")
    
    if x == 3:
        print(x, end=" ")

    if x != 1 and x != 3 and x % 3 != 0 and x % 2 != 0:
        print(x, end=" ")
    