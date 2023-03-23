# 10. A série de Fibonacci é formada pela seqüência 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

# termo = int(input("Digite um número: "))

fir = 0
sec = 1
aux = 1

while fir <= 700:
    print(fir)
    
    if fir < sec:
        fir = aux
        aux = sec
        sec = sec + fir  