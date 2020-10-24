n1 = float(input('Primeira recta: '))
n2 = float(input('Segunda recta: '))
n3 = float(input('Terceira recta: '))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n1 + n2:
    print('As recta formam um triangulo! ')
else:
    print('As rectas nao formam um triangulo! ')
