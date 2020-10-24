"""
7.Dadas as matrizes A, B e C:
Calcule:
    a) det(A)
    b) det(B)
    c) det(C)
    d) det(A+B)
    e) det(A-B)
    f) det(2A-3B+4C)
    g) det(BC)
    h) det(ACT)
    i) det((CB)A)
    j) det(C(BA))
    k) det(B(CA))
res:
 7.
    a) 22
    b) -9
    c) 0
    d) 240
    e)456
    f)1655
    g)0
    h)0
    i)0
    j)0
    k)0
"""
from matriz import Matriz, det

A = Matriz([
    [3, 4, 1],
    [-5, -2, -9],
    [7, 8, 6]
])

B = Matriz([
    [4, -1, 3],
    [3, 0, 1],
    [7, 2, -4]
])

C = Matriz([
    [2, 6, 8],
    [3, 9, 12],
    [-1, -2, -3]
])

print(f"\n a) det(A) = {det(A)}")
# print(f"\n b) det(B) = {det(B)}")
# print(f"\n c) det(C) = {det(C)}")
# print(f"\n d) det(A+B) = {det(A + B)}")
# print(f"\n e) det(A-B) = {det(A - B)}")
# print(f"\n f) det(2A-3B+4C) = {det((2*A)-(3*B)+(4*C))}")
# print(f"\n g) det(BC) = {det(B * C)}")
# print(f"\n h) det(AC^T) = {det(A * (C ** 1))}")
# print(f"\n i) det((CB)A) = {det((C * B) * A)}")
# print(f"\n j) det(C(BA)) = {det(C * (B * A))}")
# print(f"\n k) det(B(CA)) = {det(B * (C * A))}")
