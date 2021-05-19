""" __author__: Leynilson José "Snake" """

def contarPares(dic) -> int:
    numPares = 0
    for m, l in dic.items():
        if 0 in l.values(): continue
        else: numPares += min(l.values())
    return numPares

# Leitura dos dados
def cin() -> bool:
    try:
        global t
        t = int(input())
        return True
    except EOFError:
        return False

t = None
while cin():
    pares = {}  # Ex: {'45': {'e': 1, 'd': 1}, '43': {'e': 1, 'd': 1}}
    while t > 0:
        t -=1
        (m, l) = input().split()
        if m in pares.keys():
            pares[m][l] += 1
        else:
            pares[m] = {'e': 1 if l == 'e' else 0, 'd': 1 if l == 'd' else 0}

    print(contarPares(pares))