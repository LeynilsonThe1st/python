""" __author__: Leynilson José "Snake" """
# Super primos | accepted

def cin():
    try:
        global p
        p = int(input())
        return True
    except EOFError:
        return False

def isPrimo(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def isSuperPrimo(n):
    m = str(n)
    for i in m:
        if not isPrimo(int(i)):
            return False
    return True

p = None
while cin():

    if isPrimo(p):
        if isSuperPrimo(p):
            print("Super")
        else:
            print("Primo")
    else:
        print("Nada")
