""" __author__: Leynilson José "Snake" """
# Canetas | wrong answer

def cin():
    try:
        global dados
        dados = list(map(int, input().split()))
        return True
    except EOFError:
        return False

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

dados = None
while cin():
    azuis, pretas, teams = dados
    if mdc(azuis, teams) == mdc(pretas, teams):
        print("sim")
    else:
        print("nao")

