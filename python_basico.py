"""
# 1 -> print(), comentários e strings
# 2 -> Tipos de Dados
# 3 -> Operadores Aritméticos
# 4 -> Variáveis
# 5 -> Formatação de strings
# 6 -> Desafio Prático
# 7 -> Input
# 8 -> If, Elif e Else
# 9 -> Operadores Relacionais
# 10-> Operadores Lógicos
# 11-> Função len
# 12-> Documentação e Funções built-in úteis
# 13-> Pass e ellipsis como place holders
# 14-> Exercícios
# 15-> Formatando Valores em Python
# 16-> Índices e Fatiamento de Strings
# 17-> Laço While
# 18-> While/Else Repetição com acumuladores
# 19-> Iterando strings com while
# 20-> For in
# 21-> Listas
# 22-> For/Else
# 23-> Split, Join e Enumerate
# 24-> Desempacotamento de listas
# 25-> Trocando o valor entre variáveis
# 26-> Operação ternária
# 27-> Expressão condicional com operador OR
"""

# 1 -> print(), comentários e strings
from random import randint

"""
        # Isso é um comentário
        print('Linha 1!') # Outro comentário
        print('Linha 2!')
        print('Linha 3!')
        print('Linha 4!')
        print('Linha 5!')
        print('Linha 6!')
        print('123456')
        print(123456)
        print('Caio', 'Mekacheski', end=' ')
        print('Caio', 'Mekacheski', sep='-')
        print('CPF:', end=' ')
        print('359', '376', '098', sep='.', end='-')
        print('32')
        print("Isso é uma 'String' (str)")
        print('Isso é uma "String" (str)')
        print(r"Isso é outra \"String\" (str)")
        print('Isso é outra \'String\' (str)')
        print(r"Mais uma \n string")
        print("Mais uma \n string")
"""

# 2-> Tipos de Dados
"""
        str -> String -> 'Texto' "Texto"
        int -> Inteiro -> 0 1, 67, -30
        float -> Real -> 0.0, 15.50, -1.5 
        bool -> Lógico -> true/false
    
    
        print("Luiz", type("Luiz"), bool("Luiz"))
        print(1986, type(1986))
        print(14.5, type(14.5))
        print(10 == 10, type(10 == 10))
        print('l' == 'L', type('l' == 'L'))
        print("10", type("10"), type(int("10")))
        print(10 + 10)
        print('10' + '10')
        print(10 + int('10'))
        print('10' + str(10))
        
        # Exercício Tipos de Dados
        # Nome: string
        print("Nome:", end=' ')
        print("Caio Mekacheski", type("Caio Mekacheski"))
        # Idade: int
        print("Idade:", end=' ')
        print(35, type(35))
        # Altura: float
        print("Altura:", end=' ')
        print(1.74, type(1.74))
        # É maior de 18: bool
        print("É maior de 18 anos?", end=' ')
        print(35 > 18, type(35 > 18))
"""

# 3 -> Operadores Aritméticos
"""
        + -> Adição
        - -> Subtração 
        * -> Multiplicação 
        / -> Divisão 
        //-> Divisão sem casa decimal 
        **-> Potenciação 
        % -> Modulo ou resto de divisão
        ()-> Altera precedência
        
        print("Adição                    (+): ", 10 + 10)
        print("Subtração                 (-): ", 10 - 10)
        print("Multiplicação             (*): ", 10 * 10)
        print("Divisão                   (/): ", 10 / 10)
        print("Divisão sem casa decimal (//): ", 10 // 10)
        print("Potenciação              (**): ", 10 ** 2)
        print("Módulo                    (%): ", 7 % 2)
        print(" 5 + 2  x  10 = ", 5 + 2 * 10)
        print("(5 + 2) x  10 = ", (5 + 2) * 10)
        print(2 + 5 * 3 ** 2 - (23.5 + 23.5))
        
        # Operações com Strings
        print("Concatenação (+): ", '10' + '10')
        print("Concatenação (+): ", 'Nome: '+'Caio'+' '+'Cesar'+' Idade: '+str(35)+' anos')
        print("Repetição    (*): ", 10 * 'A ')
        print("Repetição    (*): ", 10 * 'Caio ')
"""

