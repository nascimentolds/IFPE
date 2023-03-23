SIND = 0.03
FGTS = 0.11
INSS = 0.10

valor_hora = float(input("Informe o valor por hora trabalhada: "))
qtde_horas = int(input("Informe quantas horas foram trabalhadas: "))

sal = valor_hora * qtde_horas

if sal <= 900: ir = 0
elif sal <= 1500: ir = 0.05
elif sal <= 2500: ir = 0.10
else: ir = 0.20

tot_desc = (SIND + INSS + ir) * sal
sal_liq = sal - tot_desc

print(f"Salário Bruto: ({valor_hora:.2f} * {qtde_horas}) : R$ {sal:.2f}")
print(f"(-) IR ({ir*100:.0f}%) : R$ {sal*ir:.2f}")
print(f"(-) INSS ({INSS*100:.0f}%) : R$ {sal*INSS:.2f}")
print(f"(-) SIND ({SIND*100:.0f}%) : R$ {sal*SIND:.2f}")
print(f"FGTS ({FGTS*100:.0f}%) : R$ {sal*FGTS:.2f}")
print(f"Total de descontos : R$ {tot_desc:.2f}")
print(f"Salário Líquido : R$ {sal_liq:.2f}")