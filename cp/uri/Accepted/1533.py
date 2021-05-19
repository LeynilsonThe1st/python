""" __author__: Leynilson José "Snake" """
# Detetive Watson | accepted

t = int(input())
while t != 0:
    dados = input().split()
    dados = list(map(int, dados))
    if len(dados) == 1:
        print(1)
    else:
        i = dados.index(max(dados))
        dados[i] = 0
        print(dados.index(max(dados)) + 1)

    t = int(input())
