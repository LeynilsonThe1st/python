from time import sleep
def isPrimo(n):
    sieve = [0] * (n+1)
    for x in range(2, (n+1)):
        if sieve[x]: continue
        for y in range(2*x, (n+1), x):
            sieve[y] = x 
    return sieve[n] == 0


i = 2
c = 0
while True:
    if (isPrimo(i)):
        print(i, end=" ")
        c += 1
        # sleep(0.5)
    if c == 20:
        print()
        c = 0
    i += 1