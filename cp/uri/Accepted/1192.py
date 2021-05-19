""" __author__: Leynilson José "Snake" """
# O jogo Matemático de Paula | accepted

# Leitura dos dados
def cin():
    dados = input()
    return int(dados[0]), dados[1], int(dados[2])


t = int(input())
while t > 0:
    t -= 1
    n1, a, n2 = cin()
    if n1 == n2:
        print(n1 * n2)
    elif a.isupper():
        print(n2 - n1)
    else:
        print(n1 + n2)