# 4 -> Variáveis
"""
    nome = 'Caio'
    print(nome, type(nome))
    print(idade * altura)
    
    nome = 'Caio Mekacheski'
    idade = 35
    altura = 1.74
    peso = 92
    imc = peso/altura ** 2
    maior_idade = idade > 18
    
    print('Nome              : ' + nome)
    print('Idade             : ', idade)
    print('Altura            : ', altura)
    print('Peso              : ', peso)
    print('IMC               : ', imc)
    print('É maior de 18 anos? ', maior_idade)
    print('\n', nome, 'tem ', idade, ' anos de idade e seu IMC é de ', imc)
"""

# 5-> Formatação de strings
"""
    nome = 'Caio Mekacheski'
    idade = 35
    altura = 1.74
    peso = 92
    imc = peso/altura ** 2
    maior_idade = idade > 18
    
    print('\n', nome, 'tem', idade, 'anos de idade e seu IMC é de ', imc)
    print(f'\n {nome} tem {idade} anos de idade e seu IMC é de {imc:.2f}')
    print('\n {} tem {} anos de idade e seu IMC é de {:.2f}'.format(nome, idade, imc))
    print('\n {1} tem {0} anos de idade e seu IMC é de {2}'.format(idade, nome, imc))
    print('\n {n} tem {i} anos de idade e seu IMC é de {im}'.format(n=nome, i=idade, im=imc))
"""

# 6 -> Desafio Prático
"""
    ano_atual = 2022
nome = 'Caio Mekacheski'
idade = 35
ano_nascimento = ano_atual - idade
altura = 1.74
peso = 92
imc = peso/altura ** 2

print(f'\n Nome:{nome}'
      f'\n Idade:{idade}'
      f'\n Ano de Nascimento:{ano_nascimento}'
      f'\n Altura:{altura}'
      f'\n Peso:{peso}'
      f'\n IMC:{imc:.2f}')
"""

# 7 -> Input
"""
nome = input('\n Qual o seu nome? ')
idade = input('\n Qual a sua idade? ')
nascimento = 2022 - int(idade)

print(f'\n Nome             : {nome}            Tipo: {type(nome)}')
print(f'\n Idade            : {idade}           Tipo: {type(idade)}')
print(f'\n Ano de Nascimento: {nascimento}      Tipo: {type(nascimento)}')

print('***Calculadora***')
num_1 = int(input('Digite um valor   : '))
num_2 = int(input('Digite outro valor: '))
soma = num_1 + num_2
print(f'\n {num_1} + {num_2} = {soma}')
"""

# 8 -> If, Elif e Else
"""
if True:
    print('Verdadeiro')

print('Falso')

if True:
    print('Verdadeiro.')
else:
    print('Falso.')
    
if False:
    print('Verdadeiro.')
elif True:
    print('Verdadeiro de novo.')
else:
    print('Falso.')
"""

# 9 -> Operadores Relacionais
"""
== < > <= >= !=
print(2 == 2)
print(2 == 1)

num_1 = 2
num_2 = '2'
print(num_1, num_2)
print(num_1 == num_2)
num_1 = 2
num_2 = '2'
expressao = num_1 == num_2
print(expressao)

nome = input('Nome: ')
idade = int(input('Idade: '))
idade_limite = 18

if idade > idade_limite:
    print(f'Empréstimo Autorizado para o Cliente {nome}.')

else:
    print(f'Empréstimo Não Autorizado para o Cliente {nome}.')
    
idade_minima = 20
idade_maxima = 30

if idade >= idade_minima and idade <= idade_maxima:
    print(f'Empréstimo Autorizado para o Cliente {nome}.')

else:
    print(f'Empréstimo Não Autorizado para o Cliente {nome}.')

"""

# 10-> Operadores Lógicos
"""
and, or, not, in e not in 

a = 1
b = 3
c = 'Caio'

if  a == 2 and a < b:
    print('Todas as comparações são verdadeiras. True')

else:
    print('Uma das comparações é falsa. False')

if a != 2 or a < b:
    print('Uma das comparações é verdadeira. True')

else:
    print('Todas as comparações são falsas. False')

if  not a == 2:
    print('True')

else:
    print('False')

if 'C' in c:
    print(f'C está em {c}')

else:
    print(f'C não está em {c}')

if 'i' not in c:
    print('True')

else:
    print('False')
    
usuario = input('Usuário: ')
senha = input('Senha: ')

usuario_bd = 'Caio'
senha_bd = '123456'

if usuario == usuario_bd and senha == senha_bd:
    print(f'Bem vindo {usuario}, seu login foi realizado com sucesso.')

else:
    print('Usuário ou senha incorretos!')
"""

