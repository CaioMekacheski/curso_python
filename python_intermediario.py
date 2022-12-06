"""
# 29-> Funções - def
# 30-> Expressões Lambda - funções anônimas
# 31-> Tuplas
# 32-> Dicionários
"""

# 29-> Funções - def
"""
texto = 'Ola Mundo'
texto2 = 'Bom Dia'

def funcao(texto):
    print(texto)


funcao(texto)
funcao(texto2)

texto = 'Ola Mundo'
texto2 = 'Bom Dia'
usuario = 'Caio'


def saudacao(msg='Ola', nome='usuário'):
    print(msg, nome)


saudacao(texto2, usuario)
saudacao(nome=usuario)

def funcao(var):
    return var


variavel = funcao('')

if variavel:
    print(variavel)
else:
    print('Nulo')
    
def divisao(n1, n2):

    if n2 > 0:
        return n1 / n2


divide = divisao(8, 4)

if divide:
    print(divide)
else:
    print('O divisor deve ser maior que 0.')
    
def dumb():
    # return 1
    # return 1.1
    # return [1, 2, 3, 4, 5]
    return 'Caio', 'Cesar'


var = dumb()
print(var, type(var))
print(var[0], type(var))
print(var[1], type(var))


def saudacao(msg, nome):
    texto = msg + ' ' + nome
    return texto


msg = 'Bom dia'
nome = 'Caio'

print(saudacao(msg, nome))


def soma(n1, n2, n3):
    return int(n1) + int(n2) + int(n3)


print(soma(2, 3, 4))


def reajustar(valor, percentual):
    novo_valor = valor + ((valor / 100) * percentual)
    return novo_valor


print(reajustar(100, 25))


def fizzbuzz(num):
    if num % 2 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    if num % 2 == 0:
        return 'buzz'
    if num % 5 == 0:
        return 'fizz'
    return num


valor = int(input('Valor: '))
print(fizzbuzz(valor))



"""

"""
def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6


var = func(1, 2, 3, 4, 5, nome='Caio', a6='6')
print(var)
print(var[0], var[1])
"""


"""
    def func2(*args, **kwargs):
    print(args)
    print(*args, sep='#')
    print(args[0])
    print(args[-1])
    print(len(args))
    args = list(args)
    args[0] = 20
    print(args)
    print(*args)

    print(kwargs)
    print(*kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])

    idade = kwargs.get('idade')

    if idade:
        print(idade)

    for i in args:
        print(i, end='!!')


print()
lista = ['a', 'b', 'c', 'd', 'e']
lista2 = [1, 2, 3, 4, 5]

print(*lista, sep='-')
print()

func2(*lista, *lista2, nome='Caio', sobrenome='Mekacheski', idade='35')
"""


"""
variavel = 'Valor'


def func3():
    print(variavel)


def func4(arg=None):
    # global variavel
    arg = 'Outro Valor'
    return arg


def func5():
    var1 = 'Caio Cesar'
    return  var1


def func6(arg):
    print(arg)


var = func5()
func6(var)

func3()
var = func4(arg=variavel)
print(var)
print(variavel)
"""


"""def funcao1(arg):
    return arg()


def funcao2():
    var = 'Valor'
    return var


def funcao3(arg, **kwargs):
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    idade = kwargs.get('idade')

    if nome and sobrenome and idade:
        arg1 = funcao4(nome, sobrenome)
        arg2 = funcao5(idade)
        return arg, arg1, arg2

    return arg


def funcao4(arg1, arg2):
    return arg1 + ' ' + arg2


def funcao5(arg):
    return 'Idade: ' + arg


def funcao7(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


print(funcao1(funcao2))
print(funcao2())
var = funcao1(funcao2)
print(*funcao3(var, nome='Caio', sobrenome='Mekacheski', idade='35'))
print(funcao7(funcao4, 'Caio', 'Cesar'))
print(funcao7(funcao5, '35'))"""

# 30-> Expressões Lambda — funções anônimas

"""
a = lambda x, y: x * y
print(a(2, 2))

lista = \
    [
        ['B', 13],
        ['E', 6],
        ['A', 7],
        ['D', 50],
        ['C', 8]
    ]


def func(item):
    return item[1]


# lista.sort(key=func, reverse=True)
# lista.sort(key=lambda item: item[1], reverse=True)
print(lista)
print(sorted(lista, key=lambda i: i[0]))
"""

# 31-> Tuplas
"""
tupla0 = ()
tupla1 = (1, 2, 3, 'a', 'Caio')
tupla2 = 'Mekacheski',
tupla3 = tupla1 + tupla2
n1, n2, n3, *_, n = tupla3
tupla3 = list(tupla3)
tupla3[1] = 3000
tupla3 = tuple(tupla3)
print(tupla1, type(tupla1))
# print(tupla1[4], type(tupla1[4]))
# print(tupla1[2:])
print(tupla2)
print(tupla3)
print(n1)
print(n2)
print(n3)
print(*_)
print(n)
for i in tupla1:
    print(i, end=' ')
"""

