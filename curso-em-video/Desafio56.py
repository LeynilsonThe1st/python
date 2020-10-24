import colors
mNome = ''
idades = 0
maior = 0
media = 0
f = 0
fIdades = 0
fMaior = 0

for i in range(1, 6):
    print('{}----- {}ª PESSOA -----'.format(colors.blue, i))
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: '))
    idades += idade

    if idade > maior:
        if sexo == 'f':
            fMaior = idade
        else:
            maior = idade
            mNome = nome

    if sexo == 'f':
        f += 1
        fIdades += idade

if fIdades < 20:
    estado = 'menos'
else:
    estado = 'mais'
    
media = idades / 5
print('A média de idades do grupo é de {} '.format(media))
print('O homem mais velho tem {} anos e se chama {} '.format(maior, mNome))
print('Ao todo são {} mulheres com {} de {} anos'.format(f, estado, fMaior))
