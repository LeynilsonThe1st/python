from random import randint as rd
import colors
cpu = rd(0, 10)
vitorias = 0
estado = ""
digitou = False
print('==--==--' * 6)
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    if not digitou:
        print('==--==--' * 6)
        ply = int(input('Escolhec um numero: '))
        digitou = True
    ParOuImpar = str(input('Par ou Impar? [P/I] '))
    if ParOuImpar in 'Pp':
        estado = "Par"
    elif ParOuImpar in 'Ii':
        estado = "impar"
    if (ply + cpu) % 2 == 0 and ParOuImpar in 'Pp' or (ply + cpu) % 2 == 1 and ParOuImpar in 'Ii':
        vitorias += 1
        digitou = False
        print('---' * 20)
        print(f'Voce jogou {ply} e o Computador {cpu}. Total de {ply + cpu} deu {estado}')
        print('---' * 20)
        print('Voce Veeenceu!\nVamos jogar novamente...')
    elif (ply + cpu) % 2 == 0 and ParOuImpar in 'Ii' or (ply + cpu) % 2 == 1 and ParOuImpar in 'Pp':
        print('---' * 20)
        print(f'Voce jogou {ply} e o Computador {cpu}. Total de {ply + cpu} deu {estado}')
        print('---' * 20)
        print('Voce perdeu!')
        break
print(f'Game Over, Voce venceu {vitorias} vezes.')
        