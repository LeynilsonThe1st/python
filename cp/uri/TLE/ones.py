""" __author__: Leynilson José "Snake" """
# Uri Online Judge | 1213 limit time exceded
from time import sleep

def findOne(n):
    return (n * 10) + 1

# Leitura dos dados
def cin():
    try:
        global y
        y = int(input())
        return True
    except EOFError:
        return False

y = None
while cin():
    num = 1
    while num % y != 0:
        num = findOne(num)
    print(len(str(num)), num)
