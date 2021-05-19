"""
@author: <leinilsonsn@gmail.com> Leynilson Harden

Este modulo contem funcoes para manipular matrizes e realizar operacoes basicas com matrizes
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

    # value in mat
    def __contains__(self, value):
        return value in self.mat

    # for value in mat: ...
    def __iter__(self):
        return (self[i] for i in range(len(self)))

    # mat + mat
    def __add__(self, mat):
        return Matriz(soma_matriz(self, mat))

    # mat - mat
    def __sub__(self, mat):
        return Matriz(soma_matriz(self, -mat))

    # mat * mat ou escalr * mat
    def __mul__(self, value):
        if not isinstance(value, (int, float, Matriz)):
            raise ValueError
        return Matriz(mult_escalar(self, value) if isinstance(value, (int, float)) else mult_matriz(self, value))

    # mat * mat ou escalr * mat
    def __rmul__(self, value):
        if not isinstance(value, (int, float, Matriz)):
            raise ValueError
        return Matriz(mult_escalar(self, value) if isinstance(value, (int, float)) else mult_matriz(self, value))

    # mat ** 1 retorna a matriz transposta
    # mat ** -1 retorna a matriz inversa
    def __pow__(self, value):
        if value == 1:
            return Matriz(transpor(self))
        elif value == -1:
            return Matriz(inversa(self))


def linhas(mat, n):
    return [i for i in mat[n]]

def colunas(mat, n):
    return [i[n] for i in mat]

def construir(lin, col, func=None) -> list:
    """
    Constroi uma matriz com `lin` linhas e `col` colunas
    preenchedo em cada pos `mat[i][j]` o valor de retorno da funcao `f`.

    A funcao `f` tem como parametros `f(i, j)`
    """
    return [[f"a{i+1}{j+1}" if func is None else func(i, j) for i in range(lin)] for j in range(col)]
    # res = []
    # for i in range(lin):
    #     res.append([])
    #     for j in range(col):
    #         if func is not None:
    #             res[i].append(func(i, j))
    #         else:
    #             res[i].append(f"a{i+1}{j+1}")
    # return res

def percorrer(mat, func=None) -> list:
    """
    percorre a matriz e aplica uma funcao definida pelo usuario.\n
    Caso nenhuma funcao seja passada, retorna uma copia da matriz

    Parametros de `f`:\n
    # `a`: elemento de cada linha\n
    # `i`: index dos elemento de cada linha\n
    # `j`: index das linhas
    """
    return [[a if func is None else func(a, i, j) for i, a in enumerate(l)] for j, l in enumerate(mat)]

def transpor(mat) -> list:
    """ Retorna a matriz transposta """
    return [[j[i] for j in mat] for i in range(len(mat[0]))]

def inversa(mat) -> list:
    """ Retorna a matriz inversa """
    d = det(mat)
    if d == 0:
        raise ValueError("A matriz não é inversivel, det(mat) = 0")
    return mult_escalar(adjunta(mat), 1 / d)

def soma_matriz(m1, m2) -> list:
    """ Soma duas matrizes """
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("As matrizes devem ter o mesmo número de linhas e de colunas")
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[i]))] for i in range(len(m1))]

def mult_escalar(mat, escalar) -> list:
    """ Multiplica uma matriz por um número """
    return percorrer(mat, lambda a, i, j: a * escalar)

def mult_matriz(mat1, mat2) -> list:
    """multiplica duas matrizes"""
    if len(mat1[0]) != len(mat2):
        raise ValueError("O número de colunas da 1ª matriz não é igual ao número de linhas da 2ª")
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            mult = [x * y for x, y in zip(linhas(mat1, i), colunas(mat2, j))]
            res[i].append(sum(mult))
    return res

def det(mat) -> int:
    """ calcula o determinane """
    if len(mat) == len(mat[0]):
        if len(mat) == 1:
            return mat[0][0]
        elif len(mat) == 2:
            return mat[0][0] * mat[1][1] - (mat[0][1] * mat[1][0]) # Sarrus
        elif len(mat) > 2:
            return sum([x * pow(-1, 2+j) * det(cofactores(mat, 0, j)) for j, x in enumerate(mat[0])]) #L'Place

def mat_cofactores(mat) -> str:
    """ retorna a matriz dos cofactores """
    cof = []
    for i in range(len(mat)):
        cof.append([])
        for j in range(len(mat)):
            cof[i].append(pow(-1, i+j) * det(cofactores(mat, i, j)))
    return cof

def adjunta(mat) -> str:
    """ Retorna a matriz adjunta """
    return transpor(mat_cofactores(mat))

def cofactores(mat, i, j) -> list:
    """ Retorna a matriz sem os elementos da linha `i` e da coluna `j` (LaPlace) """
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

def mat_identidade(ordem) -> list:
    return construir(ordem, ordem, lambda i, j: 1 if i==j else 0)

def resolver_sistema(a, b, inversa=False) -> dict:
    """ Resolve o sistema com o metodo de cremmer ou da matriz inversa """
    return metodo_inversa(a, b) if inversa else metodo_crammer(a, b)

def metodo_inversa(a, b) -> dict:
    """ resolve o sistema utilizando o metodo da matris inversa """
    d = det(a)
    if d != 0:
        de = 1 / d
        mat = mult_matriz(adjunta(a), construir(len(a), 1, lambda i, j: b[i])) 
        res = [int(de*x) if int(de*x) == de*x else float_to_fracao(x, d) for x in colunas(mat, 0)]
        return dict(zip([f"X{i+1}" for i in range(len(mat))], res))

def metodo_crammer(a, b) -> dict:
    """ resolve o sistema utilizando o metodo da matris inversa """
    ordem = len(b)
    res = []
    axn = []
    d = det(a)
    if d != 0:
        print(d)
        for xn in range(ordem):
            axn.append(percorrer(a, lambda el, i, j: b[j] if i == xn else el))
            r = det(axn[xn]) / d
            res.append(int(r) if int(r) == r else float_to_fracao(det(axn[xn]), d))
            
        return dict(zip([f"X{x+1}" for x in range(ordem)], res)) 

def float_to_fracao(numerador, denominador) -> str:
    """ Retorna o numerador e o deniminador no formato de fraccao irredutivel """
    d = 1
    i = denominador if denominador>0 else -denominador
    while True:
        i -= 1
        # print(numerador, denominador, i)
        if  numerador % i == 0 and denominador % i == 0:
            break
    return f"{numerador // i}/{denominador // i}"

def bonificar(mat) -> str:
    """ Retorna uma string com a matriz identada de modo a facilitar a leitura """
    res = "".join(str(mat))
    return res.replace('],', ']\n').replace('[[', '[\n [').replace(']]', ']\n]\n')
