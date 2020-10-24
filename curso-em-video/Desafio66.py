import colors
soma = 0
numeros = 0

while True:
    while True:
        num = int(input('Degite um numero (999 para parar): '))
        if num == 999:
            break
        else:
            numeros += 1
            soma += num
    print(f'A soma dos {numeros} numeros foi {soma}!')
    continuar = str(input('\nQuer inserir outros numeros? (S ou N): '))
    if continuar in 'Nn':
        break
