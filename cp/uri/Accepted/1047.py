""" __author__: Leynilson José "Snake" """
# Tempo de jogo com minito | accepted

def toSeg(hora, minunto):
    return (hora * 3600, minunto * 60)

def toMin(seg):
    return seg * 60

def toHora(seg):
    hora = seg // 3600
    return (hora, (seg % 3600) // 60)

dados = input().split()
(h0, m0, h, m) = map(lambda x: int(x), dados)

t0 = toSeg(h0, m0)
t = toSeg(h, m)
t0Total = sum(t0)
tTotal = sum(t)

if t0Total == tTotal:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif tTotal > t0Total:
    horas, minutos = toHora(tTotal - t0Total)
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
else:
    dif = abs(t0Total - tTotal)
    x = sum(toSeg(24, 0)) - dif
    horas, minutos = toHora(x)
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

