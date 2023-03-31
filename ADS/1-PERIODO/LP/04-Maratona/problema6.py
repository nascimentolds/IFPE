A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

n = input("Digite a palavra: ")
pos = int(input("Quantas posições deseja alterar: "))

novo = []

for i in n:
    if i in A:
        l = A.index(i) + pos
        novo.append(A[l])
        
    if i in a:
        s = a.index(i) + pos
        novo.append(a[s])

for nv in novo:
    print(nv, end='')