# 11-> Função len
"""
usuario = input('\n Usuario: ')
qtd_caracteres = len(usuario)

print('\n', usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('\n Digite no minimo 6 caracteres.')

else:
    print('\n Cadastro realizado com sucesso.')
    
nome = input('\n Nome: ')
sobre_nome = input(' Sobrenome: ')
usuario = nome + sobre_nome
qtd_char = len(usuario)
print(usuario, qtd_char)

mes_atual = 3
ano_atual = 2022
nome =           input(' Nome:      ')
sobre_nome =     input(' Sobrenome: ')
print('\n Data de Nascimento:')
dia_nascimento = input(' Dia:       ')
mes_nascimento = input(' Mês:       ')
ano_nascimento = input(' Ano:       ')
cpf =            input(' CPF:       ')
print('\n Endereço: ')
rua =            input(' Rua:       ')
numero =         input(' Numero:    ')
bairro =         input(' Bairro:    ')
cidade =         input(' Cidade:    ')
cep =            input(' CEP   :    ')
estado =         input(' Estado:    ')
pais =           input(' País  :    ')
telefone =       input(' Telefone:  ')
email =          input(' E-mail:    ')

cliente = nome + sobre_nome
idade =
"""

# 12-> Documentação e Funções built-in úteis
"""
import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False

def is_number(val):
    return is_int(val) or is_float(val)

num_01 = input('Digite um número: ')
num_02 = input('Digite outro número: ')

if is_float(num_01) and is_float(num_02):
    print(float(num_01) + float(num_02))
else:
    print('Entrada Inválida! Digite valores Númericos.')
"""

# 13-> Pass e ellipsis como place holders
"""
valor = False

if valor:
    pass
else:
    print('Tchau')

valor = False

if valor:
    ...
else:
    print('Tchau')

"""

# 14-> Exercícios
"""
#1
num = input('Digite um Número: ')

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(num, 'é par')
    else:
        print(num, 'é impar')
else:
    print('O valor digitado é inválido')

#2
horas = input('Horas: ')
minutos = input('Minutos: ')

if horas.isdigit() and minutos.isdigit():
    horas = int(horas)
    minutos = int(minutos)
    if horas >= 0 and horas < 12:
        print('Bom dia!')

    elif horas >=12 and horas < 18:
        print('Boa Tarde!')

    elif horas >=18 and horas < 24:
        print('Boa Noite!')

    else:
        print('Erro!')
else:
    print('Erro2!')

#3
nome = input('Nome: ')
qtd_char = len(nome)

if qtd_char <= 4:
    print('Nome curto.')

elif qtd_char >= 5 and qtd_char <= 6:
    print('Nome normal.')
    
else:
    print('Nome longo.')
"""

# 15-> Formatando Valores em Python
"""
:s - Strings
:d - Int
:f - Float

num1 = 3
num2 = 10
num3 = 1
num4 = 1155
nome = 'Caio Cesar'
sobrenome = 'Mekacheski'
divisao = num2 / num1

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

print(f'{num3:0>10}')
print(f'{num4:0^10}')
print(f'{num1:0<10}')
print(f'{num4:.2f}')
print(f'{num4:0>10.2f}')

print(f'{nome:s}')
print(f'{nome:#<50}')
print(f'{nome:#^50}')
print(f'{nome:#>50}')
print(f'{nome:*^30}{sobrenome:$^30}')

print(nome.ljust(20, '#'), sobrenome.ljust(20, '#'))
print(nome.center(20, '#'), sobrenome.center(20, '#'))
print(nome.rjust(20, '#'), sobrenome.rjust(20, '#'))
print(nome.lower(), sobrenome.lower())
print(nome.upper(), sobrenome.upper())
print(nome.capitalize(), sobrenome.capitalize())
print(nome.title(), sobrenome.title())
print(nome.casefold(), sobrenome.casefold())
print(nome.swapcase(), sobrenome.swapcase())
"""

# 16-> Índices e Fatiamento de Strings
"""
#        012345678
texto = 'Python S2'
#       -987654321
url = 'www.google.com.br/'
texto2 = texto[2:6]
texto3 = texto[:6]
texto4 = texto[2:]
texto5 = texto[-8:-2]
texto6 = texto[0::2]
print(texto[2])
print(url)
print(url[:-1])
print(texto2)
print(texto3)
print(texto4)
print(texto5)
print(texto6)
print(len(texto))

for letra in texto:
    print(letra)
"""

