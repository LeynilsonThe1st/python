from matriz import *

A = Matriz(None, 3, 3)
E = Matriz(None, 2, 2, lambda i, j: i + j + i)



# print(percorrer(E.mat, lambda el, i, j: j + i))


# print(bonificar(construir(1, 5, lambda i, j: i + j if i > j else j - i)))
# print(det(E))
print(A)
print(bonificar(cofactores(A, 1, 2)))
