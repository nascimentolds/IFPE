# Importando as bibliotecas que serão utilizadas no sistema
import json
import os
import datetime

# Constante para o salário mínimo
SALARIO_MINIMO = 1320

# Arquivo principal
arquivo = "dict.json"

# Caso o arquivo não exista ele será criado nesse momento
if not os.path.exists(arquivo): open(arquivo, "x")

# Criando o dicionário principal
dados = {"familias": []}

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
        if len(conteudo) == 0: return True
        try: json.loads(conteudo)
        except json.JSONDecodeError: return False
        else: return False
        
# Se existeir algum conteúdo ele é carregado para o dicionário principal
vazio = verificar_arquivo_json_vazio(arquivo)
if not vazio:
    with open(arquivo, 'r') as file: dados = json.load(file)
        
# Verifica se o cpf ja existe. Se não existe adiciona o novo cpf.       
def valida_cpf():
    while True:
        cpf = input("Digite o cpf do responsável: ")
        cpfs = [familia["cpf"] for familia in dados["familias"]]
        if cpf in cpfs: print("Família já esxistente!")
        else: break 
    return cpf

# Insere os dados do dicionário principal no arquivo JSON
def inserir_dados_no_arquivo():
    with open(arquivo, 'w') as file: json.dump(dados, file, indent=2)

# Inclusão de nova familia  
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

        print()
        print("CPF:", cpf)
        print("-" * 35)
        imprimir_dados_da_familia(cpf)
        print("-" * 35)
        print("Família cadastrada com sucesso!")
        break

# Se não existir dados no arquivo essa função é chamada    
def nao_ha_dados():
    opcao = input("Não há dados cadastrados! Deseja cadastrar? (S/N)").upper()
    print()
    if opcao == "S": return insercao_de_familias()
    else: return exit()

# Busca e mostra os dados da familia pelo CPF         
def buscar_dados_da_familia():
    cpfs = [familia["cpf"] for familia in dados["familias"]]
    while True:
        cpf = input("Digite o CPF: ")
        if cpf in cpfs:
            print("-" * 35)
            imprimir_dados_da_familia(cpf)
            break
        else: print("CPF inexistente! \n")

# Imprimir dados da familia         
def imprimir_dados_da_familia(cpf):
    for familia in dados["familias"]:
        if familia["cpf"] == cpf:
            print(f'Quantidade de Membros da Família: {familia["resumo"]["qt_membros"]}')
            print(f'Renda Total da Família: R$ {familia["resumo"]["renda_total"]:.2f}')
            print(f'Renda Média da Família: R$ {familia["resumo"]["renda_media"]:.2f}')

            
# Lista todos os CPFs cadastrados
def listar_cpfs():
    print("CPFs Cadastrados")
    print("-" * 30)
    for familia in dados["familias"]:
        print(familia["cpf"])

# Lista o resumo de dados de todas as familias    
def listar_dados_das_familias():
    for familia in dados["familias"]:
        print(f'CPF: {familia["cpf"]}')
        print("-" * 35)
        print(f'Quantidade de Membros da Família: {familia["resumo"]["qt_membros"]}')
        print(f'Renda Total da Família: R$ {familia["resumo"]["renda_total"]:.2f}')
        print(f'Renda Média da Família: R$ {familia["resumo"]["renda_media"]:.2f}')
        print()

# Calcula a renda média da cidade
def renda_media_cidade():
    renda_total_cidade = 0   
    for familia in dados["familias"]:
        renda_total_cidade += familia["resumo"]["renda_total"]        
    return renda_total_cidade / len(dados["familias"])

# Calcula a quantidade média de indivivuos por familia
def media_individous_por_familia():
    media_individous = 0
    for familia in dados["familias"]:
        media_individous += familia["resumo"]["qt_membros"]
    return media_individous / len(dados["familias"])

# Calcula o percentual de familias com renda inferior de um salário mínimo     
def familias_com_renda_inferior():
    count = 0
    for familia in dados["familias"]:
        if familia["resumo"]["renda_media"] < SALARIO_MINIMO:
            count += 1                
    return (count * 100) / len(dados["familias"])

# Calcula a quantidade de familias com renda superior a 12 salários mínimo
def familias_com_renda_superior():
    count = 0
    for familia in dados["familias"]:
        if familia["resumo"]["renda_media"] > (SALARIO_MINIMO) * 10: count += 1                
    return count

# Imprime os dados consolidados da cidade
def dados_cosolidados():
    print("Dados Consolidados")
    print("-" * 30)
    print(f"Renda média da cidade: R$ {renda_media_cidade():.2f}")  
    print(f"Média de individous por famílias: {media_individous_por_familia():.2f}")
    print(f"Famílias com renda inferior a um salário mínimo: {familias_com_renda_inferior():.0f}%")  
    print(f"Famílias com renda superior a 10 salários mínimo: {familias_com_renda_superior()}")  

# Prepara os dados e os escreve no arquivo
def backup_dados(versao):
    data_hora_atual = datetime.datetime.now()
    data_formatada = data_hora_atual.strftime("%d/%m/%Y")
    hora_formatada = data_hora_atual.strftime("%H:%M:%S")
    linhas_do_arquivo = 0
    
    with open(arquivo, "r") as file:
        for l in file:
            linhas_do_arquivo += 1
    
    with open("dict_backup.json", "w") as file:            
        first_line = f"{data_formatada} {hora_formatada} {linhas_do_arquivo} v{versao}"
        data = [first_line, dados]
        json.dump(data, file, indent=2)
        
        print("-" * 30)
        print("Backup criado com sucesso!")
        print("-" * 30)
            
# Verifica se o arquivo de backup existe, se existeir incrementa a versão, 
# caso não exista é crido o primeiro arquivo
def backup():     
    if not os.path.exists("dict_backup.json"): backup_dados(1) 
    else:
        with open("dict_backup.json", "r") as file:
            data = json.load(file)
            data_list = data[0].split()
            versao = data_list[-1]
            versao = versao.replace('v', '')            
            versao = int(versao) + 1            
            backup_dados(versao)   

# Roda o sistema e verifica se há dados no dicionário principal, caso não exista,
# é chamada a função para a inclusão de novos dados    
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
        elif opcao == 6: backup()
        elif opcao == 0:
            print("Sistema encerrado! \n")
            break
        else: print("Opção Invalida!")