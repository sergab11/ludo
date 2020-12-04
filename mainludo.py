import tkinter as tk
from tkinter import ttk

from view import des_canvas
from model import ludo
from controller import handler

def getValor():
	v = int(escolhevalor.get())
	escolhevalor.set("")
	handler.escolheuDado(v)

raiz = tk.Tk()
raiz.title("Super Ludo")
raiz.geometry('850x600')

tab = tk.Frame(raiz, width=600, height=600)
tab.pack(side="left", fill='y')
cnv = tk.Canvas(tab, height=600, width=600)
cnv.bind("<Button-1>", handler.mouseClica)

botoes = tk.Frame(raiz)
botoes.pack(side="top", fill='y')

njogo = tk.Button(botoes, text="Novo Jogo", command=handler.novoJ)
njogo.pack(pady=10)

carregar = tk.Button(botoes, text="Carregar Jogo", command=lambda:handler.selecionaArq())
carregar.pack(pady=10)

salvar = tk.Button(botoes, text="Salvar", command=lambda:handler.salvaArq())
salvar.pack(pady=10)

texto1 = tk.Label(botoes, text="A JOGAR:")
texto1.config(font="Arial 16 bold", bd=2, height=1, width=18)
texto1.pack(pady=10)

cnvdado = tk.Canvas(botoes, height=50, width=50)
cnvdado.pack(pady=10)

texto2 = tk.Label(botoes, text="Escolha o valor do dado:")
texto2.config(font="Arial 12 bold", bd=2, height=1, width=30)
texto2.pack(pady=5)

escolhevalor = ttk.Combobox(botoes, values=["1", "2", "3", "4", "5", "6"])
escolhevalor.pack(pady=5)

enviavalor = tk.Button(botoes, text="Enviar", command=getValor)
enviavalor.config(font="Arial 9 bold", bg="white", bd=2, height=1, width=7)
enviavalor.pack(pady=3)

lancar = tk.Button(botoes, text="Lançar Dado", command=handler.lanca)
lancar.pack(pady=30)

for i in (njogo, carregar, salvar, lancar):
	i.config(font="Arial 12 bold", bg="white", bd=2, height=1, width=18)

des_canvas.inicializar(cnv, cnvdado)

cnv.pack()
raiz.mainloop()
