""" __author__: Leynilson José "Snake" """
# Coordenandas de um ponto | accepted

x, y = map(float, input().split())

if x == 0 and y == 0:   r = 'Origem' # (0, 0)
elif x == 0:            r = 'Eixo Y' # (0, 3)
elif y == 0:            r = 'Eixo X' # (3, 0)
elif x > 0 and y > 0:   r = 'Q1'     # (2, 2)
elif x < 0 and y > 0:   r = 'Q2'     # (-3, 2)
elif x < 0 and y < 0:   r = 'Q3'     # (-2, -2)
elif x > 0 and y < 0:   r = 'Q4'     # (3, -2)

print(r)
