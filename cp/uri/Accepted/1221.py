""" __author__: Leynilson José "Snake" """
# Luzes de natal | accepted

def maiorSequencia(binario):
    sequencias = []
    maior = 0
    for digito in binario:
        if digito == '1':
            maior += 1
        else:
            sequencias.append(maior)
            maior = 0
    #sequencias.append(maior)
    return max(sequencias)

n = int(input())
while n > 0:
    n -= 1
    x = int(input())
    print(maiorSequencia(bin(x)[2:]))

