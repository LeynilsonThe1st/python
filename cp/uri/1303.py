""" __author__: Leynilson José "Snake" """
# Spurs Rocks | por terminar


def bonificar(mat) -> str:
    """ Retorna uma string com a matriz identada de modo a facilitar a leitura """
    res = "".join(str(mat))
    return res.replace('],', ']\n').replace('[[', '[\n [').replace(']]', ']\n]\n')


def construir(lin, col, func=None) -> list:
    """
    Constroi uma matriz com `lin` linhas e `col` colunas
    preenchedo em cada pos `mat[i][j]` o valor de retorno da funcao `f`.

    A funcao `f` tem como parametros `f(i, j)`
    """
    return [[func(i, j) for i in range(lin)] for j in range(col)]

n = int(input())
partidas = int(n * ((n-1)/2))
placar = construir(6, n, lambda i, j: j+1 if i == 0 else 0)
# print(bonificar(placar))
"""
[
    [team, num_partidas, pontos, cestas, cestas_sofridas, cestas_avg]

]
"""
"""   0          1          2       3           4               5 """
while n != 0:
    while partidas > 0:
        partidas -= 1
        team1, pts1, team2, pts2 = map(int, input().split())
        placar[][0] =

    #fim
    n = int(input())


