from colors import BOLD, CLEAR, GREEN, RED, UNDERLINE, YELLOW, WHITE, CYAN
from bases_numericas import converter, verificar_binario, verificar_octal


def show_intro():
    print(f"\n\t{BOLD}{WHITE}+------------------------------------------------------------+" +
          f"\n\t|  O que deseja converter? prima [D ou B]                    |" +
          "\n\t+------------------------------------------------------------+" +
          "\n\t|  (A) - Decimal para Binário  |  (B) - Binário para Decimal |" +
          "\n\t|  (C) - Octal para Binário    |  (D) - Binário para Octal   |" +
          "\n\t|  (E) - Decimal para Octal    |  (F) - Octal para Decimal   |" +
          "\n\t|  (Qualquer outra tecla) - Sair                             |"+
          "\n\t+------------------------------------------------------------+")

def show_converter(base=str, para=str):
    print(f"\n\t{YELLOW}+------------------------------------------------------------+" +
          f"\n\t|  {base} para {para}                                        |" +
          "\n\t+------------------------------------------------------------+" +
          f"\n\n\t   Insira um numero {base}")

def show_repetir():
    print(f"\n\t{BOLD}{YELLOW}+------------------------------------------------------------+" +
          f"\n\t|  Converter de novo?                                        |" +
          "\n\t|  (S) - Sim | (Qualquer outra tecla) - Não                  |" +
          "\n\t+------------------------------------------------------------+")

def show_decimal(base=str, inicial=int, final=int):
    show_converter(base, "decimal")
    while True:
        numero = str(input("\t   == ")).strip()
        if inicial == 8:
            if verificar_octal(numero) is False:
                print(f"\t{RED}   == Insira um número Octal válido{YELLOW}")
                continue
            else:
                break
        else:
            if verificar_binario(numero) is False:
                print(f"\t{RED}   == Insira um número binario válido{YELLOW}")
                continue
            else:
                break
    print(f"\n\t   {UNDERLINE}Número {base} = {numero}{CLEAR}{BOLD}{YELLOW}" +
          f"\n\t   {UNDERLINE}Número Decimal = {converter(numero, inicial, final)}{CLEAR}\n")
    show_repetir()

def show_binario(base=str, inicial=int, final=int):
    show_converter(base, "Binário")
    numero = int(input("\t== "))
    print(f"\n\t{UNDERLINE}Número {base} = {numero}")
    print(f"\tNúmero Binário = {converter(numero, inicial, final)}{CLEAR}{BOLD}")
    show_repetir()

def show_octal(base=str, inicial=int, final=int):
    show_converter(base, "Octal")
    numero = int(input("\t== "))
    print(f"\n\t{UNDERLINE}Número {base} = {numero}")
    print(f"\tNúmero OCtal = {converter(numero, inicial, final)}{CLEAR}{BOLD}")
    show_repetir()

def run():
    """Executa o Conversor"""

    while True:
        show_intro()
        cvt = str(input("\t== ")).strip().upper()
        if cvt in 'ABCDEF' and cvt != '':
            if cvt == "A":
                while True:
                    show_binario('Decimal', 10, 2)
                    continuar = str(input("\t== ")).upper()
                    if continuar != "S":
                        break
            elif cvt == "B":
                while True:
                    show_decimal('Binário', 2, 10)
                    continuar = str(input("\t   == ")).upper()
                    if continuar != "S":
                        break
            elif cvt == "C":
                while True:
                    show_binario("Octal", 8, 2)
                    continuar = str(input("\t== ")).upper()
                    if continuar != "S":
                        break
            elif cvt == "D":
                while True:
                    show_octal("Binário", 2, 8)
                    continuar = str(input("\t== ")).upper()
                    if continuar != "S":
                        break
            elif cvt == "E":
                while True:
                    show_octal("Decimal", 10, 8)
                    continuar = str(input("\t== ")).upper()
                    if continuar != "S":
                        break
            elif cvt == "F":
                while True:
                    show_decimal("Octal", 8, 10)
                    continuar = str(input("\t== ")).upper()
                    if continuar != "S":
                        break
            else:
                break
        else:
            print(f"\n\t{RED}-----------------\n\tMade by Leynilson")
            print(f"\t              Fim\n\t-----------------")
            break


run()
