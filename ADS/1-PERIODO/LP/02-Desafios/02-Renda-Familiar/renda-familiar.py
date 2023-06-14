import json
arquivo = 'dict.json'
SALARIO_MINIMO = 1320

# Criando o dicionário principal
dados = {
    "familias": []
}

# Menu do sistema
def menu():
    print("[0] Sair do sistema")
    print("[1] Incluir família")
    print("[2] Buscar dados da famílias")
    print("[3] Listar CPFs cadastrados")
    print("[4] Lista dados das famílias")
    print("[5] Lista de dados consolidados")
    print("[6] Realizar backup dos dados")
    print()

# Verifica se o arquivo JSON está vazio.
def verificar_arquivo_json_vazio(nome_arquivo):
    with open(arquivo, 'r') as file:
        conteudo = file.read()
        if len(conteudo) == 0:
            return True
        try:
            json.loads(conteudo)
        except json.JSONDecodeError:
            return False
        else:
            return False

# se não estiver carrega os dados do arquivo para o dicionário principal.
vazio = verificar_arquivo_json_vazio(arquivo)
if not vazio:
    with open(arquivo, 'r') as file:
        dados = json.load(file)
        
# Verifica se o cpf ja existe. Se não existe adiciona o novo cpf.       
def valida_cpf():
    while True:
        cpf = input("Digite o cpf do responsável: ")
        cpfs = [familia["cpf"] for familia in dados["familias"]]
        if cpf in cpfs: print("Família já esxistente!")
        else: break 
    return cpf

#Insere os dados no arquivo
def inserir_dados_no_arquivo():
    with open(arquivo, 'w') as file:
        json.dump(dados, file, indent=2)
    
def insercao_de_familias():
    while True:
        cpf = valida_cpf()
        pessoas = int(input("Quantos membros tem a família? "))
        membros = {}
        renda_total = 0
        for x in range(pessoas):
            renda = int(input(f"Digite a renda da pessoa {x+1}: "))
            membros[x+1] = renda            
            renda_total += renda
            
        renda_media = renda_total / pessoas
            
        resumo = {
            "qt_membros" : pessoas,
            "renda_total" : renda_total,
            "renda_media" : renda_media
        }       
                  
        dicionario = {
			"cpf" : cpf,
			"membros" : membros,
            "resumo" : resumo
		}        
        dados["familias"].append(dicionario)
        
        inserir_dados_no_arquivo()
        break
    
def nao_ha_dados():
    opcao = input("Não há dados cadastrados! Deseja cadastrar? (S/N)").upper()
    if opcao == "S": return insercao_de_familias()
    else: return exit()
         
def buscar_dados_da_familia():
    cpfs = [familia["cpf"] for familia in dados["familias"]]
    while True:
        cpf = input("Digite o CPF: ")
        if cpf in cpfs:
            print("-" * 35)
            for familia in dados["familias"]:
                if familia["cpf"] == cpf:
                    print(f'Quantidade de Membros da Família: {familia["resumo"]["qt_membros"]}')
                    print(f'Renda Total da Família: R$ {familia["resumo"]["renda_total"]:.2f}')
                    print(f'Renda Média da Família: R$ {familia["resumo"]["renda_media"]:.2f}')
            break
        else: print("CPF inexistente! \n")
            

def listar_cpfs():
    print("CPFs Cadastrados")
    print("-" * 30)
    for familia in dados["familias"]:
        print(familia["cpf"])
    
def listar_dados_das_familias():
    for familia in dados["familias"]:
        print(f'CPF: {familia["cpf"]}')
        print("-" * 35)
        print(f'Quantidade de Membros da Família: {familia["resumo"]["qt_membros"]}')
        print(f'Renda Total da Família: R$ {familia["resumo"]["renda_total"]:.2f}')
        print(f'Renda Média da Família: R$ {familia["resumo"]["renda_media"]:.2f}')
        print()

def renda_media_cidade():
    renda_total_cidade = 0   
    for familia in dados["familias"]:
        renda_total_cidade += familia["resumo"]["renda_total"]        
    return renda_total_cidade / len(dados["familias"])

def media_individous_por_familia():
    media_individous = 0
    for familia in dados["familias"]:
        media_individous += familia["resumo"]["qt_membros"]
    return media_individous / len(dados["familias"])
     
def familias_com_renda_inferior():
    count = 0
    for familia in dados["familias"]:
        if familia["resumo"]["renda_media"] < SALARIO_MINIMO:
            count += 1                
    return (count * 100) / len(dados["familias"])

def familias_com_renda_superior():
    count = 0
    for familia in dados["familias"]:
        if familia["resumo"]["renda_media"] > (SALARIO_MINIMO) * 12:
            count += 1                
    return count

def dados_cosolidados():
    print("Dados Consolidados")
    print("-" * 30)
    print(f"Renda média da cidade: R$ {renda_media_cidade():.2f}")  
    print(f"Média de individous por famílias: {media_individous_por_familia():.0f}")
    print(f"Famílias com renda inferior a um salário mínimo: {familias_com_renda_inferior():.0f}%")  
    print(f"Famílias com renda superior a um salário mínimo: {familias_com_renda_superior()}")  
      
while True:
    print()
    if not dados["familias"]: nao_ha_dados()
    else:
        menu()
        opcao = int(input("Escolha uma das opções acima: "))
        print("-" * 30)
        print()  
        
        if opcao == 1: insercao_de_familias()
        elif opcao == 2: buscar_dados_da_familia()
        elif opcao == 3: listar_cpfs()
        elif opcao == 4: listar_dados_das_familias()
        elif opcao == 5: dados_cosolidados()
        elif opcao == 0:
            print("Sistema encerrado! \n")
            break
        else: print("Opção Invalida!")