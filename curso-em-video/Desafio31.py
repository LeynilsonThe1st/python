d = float(input('Distancia? = Km  '))
if d <= 200:
    pr = 0.50*d
    print('0.50 R$ / Km')
    print('Ira pagar {:.2f} R$'.format(pr))
else:
    d > 200
    pr = 0.45*d
    print('0.45 R$ / km')
    print('Ira pagar {:.2f} R$'.format(pr))
