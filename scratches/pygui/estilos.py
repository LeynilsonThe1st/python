from tkinter.ttk import Style

class Estilos(Style):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.map(
            "C.TButton",
            foreground=[('pressed', 'red'), ('active', 'blue')],
            background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )
        self.layout("TMenubutton", [
            ("Menubutton.background", None),
            ("Menubutton.button", {
                "children": [
                    ("Menubutton.focus", {
                        "children": [
                            ("Menubutton.padding", {
                                "children": [
                                    ("Menubutton.label", {
                                        "side": "left",
                                        "expand": 1
                                    })
                                ]
                            })
                        ]
                    })
                ]
            })
        ])
