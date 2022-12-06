# Algoritmo para calcular a fatorial de um número

n = 7
i = n-1

while i >= 1:
    print(n, 'x', i)
    n *= i
    i -= 1

print(n)

#OUTPUT

#7 x 6
#42 x 5
#210 x 4
#840 x 3
#2520 x 2
#5040 x 1
#5040
