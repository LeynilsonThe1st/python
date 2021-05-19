""" __author__: Leynilson José "Snake" """
# Decifrando a carta Criptografica | presentation error


def cin():
    try:
        global c, n
        c, n = list(map(int, input().split()))
        return True
    except EOFError:
        return False


def decode(a: str, b: str, s: list):
    aux = s[:]
    s = [x.lower() for x in s]
    for i in range(len(s)):
        minusc = aux[i].islower() or not aux[i].isalpha()
        if s[i] in a:
            posi = a.index(s[i])
            s[i] = b[posi] if minusc else b[posi].upper()
        elif s[i] in b:
            posi = b.index(s[i])
            s[i] = a[posi] if minusc else a[posi].upper()
    return "".join(s)


c = n = None

while cin():
    a = input().lower()
    b = input().lower()
    frases = [''] * n
    for i in range(n):
        frases[i] = input()

    for frase in frases:
        print(decode(a, b, list(frase)))
    print()
