import colors
numeros = 0
soma = 0
sair = False
while not sair:
    num = int(input('Degite um numero inteiro: '))
    if num == 999:
        sair = True
        print('Fim')
    else:
        numeros += 1
        soma += num
print('Soma dos {} numeros inseridos = {}'.format(numeros, soma))
