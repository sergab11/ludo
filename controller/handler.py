from model import ludo
from view  import des_canvas
from tkinter import messagebox
import json


ladoCasa = 40

def novoJ():
	global jogo 
	jogo = ludo.novoJogo()
	des_canvas.novo()

def getJogo():
	global jogo
	return jogo

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
		ludo.moverPeca(jogo, pecaEscolhida, valorDado, True)
		des_canvas.aposclique()
		if jogo['tabuleiro'][jogo['jogadorVez']].count(58) == 4:
			colocacao = list(range(4))
			colocacao.sort(key=lambda x: sum(jogo['tabuleiro'][x]), reverse=True)
			print(colocacao)
			messagebox.showinfo(message=str([cores[i] + ":  " + str(sum(jogo['tabuleiro'][i])) for i in colocacao]))
	 
	return

def salvarJogo():
	global jogo
	f = open("jogoSalvo.txt", "w")
	f.write(str(jogo))
	f.close()

def carregarJogo():
	global jogo
	f = open("jogoSalvo.txt", "r")
	jogo = json.loads(f.read().replace("'", "\"")) 
	f.close()
	print(jogo['tabuleiro'])
	des_canvas.novo()
