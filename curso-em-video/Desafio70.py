import colors as c
print(f'{c.blue}-' * 38, '\n\t', 'LOJA SUPER BARATÃO', '\n', '-' * 38)
tot_compra = tot_produto = 0
prod_barato = ' '
preco_barato = 0
while True:
    nome_produto =  str(input('Nome do produto: ')).strip().capitalize()
    preco =  float(input('Preço: USD '))
    tot_compra += preco
    if preco > 100:
        tot_produto += 1
    if preco_barato == 0:
        preco_barato = preco
        prod_barato = nome_produto
    elif preco < preco_barato:
        preco_barato = preco
        prod_barato = nome_produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N] ')).strip().upper()
    if continuar in 'N':
        break
print(f'\n{c.green}O total de compras foi: {tot_compra:2f}\nTemos {tot_produto} produto\s custando mais de 100USD\nO produto mais barato foi: {prod_barato} que custa {preco_barato:2f} {c.clear}')
