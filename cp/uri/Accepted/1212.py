""" __author__: Leynilson José "Snake" """
# Aritmetica Primaria | accepted

# retorna um array com os digitos do num passado
def getDigits(num) -> list:
    arr = []
    while num > 0:
        resto = num % 10
        num = (num - resto) / 10
        arr.append(int(resto))
    arr.reverse()

    size = len(arr)
    if size < 9:
        arr = [0] * (9 - size) + arr
    return arr

# Leitura dos dados
def cin() -> bool:
    dados = input().split()
    global a, b # Acesso a variaveis gloabais
    (a, b) = map(lambda num: int(num), dados)
    return False if a == 0 and b == 0 else True

# Impressao dos dados
def cout(carry) -> None:
    if carry == 0:
        print("No carry operation.")
    elif carry == 1:
        print(carry, "carry operation.")
    else:
        print(carry, "carry operations.")

# Codigo principal
a = b = None
while cin():
    carry = 0
    vai1 = False
    x = getDigits(a)
    y = getDigits(b)
    print(x)
    print(y)
    # for x, y in zip(getDigits(a), getDigits(b)):
    for i in range(8, -1, -1):
        # se a soma de cada digito for > que 9
        # quer dizer que "vai 1"
        if vai1:
            if x[i] + y[i] + 1 > 9:
                carry += 1
            else:
                vai1 = False
        else:
            if x[i] + y[i] > 9:
                carry += 1
                vai1 = True
        print(vai1, x[i], y[i], carry)

    cout(carry)
