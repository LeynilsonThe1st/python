import colors

sair = False
inserir_numeros = True
while not sair:
    if inserir_numeros:
        num1 = int(input('Degite o primeiro numero: '))
        num2 = int(input('Degite o segundo numero: '))
        inserir_numeros = False
    else:
        print(colors.yellow, 'O que deseja fazer?\n Seleciona:')
        print(colors.blue, '\n[1] Para Somar'
                           '\n[2] Para Subtrair'
                           '\n[3] Para Multiplicar'
                           '\n[4] Para Dividir'
                           '\n[5] Para Ver o Maior'
                           '\n[6] Para Inserir novos Numeros'
                           '\n[0] Para Sair'
                           '\n')
        operacao = int(input('== '))
        if operacao == 1:
            resultado = num1 + num2
            print(colors.green, '\n{} + {} = {}'.format(num1, num2, resultado))
        elif operacao == 2:
            resultado = num1 - num2
            print(colors.green, '\n{} - {} = {}'.format(num1, num2, resultado))
        elif operacao == 3:
            resultado = num1 * num2
            print(colors.green, '\n{} X {} = {}'.format(num1, num2, resultado))
        elif operacao == 4:
            if num1 == 0 or num2 == 0:
                print(colors.red, '\nErro, Não pode dividir por 0')
            else:
                resultado = num1 / num2
                print(colors.green, '\n{} / {} = {}'.format(num1, num2, resultado))
        elif operacao == 5:
            if num1 > num2:
                resultado = num1
                print(colors.green, '\n{} > {}'.format(num1, num2))
            elif num1 < num2:
                resultado = num2
                print(colors.green, '\n{} > {}'.format(num2, num1))
            else:
                print(colors.green, '\n{} == {}'.format(num1, num2))
        elif operacao == 6:
            inserir_numeros = True
        elif operacao == 0:
            sair = True
        else:
            print(colors.red, '\nErro! degite uma das opções acima citadas')

print(colors.red, '\nFIM')
