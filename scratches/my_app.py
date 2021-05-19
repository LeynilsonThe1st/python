import tkinter as tk

janela = tk.Tk()
janela.title("Formulário")
janela.geometry("500x400")


def press():
    print("Press")

#Nome
Nome = tk.Label(text="Nome:", font=("arial", 16))
Nome.grid(column=0, row=0)

#Input nome
input_nome = tk.Entry()
input_nome.grid(column=0, row=1)

#Idade
idade = tk.Label(text="Idade:", font=("arial", 16))
idade.grid(column=1, row=0)

#Input Idade
input_idade = tk.Entry()
input_idade.grid(column=1, row=1)

#Genero
genero = tk.Label(text="Genero:", font=("arial", 16))
genero.grid(column=0, row=2)

#Input número
input_genero = tk.Entry()
input_genero.grid(column=0, row=3)

#Número
numero = tk.Label(text="Número:", font=("arial", 16))
numero.grid(column=1, row=2)

#Input número
input_numero = tk.Entry()
input_numero.grid(column=1, row=3)

#Classe
classe = tk.Label(text="Classe:", font=("arial", 16))
classe.grid(column=0, row=4)

#Input número
input_classe = tk.Entry()
input_classe.grid(column=0, row=5)

#Turma
turma = tk.Label(text="Turma:", font=("arial", 16))
turma.grid(column=1, row=4)

#Input número
input_classe = tk.Entry()
input_classe.grid(column=1, row=5)

#Gravar
btn_gravar = tk.Button(text="Gravar", font="arial", padx=30, pady=15, foreground="blue")
btn_gravar["command"] = press
btn_gravar.grid(column=0, row=7)

janela.mainloop()
