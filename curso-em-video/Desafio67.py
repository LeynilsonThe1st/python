import colors
while True:
    c = 1
    num = int(input('\nQuer ver a tabuada e qual valor: '))
    if num < 0:
        break 
    else:       
        while c <= 12:
            print(f'{num} X {c} = {num*c}')
            c += 1
print(f'{colors.red}FIM')