"""
2.Dadas as matrizes A, B e C:
    |2,  3,  8|      |-3, 7,  1|      |7, -8, 3|
A = |-5, 9, -6|  B = |-4, 2,  5|  C = |4, -3, 2|
    |7,  4,  1|      |0,  9,  4|      |9, -5, 1|

Calcule:
    a) A+B;
    b) C-A;
    c) 3A-2B+4C;
    d) (A+B)C
"""
from matriz import Matriz

A = Matriz([
    [2, 3, 8],
    [-5, 9, -6],
    [7, 4, 1]
])

B = Matriz([
    [-3, 7, 1],
    [-4, 2, 5],
    [0, 9, 4]
])

C = Matriz([
    [7, -8, 3],
    [4, -3, 2],
    [9, -5, 1]
])

print('a) A+B \n')
print(A + B)

print('b) C-A \n')
print(C - A)

print('c) 3A-2B+4C \n')
print((A * 3) - (B * 2) + (C * 4))

print('d) (A+B)C \n')
print((A + B) * C)
