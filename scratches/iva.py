"""
Calculo de iva
"""

def calc_iva(valor, percentagem=14):
    percentagem = float(percentagem) / 100
    valor_acrescentado = valor * percentagem
    valor_com_iva = valor + valor_acrescentado
    valor_sem_iva = valor_com_iva - valor_acrescentado

    iva = {
        'valor': valor,
        'percentagem': f'{int(percentagem * 100)}%',
        'valor-acrescentado': f'{valor_acrescentado:.2f}',
        'valor-com-iva': valor_com_iva,
        'valor-sem-iva': valor_sem_iva
    }

    for key, value in iva.items():
        print(f'\n{key} : {value}')

    return valor_com_iva


def com_iva(valor, percentagem=14):
    """
    returna o valor com a adição do iva.\n
    param:\n
    valor: float | int.\n
    percentagem: float | int. default = 14
    """

    valor_com_iva = valor + valor * float(percentagem) / 100
    return valor_com_iva


def sem_iva(valor, percentagem=14):
    """
    returna o valor sem a adição do iva.\n
    param:\n
    valor: float | int.\n
    percentagem: float | int. default = 14
    """
    # valor_sem_iva = valor / percentagem
    valor_sem_iva = valor / ((percentagem + 100) / 100)
    return round(valor_sem_iva, 2)


preco = int(input("Preço: "))
preco_com_iva = com_iva(preco)
preco_sem_iva = sem_iva(preco_com_iva)


print('\n', calc_iva(preco))
print(preco, "Com iva:", preco_com_iva)
print(preco, "Sem iva:", preco_sem_iva)
