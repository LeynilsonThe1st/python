""" __author__: Leynilson José "Snake" """
# Notas e moedas | accepted

notas = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0}
moedas = {1: 0, 0.50: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}

dinheiro = float(input())

for nota in notas.keys():
        while dinheiro - nota >= 0:
            notas[nota] += 1
            dinheiro -= nota

for moeda in moedas.keys():
        while round(dinheiro - moeda, 2) >= 0:
            moedas[moeda] += 1
            dinheiro -= moeda

print("NOTAS:")
for nota, counter in notas.items():
    print(f"{counter} nota(s) de R$ {nota:.2f}")

print("MOEDAS:")
for nota, counter in moedas.items():
    print(f"{counter} moeda(s) de R$ {nota:.2f}")
