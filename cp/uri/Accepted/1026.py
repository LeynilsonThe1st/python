""" __author__: Leynilson José "Snake" """
# Carrega ou nao carrega | accepted

# Leitura dos dados
def cin():
    try:
        global a, b
        (a, b) = input().split()
        a = int(a)
        b = int(b)
        return True
    except EOFError:
        return False

def xor(digitos):
    (x, y) = digitos
    return '0' if x == y else '1'

def criar_num_32bits(num):
    binario = bin(num)[2:]
    size = len(binario)
    if size > 32:
        array = list(binario[size - 32:])
    else:
        array = ['0'] * (32 - size)
        array.extend(list(binario))
    return array

def somaMofiz(x, y):
    n1 = criar_num_32bits(x)
    n2 = criar_num_32bits(y)
    # notei que a soma 'Mofiz' consiste em fazer o xor entre os digitos dos dois numeros
    soma = list(map(lambda digitos: xor(digitos), zip(n1, n2)))
    return int('0b' + ''.join(soma), base=0)

a = b = None
while cin():
    print(somaMofiz(a, b))
