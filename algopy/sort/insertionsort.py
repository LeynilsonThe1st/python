from random import shuffle
from time import monotonic as tempo


def sort(lista):
    for i in range(1, len(lista)):
        temp = lista[i]
        menor = i
        while menor > 0 and temp < lista[menor - 1]:
            lista[menor] = lista[menor - 1]
            menor -= 1

        lista[menor] = temp

    return lista

ls = list(range(0, 9999 + 2))
shuffle(ls)
print(f"\n----  {tempo():0.2f}\n")
sort(ls)
# ls.sort()
print(ls[len(ls) - 11:])
print(f"\n----  {tempo():0.2f}\n")
