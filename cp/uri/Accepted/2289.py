""" __author__: Leynilson José "Snake" """
# distancia hamming | accepted

# Leitura dos dados
def cin():
    dados = input().split()
    dados = list(map(int, dados))
    dados.sort()
    global a, b
    (a, b) = dados
    return False if a == 0 and b == 0 else True

def arrange(b1, b2):
    size1, size2 = len(b1), len(b2)
    if size1 > size2:
        b2 = ('0' * (size1 - size2)) + b2
    elif size1 < size2:
        b1 = ('0' * (size2 - size1)) + b1
    return b1, b2

def getDistance(x, y):
    counter = 0
    for i, j in zip(x, y):
        if i != j:
            counter += 1
    return counter


a = b = None
while cin():
    a, b = arrange(bin(a)[2:], bin(b)[2:])
    print(getDistance(a, b))



