import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text='Nome: '))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text='Idade: '))
        self.idade = TextInput(multiline=False)
        self.inside.add_widget(self.idade)

        self.inside.add_widget(Label(text='Profissão: '))
        self.prof = TextInput(multiline=False)
        self.inside.add_widget(self.prof)

        self.inside.add_widget(Label(text='Cidade: '))
        self.cidade = TextInput(multiline=False)
        self.inside.add_widget(self.cidade)

        self.inside.add_widget(Label(text='Estado: '))
        self.estado = TextInput(multiline=False)
        self.inside.add_widget(self.estado)

        self.inside.add_widget(Label(text='Telefone: '))
        self.fone = TextInput(multiline=False)
        self.inside.add_widget(self.fone)

        self.inside.add_widget(Label(text='E-mail: '))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.button_enviar = Button(text='Enviar', font_size=40)
        self.button_enviar.bind(on_press=self.pressed)
        self.add_widget(self.button_enviar)

    def pressed(self, instance):
        name = self.name.text
        idade = self.idade.text
        prof = self.prof.text

        print('Nome: ', name, 'Idade: ', idade, 'Profissão: ', prof)
        self.name.text =''
        self.idade.text = ''
        self.prof.text = ''



class MyApp(App):
    def build(self):
        return MyGrid()

if __name__== '__main__':
    MyApp().run()