# 17-> Laço While
"""
while False:
    nome = input('Qual o seu nome?')
    print(f'Ola {nome}')
x = 0

while x < 10:
    print(x)
    x = x+1
    
while x < 10:
    if x == 3:
        x = x+1
        continue
    print(x)
    x = x+1

x = 0    
while x < 10:
    if x == 3:
        x = x+1
        break
    print(x)
    x = x+1

x = 0
y = 0

while x < 5:
    y = 0
    while y < 5:
        print(f'({x}), ({y})')
        y += 1

    x = x+1
    
while True:
    num_1 = input('Digite um Número: ')
    num_2 = input('Digite outro Numero: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Digite um número!')
        continue

    operador = input('Digite um operador (+, -. *, /): ')

    num_1 = float(num_1)
    num_2 = float(num_2)

    if operador == '+':
        print(num_1 + num_2)

    elif operador == '-':
        print(num_1 - num_2)

    elif operador == '*':
        print(num_1 * num_2)

    elif operador == '/':
        print(num_1 / num_2)

    else:
        print('Operador Inválido!!!')

    sair = input('Sair? (S)im/(N)ão')

    if sair == 's':
        break
"""

# 18-> While/Else Repetição com acumuladores
"""
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
#    if contador > 5:
#        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('cheguei no else1')
    
print('cheguei no else2')
"""

# 19-> Iterando strings com while
"""
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
input = input('Qual Letra será maiuscula? ')

while contador < tamanho_frase:
    # print(frase[contador], contador)
    letra = frase[contador]

    if letra == input:
        nova_string += input.upper()
    else:
        nova_string += letra

    # nova_string += frase[contador]
    contador += 1
    # print(nova_string)

print(nova_string)

"""

# 20-> For in
"""
texto = 'Python'
nova_string = ''

for letra in texto:
    print(letra)

for n,letra in enumerate(texto):
    print(n, letra)

for n in range(10):
    print(n)

for m in range(5, 10, 2):
    print(m)

for letras in texto:
    if letras == 't':
        nova_string += letras.upper()
    elif letras == 'h':
        nova_string += letras.upper()
    else:
        nova_string += letras

print(nova_string)
"""

# 21-> Listas
"""
lista = ['Caio', 25, 2.5, True, 'E']
tamanho_lista = len(lista)

print(tamanho_lista)
contador = 0
for letra in range(tamanho_lista):
     print(letra, end=' ')

print('\n')

for letra in lista:
     print(letra, end=' ')
print('\n')
print(lista[0])
print(lista[1:4])
print(lista[::2])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
# l3 = l1 + l2

print(l1)
print(l2)
# print(l3)

l2.append('B')
l2.insert(0, 'A')
# l1.pop(0)

print(l1)
print(max(l1))
print(min(l1))

print(l2)

del(l2[1:4])

print(l2)

l2 = range(1,5)
print(l2)

l2 = list(range(0,10))
print(l2)

l2 = list(range(0,10, 2))
print(l2)

for valor in l2:
     print(valor, end='-')
print('\n')
for elemento in lista:
     print(f'O tipo de elemento é {type(elemento)} e seu valor é {elemento}')
     
linhas = int(input('Linhas: '))
colunas = int(input('Colunas: '))

matriz = [[0 for x in range(colunas)] for x in range(linhas)]

for i in range(0, linhas):
    for j in range(0, colunas):
        matriz[i][j] = input(f'Elemento[{i}, {j}]')

print('\nMatriz Digitada:')

for i in range(0, linhas):
    for j in range(0, colunas):
        print(f'{matriz[i][j]}', end=' ')

    print()
"""

# 22-> For/Else
"""
var = ['Caio', 'Isadora', 'Leticia', 'Luiz']
ini_c = False

for valor in var:
    print(valor)

    if valor.lower().startswith('c'):
        ini_c = True
        print(f'{valor} começa com C.')

    else:
        print(f'{valor} não começa com C.')

if ini_c:
    print('Existe nome com C.')

else:
    print('Não existe nome com C.')
"""

