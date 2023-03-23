# A série de Fibonacci é formada pela seqüência 1, 1, 2, 3, 5, 8, 13, 21, 34,
# 55, ... Faça um programa capaz de gerar a série até o n−ésimo termo.

termo = int(input("Digite um número: "))
fir = 0
sec = 1
aux = 1

for i in range(termo):
    print(fir)
    
    if fir < sec:
        fir = aux
        aux = sec
        sec = sec + fir    
          
