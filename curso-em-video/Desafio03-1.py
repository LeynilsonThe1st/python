n1 = int(input('\33[0;31mdegite um número '))
n2 = int(input('\33[0;34mdegite outro número '))

print('\33[4;36mA soma de {} + {}  = {}' .format(n1, n2, n1+n2))
print('\33[4;32mA subtrcção de {} - {}  = {}' .format(n1, n2, n1-n2))
print('\33[4;33mA multiplicação de {} * {}  = {}' .format(n1, n2, n1*n2))
print('\33[4;35mA divisão de {} / {}  = {}' .format(n1, n2, n1/n2))
print('\33[7;30mPronto\33[m')
