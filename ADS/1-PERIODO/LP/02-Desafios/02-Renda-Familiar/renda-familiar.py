import json

# with open('dict.json', 'r') as arquivo:
#     if arquivo:
#         dados = json.load(arquivo)

dados = {
    "familias": [
        {
            "cpf": "",
            "membros": {},
            "resumo": {}
        }
    ]
}


while True:
    cpf = dados["familias"][0]["cpf"] = input("Digite o cpf do responsável: ")
    
    if cpf == '':
        break
    
    pessoas = int(input("Quantos membros tem a família? "))

    for x in range(pessoas):
        dados["familias"][0]["membros"][x+1] = int(input(f"Digite a renda da pessoa {x+1}: "))

    

# data_json = json.dumps(dados, indent=4)

with open('dict.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=2)
    print(dados)
