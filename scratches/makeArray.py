def makeArray(size, type):
    if type == 'int':
        from random import randint as rd
        i = 0
        array = []
        while i <= size:
            array.append(rd(0, 100))
            i += 1
        return array
    elif type == 'float':
        from random import uniform as rd
        from random import randrange as rg
        i = 0
        array = []
        while i <= size:
            array.append(round(rd(0, 10), rg(3)))
            i += 1
        return array
    elif type == 'str':
        from random import randint as rd
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']
        def strMaker(ltrs, times):
            string: str = ""
            for i in range(times):
                string += ltrs[rd(0, len(ltrs) - 1)]
            return string
        i = 0
        array = []
        while i <= size:
            string = strMaker(letras, rd(0, 10))
            array.append(string)
            i += 1
        return array
    else:
        return 'defina o tipo de array'


print(makeArray(5, "int"))
print(makeArray(5, "float"))
print(makeArray(5, "str"))
# print(makeArray(5, 'bool'))
