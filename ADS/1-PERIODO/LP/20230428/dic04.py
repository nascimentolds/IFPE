telefones = {}

while True:
    print()
    print(telefones)
    print()

    opcao = int(input('''
    - Incluir novo nome = 1
    - Incluir telefone = 2
    - Excluir telefone = 3
    - Excluir nome = 4
    - Consultar telefone = 5
    - Sair do sistema = 6

    Escolha uma das opções acima: '''))

    print()

    chave = ''
    valor = []

    if opcao == 1:
        chave = input('Digite o nome da pessoa: ').upper()

        while True:
            valor.append(input('Digite o telefone: '))

            o = input('Deseja adicionar outro número? S/N: ').upper()

            telefones[chave] = valor

            if o != 'S':
                break

    elif opcao == 2:
        while True:
            busca = input('Digite o nome da pessoa: ').upper()
            
            if busca in telefones:
                while True:
                    telefones[busca].append(input('Digite o telefone: '))

                    o = input('Deseja adicionar outro número? S/N: ').upper()

                    if o != 'S':
                        break
            else:
                o = input('Pessoa não encontrada, Deseja incluir? S/N: ').upper()
                if o == 'S': 
                    while True:
                        chave = busca
                        valor.append(input('Digite o telefone: '))

                        o = input('Deseja adicionar outro número? S/N: ').upper()

                        telefones[chave] = valor

                        if o != 'S':
                            break
                else: 
                    break
            break

    elif opcao == 3:
        while True:
            busca = input('Digite o nome da pessoa: ').upper()
            
            if busca in telefones:
                if len(telefones[busca]) == 1:
                    telefones.pop(busca)
                    print('Telefone excluido!')
                    break

                else:
                    c = 1
                    print(f'Foram encontrados os seguintes telefones para {busca}')
                    for i in telefones[busca]:
                        print(f'{c} - {i}')
                        c += 1

                    remover = int(input('Digite o número correspondente ao telefone que deseja excluir: '))

                    del telefones[busca][remover-1]
                    print('Telefone excluido!')
                    break

            else:
                print('Pessoa não encontrada!')
                break

    elif opcao == 4:
        while True:
            busca = input('Digite o nome da pessoa: ').upper()
            
            if busca in telefones:
                telefones.pop(busca)
                print('Nome excluido da lista!')
                break

            else:
                print('Pessoa não encontrada!')
                break

    elif opcao == 5:
        while True:
            busca = input('Digite o nome da pessoa: ').upper()
            
            if busca in telefones:
                c = 1
                print(f'Foram encontrados os seguintes telefones para {busca}')
                for i in telefones[busca]:
                    print(f'{c} - {i}')
                    c += 1
                
                input('Aperte "ENTER" para voltar ao menu!')
                break

            else:
                print('Pessoa não encontrada!')
                break

    elif opcao == 6:       
        break

    else:
        print('Opção inexistente!')

print(telefones)