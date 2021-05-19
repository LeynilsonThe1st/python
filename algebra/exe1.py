"""
1.Construa as seguintes matrizes:
    a) A = (aij)2x5, em que aij = 3i - 3j
    b) B = (bij)2x3, em que bij = i^2 + j^3
    c) C = (cij)3x3, em que cij = i + j
"""
from matriz import Matriz


def alinea_a(i, j):
    return 3 * i - 3 * j

def alinea_b(i, j):
    return (i ** 2) + (j ** 3)

def alinea_c(i, j):
    return i + j

A = Matriz(None, 2, 5, alinea_a)
B = Matriz(None, 2, 3, alinea_b)
C = Matriz(None, 3, 3, alinea_c)

print('a)\n')
print(A)

print('b)\n')
print(B)

print('c)\n')
print(C)
