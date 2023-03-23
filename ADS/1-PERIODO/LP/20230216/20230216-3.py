idade_anos = int(input("Quantos anos você tem? "))
idade_meses = int(input("E quantos meses? "))
idade_dias = int(input("E quantos dias? "))

total_dias = (idade_anos * 365) + (idade_meses * 30) + idade_dias

print("Você tem {} dias".format(total_dias))