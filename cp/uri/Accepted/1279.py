""" __author__: Leynilson José "Snake" """
# Ano Bissexto | accepted

# Leitura dos dados
def cin():
    try:
        ano = int(input())
        return ano
    except EOFError:
        return

ano = cin()
while (True):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print("This is leap year.")

        if ano % 15 == 0:
            print("This is huluculu festival year.")

        if ano % 55 == 0:
            print("This is bulukulu festival year.")

    elif ano % 15 == 0:
        print("This is huluculu festival year.")

    else:
        print("This is an ordinary year.")

    ano = cin()
    if ano:
        print()
    else:
        break
