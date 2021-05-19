""" __author__: Leynilson José "Snake" """
# Uri Online Judge | 1213 limit time exceded

def findOne(n):
    return (n * 10) + 1

with open('entrada.txt') as entradas:
    for dado in entradas:
        a = int(dado)
        num = 1
        while num % a != 0:
            num = findOne(num)
        print(len(str(num)), file=open('saida.txt', 'a'))
