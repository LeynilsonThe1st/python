""" __author__: Leynilson José "Snake" """
# De dentro para fora | accepted

t = int(input())
while t > 0:
    t -= 1
    string = input()
    size = len(string)
    s2, s1 = string[:size//2 - 1:-1], string[size//2 - 1::-1]

    print(s1 + s2)
