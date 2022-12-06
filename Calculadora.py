print('\n######## Calculadora########')
operador = input('\n Escolha Uma Operação (+)(-)(*)(/): ')
num_1 = int(input('\n Digite um Número: '))
num_2 = int(input('\n Digite outro Número: '))
resultado = 0;
if operador == '+':
    resultado = num_1 + num_2

elif operador == '-':
    resultado = num_1 - num_2

elif operador == '*':
    resultado = num_1 * num_2

elif operador == '/':
    resultado = num_1 / num_2

else:
    print('\n Operador Inválido!')

print(f'\n {num_1} {operador} {num_2} = {resultado}')