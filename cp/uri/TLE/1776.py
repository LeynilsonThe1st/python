""" __author__: Leynilson José "Snake" """
# Baile de formatura | time limit exceded
from math import sqrt

t = int(input())
c = 1
while t > 0:
    t -= 1
    n = int(input())
    i = n
    while not sqrt(n).is_integer():
        n += i
    print(f"Caso {c}: {n}")
    c += 1

