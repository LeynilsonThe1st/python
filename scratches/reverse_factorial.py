""" __author__: Leynilson José "Snake" """

"""
- Papoite Tuling está bater?
- Sempre cassule, e do teu lado? o que fazes?
- Comigo tambem meu cota, acabei de sair de uma aula de programação, falamos da estutura de
    repetição, vimos que é muito útil para determinar numeros de uma serie e não só.
    Resolvemos alguns exercicios: O somatório do n primeiro números, numeros da serie de Padovan e de Fibonacci,
    e por ultimo vimos como calcular o factorial de um numero, achei muito interessante, mas
    infelizmente o professor não deixou tarefa, será que o papoite pode dar-me algum para eu praticarem casa?
- Claro meu cassule!, como tu já sabes calcular o factorial de um número eu vou querer que faças
o seguinte:

Dado um numero inteiro f, dizer se f é o factorial n. n! = f, onde (0!<=f<=10!)
Nota: caso existir mais de um numero n, mostre o maior.

    """

def cin():
    try:
        global f
        f = int(input())
        return True
    except EOFError:
        return False


f = None
while cin():
    fa = f
    i = 2
    if f in (0, 1):
        print(1)
    else:
        while fa % i == 0:
            fa /= i
            i += 1
        if fa == 1:
            print(i-1)
        else:
            print("nao existe n | n! =", f)

    # while fa / i > 1:
    #     if fa % i != 0:
    #         print("nao existe n | n! =", f)
    #         break
    #     fa /= i
    #     i += 1
    # print(i)





