# from poo_py import colors

numero = int(input('Degite um numero: '))
contador = 0
factorial = 1
print('{}!'.format(numero), end=' = ')
while contador < numero:
    factorial *= numero - contador
    print('{}'.format(numero - contador), end=' X ')
    contador += 1
print('0 = {}'.format(factorial))