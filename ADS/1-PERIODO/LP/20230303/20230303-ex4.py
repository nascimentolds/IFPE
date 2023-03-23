preco = float(input("Informe o valor do produto: "))
cod = int(input("Informe o código de pagamento entre 1 e 5: "))

if cod == 1:
    total = preco - preco * 0.1
    print(f"{preco} menos 10%, valor total: {total}")
elif cod == 2:
    total = preco - preco * 0.15
    print(f"{preco} menos 15%, valor total: {total}")
elif cod == 3:
    total = preco - preco * 0.1
    print(f"valor total: {total}")
elif cod == 4:
    total = preco + preco * 0.1
    print(f"{preco} mais 10%, valor total: {total}")
if cod == 5:
    total = preco + preco * 0.2
    print(f"{preco} mais 20%, valor total: {total}")
else: print("Código enexistente")