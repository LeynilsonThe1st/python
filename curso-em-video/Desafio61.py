import colors
print('-=-' * 20)
print(' ' * 6, ' Arithmetic Progression')
print('-=-' * 20)
first_term = int(input('Insert the first term: '))
reason = int(input('Insert the reason: '))
cont = 0
while cont < 10:
    print('{} '.format(first_term), end='-> ')
    first_term += reason
    cont += 1
print(colors.red, 'Finish')
