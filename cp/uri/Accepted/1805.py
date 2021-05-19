""" __author__: Leynilson José "Snake" """
# Soma natural | accepted

(a, b) = input().split()
a = int(a)
b = int(b)
n = abs(a - b) + 1
s = ((a + b) * n) / 2

print(int(s))
