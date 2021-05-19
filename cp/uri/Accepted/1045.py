""" __author__: Leynilson José "Snake" """
# tipo de trinagulo | accepted

# Leitura dos dados
def cin():
    dados = input().split()
    dados = list(map(float, dados))
    dados.sort(reverse=True)
    return dados

a, b, c = cin()
a2 , b2, c2 = pow(a, 2), pow(b, 2), pow(c, 2)

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a2 == b2 + c2:
        print("TRIANGULO RETANGULO")
    elif a2 > b2 + c2:
        print("TRIANGULO OBTUSANGULO")
    elif a2 < b2 + c2:
        print("TRIANGULO ACUTANGULO")

    if  a == b and b == c:
        print("TRIANGULO EQUILATERO")
    elif  a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")

