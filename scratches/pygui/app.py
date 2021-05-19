from tkinter import Tk, StringVar
from tkinter.ttk import *
from estilos import Estilos
from janela2 import Janela2

class App(Tk):

    def __init__(self):
        super().__init__()
        self.title('Minha App')
        self.maxsize(600, 400)
        self.geometry('400x200')
        self.estilo = Estilos()
        self.janela_actual = Janela1()

    def run(self):
        self.mainloop()


class Janela1(Frame):

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)

        self.label = Label(text='Insira o seu nome:')
        self.label.pack()
        self.nome = StringVar()
        self.text_input = Entry(textvariable=self.nome)
        self.text_input.bind('<KeyRelease>', self.dizer_ola)
        self.text_input.pack()
        self.ola = Label()
        self.ola.pack()

    def dizer_ola(self, event):
        self.ola['text'] = "Ola {}!".format(self.nome.get().capitalize())
        if any(self.ola.cget('text')):
            self.ola.pack()
        else:
            self.ola.destroy()


if __name__ == '__main__':
    myapp = App()
    myapp.run()
