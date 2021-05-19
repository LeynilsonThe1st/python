distância = float(input('degite a distância percorrida: '))
dias = int(input('degite os dias alugados: '))
pr = (60 * dias) + (0.15 *distância)
print('o preço  a pagar será de {:.2f} kz'.format(pr))
