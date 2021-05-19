""" __author__: Leynilson José "Snake" """
# Area do triangulo* | wrong answer

a, b, c = map(float, input().split())

if a >= b + c:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")
else:
    per = a + b + c
    print(f"Perimetro = {per:.1f}")
