limite = 50
multa = 4.00
e = 0
m = 0

p = float(input("Quantos quilos de peixe? "))

if (p > limite):
    e = p - limite
    m = multa * e

print()
print("Kilos excedentes: ", e)
print("Valor da multa: ", m)
