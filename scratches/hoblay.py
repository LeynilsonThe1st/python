""" __Author__ : Winslet Di Caprio M. Mateus"""


def igualdade(array):
    c = []
    for i in range(len(array)):
        for j in range(len(c)):
            if array[i] == c[j]:
                print(array[i], end=' ')
        c.append(array[i])


array = [1, 2, 4, 5, 2, 4, 1]
igualdade(array)
