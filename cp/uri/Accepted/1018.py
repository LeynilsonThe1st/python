""" __author__: Leynilson José "Snake" """
# Uri Online Judge | 1018 accepted

notas = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

dinheiro = int(input())
d = dinheiro

for nota in notas.keys():
        while dinheiro - nota >= 0:
            notas[nota] += 1
            dinheiro -= nota

print(d)
for nota, counter in notas.items():
    print(f"{counter} nota(s) de R$ {nota},00")
