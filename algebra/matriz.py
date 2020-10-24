"""
@author: Leynilson Harden
"""
class Matriz:
    """ Classe com funcionalidades para manipular matrizes """

    def __init__(self, matriz, i=1, j=1, fill=None):
        if matriz is None and i > 0 and j > 0:
            self.mat = construir(i, j, fill)
        elif isinstance(matriz, list):
            self.mat = matriz
        else:
            raise ValueError("Matriz tem de ter no mínimo uma linha e uma coluna [[0]]")

    def __str__(self):
        return bonificar(self.mat)

    def __repr__(self):
        return repr(self.mat)

    def __len__(self):
        return len(self.mat)

    # -mat
    def __neg__(self):
        return Matriz(percorrer(self.mat, lambda a, i, j: -a))

    # mat[i]
    def __getitem__(self, i):
        if i >= len(self.mat):
            raise IndexError(i)
        if i < 0:
            i += len(self.mat)
        return self.mat[i]

    # mat[i] = value
    def __setitem__(self, i, value):
        self.mat[i] = value

    # del mat[i]
    def __delitem__(self, i):
        raise NotImplementedError('Não pode remover elementos de uma matriz')
        # if index in self.mat:
        #     del self.mat[index]

    # value in mat
    def __contains__(self, value):
        return value in self.mat

    # for value in mat: ...
    def __iter__(self):
        return (self[i] for i in range(len(self)))

    # mat + mat
    def __add__(self, mat):
        return Matriz(soma_matriz(self, mat))
        # res = []
        # for (i, l1), l2 in zip(enumerate(self.mat), mat.mat):
        #     res.append([])
        #     for el1, el2 in zip(l1, l2):
        #         # print(el1, el2, el1 + el2)
        #         res[i].append(el1 + el2)
        # return Matriz(res)

    # mat - mat
    def __sub__(self, mat):
        return Matriz(soma_matriz(self, -mat))
        # res = []
        # for (i, l1), l2 in zip(enumerate(self), mat):
        #     res.append([])
        #     for el1, el2 in zip(l1, l2):
        #         res[i].append(el1 - el2)
        # return Matriz(res)

    # mat * mat
    def __mul__(self, value):
        if not isinstance(value, (int, Matriz)):
            raise ValueError
        return Matriz(mult_escalar(self, value) if isinstance(value, int) else mult_matriz(self, value))

    # mat * mat
    def __rmul__(self, value):
        if not isinstance(value, (int, Matriz)):
            raise ValueError
        return Matriz(mult_escalar(self, value) if isinstance(value, int) else mult_matriz(self, value))

    def __pow__(self, value):
        if value == 1:
            return Matriz(transpor(self))




def linhas(mat, n):
    return [i for i in mat[n]]

def colunas(mat, n):
    return [i[n] for i in mat]

def construir(lin, col, f=None):
    res = []
    for i in range(lin):
        res.append([])
        for j in range(col):
            if f is not None:
                res[i].append(f(i+1, j+1))
            else:
                res[i].append(f"a{i+1}{j+1}")
    return res

def percorrer(mat, f=None):
    """
    percorre a matriz e aplica uma funcao definida pelo usuario.\n
    Caso nenhuma funcao seja passada, retorna uma copia da matriz

    Parametros de `f`:\n
    # `a`: elemento de cada linha\n
    # `i`: index dos elemento de cada linha\n
    # `j`: index das linhas
    """
    return [[a if f is None else f(a, i, j) for i, a in enumerate(l)] for j, l in enumerate(mat)]

def transpor(mat):
    # return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return [[j[i] for j in mat] for i in range(len(mat[0]))]

def soma_matriz(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("As matrizes devem ter o mesmo número de linhas e de colunas")
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[i]))] for i in range(len(m1))]

    # try:
    #     return [[m1[i][j] + m2[i][j] for j in range(len(m1[i]))] for i in range(len(m1))]
    # except Exception:
    #     print('As matrizes devem ter o mesmo número de linhas e de colunas')
    #     raise

def mult_escalar(mat, escalar):
    res = []
    for i, linha in enumerate(mat):
        res.append([])
        for j in range(len(linha)):
            res[i].append(linha[j] * escalar)
    return res

def mult_matriz(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            mult = [x * y for x, y in zip(linhas(mat1, i), colunas(mat2, j))]
            res[i].append(sum(mult))
    return res

def det(mat):
    if len(mat) == len(mat[0]):
        if len(mat) == 2:
            print(bonificar(mat))
            print(mat[0][0] * mat[1][1] - mat[0][1] - mat[1][0])
            return mat[0][0] * mat[1][1] - mat[0][1] - mat[1][0]
        if len(mat) > 2:
            # res = 0
            # for i in range(len(mat)):
            #     for j in range(len(mat[i])):
            #         if i+2 % 2 == 0:
            #             res += mat[i][j] * det(cofactores(mat, i, j))
            #         else:
            #             res -= mat[i][j] * det(cofactores(mat, i, j))
            #         # res += ((-1 ** (2 + i)) * mat[i][j]) * det(cofactores(mat, i, j))
            # return res
            return sum([x * (-1**(2+j) * det(cofactores(mat, 0, j))) for j, x in enumerate(mat[0])])



def cofactores(mat, i, j):
    res = []
    c1 = 0
    for x in range(len(mat)):
        if i == x:
            c1 += 1
            continue
        else:
            res.append([])
        for y in range(len(mat)):
            if j == y:
                continue
            else:
                res[x - c1].append(mat[x][y])
    return res
    # return [[mat[x][y] if i != x and j != y else None for y in range(len(mat))] for x in range(len(mat))]


def bonificar(mat):
    res = "".join(str(mat))
    return res.replace('],', ']\n').replace('[[', '[\n [').replace(']]', ']\n]\n')

# def transpor(mat):
#     res = []
#     for i in range(len(mat[0])):
#         res.append([])
#         for j in range(len(mat)):
#             res[i].append(mat[j][i])
#     return res
