def mdc(dividendo, divisor):
    """
    O Algortimo de Euclides é um algoritmo
    que encontra o máximo divisor comum de 2 números.
    """
    resto = dividendo % divisor
    # print(dividendo, divisor, resto)
    if resto == 0:
        return divisor

    return mdc(divisor, resto)


print(mdc(1112, 695))
print(mdc(14370, 12080))
print(mdc(6, 12))
