# p = bool(input("Digite 0 ou 1: "))
# q = bool(input("Digite 0 ou 1: "))

p = True
q = False

print(p and q, "---", not(p or q), "---", (p and q) and not(p or q))
print(p and q, "---", not(p or q), "---", not(p and q) or q)