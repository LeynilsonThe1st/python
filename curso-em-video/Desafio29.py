vel = float(input('Qual  é a velocidade do carro? '))
multa = (vel - 80)*7
if vel >= 80:
    print('Vc foi multado!')
    print('A sua multa = {:.1f} R$'.format(multa) )
print('velocidade do carro = {:.1f} Km/h'.format(vel))
