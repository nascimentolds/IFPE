# 3. Escreva uma função que recebe um número como parâmetro e para cada número menor que o parâmetro, 
# a função imprime "Fizz" se o número for múltiplo de três, imprime "Buzz" se o número for múltiplo
# de cinco, e imprime "FizzBuzz" se o número for múltiplo de três e cinco. Caso o número não seja 
# múltiplo nem de três nem de cinco, ele deve ser impresso.

def multiplos(n):
    for i in range(1, n+1):
        print(i)

multiplos(15)