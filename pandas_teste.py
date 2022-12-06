import pandas
import easygui

"""nome = {'Nome': ['Caio', 'Isadora', 'Leticia'],
        'Sobrenome': ['Mekacheski', 'Araujo', 'Arias']}
dataframe = pandas.DataFrame(nome)
# dataframe.to_excel('dataframe.xls')
dataframe.to_excel('dataframe.xlsx')"""

dataframe = pandas.read_excel('profissoes.xlsx')
item = []

for i, p in enumerate(dataframe['PROFISSOES']):
    item.append(p)
    print(item[i])

easygui.choicebox('Escolha uma profissao: ', choices=item)



