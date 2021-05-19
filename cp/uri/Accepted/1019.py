""" __author__: Leynilson José "Snake" """
# Conversao de tempo | accepted

n = int(input())
h = n // 3600
resto = n % 3600
m = int(resto / 60)
s = resto % 60

print(f"{h}:{m}:{s}")
