def particao(dados, esquerda, direita):
    pivo = dados[esquerda]
    e = esquerda + 1
    d = direita

    while True:
        # print(dados, dados[e], dados[d])
        while e <= d and dados[e] <= pivo:
            e += 1
        # print("dados[e] =", dados[e], "dados[d] =", dados[d])
        while d >= e and dados[d] >= pivo:
            d -= 1
        # print("dados[e] =", dados[e], "dados[d] =", dados[d])
        if d <= e:
            break
        dados[e], dados[d] = dados[d], dados[e]
    dados[esquerda], dados[d] = dados[d], dados[esquerda]
    # print("dados[esquerda] =", dados[esquerda], "dados[d] =", dados[d])
    # print(dados,"\n")
    return d


def quicksort(dados, esquerda, direita):
    if direita <= esquerda:
        return
    else:
        pivo = particao(dados, esquerda, direita)
        quicksort(dados, esquerda, pivo - 1)
        quicksort(dados, pivo + 1, direita)
    return dados


ls = list(range(1, 999))
# ls = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]
# print(ls)
# print(particao(ls, 0, len(ls)-1))
lst = quicksort(ls, 0, len(ls) - 1)
print(lst[:36])
