class Pessoa():

    def __init__(self, nome, sobrenome, idade):
        self.nome = nome.strip().capitalize()
        self.sobrenome = sobrenome.strip().capitalize()
        self.idade = int(idade)
        self.nome_completo = f"{self.nome} {self.sobrenome}"

    def saudar(self):
        print(f"\n>>> Olá! Eu chamo-me {self.nome_completo} e tenho {self.idade} anos de idade.")

    def fazer_anos(self):
        self.idade += 1

    def info(self):
        print(f"\nNome : {self.nome}\nSobrenome : {self.sobrenome}\nIdade : {self.idade}")


bob = Pessoa("bob","marley", "23")
bob.saudar()
bob.info()
bob.fazer_anos()
bob.info()
print(bob.idade)
