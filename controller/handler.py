from model import ludo
from view  import des_canvas
from tkinter import filedialog
from tkinter import messagebox

ladoCasa = 40

def selecionaArq():
	input = filedialog.askopenfile(initialdir=".", title="Super Ludo", filetypes=(("text files","*.txt"),("all files","*.*")))
	if input == None:
		messagebox.showerror("Erro", "Erro ao carregar arquivo!")
		return
	carregar(input)

def salvaArq():
	global jogo

	data = [("text files","*.txt"),("all files","*.*")]
	file = filedialog.asksaveasfile(initialdir=".", title="Super Ludo", filetypes=data, defaultextension=data)
	if file == None:
		messagebox.showerror("Erro", "Erro ao salvar arquivo!")
		return

	ludo.salvaContexto(jogo, file)

def novoJ():
	global jogo 
	jogo = ludo.novoJogo()
	des_canvas.novo()

def carregar(arquivo):
	global jogo
	jogo = ludo.novoJogo()
	ludo.carregaContexto(jogo, arquivo)
	des_canvas.aposclique()

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

	pecaEscolhida = escolhePeca(jogo['tabuleiro'], jogo['jogadorVez'], [event.x, event.y])
	if pecaEscolhida == -1:
		return
		
	if ludo.podeMoverPeca(jogo['tabuleiro'], jogo['jogadorVez'], pecaEscolhida, valorDado):
		ludo.moverPeca(jogo, pecaEscolhida, valorDado, True)
		des_canvas.aposclique()
	 
	return
