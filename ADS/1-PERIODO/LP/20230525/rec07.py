# 7. Crie uma função recursiva para verificar se um número é primo.

def is_prime(n, divisor=2):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return is_prime(n, divisor + 1)

print(is_prime(0))