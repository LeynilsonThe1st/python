import colors
print('-=-' * 20)
print(' ' * 6, ' Arithmetic Progression')
print('-=-' * 20)
first_term = int(input('Insert the first term: '))
log = first_term
reason = int(input('Insert the reason: '))
num_of_terms = 5
count = 0
sair = False
while not sair:
    while count < num_of_terms:
        print('{} '.format(first_term), end='-> ')
        first_term += reason
        count += 1
    print(colors.red, 'Finish', colors.clear)
    more = int(input('How many terms you want to see : '))
    if more == 0:
        sair = True
    else:
        num_of_terms += more
        first_term = log
        count = 0

print(colors.red, 'Finish')
