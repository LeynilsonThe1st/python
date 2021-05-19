import colors

n_termos = int(input('Degite um numero: '))
i = 0
n1 = 0
n2 = 1
c = i
while i < n_termos:
    c += 1
    n = n1 + n2
    print(' {}{}'.format(colors.pink ,n1), colors.green, end=' ,')
    n1 = n2
    n2 = n
    i += 1
    if i == 10 or c == 10:
        print('\n', end='')
        c = 0
