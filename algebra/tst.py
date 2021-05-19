from matriz import *

A = Matriz([
    [1, 0, 1, 0],
    [3, 1, -3, 1],
    [-9, 6, -9, -6],
    [-27, 9, 27, 9]
])

B = [1, 3, 3, -63]


print(resolver_sistema(A, B))