# 32-> Dicionários
"""
"""
# Parte 1
print('Parte 1:')
d1 = {'chave1': 'valor da chave1'} # Criação de dicionário de modo direto
d2 = dict(chave01='Valor01', chave02='Valor02') # Criação de dicionário usando a função dict
d3 = {1: 10, 2: 20, 3: 30} # Dicionário de valores inteiros
d4 = {'str': 10, 123: 'Valor', (1, 2, 3, 4): 'Tupla'} # Dicionário com vários tipos de dados
print(d1)
print(d2)
print(d3)
print(d4)
print('\n')

# Parte 2
print('Parte2')
d1['chave2'] = 'valor da chave2' # Atribuindo valor a uma chave do dicionário
d2['chave03'] = 'Valor03'
print(d1) # Imprimindo o dicionário inteiro
print(d2)
print(d1['chave1']) # Imprimindo uma chave do dicionário
print(d2['chave02'])
print(d4[(1, 2, 3, 4)])
print('\n')

# Parte 3
print('Parte3')
chave = input('Insira uma chave: ') # Recebe a chave do usuário

if chave not in d4: # Se a chave não existir, cria uma chave
    print(f'A chave {chave} não existe')
    d4[chave] = 'Nova Chave'
    print(f'Chave {chave} criada')
    print(d4)
else: # Senão, imprime o valor da chave digitada
    print(f'O valor da chave {chave} é {d4[chave]}')

if d1.get(chave) is None: # A mesma coisa do anterior, mas utilizando a função get
    print(f'A chave {chave} não existe')
    d1[chave] = 'Nova Chave'
    print(f'Chave {chave} criada')
    print(d1)
else:
    print(f'O valor da chave {chave} é {d1[chave]}')
print('\n')

# Parte 4
print('Parte 4')
d4['str'] = 'String' # Muda o valor da chave selecionada
print(d4)

d1.update({'chave2': 500}) # Mesmo caso usando a função update
print(d1)
print('\n')

# Parte 5
print('Parte 5')
print(d4)
del d4[chave] # Deleta uma chave
print(d4)
print('\n')

# Parte 6
print('Parte 6')
print('str' in d4)
print('String' in d4.values())
print(d4.values())
print(len(d4))
print('\n')

# Parte 7
print('Parte 7')
for k in d4: # Imprime as chaves
    print(k)
for v in d4.values(): # Imprime os valores
    print(v)
for i in d4.items(): # Imprime as chaves e os valores
    print(i)
for j in d4.items(): # Imprime os valores sem parenteses e sem aspas
    print(j[0], j[1])
for l, m in d4.items(): # Imprime os valores sem parenteses e sem aspas com as chaves separadas
    print(l, m)         # dos valores
print('\n')

# Parte 8
print('Parte 8')
# Dicionários de dicionários
clientes =\
    {
        'Cliente 01': # O valor da chave é outro dicionário
            {
                'Nome': 'Caio',
                'Sobrenome': 'Mekacheski'
            },
        'Cliente 02':
            {
                'Nome': 'Letícia',
                'Sobrenome': 'Arias'
            }
    }

for cliente_k, cliente_v in clientes.items(): # Exibe as chaves Cliente 01 e Cliente 02 em clientes
    print(f'Exibindo {cliente_k}')
    for dados_k, dados_v in cliente_v.items(): # Para cada chave em clientes, exibe o conteúdo
        print(f'\t {dados_k} = {dados_v}')     # correspondente
print('\n')
print('Fim.')

# Parte 9
print('Parte 9')
import copy
d5 = {1: 'a', 2: 'b', 3: 'c', 4: ['Caio', 'Cesar']}
v = d5 # Atribuir um dicionário a uma variável, não cria uma variável
print('\n')
print(d5)
print(v)
print('\n')
v[1] = 'Caio' # Qualquer modificação feita em v, tabém influenciará d5
print(d5)
print(v)
print('\n')
v2 = d5.copy() # Para evitar isso, ao atribuir um dicionário a uma variável, use a função copy
v2[2] = 'Cesar'
v2[4][1] = 'Mekacheski'
print(v2[4][0])
print(d5)
print(v2) # Ainda assim, no caso de uma chave que recebe como valor uma lista,
print('\n') # tanto a cópia como o dicionário original terá os seus valores alterados
v3 = copy.deepcopy(d5) # Para resolver essa situação, use copy.deepcopy
v3[4][1] = 'Araujo'
print(d5)
print(v3)
print('\n')
# continuar aula 62 (30:26)
"""
"""

