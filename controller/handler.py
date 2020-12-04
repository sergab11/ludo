from model import ludo
from view  import des_canvas
from tkinter import messagebox, filedialog
import json


ladoCasa = 40

def novoJ():
	global jogo 
	jogo = ludo.novoJogo()
	des_canvas.novo()

def getJogo():
	global jogo
	return jogo

def escolheuDado(valor):
	global jogo, valorDado
	valorDado = valor
	des_canvas.jogou(valorDado)

	if ludo.casaInicialCheia(jogo['tabuleiro'], jogo['jogadorVez']):
		if valorDado != 5:
			ludo.proximo(jogo)
			des_canvas.aposclique()

	if valorDado == 5:
		trata5()

def lanca():
	global jogo, valorDado
	valorDado = ludo.jogarDado()
	des_canvas.jogou(valorDado)

	if ludo.casaInicialCheia(jogo['tabuleiro'], jogo['jogadorVez']):
		if valorDado != 5:
			ludo.proximo(jogo)
			des_canvas.aposclique()

	if valorDado == 5:
		trata5()

def trata5():
	global jogo
	
	if not ludo.casaInicialVazia(jogo['tabuleiro'], jogo['jogadorVez']):
		if ludo.casaSaidaVazia(jogo['tabuleiro'], jogo['jogadorVez']):
			pecaEscolhida = jogo['tabuleiro'][jogo['jogadorVez']].index(0)
			if ludo.podeMoverPeca(jogo['tabuleiro'], jogo['jogadorVez'], pecaEscolhida, 5):
				ludo.moverPeca(jogo, pecaEscolhida, 5, True)
				des_canvas.aposclique()

def clicouCasa(coordCasa, coordPonteiro):
	cx, cy = coordCasa
	px, py = coordPonteiro
	return cx <= px <= cx + ladoCasa and cy <= py <= cy + ladoCasa

def escolhePeca(tabuleiro, jogadorVez, coordPonteiro):
	for i, casaTabuleiro in enumerate(tabuleiro[jogadorVez]):
		if 1 <= casaTabuleiro <= ludo.ultimaCasaBranca(0)+1:
			if clicouCasa(des_canvas.coordCasaComum(casaTabuleiro), coordPonteiro):
				return i
		elif ludo.ultimaCasaBranca(0)+1 < casaTabuleiro < ludo.casaFinal:
			if clicouCasa(des_canvas.coordCasaRetaFinal(jogadorVez)[casaTabuleiro - ludo.ultimaCasaBranca(0) - 2], coordPonteiro):
				return i

	return -1

def mouseClica(event):
	global valorDado, jogo
	cores = ["red", "green", "yellow", "blue"]
	print([event.x, event.y])
	pecaEscolhida = escolhePeca(jogo['tabuleiro'], jogo['jogadorVez'], [event.x, event.y])
	print(pecaEscolhida)
	if pecaEscolhida == -1:
		return
	
	print(jogo['jogadorVez'], pecaEscolhida, valorDado, ":", ludo.podeMoverPeca(jogo['tabuleiro'], jogo['jogadorVez'], pecaEscolhida, valorDado))
	if ludo.podeMoverPeca(jogo['tabuleiro'], jogo['jogadorVez'], pecaEscolhida, valorDado):
		jogadorAtual = jogo['jogadorVez']
		ludo.moverPeca(jogo, pecaEscolhida, valorDado, True)
		des_canvas.aposclique()
		if jogo['tabuleiro'][jogadorAtual].count(58) == 4:
			colocacao = list(range(4))
			colocacao.sort(key=lambda x: sum(jogo['tabuleiro'][x]), reverse=True)
			#print('colocacao', colocacao)
			messagebox.showinfo(message=str([cores[i] + ":  " + str(sum(jogo['tabuleiro'][i])) for i in colocacao]))
	 
	return

def salvarJogo():
	global jogo
	data = [("text files","*.txt"),("all files","*.*")]
	f = filedialog.asksaveasfile(initialdir=".", title="Salvar Jogo - Super Ludo", mode='w', defaultextension=data, filetypes=data)
	if f is None:
		messagebox.showerror("Erro", "Erro ao salvar arquivo!")
		return
	text2save = str(jogo) # starts from `1.0`, not `0.0`
	f.write(text2save)
	f.close()
	# f = open("jogoSalvo.txt", "w")
	# f.write(str(jogo))
	# f.close()

def carregarJogo():
	global jogo
	#f = open("jogoSalvo.txt", "r")
	input = filedialog.askopenfile(initialdir=".", title="Carregar Jogo - Super Ludo", filetypes=(("text files","*.txt"),("all files","*.*")))
	if input == None:
		messagebox.showerror("Erro", "Erro ao carregar arquivo!")
		return
	jogo = json.loads(input.read().replace("'", "\"")) 
	input.close()
	print(jogo['tabuleiro'])
	des_canvas.novo()
