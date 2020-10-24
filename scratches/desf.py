class Armario:
	"""Um objecto usado para armazenar dados de forma organizada. basta instancia-lo e os dados passados a ele serão armazenados em listas contendo apenas uma tipo de dado cada. Todos os parâmetros diferentes de (int, float, bool, str, list, tuple, set, dict) serão guardados na mesma lista. Caso desfazer = True, todos os dados contidos em listas, tuplas e sets serão guardados nas listas dos seus respectivos tipos

	Args:
		*dados: (Obrigatório) Tipo: qualquer
		desfazer: (Opcional), (default = False) Caso passar True, todos os dados contidos em listas, tuplas e sets serão 
	"""


	tipos = [int, float, bool, str, list, tuple, set, dict]

	def __init__(self, *dados, desfazer=False):
		self.dados = list(dados)
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

	def __arumar(self, dados):
		"""Adiciona dados no Armario e arruma os dados adicionados.

		Args:
			dados: (Obrigatório) Tipo: list, set, tuple.
		Returns:
			none.
		"""


		if not self.arrumado:
			self.__adicionar(dados)
			if self.desfazer is True:
				self.__adicionar(self.desfazer_conjunto(dados))
		else:
			pass

	def __adicionar(self, dados):
		"""Adiciona dados no Armario e arruma os dados adicionados.

		Args:
			dados: (Obrigatório) Tipo: list, set e tuplas.
		Returns:
			none.
		"""


		for dado in dados:
			if type(dado) in self.tipos:
				if type(dado) == int:
					self.inteiros.append(dado)
				elif type(dado) == float:
					self.decimais.append(dado)
				elif type(dado) == bool:
					self.binarios.append(dado)
				elif type(dado) == str:
					self.caracters.append(dado)
				elif type(dado) == list:
					self.listas.append(dado)
				elif type(dado) == tuple:
					self.tuplas.append(dado)
				elif type(dado) == set:
					self.conjuntos.append(dado)
				elif type(dado) == dict:
					self.dicionarios.append(dado)
			else:
				self.outros.append(dado)

		self.arrumado = True
		self.novos.clear()

	def desfazer_conjunto(self, lista):
		"""Desfaz os (sets,lists,tuples) aninhados (nested) e retorna uma lista lisa (flat).

		Args:
			lista: (Obrigatório) Tipo: list,tuple,set
		Returns:
			list: retorna uma lista lisa (falt)
		"""


		stack = [x for x in lista if type(x) in self.tipos[4:7]]
		dados = []
		while len(stack):
			next = stack.pop()
			if type(next) in self.tipos[4:7]:
				stack.extend(next)
			else:
				dados.append(next)

		dados.reverse()
		return dados

	def push(self, *dados):
		"""Adiciona dados no Armario e arruma os dados adicionados.

		Args:
			*dados: (Obrigatório) Tipo: Qualquer
		Returns:
			none.
		Eg: cls.push(1, 2.3, [3, 4], (5, 6), '7')
		"""


		for d in dados:
			self.dados.append(d)
			self.novos.append(d)

		self.arrumado = False
		self.__arumar(self.novos)

		return self.novos
	
	@property
	def numeros(self):
		return self.inteiros + self.decimais
	
	def info(self):
		"""Mostra todas as listas do objecto."""


		print("\n>>> Todos os dados ", self.dados)
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

def desfazer_conjunto(lista):

    stack = lista[:]
    dados = []
    while len(stack):
        next = stack.pop()
        if type(next) is list:
            stack.extend(next)
        else:
            dados.append(next)

    dados.reverse()
    return dados
