restart = False
num1 = int(input("degite o primeiro numero: "))
num2 = int(input("degite o segundo numero:  "))
if num1 < num2:
    for i in range(num2 - num1 - 1):
        i = i + 1
        print(num1 + i)
elif num1 > num2:
    for i in range(num1 - num2 - 1):
        i = i + 1
        print(num1 - i)
else:
    print(num1)
