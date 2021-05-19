""" __author__: Leynilson José "Snake" """
# Blobs | accepted

def calcDias(consumo):
    i = 0
    while consumo > 1:
        consumo /= 2
        i += 1
    return i

n = float(input())
while n > 0:
    n -= 1
    c = float(input())
    print(calcDias(c), "dias")
