# 15. Faça um programa que leia um número indeterminado de valores, 
# correspondentes a notas, encerrando a entrada de dados quando for 
# informado um valor igual a -1 (que não deve ser armazenado). 
# Após esta entrada de dados, faça:

#     Mostre a quantidade de valores que foram lidos;
#     Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#     Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#     Calcule e mostre a soma dos valores;
#     Calcule e mostre a média dos valores;
#     Calcule e mostre a quantidade de valores acima da média calculada;
#     Calcule e mostre a quantidade de valores abaixo de sete;
#     Encerre o programa com uma mensagem;

lista = []
c = 1

while True:
    n = int(input(f'Digite a nota {c}: '))
    
    if n < 0:
        break
    else:
        lista.append(n)
        c += 1
        
print()
print(f'Qtde valores lidos: {len(lista)}')       

print('Valores digitados: ', end='')
for e in lista:
    print(e, end=' ')

print()
print('Valores ordem inversa: ')
lista.reverse()
for i in lista:
    print(i)
    
soma = 0
lista.reverse()
for x in lista:
    soma = x + x

media = soma / len(lista)
print(f'Soma dos valores: {soma}')
print(f'Média dos valores: {media}')

am = 0
for m in lista:
    if m > media:
        am += 1
        
print(f'Valores acima da média: {am}')

print('Valores abaixo de sete:')
for s in lista:
    if s < 7:
        print(s)
        
print()
print('Obrigado por nos ajudar com esse exercicio!')