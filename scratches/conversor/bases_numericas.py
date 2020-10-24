"""Um Simples conversor de bases numericas"""


#-------------------------------------------------------------------
#       Em Uso
#-------------------------------------------------------------------


def para_decimal(num=list, base=int) -> int:
    """
    Converte um numero binario ou octal em decimal.

    `Args`:
        num: O numero a ser convertido.
        base: A base que se deseja converter.

    `Returns`:
        Um numero decimal.
    """
    res = 0
    exp = len(num) - 1
    for i in num:
        # print(f"{i}*2^{exp} = {i*(2**exp)}")
        res += (i * (base ** exp))
        exp -= 1
    return res


def decimal_para(dec, base=int) -> str:
    """
    Converte um numero decimal em binario ou octal.

    `Args`:
        dec: O numero a ser convertido
        base: A base que se deseja converter

    `Returns`:
        Um numero decimal numa string.
    """
    octal = []
    while dec != 0:
        octal.insert(0, str(dec % base))
        dec //= base
    return "".join(octal)


def lista_int(lista=list) -> list:
    """
    Transforma uma lista com elementos `str` para `int`.

    `Args`:
        lista: A lista a ser transformada

    `Returns`:
        Uma lista com elementos do tipo `int`.
    """
    return [int(x) for x in lista]


def converter(num, base_inicial=int, base_final=int) -> int:
    """
    Converte um numero em uma outra base numerica.

    `Args`:
        num: O numero a ser convertido.
        base_inicial: A base em que o numero se encontra.
        base_final: A base que se deseja converter.

    `Returns`:
        Um numero decimal numa string.
    """

    if base_inicial and base_final in (2, 8, 10) \
        and base_inicial != base_final and str(num).isnumeric():

        if base_inicial in (2, 8):
            if base_final == 8 and verificar_binario(str(num)):
                # 1 binario   --> octal
                return decimal_para(para_decimal(lista_int(str(num)), base_inicial), base_final)

            if base_final == 2 and verificar_octal(num):
                # 1 octal     --> binario
                return decimal_para(para_decimal(lista_int(str(num)), base_inicial), base_final)

            if base_inicial == 2 and base_final == 10 and verificar_binario(num):
                # 2 binario   --> decimal
                return para_decimal(lista_int(num), base_inicial)

            if base_inicial == 8 and base_final == 10 and verificar_octal(num):
                # 2 octal     --> decimal
                return para_decimal(lista_int(num), base_inicial)

        if base_inicial == 10:
            if base_final in (2, 8):
                # 1 decimal   --> binario
                # 2 decimal   --> octal
                return decimal_para(num, base_final)

    return False

#-------------------------------------------------------------------
#       Verificar bases
#-------------------------------------------------------------------


def verificar_binario(binario):
    """
    verifica se o numero é binario

    `Args`:
        binario: O numero a vereficar

    `Returns`:
        `bool` => True ou False
    """
    for i in binario:
        if i not in "10" or i == '':
            return False
    return True

def verificar_octal(octal):
    """
    verifica se o numero é octal

    `Args`:
        octal: O numero a vereficar

    `Returns`:
        `bool` => True ou False
    """
    return str(octal).isnumeric() and not ('8' in str(octal) or '9' in str(octal))


# def converter(num, base):
#     if base == 2 or base == 8:
#         # decimal para binario ou octal
#         lista = []
#         while num != 0:
#             lista.insert(0, str(num % base))
#             num //= base
#         return "".join(lista)
#     elif base == 10:
#         # binario para decimal
#         res = 0
#         exp = len(num) - 1
#         for i in num:
#             res += (i * (2 ** exp))
#             exp -= 1
#         return res
#     else:
#         return False

# def dec_para_binario(num):
#     binario = []
#     while num > 0:
#         binario.insert(0, str(num % 2))
#         num //= 2
#     return "".join(binario)

# def dec_para_octal(dec):
#     octal = []
#     while dec != 0:
#         octal.insert(0, str(dec % 8))
#         dec //= 8
#     return "".join(octal)


# def bin_para_decimal(num=list, i=0):
#     if len(num) == 0:
#         return 0
#     # print(f"{num[0]}*2^{len(num) - 1} = {num[0] * (2 ** (len(num) - 1))}")
#     return num[0] * (2 ** (len(num) - 1)) + bin_para_decimal(num[i + 1 :])

#-------------------------------------------------------------------
#       Malucas e perigosas funcoes recursivas
#-------------------------------------------------------------------

# def para_bin(num, binr=[]):
#     if num == 1:
#         binr.insert(0, str(num % 2))
#         return "".join(binr)
#     binr.insert(0, str(num % 2))
#     return para_bin(num // 2)

# def to_octal(dec, octal=[]):
#     if dec == 0:
#         octal.insert(0, str(dec % 8))
#         return "".join(octal)
#     octal.insert(0, str(dec % 8))
#     return to_octal(dec // 8)
