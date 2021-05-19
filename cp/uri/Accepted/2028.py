""" __author__: Leynilson José "Snake" """
# Sequencia de sequencia | accepted

def cin():
    try:
        global n
        n = int(input())
        return True
    except EOFError:
        return False

n = None
c = 1
while cin():
    seq = '0'
    l = 1
    for i in range(1, n+1):
        for j in range(i):
            seq += f" {str(i)}"
            l += 1
    print(f"Caso {c}: {l} {'numero' if n == 0 else 'numeros'}")
    print(seq, end="\n\n")
    c += 1
