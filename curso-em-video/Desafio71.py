import colors as c
print(f'{c.bold + c.yellow}-' * 40, '\n', '{:^40}'.format('BANCO CEV'), '\n', '-' * 40)
valor = int(input('INSIRA A QUANTIA A QUE QUER LEVANTAR: '))
d = {'50': 0, '20': 0, '10': 0, '1': 0, }
while True:
    if valor > 50:
        valor -= 50
        d['50'] += 1
    elif valor >= 20:
        valor -= 20
        d['20'] += 1
    elif valor >= 10:
        valor -= 10
        d['10'] += 1
    elif valor >= 1:
        valor -= 1
        d['1'] += 1
    elif valor >= 0:
        break  
if d["50"] > 0:
    print(f'TOTAL DE NOTAS: {d["50"]} DE 50USD')
if d["20"] > 0:
    print(f'TOTAL DE NOTAS: {d["20"]} DE 20USD')
if d["10"] > 0:
    print(f'TOTAL DE NOTAS: {d["10"]} DE 10USD')
if d["1"] > 0:
    print(f'TOTAL DE NOTAS: {d["1"]} DE 1USD')
# print(f'{d["50"]*50 + d["20"]*20 + d["10"]*10 + d["1"]*1}')
