""" __author__: Leynilson José "Snake" """
# Soma_factorial | wrong answer

# Calcula o factorial multiplicando n pelos seus antecessores ate l
def factorial(n, l=0) -> int:
    prod = 1
    while n > l:
        prod *= n
        n -= 1
    return prod

# Leitura dos dados
def cin() -> bool:
    try:
        dados = input().split()
        dados.sort()
        global a, b
        (a, b) = map(lambda num: int(num), dados)
        return True
    except EOFError:
        return False

a = b = None
while cin():
    f1 = factorial(a)
    print(2 * f1) if a == b else print(f1 * (1 + factorial(b, a)))
