num = int(input("Digite um número: "))

if num % 4 == 0 and num % 3 == 0: print(f"{num} é divisivel tanto por 3 quanto por 4")
elif num % 3 == 0: print(f"{num} é divisivel por 3")
elif num % 4 == 0: print(f"{num} é divisivel por 4")
else: print(f"{num} não é divisivel nem por 3 nem por 4")