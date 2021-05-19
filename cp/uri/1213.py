""" __author__: Leynilson José "Snake" """
# Ones | por enviar


# Leitura dos dados
def cin():
    try:
        global y
        y = int(input())
        return True
    except EOFError:
        return False


def countOnes(a, b, y, c):
    a += b
    b *= 10
    if a % y != 0:
        return 1 + countOnes(a % y, b % y, y, c+1)
    return 1


y = None
while cin():
    """
        x % y == 0
        onde x: [1, 11, 111, 1111, 11....)
           e x: [10^0 + 10^1 + 10^2 .....)
        se X = a + b
        entao a = 10^0 e b = 10^1
        depois a = a + b e b = b * 10
        ate [(a % y) + (b % y)] % y == 0
    """
    print(countOnes(0, 1, y, 1))
