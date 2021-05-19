""" __author__: Leynilson José "Snake" """
# Corrida de lesmas | 


def cin():
    try:
        global n
        n = int(input())
        return True
    except EOFError:
        return False
