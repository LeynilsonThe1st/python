""" __author__: Winslet Di Caprio M. Mateus """

def texto(texto):
    a = "como estas"
    b = "quem es"
    n = 0
    na = 0
    for i in range(len(texto)):
        for j in range(len(a)):
            if texto[i] == a[j]:
                n += 2
                if n > 5:
                    saida = "Estou bem"
        for o in range(len(b)):
            if texto[i] == b[o]:
                na += 1
                if na > 5:
                    saida = "Sou o Jarvis"

    print(saida)


output = input("O que que o senhor quer? : ")
texto(output)
