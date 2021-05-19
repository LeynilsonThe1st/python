import colors
numeros = 0
media = 0
maior = 0
menor = 0
sair = False
while not sair:
    num = int(input('Degite um numero inteiro: '))
    if num > maior:
        maior = num
        if menor == 0:
            menor = num
    if num < menor:
        menor = num
    numeros += 1
    media += num
    escolha = str(input('Deseja sair [S, N]? \nR: '))
    if escolha in 'Ss':
        sair = True
        print('Fim')
    elif escolha in 'Nn':
        sair = False
print('Media dos {} numeros inseridos = {}\nMaior = {}\nMenor = {}'.format(numeros, media/numeros, maior, menor))
# print('Media dos {} numeros inseridos = {}\nMaior = {}\nMenor = {}'.format(numeros, media/numeros, maior, menor))
