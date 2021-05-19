""" __author__: Leynilson José "Snake" """
# Dividindo circulos | accepted
from math import pow as p

n = int(input())

print(f"{(n/24) * (p(n, 3) - (6 * p(n, 2)) + (23 * n) - 18) + 1:.0f}")
