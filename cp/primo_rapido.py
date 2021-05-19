""" __author__: Leynilson José "Snake" """
# Uri Online Judge | 1221 acepted
from time import sleep

def isPrimo(n):
    sieve = [0] * (n+1)
    for x in range(2, (n+1)):
        if sieve[x]: continue
        for y in range(2*x, (n+1), x):
            sieve[y] = x 
    return sieve[n] == 0

def isPrimoRapido(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    
    if isPrimoRapido(n):
        print("Prime")
    else:
        print("Not Prime")