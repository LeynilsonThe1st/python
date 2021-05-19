from tkinter.constants import RIDGE, LEFT, RIGHT, TOP, BOTTOM, X, Y, E, W, S, N, BOTH, NO, YES, NONE
from tkinter.ttk import Combobox, Checkbutton, Radiobutton, Spinbox
from tkinter import messagebox
import tkinter as tk

if __name__ == '__main__':

	def btn_sair():
		janela.quit()

	def mudar_txt():
		if input_text.get() != "":
			txt = input_text.get().strip().title()
			titulo.configure(text=txt + App)
			return
		
		titulo.configure(text="Tkinter App")

	def mostrar():
		cb = "ComboBox : " + combo.get()

		messagebox.askquestion(title="Your Data", message=cb)

	janela = tk.Tk()
	janela.title("Tkinter App")
	janela.geometry("800x650")
	# janela.resizable(width=False, height=False)

	# frame1
	frame1 = tk.Frame(janela, relief=RIDGE)
	frame1.pack(fill=X, pady=20, padx=50)

	sair = tk.Button(frame1, text="Sair", font=("kefa", 20), width=6, height=2, fg="red", command=btn_sair)
	sair.pack(side=RIGHT)
	titulo = tk.Label(frame1, text="Tkinter App", fg="dimgray", font=("kefa bold", 40))
	titulo.pack()
	# frame1

	# frame2
	frame2 = tk.Frame(janela, relief=RIDGE)
	frame2.pack(fill=X, padx=50)

	ttl = tk.Label(frame2, text="Nome: ", fg="dimgray", font=("kefa", 26))
	ttl.pack(side=LEFT)
	enter = tk.Button(frame2, text="Enter", font=("kefa", 20), width=8, command=mudar_txt)
	enter.pack(side=RIGHT, ipady=7)
	input_text = tk.Entry(frame2, font=("kefa", 20))
	input_text.pack(side=LEFT, ipady=5, expand=YES, fill=X)
	# frame2

	container = tk.Frame(janela, relief=RIDGE)
	container.pack(fill=X, pady=20, padx=50)

	# frame3
	frame3 = tk.Frame(container, relief=RIDGE)
	frame3.pack(anchor=N+W, side=LEFT, expand=YES, fill=BOTH)

	img = tk.PhotoImage(file="/home/leynilson/Pictures/Wallpapers/VgqiT0d.jpg")
    
	tk.Label(container, image=img).pack(anchor=E, side=LEFT)

	combo_label = tk.Label(frame3, text="ComboBox", fg="dimgray", font=("kefa", 20))
	combo = Combobox(frame3, width=5)
	combo['values'] = (tuple(range(1, 11)))
	combo.current(9)
	
	ch_label = tk.Label(frame3, text="CheckButtons", fg="dimgray", font=("kefa", 20))
	stt = tk.BooleanVar()
	stt.set(True)
	chbtn = Checkbutton(frame3, text="Eu", var=stt)

	state = tk.BooleanVar()
	state.set(False)
	chbtn1 = Checkbutton(frame3, text="Tu", var=state)

	rd_label = tk.Label(frame3, text="Radio Buttons", fg="dimgray", font=("kefa", 20))
	rd1 = Radiobutton(frame3, text="Python", value=10)
	rd2 = Radiobutton(frame3, text="PHP", value=20)
	rd3 = Radiobutton(frame3, text="Javascript", value=30)
	sp_label = tk.Label(frame3, text="spin Button", fg="dimgray", font=("kefa", 20))
	sp = Spinbox(frame3, from_=0, to=100, width=3)

	enviar = tk.Button(frame3, text="Enviar", font=("kefa", 20), command=mostrar)

	combo_label.grid(column=0, sticky=W, pady=10)
	combo.grid(row=0, column=1, sticky=W, padx=10)
	ch_label.grid(row=1, sticky=W, pady=10)
	chbtn.grid(row=1, column=1, sticky=W, padx=10)
	chbtn1.grid(row=2, column=1, sticky=W, pady=5, padx=10)
	rd_label.grid(row=3, column=0, sticky=W, pady=10)
	rd1.grid(row=3, column=1, sticky=W, padx=10)
	rd2.grid(row=4, column=1, sticky=W, pady=5, padx=10)
	rd3.grid(row=5, column=1, sticky=W, pady=5, padx=10)
	sp_label.grid(column=0, sticky=W, pady=10)
	sp.grid(row=6, column=1, sticky=W, pady=5, ipadx=5, padx=10)
	enviar.grid(columnspan=2, sticky=W, ipadx=80, ipady=5)
	# frame3

	# h = columun
	# v = row
	janela.mainloop()
