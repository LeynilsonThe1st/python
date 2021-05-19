print('-=-' * 20)
print(' ' * 6, ' Arithmetic Progression')
print('-=-' * 20)
red = '\033[0;31m'
first_term = int(input('Insert the first term: '))
reason = int(input('Insert the reason: '))
ap = 0
ap += first_term + (10 - 1) * reason
for i in range(first_term, ap + reason, reason):
    print('{} '.format(i), end='-> ')
print('{}finish'.format(red))
