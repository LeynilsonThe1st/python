from math import sqrt


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str(self.pontos)

    def __len__(self):
        return len(self.pontos)

    def __floordiv__(self, vector):
        return paralelo(self.pontos, vector.pontos)

    # pontos[i]
    def __getitem__(self, i):
        if i >= len(self.pontos):
            raise IndexError(i)
        if i < 0:
            i += len(self.pontos)
        return self.pontos[i]

    # pontos[i] = value
    def __setitem__(self, i, value):
        self.pontos[i] = value

    # del pontos[i]
    def __delitem__(self, i):
        raise NotImplementedError('Não pode remover elementos de um vector')

    # value in pontos
    def __contains__(self, value):
        return value in self.pontos

    # for value in pontos: ...
    def __iter__(self):
        return (self[i] for i in range(len(self)))

    def __mul__(self, vector):
        return produto_escalar(self, vector)

    def __rmul__(self, vector):
        return produto_escalar(self, vector)

    @property
    def pontos(self):
        return [self.x, self.y, self.z]


def produto_escalar(v, u,):
    res = 0
    for i, j in zip(v, u):
        res += i * j
    return res


def produto_vectorial(v, u):
    x = (v[1] * u[2]) - (v[2] * u[1])
    y = -1 * ((v[0] * u[2]) - (v[2] * u[0]))
    z = (v[0] * u[1]) - (v[1] * u[0])
    return Vector(x, y, z)


def mod(v):
    res = sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    return int(res) if int(res) == res else f"{v[0]**2 + v[1]**2 + v[2]**2}^½"


def paralelo(v, u):
    if v[0] / u[0] == v[1] / u[1] and v[1] / u[1] == v[2] / u[2]:
        res = v[0] / u[0]
        return (True, int(res) if int(res) == res else float_to_fracao(v[0], u[0]))
    return (False, None)


def float_to_fracao(numerador, denominador) -> str:
    """ Retorna o numerador e o deniminador no formato de fraccao irredutivel """
    d = 1
    i = denominador
    while True:
        i -= 1 if i >= 0 else -1
        if numerador % i == 0 and denominador % i == 0:
            break
    return f"{numerador // i}/{denominador // i}"


v = Vector(3, 0, 0)
u = Vector(0, 0, -2)

#print(u // v)
print(u * v)
print(mod(v))
print(mod(produto_vectorial(v,u)))
