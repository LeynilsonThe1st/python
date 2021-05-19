from random import randint as rd
from time import sleep
# from time import monotonic as tempo
from sort.colors import WHITE, YELLOW, BOLD, DIM, CLEAR, RED


# print(f"Encontrei '{item}' em {start}{
#   ''.join(str(ls[item - i : item + i + 1])).strip('[]')
# }{end}")
def procurar(ls, item):
    lista = ls

    if item > lista[-1] or item < lista[0]:
        print(f"{RED}Nenhum {item} em {DIM}\
{lista[:16] if item < lista[0] else lista[16:]}{CLEAR}{WHITE}{BOLD}")
        return False

    else:
        # Encontra o meio da lista
        meio = len(lista) // 2

        # Continua até haver apenas um numero na lista
        while len(lista) >= 1:

            if item == lista[meio]:
                i = 5 if item >= 5 else item
                start = f'[{DIM}' if item <= 5 else f'[{DIM} ... '

                end = ']' if item + 5 >= ls[-1] \
                    else f'{DIM} ... {CLEAR}{WHITE}{BOLD}]'

                sep = ', ' if len(ls[item:]) != 0 else ''

                inicio = f"{''.join(str(ls[item - i : item - 1])).strip('[]')},\
{CLEAR}{WHITE}{BOLD}" if item > 1 else f'{CLEAR}{WHITE}{BOLD}'

                fim = f"{DIM}{sep}{''.join(str(ls[item : item + i])).strip('[]')}\
{CLEAR}{WHITE}{BOLD}"

                print(f"Encontrei '{item}' em {start}{inicio} {YELLOW}{item}\
{WHITE}{fim}{end}")

                return True

            elif item > lista[meio]:
                lista = lista[meio:]
                meio = len(lista[meio:]) // 2

            else:
                lista = lista[:meio]
                meio = len(lista[:meio]) // 2

            # print(lista)


dados = list(range(1, 37))
print(dados)

print(f"{WHITE}{BOLD}")
for x in range(20):
    k = rd(-15, 45)
    procurar(dados, k)
    sleep(0.5)
