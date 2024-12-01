operacao = str(input('Informe a operação (+, -, /, *): '))
num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))

if operacao == '+':
    soma = num1 + num2
    print("O resultado da soma entre {} e {} é igual a {}".format(num1, num2, soma))
elif operacao == '-':
    subtracao = num1 - num2
    print("O resultado da subtração entre {} e {} é igual a {}".format(num1, num2, subtracao))
elif operacao == '*':
    multiplicacao = num1 * num2
    print("O resultado da multiplicação entre {} e {} é igual a {}".format(num1, num2, multiplicacao))
elif operacao == '/':
    divisao = num1 / num2
    print("O resultado da soma de {} e {} é igual a {}".format(num1, num2, divisao))
else:
    print('Inicie novamente e informe o operador.')
