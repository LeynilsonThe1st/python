""" __author__: Leynilson José "Snake" """
# Encaixa ou nao encaixa | accepted


def checkEncaixa(a: str, b: str):
    sa, sb = len(a), len(b)
    if sb > sa:
        return 'nao encaixa'
    elif sb < sa:
        return 'encaixa' if a[-sb:] == b else 'nao encaixa'
    return 'encaixa' if a == b else 'nao encaixa'


t = int(input())
while t > 0:
    t -= 1
    a, b = input().split()
    print(checkEncaixa(a, b))
