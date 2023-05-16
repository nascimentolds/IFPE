# 8. Escreva um programa para armazenar uma agenda de telefones em um
# dicionário. Cada pessoa pode ter um ou mais telefones e a chave do
# dicionário é o nome da pessoa. Seu programa deve conter um menu onde
# dependendo da entrada do usuário, será possível:
#     - incluirNovoNome – acrescenta um novo nome na agenda, com um ou mais telefones. 
#     - incluirTelefone – acrescenta um telefone em um nome existente na agenda. Caso o 
#       nome não exista na agenda, você deve perguntar se a pessoa deseja incluí-lo. 
#     - excluirTelefone – exclui um telefone de uma pessoa que já está na agenda. 
#       Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda. 
#     - excluirNome – exclui uma pessoa da agenda. 
#     - consultarTelefone – retorna os telefones de uma pessoa na agenda.


telefones = {}

def menu():
    print('[1] Incluir novo nome')
    print('[2] Incluir telefone')
    print('[3] Excluir telefone')
    print('[4] Excluir nome')
    print('[5] Consultar telefone')
    print('[6] Sair do sistema')
    print()
    
def listar_telefones(pessoa):
    c = 1
    print(f'Foram encontrados os seguintes telefones para {pessoa}')
    for i in telefones[pessoa]:
        print(f'{c} - {i}')
        c += 1
    
def incluir_pessoa(pessoa):
    telefones[pessoa] = []
    
def incluir_telefone(pessoa, telefone):
    telefones[pessoa].append(telefone)
    
def incluir_outro_telefone(pessoa):
     while True:
        telefone = input('Digite o telefone: ')            
        incluir_telefone(pessoa, telefone)
        o = input('Deseja adicionar outro número? S/N: ').upper()
        
        if o != 'S':
            break
    
def excluir_telefone(pessoa, telefone):
    del telefones[pessoa][telefone-1]
    print('Telefone excluido!')
    
def excluir_pessoa(pessoa):
    telefones.pop(pessoa)
    print('Pessoa excluida!')
    
def pessoa_nao_encontrada(busca):
    o = input('Pessoa não encontrada, Deseja incluir? S/N: ').upper()
    if o == 'S': 
        incluir_pessoa(busca)
        while True:
            incluir_telefone(busca, input('Digite o telefone: '))
            o = input('Deseja adicionar outro número? S/N: ').upper()

            if o != 'S':
                break
            

while True:
    print(telefones)
    
    menu()
    opcao = int(input('Escolha uma das opções acima: '))
    
    if opcao == 1:
        pessoa = input('Digite o nome da pessoa: ').upper() 
        if pessoa not in telefones: incluir_pessoa(pessoa)
        else: print('Pessoa já existe!')
        
        incluir_outro_telefone(pessoa)
            
    elif opcao == 2:
        while True:
            busca = input('Digite o nome da pessoa: ').upper()
            
            if busca in telefones:
                incluir_outro_telefone(busca)
            else:
                pessoa_nao_encontrada(busca)
                break
        
    elif opcao == 3:
        while True:
            busca = input('Digite o nome da pessoa: ').upper()
            
            if busca in telefones:
                if len(telefones[busca]) <= 1:
                    excluir_pessoa(busca)
                    break

                else:
                    listar_telefones(busca)
                    remover = int(input('Digite o número correspondente ao telefone que deseja excluir: '))
                    excluir_telefone(busca, remover)
                    break

            else:
                pessoa_nao_encontrada(busca)
                break
            
    elif opcao == 4:
        while True:
            busca = input('Digite o nome da pessoa: ').upper()
            
            if busca in telefones:
                excluir_pessoa(busca)
                break

            else:
                pessoa_nao_encontrada(busca)
                break
            
    elif opcao == 5:
        while True:
            busca = input('Digite o nome da pessoa: ').upper()
            
            if busca in telefones:
                listar_telefones(busca)                
                input('Aperte "ENTER" para voltar ao menu!')
                break

            else:
                pessoa_nao_encontrada(busca)
                break
      
    if opcao == 6:
        print('Sistema encerrado!')
        break