"""
`sequencia(list)`
Mostra a maior sequência de números dentro de uma lista
"""

from random import shuffle, randint as rd
from os import system
from time import sleep
from conversor.colors import WHITE, YELLOW, GREEN, BOLD

def formatar(ini=list, mid=list, fim=list):
    """ Troca a cor do texto da maior sequência de números da lista para amarelo """
    start = "".join(str(ini)).strip("]")
    middle = "".join(str(mid)).strip("[]")
    end = "".join(str(fim)).strip("[")
    middle = f",{YELLOW} " + middle if any(ini) else f"{YELLOW}" + middle
    end = f"{WHITE}, " + end if any(fim) else f"{WHITE}" + end

    return start + middle + end


def sequencia(vector, rigido=False):
    """ Mostra a maior sequência de números dentro de uma lista """
    count = 1
    pos = 0
    maior_seq = 1

    for j, num2 in enumerate(vector[:-1]):
        # if vector[j + 1] > num2:
        cond = vector[j + 1] - num2 == 1 if rigido else vector[j + 1] > num2
        if cond:
            count += 1
        else:
            count = 1

        if count > maior_seq:
            maior_seq = count
            pos = len(vector[:j+1]) - maior_seq + 1

    lista = formatar(
        vector[:pos],
        vector[pos: maior_seq + pos],
        vector[maior_seq + pos :]
        ) if maior_seq > 1 else str(vector)

    return lista, maior_seq, pos


def ver_maior_seq(limite=50000):
    """
    Executa a função `sequencia()` o numero de vezes definidas (default = 10000)\n
    retorna `tuple` com 3 itens:\n
    [0] = a lista formatada com a maior sequência -> str;\n
    [1] = a quantidade de números da maior sequência -> int;\n
    [2] = a posição do primeiro número da maior sequência -> int;
    """
    # arr = [x for x in range(30, 0, -1)]
    # arr = [x for x in range(11, 1, -1)]
    arr = [rd(1, 99) for x in range(1, 11)]
    # arr = [10 for x in range(1, 11)]
    lst2 = ""
    i = pos2 = seq2 = 0
    while i != limite:
        shuffle(arr)
        lst, seq, pos = sequencia(arr, True)
        lst2, seq2, pos2 = (lst, seq, pos) if seq >= seq2 else (lst2, seq2, pos2)
        i += 1

    return lst2, seq2, pos2

def thead():
    system('clear')
    print(f"{BOLD}{WHITE}")
    print("-" * 100)
    print(f"|{GREEN} {'Lista':<40} {WHITE}|", end="")
    print(f"{GREEN} Posição do primeiro item {WHITE}|", end="")
    print(f"{GREEN} Tamanho da maior sequência {WHITE}|")
    print("+-" + ("-" * 40) + "-+-" + ("-" * 24) + "-+-" + ("-" * 26) + "-+")

# print("| {:<26} | {:<24} | {:<5} |")
thead()
for x in range(1, 51):
    LST, TMS, PPI, = ver_maior_seq()

    if PPI == 0 and TMS == 1:
        print(f"| {LST:<40} | {PPI:>24} | {TMS:>26} |")
    else:
        print(f"| {LST:<50} | {PPI:>24} | {TMS:>26} |")

    if x % 10 == 0 and x != 50:
        print("-" * 100)
        sleep(5)
        thead()
    else:
        print("+-" + ("-" * 40) + "-+-" + ("-" * 24) + "-+-" + ("-" * 26) + "-+")



    # print(f"{BOLD}{WHITE}")
    # print(f"Tamanho da maior sequência = {TMS}")
    # print(f"{DIM}.{CLEAR}{WHITE}{BOLD} Posição do primeiro item = {PPI}")
    # print(f"{DIM}....................{CLEAR}{WHITE}{BOLD} Lista = {LST}")
    # if TMS == 1:
    #     break
