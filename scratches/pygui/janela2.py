from tkinter.ttk import Frame, Button, Menubutton


class Janela2(Frame):

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.btn = Button(text='OFF', style="C.TButton")
        self.btn_menu = Menubutton(text='texto')
        self.btn_menu.pack()
        self.btn.bind('<ButtonPress>', self.btn_press)
        self.btn.pack()

    def btn_press(self, event):
        if event.widget['text'] == 'OFF':
            event.widget['text'] = 'ON'
        else:
            event.widget['text'] = 'OFF'
