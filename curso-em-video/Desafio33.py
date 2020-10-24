num1 = int(input('Degite o primeiro numero '))
num2 = int(input('Degite o segundo numero '))
num3 = int(input('Degite o terceiro numero '))
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3

maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3

print('Menor = {}'.format(menor))
print('Maior = {}'.format(maior))

