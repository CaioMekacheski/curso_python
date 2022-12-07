# Algoritmo para calcular a fatorial de um número (atualizado 07/12/2022)

n = 7
i = n-1
# Enquanto i maior ou igual a 1, imprime o valor atual de n 'X' o valor de i (n-1).
# calcula o novo valor de n (n = n * i) e subtrai 1 de i.
while i >= 1:
    print(n, 'x', i)
    n *= i
    i -= 1

# Imprime o valor total de n
print(n)

# Converte n em uma ‘string’, armazena o seu tamanho em qt e imprime o seu valor na tela
n2 = str(n)
qt = len(n2)
print(qt)

# Armazena o valor convertido em ‘string’ numa lista e imprime a lista na tela
lista = []

for i in enumerate(n2):
    lista.append(i)

print(lista)


# Output
# 7 x 6
# 42 x 5
# 210 x 4
# 840 x 3
# 2520 x 2
# 5040 x 1
# 5040
# 4
# [(0, '5'), (1, '0'), (2, '4'), (3, '0')]
