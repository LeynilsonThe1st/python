import colors
tot_pessoas = tot_homens = tot_mulheres = 0
while True:
    print(f'{colors.blue}-' * 38, '\n\t', 'CADASTRAR UMA PESSOA', '\n', '-' * 38)
    idade = int(input(f'{colors.yellow}Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'Sexo:{colors.clear} [{colors.blue}M{colors.clear} / {colors.pink}F{colors.clear}]{colors.yellow} ')).strip().upper()
    if idade > 18:
        tot_pessoas += 1
    if sexo == 'M':
        tot_homens += 1
    elif sexo == 'F' and idade < 20:
        tot_mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input(f'\n{colors.red}Continuar: [S/N] ')).upper()
    if continuar in 'N':
        break
print(f'\n{colors.green}Total de pessoas com mais de 18 anos: {tot_pessoas}\nAo todo temos {tot_homens} homen/s cadastrado/s\nE temos {tot_mulheres} mulheres com menos de 20 anos {colors.clear}')      