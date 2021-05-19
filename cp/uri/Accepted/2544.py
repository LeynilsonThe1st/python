""" __author__: Leynilson José "Snake" """
# Kage bunshin no jutsu | accepted

# Leitura dos dados
def cin():
    try:
        global a
        a = int(input())
        return True
    except EOFError:
        return False

def dividir(n):
    counter = 0
    while n > 1:
        n //= 2
        counter += 1
    return counter

a = None
while cin():
    print(dividir(a))
