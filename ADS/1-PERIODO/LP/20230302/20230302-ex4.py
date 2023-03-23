n = int(input("Digite um número: "))

if n >= 0:
    print(f"{n} é Positivo")
    if n % 2 == 0: print(f"{n} é Par")
    else: print(f"{n} é Impar")
else: 
    print(f"{n} é Negativo")
    if n % 2 == 0: print(f"{n} é Par")
    else: print(f"{n} é Impar")