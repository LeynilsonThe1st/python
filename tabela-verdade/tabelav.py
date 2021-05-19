class Tabelav:

    def __init__(self, nomes):
        self.variaveis = len(nomes)
        self.combinacoes = pow(2, self.variaveis)
        self.tabela = construir(nomes, self.combinacoes)
        self.tabela_modificada = construir(nomes, self.combinacoes)

    def __str__(self):
        return bonificar(self.tabela_modificada)

    def proposicao(self, nome, prop=None):
        if prop:
            self.tabela_modificada[0].append(nome.upper())
            for i in range(1, len(self.tabela_modificada)):
                self.tabela_modificada[i].append(int(prop(*self.tabela[i])))


def construir(nomes, comb):
    tabela = []
    valores = [0, 1]
    for i in range(1, len(nomes)+1):
        tabela.append([])
        d = pow(2, len(nomes) - i)
        c = comb / d
        j = 0
        for j in range(int(c)):
            for k in range(d):
                tabela[i-1].append(valores[j])
        valores.extend(valores)
    tabela = transpor(tabela)
    tabela.insert(0, [nome.upper() for nome in nomes])
    return tabela


def xor(a, b, *args):
    res = int(a != b)
    if args is not None:
        for arg in args:
            res = int(res != arg)
    return res


def xnor(a, b, *args):
    return not xor(a, b, args)


def transpor(tabela):
    return [[j[i] for j in tabela] for i in range(len(tabela[0]))]


def bonificar(mat) -> str:
    res = "".join(str(mat)).replace(
        '],', '|\n').replace('[[', ' |').replace('[', '|').replace(']]', '|\n')
    return res.replace('0', ' 0 ').replace('1', ' 1 ').replace(', ', '|')


def funS(a, b, c):
    w = not(a) and not(b) and not(c)
    x = not(a) and b and c
    y = not(a) and b and not(c)
    z = a and b and not(c)
    return w or x or y or z


# T = Tabelav(['a', 'b', 'c'])
# T.proposicao('P', lambda a, b, c: (not a and (b or not(c))) or b and not(c))
# T.proposicao('Q', lambda a, b, c: (b and not(a and c)) or not(a or c))
# T.proposicao('R', lambda a, b, c: (not(c) and (not(a) or b)) or not(a) and b)
# T.proposicao('S', funS)
# T.proposicao('T', lambda a, b, c: (not(a) and b)
#              or not(a or c) or (b and not(c)))
# T.proposicao('U', lambda a, b, c: not(a or c) or (b and xor(a, c)))


# print(T)

T = Tabelav(['a', 'b', 'c'])
T.proposicao('P', lambda a, b, c: not(not(xnor(a, b and not(c))) and a or not(b)))
T.proposicao('Q', lambda a, b, c: not(a) or (b and not(c)))
T.proposicao('R', lambda a, b, c: not(a) or (a and b and not(c)))



print(T)




