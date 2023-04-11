
pessoas = []

while True:
    entrada = input("Digite o comando: ").split()

    if entrada[0] == '-1':
        break
    
    elif entrada[0] == "add":
        id = int(entrada[1])
        first_name = entrada[2]
        last_name = entrada[3]
        birtday = entrada[4]
        phone_number = entrada[5]
        
        # Verifica se já existe um indivíduo com o mesmo ID
        if any(pessoa['id'] == id for pessoa in pessoas):
            print("Erro: já existe um indivíduo com o mesmo ID")
        else:
            # Adiciona o indivíduo à lista de pessoas
            pessoas.append({'id': id, 'first_name': first_name, 'last_name': last_name, 'birtday': birtday, 'phone_number': phone_number})
                        

        
print(pessoas)