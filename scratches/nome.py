""" __Author__ : Winslet Di Caprio M. Mateus"""

def nomes(nome):
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']
    for i in range(len(nome)):
        for j in range(len(array)):
            if nome[i] == array[j]:
                print(array[j], end='|')


nome = input('Digite o seu nome: ').lower()
nomes(nome)
