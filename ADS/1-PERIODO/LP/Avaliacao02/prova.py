# # QUESTÃO 1
# def remover_duplicados(tupla):
#     tn = ()
#     for i in tupla:
#         if i not in tn:
#             tn = tn + (i,)

#     return tn

# tupla = (1, 3, 5, 2, 3, 5, 1, 1, 3)
# print(remover_duplicados(tupla))


# # QUESTÃO 2
# def iterativa(lista):
#     for i in range(len(lista) - 1):
#       if lista[i] > lista[i + 1]:
#           return False
#     return True
             
# def recursiva(lista):
#     if len(lista) == 1:
#         return True
#     elif lista[0] < lista[1]:
#         return recursiva(lista[1:])
#     else:
#         return False
    
# lista = [1, 2, 3, 4, 5]
# print(iterativa(lista))
# print(recursiva(lista))


# # QUESTÃO 3
# arquivo = open("backup.txt", "w")
# arquivo.close()

# pessoas = {}

# def criar_usuario():
#     nome = input("Digite o Nome: ")
#     apelido = input("Digite o Apelido: ")
#     idade = int(input("Digite o Idade: "))
#     cpf = input("Digite o CPF: ")

#     if apelido == "":
#         apelido = "n/a"

#     pessoas[nome] = [apelido, idade, cpf]

# def backup():
#     with open("backup.txt", "a") as file:
#         for c, v in pessoas.items():
#             print(f"Nome: {c}, apelido: {v[0]},  idade: {v[1]},  cpf: {v[2]}", file=file)

# def imprime_dados():
#     for c, v in pessoas.items():
#         print(f"Nome: {c}, apelido: {v[0]},  idade: {v[1]},  cpf: {v[2]}")

# def deleta_dados():
#     pessoas.clear()

# def imprimir_do_backup():
#     with open("backup.txt", "r") as file:
#         for linha in file:
#             print(linha)

# def menu():
#     print()
#     print("-" * 30)
#     print("Menu")
#     print("-" * 30)
#     print("[1] - Inerir pessoa")
#     print("[2] - imprimir dados")
#     print("[0] - sair")
#     print()   
    
# while True:
#     menu()    
#     op = int(input("Escolha a opção: "))
#     print()

#     if op == 1: criar_usuario()
#     elif op == 2: 
#         imprime_dados()
#         imprimir_do_backup()
#     elif op == 0: break
#     else: print("Opção inválida!") 
    
#     print()
#     if len(pessoas) == 2:
#         backup()
#         imprime_dados()
#         deleta_dados()