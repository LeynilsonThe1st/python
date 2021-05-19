from random import randint
from time import sleep
com = randint(0, 5)
print('\033[4;36m-=-' * 5, '\033[4;30meu vou pensar em um numero de 0 a 5', '\033[4;36m-=-' * 5)
jog = int(input('\033[0;33mEm que numero eu pensei ?'))
print('\n\033[1;37;40m...    LOADING     ...\033[m')
sleep(2)
if jog == com:
    print('\n\033[0;32mvenceu')
else:
    print('\n\033[0;31mperdeu seu idiota! eu pensei no numero {}. '.format(com))
print('\n\033[4;30mFim')

