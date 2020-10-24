from datetime import date
ano = int(input('Degite o ano. Degite 0 para escolher o ano actual : '))
if ano == 0:
        ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissesto'.format(ano))
