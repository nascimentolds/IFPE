# 1. Faça um programa que leia 2 strings e informe o conteúdo delas
# seguido do seu comprimento. Informe também se as duas strings
# possuem o mesmo comprimento e são iguais ou diferentes no
# conteúdo.

st1 = "Marcelo"
st2 = "olecraM"

if st1 == st2: 
    con = "Posuem o mesmo conteúdo"
else:
    con = "Não posuem o mesmo conteúdo"

if len(st1) == len(st2): 
    tam = "Tem a mesma qtde de caracteres"
else:
    tam = "Não tem a mesma qtde de caracteres"

print(f"{st1} possui {len(st1)} carcteres")
print(f"{st2} possui {len(st2)} carcteres")
print(f"{st1} e {st2} {con} e {tam}")
