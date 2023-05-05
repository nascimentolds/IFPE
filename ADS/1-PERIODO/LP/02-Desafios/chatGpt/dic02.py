# Crie um programa que solicite ao usuário que insira uma frase e conte quantas vezes 
# cada letra aparece na frase. Em seguida, o programa deve exibir um dicionário que mapeia 
# cada letra para o número de vezes que ela aparece na frase.

# Para resolver este desafio, você pode começar criando um dicionário vazio para armazenar 
# as contagens de letras. Em seguida, use um loop para iterar sobre cada caractere na frase 
# e atualizar a contagem correspondente no dicionário. Lembre-se de tratar letras maiúsculas 
# e minúsculas como equivalentes.

# Para exibir o dicionário final, você pode iterar sobre as chaves do dicionário e exibir 
# a letra correspondente e a contagem de vezes que ela aparece.

# Aqui está um exemplo de entrada e saída para este programa:

# Digite uma frase: Hello, world!
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}

# Espero que você ache este desafio interessante e desafiador! Boa sorte!

letras = {}
frase = input('Digite uma frase: ').lower()

for f in frase:
    letras[f] = frase.count(f)
    
print(letras)