sal = float(input('Quanto vc ganha? R$  '))
if sal > 1250:
    aum = sal + (sal * (10 / 100))
    print('O seu salario sera de {:.2f} R$'.format(aum))
else:
    aum = sal + (sal * (15 / 100))
    print('O seu salario sera de {:.2f} R$'.format(aum))