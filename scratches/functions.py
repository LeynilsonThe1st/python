def ola(nome):
    return f"Olá {nome.capitalize()}!"

def args(*nums):
    arr = []
    for n in nums:
        arr.append(n)

    return arr

def dicc(o, dic):
    for k, v in dic.items():
        print(o, f"{k}:{v}")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


out = ">>>\a"
dicionario = {'name': 'Leyn', 'age': 19}

# print('\n')
# print(out, ola("leynilson"))
# print(out, args("eu", "tu", 1, 20, 's', 'n'))
# dicc(out, dicionario)
# print(out, factorial(7))

nome = "meu   "
n = nome.split(" ", 2)[0]
print(n)
