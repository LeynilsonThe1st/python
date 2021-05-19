""" __author__: Leynilson José "Snake" """
# Digitos | accepted

t = int(input())
while t > 0:
    t -= 1
    (n, m) = input().split()
    n = int(n)
    m = int(m)
    print(len(str(pow(n, m))))
