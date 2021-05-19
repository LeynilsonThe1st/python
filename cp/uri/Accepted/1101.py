""" __author__: Leynilson José "Snake" """
# sequencia de numeros e soma | accepted

# Leitura dos dados
def cin():
    dados = input().split()
    dados.sort()
    global a, b
    (a, b) = map(lambda num: int(num), dados)
    return False if a <= 0 or b <= 0 else True


a = b = None
while cin():
    soma = 0
    for i in range(a, b + 1):
        print(i, end=" ")
        soma += i
    print(f"Sum={soma}")
