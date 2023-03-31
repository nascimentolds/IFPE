idade = int(input("Digite sua idade em dias: "))

anos = idade // 365
meses = idade % 365 // 30
dias = (idade % 365) % 30

print(anos, "ano(s)")
print(meses, "mês(es)")
print(dias, "dia(s)")