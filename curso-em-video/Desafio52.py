pink = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
clear = '\033[0m'
bold = '\033[1m'
underline = '\033[4m'

number = int(input('\033[92mInsert a Number : \033[0m'))
divide_times = 0
status = ''
c = 0
for i in range(1, number + 1):
    c += 1
    if (number / i).is_integer():
        color = yellow
        divide_times += 1
        print('{} {} '.format(color, i), end='')
        if i == 10 or c == 10:
            print('\n', end='')
            c = 0
    else:
        color = red
        print('{} {} '.format(color, i), end='')
        if i == 10 or c == 10:
            print('\n', end='')
            c = 0

if divide_times <= 2:
    status = 'prime'
else:
    status = 'not prime'
print('\nThe number {} was devised {} times\nand it is a {}!'.format(number, divide_times, status))
