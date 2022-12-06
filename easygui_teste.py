import sys

from easygui import *

# msgbox
title = 'Erro!'
msg = 'Adicione o seu curriculo'
button = 'Fechar'
msgbox(msg, title, button)

# choicebox
choices = ['Frentista', 'Marceneiro', 'Programador']
msg2 = 'Selecione uma Profissão'
reply = choicebox(msg2, choices=choices)

# multchoicebox
texto = 'Quais dos seguinte itens vc possui? '
titulo = 'Bens Moveis'
bens = ['Carro', 'Moto', 'Barco', 'Aeronave', 'Skate', 'Bicicleta', 'Patinete', 'Patins', 'Nenhum']
select_bens = multchoicebox(texto, titulo, bens)

meus_bens = msgbox(f'Meus Itens: {select_bens}')

print(f'Profissão: {reply}')

# ccbox
msg3 = 'Deseja Continuar?'
title2 = 'Confirmar'
continuar = ccbox(msg3, title2)

if continuar:
    print(continuar)

else:
    sys.exit(0)

# ynbox
msg4 = 'Tem filhos?'
title3 = 'Dependentes'
dependentes = ynbox(msg4, title3)

if dependentes:
    print('Com dependentes')

else:
    print('Sem dependentes')

# buttonbox
msg5 = 'Qual o seu sexo?'
title4 = 'Sexo'
btn_list = ['Masculino', 'Feminino', 'Outro']
sexo = buttonbox(msg5, title4, btn_list)
print(f'Sexo: {sexo}')

# indexbox
msg6 = 'QuaL seu estado civil?'
title5 = 'Estado Civil'
btn_list2 = ['Casado', 'Solteiro', 'Divorciado', 'Viuvo']
estado_civil = indexbox(msg6, title5, btn_list2)

if estado_civil == 0:
    msg6 = 'Casado'

elif estado_civil == 1:
    msg6 = 'Solteiro'

elif estado_civil == 2:
    msg6 = 'Divorciado'

elif estado_civil == 3:
    msg6 = 'Viuvo'

print(f'Estado Civil: {msg6}')
msgbox(msg6, title5)

# Carregar Imagem
message = 'Selecione um Arquivo:'
titulo = 'Imagem'
entrada = []
imagem = fileopenbox()
resultado = msgbox(image=imagem)

# enterbox
campo = 'Nome: '
ttlo = 'Formulario'
entrada = enterbox(campo, ttlo, entrada)


