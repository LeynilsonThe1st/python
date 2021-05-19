import math

# an = an-1 + n
def soma1(n=100):
    if n == 1:
        return 1
    return soma1(n - 1) + n


# an = ( an - 1 ) / ( n )
def soma2(n=100):
    if n == 1:
        return 1
    return soma1(n - 1) / n

# an = ( ( -1 ) ** n ) * ( ( n**2 - 1 ) / ( 2n + 1) )
def soma3(n=100):
    soma = 0
    while n > 0:
        soma += ((-1) ** n) * (((n ** 2) - 1) / (2 * n + 1))
        n -= 1
    return soma

def soma3_1(n=100):
    if n == 1:
        return ((-1) ** n) * (((n ** 2) - 1) / (2 * n + 1))
    return ((-1) ** n) * (((n ** 2) - 1) / (2 * n + 1)) + soma3_1(n-1)

# print(soma1())
# print(soma2())
# print(soma3())
# print(soma3_1())


def func(x, y):
    return math.sqrt(x) / (((y) ** 2) - 1)

# print(func(-50, -4))
# print(func(-48, -39))
print(func(0, 0))
print(func(48, 39))
print(func(50, 40))
