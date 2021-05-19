"""
4.Dadas as matrizes A, B, C e D:

    |1, -2|                                      |1,   7,  3, −8|
A = |3,  1|  B = |1, 3, -5, -7|  C = |2,  4| D = |−3, −1, −1, −3|
    |7, -4|      |6, 2, -8,  3|      |-3, 5|     |4,   1,  9,  0|
    |5,  9|                                      |5,   3,  2, −3|


Calcule:
    a) AB
    b) (AB)D
    c) A(BD)
    d) BA
    e) (BA)C
    f) B(AC)
"""
from matriz import Matriz


A = Matriz([
    [1, -2],
    [3, 1],
    [7, -4],
    [5, 9],
])

B = Matriz([
    [1, 3, -5, -7],
    [6, 2, -8, 3]
])

C = Matriz([
    [2, 4],
    [-3, 5]
])

D = Matriz([
    [1, 7, 3, -8],
    [-3, -1, -1, -3],
    [4, 1, 9, 0],
    [5, 3, 2, -3]
])

print('a) AB\n')
print(A * B)

print('b) (AB)D\n')
print((A * B) * D)

print('c) A(BD)\n')
print(A * (B * D))

print('d) BA\n')
print(B * A)

print('e) (BA)C\n')
print((B * A) * C)

print('f) B(AC)\n')
print(B * (A * C))
