""" __author__: Leynilson José "Snake" """
# combinador | accepted


def combine(x: list, y: list):
    z = []
    for i, j in zip(x, y):
        z.append(i + j)
    l1, l2 = len(x), len(y)
    if l1 > l2:
        z.append("".join(x[l2:]))
    elif l2 > l1:
        z.append("".join(y[l1:]))
    return "".join(z)


t = int(input())
while t > 0:
    t -= 1
    a, b = map(list, input().split())
    print(combine(a, b))
