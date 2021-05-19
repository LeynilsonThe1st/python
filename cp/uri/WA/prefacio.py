#wrong answer

# Leitura dos dados
def cin() -> bool:
    try:
        global a, b
        (a, b) = input().split()
        a = int(a) if a[0] != '-' else int(a[1:]) * -1
        b = int(b) if b[0] != '-' else int(b[1:]) * -1
        return True
    except EOFError:
        return False

a = b = None
if cin():
    print(a // b, a % b)
