def sort(lista):

    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j

        print(lista[menor], lista)
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]


sort([7, 3, 9, 2, 5, 1, 10, 4, 6])
