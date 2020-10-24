"""
Uma modulo desenvolvido para facilitar a filtração de dados
em listas, tuplas e sets.
"""


class Armario:
    """
    Uma classe usada para armazenar dados de forma organizada.
    basta instancia-lo e os dados passados a ele serão armazenados
    em listas contendo apenas um tipo de dado cada. Todos os parâmetros
    de tipo diferentes de (int, float, bool, str, list, tuple, set, dict)
    serão guardados na mesma lista.

    Caso `desfazer = True`, todos os dados contidos em listas, tuplas e sets
    serão guardados nas listas dos seus respectivos tipos

    Args: `dados == any`, `desfazer == bool`, default False
    """

    tipos = (int, float, bool, str, list, tuple, set, dict)

    def __init__(self, *dados, desfazer=False):
        self.dados = self.__find(list(dados))
        self.inteiros = []
        self.decimais = []
        self.binarios = []
        self.caracters = []
        self.listas = []
        self.tuplas = []
        self.conjuntos = []
        self.dicionarios = []
        self.outros = []
        self.novos = []
        self.arrumado = False
        self.desfazer = desfazer if desfazer else False
        self.__arumar(self.dados)

    def __repr__(self):
        return "Armário - tamanho: " + str(self.__contar_dados())

    def __str__(self):
        return "Armário - tamanho: " + str(self.__contar_dados())

    def __contar_dados(self):
        if self.desfazer:
            return len(self.numeros) + len(self.caracters) + len(self.binarios) + len(self.outros)

        return len(self.dados)

    def __find(self, dados) -> list:
        """
        find() -> list

        caso seja passada uma lista aninhada

        ex: `[[[1, 2, [3, 4], (5, 6)]]]`

        retorna sempre um lista flat sem alterar o conteudo
        da lista

        `[1, 2, [3, 4], (5, 6)]`
        """

        if len(dados) == 1 and isinstance(dados[0], self.tipos[4:7]):
            return self.__find(dados[0])
        return dados

    def __arumar(self, dados):
        """Adiciona dados no Armario e arruma os dados adicionados."""

        if not self.arrumado:
            if self.desfazer is True:
                self.__adicionar(self.__desfazer_conjunto(dados))
            else:
                self.__adicionar(dados)
        else:
            pass

    def __adicionar(self, dados):
        """
        Adiciona dados no Armario e arruma os dados adicionados.

        Args: dados == any.
        """

        for dado in dados:
            if isinstance(dado, self.tipos):
                if isinstance(dado, bool):
                    self.binarios.append(dado)
                elif isinstance(dado, int):
                    self.inteiros.append(dado)
                elif isinstance(dado, float):
                    self.decimais.append(dado)
                elif isinstance(dado, str):
                    self.caracters.append(dado)
                elif isinstance(dado, list):
                    self.listas.append(dado)
                elif isinstance(dado, tuple):
                    self.tuplas.append(dado)
                elif isinstance(dado, set):
                    self.conjuntos.append(dado)
                elif isinstance(dado, dict):
                    self.dicionarios.append(dado)
            else:
                if dado is not None:
                    self.outros.append(dado)

        self.arrumado = True
        self.novos.clear()

    def __desfazer_conjunto(self, lista):
        """
        desfazer_conjunto() -> list.

        Arg: lista == list or tuple or set

        Desfaz os (sets, lists, tuples) aninhados (nested)
        e retorna uma lista lisa (flat).
        """

        pilha = lista[:]
        dados = []
        while len(pilha) >= 1:
            seguinte = pilha.pop()
            if isinstance(seguinte, self.tipos[4:7]):
                pilha.extend(self.__find(seguinte))
                if isinstance(seguinte, list):
                    self.listas.append(self.__find(seguinte))
                elif isinstance(seguinte, tuple):
                    self.tuplas.append(seguinte)
                elif isinstance(seguinte, set):
                    self.conjuntos.append(seguinte)
            else:
                dados.append(seguinte)

        dados.reverse()
        return dados

    def push(self, *dados):
        """
        Adiciona dados no Armario e arruma os dados adicionados.

        push() -> list

        Args: *dados == any

        Eg: cls.push(1, 2.3, [3, 4], (5, 6), '7')
        """

        for dado in dados:
            self.dados.append(dado)
            self.novos.append(dado)

        self.arrumado = False
        self.__arumar(self.novos)

        return self.novos

    @property
    def numeros(self):
        """
        numeros -> list

        Este método será tratado como uma propriedade (variavel)
        retorna uma lista de todos os numeros adicionados ao objecto.

        Se `desfazer == True` retonrna todos o números incluindo os números
        contidos em listas, sets ou tuplas
        """

        return self.inteiros + self.decimais

    def info(self):
        """Mostra todas as listas do objecto."""
        print("\n===========================================================\n")
        print(">>> Todos os dados ", self.dados)
        print(">>> Todos os dados int    ", self.inteiros)
        print(">>> Todos os dados float  ", self.decimais)
        print(">>> Todos os numeros      ", self.numeros)
        print(">>> Todos os dados bool   ", self.binarios)
        print(">>> Todos os dados str    ", self.caracters)
        print(">>> Todos os dados list   ", self.listas)
        print(">>> Todos os dados tuple  ", self.tuplas)
        print(">>> Todos os dados set    ", self.conjuntos)
        print(">>> Todos os dados dict   ", self.dicionarios)
        print(">>> Outros                ", self.outros)
