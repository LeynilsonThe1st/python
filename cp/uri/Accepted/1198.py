""" __author__: Leynilson José "Snake" """
# O bravo guerreiro Hasmat accepted

# Leitura dos dados
def cin():
    try:
        global a, b
        (a, b) = input().split()
        a = int(a)
        b = int(b)
        return True
    except EOFError:
        return False

a = b = None
while cin():
    print(abs(a - b))
