from matriz import *

# C = Matriz([
#     [2, 6, 8],
#     [3, 9, 12],
#     [-1, -2, -3]
# ])

# print(C)
# print(det(C))
# print(bonificar(mat_cofactores(C)))
# print(bonificar(adjunta(C)))
# print(C**-1)
# print(det(C**-1))


A = Matriz([
    [1, 0, 2],
    [-3, 4, 6],
    [-1, -2, 3]
])

B = [6, 30, 8]

D = Matriz([
    [-1, 1],
    [1, 1]
])

E = [1, -1]

X = Matriz([
	[2, -2, 3],
	[-1, 1, -1],
	[1, 1, -1]
])

XB = [0, 4, 2]

# print(resolver_sistema(A, B))
# print(resolver_sistema(D, E))


# print(det(X))
# print(bonificar(mat_cofactores(X)))
# print(bonificar(adjunta(X)))
# print(bonificar(resolver_sistema(X, XB)))
# print((A**-1) * Matriz(B) * 1/det(A))

I = Matriz(mat_identidade(3))
# print(det(I))

M = Matriz([
	[1, 0, 0, 0],
	[2, 1, 0, 0],
	[3, 2, 1, 0,],
	[4, 3, 2, 1],
])

V = Matriz([
	[-1, -1, -1],
	[-3, -3, -4],
	[-3, -4, -3]
])

# print(det(V))
# print(V**-1)

# H = Matriz([
# 	[2, 1, 1, 1],
# 	[1, 2, 1, 1],
# 	[1, 1, 2, 1],
# 	[1, 1, 1, 2],
# ])

H = Matriz([
	[3, 1, 1],
	[0, 1, -1],
	[-1, 0, 1]
])
# K = [1, 2, 3, 4]
print(2*H)
print(bonificar(inversa(mat_identidade(3))))
# print(resolver_sistema(H, K))

G = Matriz([
	[1, 2],
	[1, 2]
])

print(G)
