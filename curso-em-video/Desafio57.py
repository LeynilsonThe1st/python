import colors
sair = False
while not sair:
    sexo = str(input('Degite o seu sexo: '))
    if sexo in 'Mm' or sexo in 'Ff':
        sair = True
print(colors.red, 'Terminou')