import math
an = float(input('Degite o ângulo que você de deseja: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem o seno de {:.2f}  ' .format(an, seno))
print('O ângulo de {} tem de cosseno {:.2f}  '  .format(an, cosseno))
print('O ângulo de {} tem de tangente {:.2f} ' .format(an, tangente))
