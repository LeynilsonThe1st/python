from random import shuffle
from time import monotonic as tempo


def mergeSort(lista):
    # Determina se a lista esta dividida
    # em partes individuais.
    if len(lista) < 2:
        return lista

    # Encontra o meio da lista.
    meio = len(lista) // 2

    # Quebra a lista em partes.
    esquerda = mergeSort(lista[:meio])
    direita = mergeSort(lista[meio:])

    # Une os as duas partes em uma lista maior.
    lista_unida = unir(esquerda, direita)
    return lista_unida


def unir(esquerda, direita):
    # Quando o lado direito ou lado esquerdo for vasio
    # significa que este é um item individual
    # e já esta ordenado.
    if not len(esquerda):
        return esquerda
    if not len(direita):
        return direita

    # Defina as variaveis utilizadas para unir as dua partes.
    resultado = []
    esqIndex = 0
    dirIndex = 0
    tamanho_total = len(esquerda) + len(direita)

    # Continua até todas as partes forem unidas.
    while len(resultado) < tamanho_total:

        # Realiza as comparaçõe necessárias e une
        # as duas parte de acordo com o valor.
        if esquerda[esqIndex] < direita[dirIndex]:
            resultado.append(esquerda[esqIndex])
            esqIndex += 1
        else:
            resultado.append(direita[dirIndex])
            dirIndex += 1

        # Quando o um dos lados for maior do que o outro
        # adiciona os dados restantes no resultado.
        if esqIndex == len(esquerda) or dirIndex == len(direita):
            resultado.extend(esquerda[esqIndex:] or direita[dirIndex:])
            break

    return resultado


ls = list(range(0, 99999 + 2))
shuffle(ls)
print(f"\n----  {tempo():0.2f}\n")
# ls.sort()
lst = mergeSort(ls)
# print(lista)
print(lst[len(ls) - 11:])
print(f"\n----  {tempo():0.2f}\n")
