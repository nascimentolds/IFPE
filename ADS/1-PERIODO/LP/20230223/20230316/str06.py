# 6. Faça uma função que recebe uma string que representa uma cadeia de DNA
# e gera a cadeia complementar. A entrada e saída de dados deve ser feita
# pelo programa principal.  Exemplo:
#  Entrada: AATCTGCAC
#  Saída: TTAGACGTG

entrada = "AATCTGCAC"

print(entrada)
print(entrada.replace("A", "t").replace("T", "A").replace("G", "c").replace("C", "g").upper())