n = str(input('Qual eh o seu nome?  ')).strip()
nome = n.split ()
print('primeiro = {}'.format(nome[0]))
print('Ultimo = {}'.format(nome[len(nome)-1]))
