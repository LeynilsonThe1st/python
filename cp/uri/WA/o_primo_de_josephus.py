""" __author__: Leynilson José "Snake" """
# Uri Online Judge | 1032 wrong answer

# verifica a primalidade de n
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

# retorna um numero primo tal que a quantidade
# de primos que o antecedem seja igual a n-1
def getPrimo(n):
    p = 2
    c = 0
    while c != n:
        if isPrimo(p):
            c += 1
        p += 1
    return p - 1

# retorna um numero primo maior que n
def getNextPrimo(n):
    c = 1
    n += 1
    while True:
        if isPrimo(n):
            return c
        c += 1
        n += 1

n = int(input())
while n != 0:
    print(getNextPrimo(getPrimo(n)), file=open('saida.txt', 'a'))
    n = int(input())

# 2,3,5,7,11,13,17,19,23,27,29,31,37,39,41,43
# 1,2,3,4,05,06,07,08,09,10,11,12,13,14,15,16

"""
        2(3)
1(2)           3(5)

6(13)          4(7)
        5(11)


"""

