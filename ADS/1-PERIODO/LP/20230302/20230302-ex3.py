idade = int(input("Qual a idade do nadador? "))

if idade > 18:
    print("Adulto")
elif idade >= 14:
    print("Juvenil B")
elif idade >= 11:
    print("Juvenil A")
elif idade >= 8:
    print("Infantil B")
elif idade >= 5:
    print("Infantil A")
else:
    print("Nenhuma das categorias")