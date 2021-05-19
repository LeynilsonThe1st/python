from random import randint
from time import sleep
from colors import yellow, pink, red, blue, green

computador = randint(1, 11)
sair = False
tentativas = 3
print(yellow, '-=-' * 3, 'Eu vou pensar em um numero de 1 a 10', '-=-' * 3)
jogador = int(input('\n{}{} Vidas restantes\n{}Em que numero eu pensei ?: '.format(red, tentativas, pink)))
while not sair:
    print('\n\033[1;37;40m...    LOADING     ...\033[m')
    sleep(1)
    if jogador == computador:
        print(green, f'\nvennnnnnnnnnceeeeeeuuuuuu!!\nComputador: {computador}')
        sair = True
    elif tentativas == 1:
        print(red, f'\nPerdeuuuuuu!!\nComputador: {computador}')
        sair = True
    else:
        tentativas -= 1
        if jogador < computador - 2 or jogador > computador + 2:
            print(blue, '\nFrio')
        else:
            print(red, '\nQuente')
        jogador = int(input('\n{}{} Vidas restanttes\n{}Tenta outra vez: '.format(red, tentativas, pink)))


print(f"{red}\nFim")
