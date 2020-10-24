from armario import Armario

d = [[[[[[[
    1, 2, 3.5, 4.3, True, False, 'a', 'b',
    [5, 'c'], (6, 'd'), {7, 8}, {'eu': 'tu'}
]]]]]], ['e', 'f']]
# dados = Armario(
#     1, 2, 3.5, 4.3,
#     True, False, 'a', 'b',
#     [5, 'c'], (6, 'd'), {7, 8}, {'eu': 'tu'},
#     None, desfazer=True)
# dados.push([12, 'g'])
# dados.info()

dados2 = Armario(d, desfazer=True)
# dados2.info()
# dados2.push("leynilson", "Pascoal", "Trigo", "Jose")
# dados2.info()
# dados2.push([100, 200, 300], ['v', 'g'])
# dados2.info()
dados = Armario(d, desfazer=True)
dados.push(dados2)
dados.info()