# 23-> Split, Join e Enumerate
"""
* Split - Divide uma String
* Join - Junta uma Lista/String
* Enumerate - Enumera elementos

string1 = "Star Trek é demais, Star Trek é sensacional."
lista1 = string1.split(' ')
lista2 = string1.split(',')
lista3 = [['Isadora', 'Caio', 'Leticia'],
          ['João', 'Mario', 'Bruna'],
          ['Ricardo', 'Ana', 'Bianca']]
string2 = ' '.join(lista1)


for v in enumerate(lista3, 1):
    valor, lista = v
    a, b, c = lista
    print(valor, a, b, c)

for v in lista3:
    print(v)

for v in lista3:
    print(v[0], v[1])

for i, v in enumerate(lista3):
    print(i, lista3[i])

for i, valor in enumerate(lista1):
    print(i, lista1[i])

for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase')
print(lista1)
print(lista2)
print(string1)
print(string2)
print(lista3[1])
print(lista3[1][2])
"""

# 24-> Desempacotamento de listas
"""
lista = ['Caio', 'Leticia', 'Isadora', 'Ricardo', 'Joao']

n1, n2, *outra_lista, n = lista
print(n)
"""

# 25-> Trocando o valor entre variáveis
"""
x = 10
y = 'Caio'
x, y = y, x
print(f'x = {x} e y = {y}')
"""

# 26-> Operação ternária
"""
logged_user = True
msg = 'Usuário logado.' if logged_user else 'Faça login.'
print(msg)

idade = input('Idade: ')

if not idade.isnumeric():
    print('Digite numeros.')

else:
    maior_idade = int(idade) >= 18
    message = 'Acesso condedido.' if maior_idade else 'Acesso negado.'
    print(message)
"""

# 27-> Expressão condicional com operador OR
"""
# nome = input('Qual seu nome? ')

# print(nome) if nome else print('Voce não digitou nada.')
# print(nome or 'Você não digitou nada.')

a = 0
b = None
c = False
d = []
e = {}
f = 35
g = 'Caio'

var = a or b or c or d or e or f or g
print(var)
"""

# 28-> Desafio Contadores
"""
for i, r in enumerate(range(9, -1, -1)):
    print(i, r)
"""

# 29-> Desafio Valide um CPF
"""
cpf = '359.376.098-32'

lista = cpf.split('-')
a, digito = lista
print(lista)

lista2 = a.split('.')
n1, n2, n3 = lista2
numero = n1 + n2 + n3

cpf_inserido = numero + digito
contador = 10
acumulador = 0

for i in numero:
    resultado = int(i) * contador
    contador -= 1
    acumulador += resultado

print(acumulador)

x1 = 11 - (acumulador % 11)

if x1 > 9:
    x1 = '0'
digito_valido = str(x1)
cpf_parcial = numero + digito_valido

print(x1)

contador = 11
acumulador = 0

for i in cpf_parcial:
    resultado = int(i) * contador
    contador -= 1
    acumulador += resultado

print(acumulador)

x2 = 11 - (acumulador % 11)

if x2 > 9:
    x2 = '0'

print(x2)

digito_valido = str(x1) + str(x2)
cpf_valido = numero + digito_valido
print(cpf_valido)

if cpf_valido:
    print(f'CPF válido.')
    print(n1, n2, n3, sep='.', end='-')
    print(digito_valido)

else:
    print('CPF inválido.')
    
    
"""

# cpf = input('CPF: ')
# Gerador de CPF

cpf = str(randint(100000000, 999999999))
n1 = cpf[0:3]
n2 = cpf[3:6 ]
n3 = cpf[6:]

numero = n1 + n2 + n3
print(numero)
print(n1, n2, n3, sep='.')

cpf_inserido = numero
contador = 10
acumulador = 0

for i in numero:
    resultado = int(i) * contador
    contador -= 1
    acumulador += resultado

print(acumulador)

x1 = 11 - (acumulador % 11)

if x1 > 9:
    x1 = '0'
digito_gerado = str(x1)
cpf_parcial = numero + digito_gerado

print(x1)

contador = 11
acumulador = 0

for i in cpf_parcial:
    resultado = int(i) * contador
    contador -= 1
    acumulador += resultado

print(acumulador)

x2 = 11 - (acumulador % 11)

if x2 > 9:
    x2 = '0'

print(x2)

digito_gerado = str(x1) + str(x2)
cpf_gerado = numero + digito_gerado
print(cpf_gerado)
print(n1, n2, n3, sep='.', end='-')
print(digito_gerado)
