def factorial(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f


x = int(input("insira um valor: "))
s = 1
y = 0
while y < x:
    y += 1
    f = factorial(y)
    s += (1/f)

print(s)

