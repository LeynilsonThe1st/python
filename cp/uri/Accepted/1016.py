""" __author__: Leynilson José "Snake" """
# Distancia | accepted

"""
x = x0 + v0t | d = xb - xa  onde d: distancia
xa = 0 + 60t | 30t = d
xb = 0 + 90t | t = d/30
"""

distancia = int(input())
t = distancia * 2  # ou t = (distancia/30) * 60
print(f"{t} minutos")
