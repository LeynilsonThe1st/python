lista = []
for i in range(1, 7):
    num = int(input('insert some numbers : '))
    if num % 2 == 0:
        lista.append(num)

print("A soma do pares = ", sum(lista))
