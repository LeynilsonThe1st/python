"""
2.Dadas as matrizes A, B, C e D. Calcule:

    a) (AB)^T;
    b) (AB)D^T;
    c) A(BD^T);
    d) B^TC;
    e) 2(A^TB^T)+3C^T
"""
from matriz import Matriz

A = Matriz([
    [5, 0, 6],
    [-8, 0, 3],
    [-2, 2, 7],
    [1, -1, -5]
])

B = Matriz([
    [1, -3, -2, 4],
    [7, 8, 5, 9],
    [0, 6, 3, -8]
])

C = Matriz([
    [2, 3, 0],
    [1, 1, -8],
    [3, 5, 4]
])

D = Matriz([
    [5, 0, 3, 2],
    [-8, 1, -2, 4],
    [-3, 2, 1, -5],
    [0, 1, 0, 2]
])

print(f"\n a) (AB)^T\n{(A * B) ** 1}")
print(f"\n b) (AB)D^T\n{(A * B) * D ** 1}")
print(f"\n c) A(BD^T);\n{A * (B * D ** 1)}")
print(f"\n d) B^TC\n{B ** 1 * C}")
print(f"\n e) 2(A^TB^T)+3C^T\n{2 * (A ** 1 * B ** 1) + 3 * (C ** 1)}")
