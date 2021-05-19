""" __author__: Leynilson José "Snake" """
# Resto da divisao | accepted

x = int(input())
y = int(input())

(x, y) = (y, x) if x > y else (x, y)

for i in range(x+1, y):
    resto = i % 5
    if resto == 2 or resto == 3:
        print(i)
