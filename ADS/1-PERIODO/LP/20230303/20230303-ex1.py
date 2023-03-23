peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso // (altura**2)

if imc < 20: print("Seu IMC está ABAIXO DO NORMAL")
elif imc >= 20 and imc <= 24: print("Seu IMC está NORMAL")
elif imc >= 25 and imc <= 29: print("Seu IMC está SOBREPESO")
elif imc >= 30 and imc <= 34: print("Seu IMC está OBESIDADE LEVE")
elif imc >= 35 and imc <= 39: print("Seu IMC está OBESIDADE MODERADA")
elif imc >= 40: print("Seu IMC está OBESIDADE MÓRBIDA")
else: print("Informações inválidas")
