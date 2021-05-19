""" __author__: Leynilson José "Snake" """
# Estiagem | por terminar

# Leitura dos dados
def cin():
    dados = input().split()
    return map(int, dados)

def ordenar(arr):
    print(arr)
    arr.sort(key=lambda item: item[item.index('-'):])
    print(arr)
    return arr

i = 1
m = c = None
t = int(input())
while t != 0:
    dados = []
    totalConsumo = totalMoradores = 0
    while t > 0:
        t -= 1
        (m, c) = cin()
        dados.append(f"{m}-{c // m}")
        totalMoradores += m
        totalConsumo += c

    print(f"Cidade# {i}:")
    print(ordenar(dados))
    print(f"Consumo medio: {totalConsumo / totalMoradores:.2f} m3.\n")
    i += 1
    t = int(input())




