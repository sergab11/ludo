import tkinter
from model import ludo
from controller import handler

#lado casa inicial -> 240
#lado casa branca -> 40
#raio da peça -> 40
#base do triângulo da casa final -> 120
#altura do triângulo da casa final -> 60
#altura do triângulo branco -> 30
#base do triângulo branco -> 30

ladoCasa = 40
cnv = {}
jogo = {}
valorDado = 0
cnvdado = {}
dadoimg = []
cores = ["red", "green", "yellow", "blue"]

def jogou(dado):
	global valorDado
	valorDado = dado
	desenhaDadoJogador(cnvdado, valorDado, jogo['jogadorVez'])

def novo():
	global jogo, valorDado, dadoimg, cnvdado

	jogo = handler.getJogo()
	desenhaCasas(cnv)
	desenhaPecas(cnv, jogo['tabuleiro'])
	cnvdado.create_rectangle(0, 0, 40, 40, fill=cores[0])

def desenhaDadoJogador(cnvdado, n, j):
	global dadoimg
	cnvdado.create_rectangle(0, 0, 40, 40, fill=cores[j])
	cnvdado.create_image(5, 5, image=dadoimg[n-1], anchor='nw')

def aposclique():
	global jogo
	
	desenhaCasas(cnv)
	desenhaPecas(cnv, jogo['tabuleiro'])
	cnvdado.create_rectangle(0, 0, 40, 40, fill=cores[jogo['jogadorVez']])

def inicializar(canvtab, canvdado):
	global cnv, cnvdado, dadoimg
	for n in range(6):
		dadoimg.append(tkinter.PhotoImage(file="dado_"+str(n + 1)+".png"))

	cnv = canvtab
	cnvdado = canvdado
	desenhaCasas(cnv)

def desenhaCasasBrancas(cnv):
	for x1 in [ladoCasa * i for i in range(15)]:
		for y1 in [ladoCasa * j for j in range(15)]:
			cnv.create_rectangle(x1, y1, x1+ladoCasa, y1+ladoCasa, fill="white")
			
def coordCasasIniciais(j):
	v = [ladoCasa, 4*ladoCasa]
	coords = []
	for x0 in v:
		for y0 in v:
			coords.append(rotacionase([x0, y0], j))

	return coords

def coordCasaRetaFinal(j):
	return [rotacionase([(i+1)*ladoCasa, 7*ladoCasa], j) for i in range(6)]

def desenhaCasasIniciais(cnv, j):
	x1, y1 = rotaciona([0, 0], j)
	x2, y2 = rotaciona([6*ladoCasa, 6*ladoCasa], j)
	cnv.create_rectangle(x1, y1, x2, y2, fill=cores[j])

	for x, y in coordCasasIniciais(j):
		cnv.create_oval(x, y, x+ladoCasa, y+ladoCasa, fill="white", width=3)

def desenhaCasaSaida(cnv, j):
	x, y = coordCasaComum(ludo.casaSaida(0))
	cnv.create_rectangle(rotaciona([x, y], j) + rotaciona([x + ladoCasa, y + ladoCasa], j), fill=cores[j])
	cnv.create_polygon(rotaciona([x+5, y+35], j) + rotaciona([x+5, y+5], j) + rotaciona([x+35, y+20], j), fill="white")

def desenhaCasasRetaFinal(cnv, j):
	for c in coordCasaRetaFinal(j):
		x, y = c
		cnv.create_rectangle(x, y, x+ladoCasa, y+ladoCasa, fill=cores[j])

def desenhaCasaFinal(cnv, j):
	p = rotaciona([ladoCasa * 6, ladoCasa * 6], j) + rotaciona([ladoCasa * 6, ladoCasa * 9], j) + rotaciona([ladoCasa * 7.5, ladoCasa * 7.5], j)
	cnv.create_polygon(p, outline="black", fill=cores[j])

def desenhaCasasAbrigos(cnv):
	for x, y in [coordCasaComum(a) for a in ludo.abrigos]:
		cnv.create_rectangle(x, y, x + ladoCasa, y + ladoCasa, fill="black")

def coordCasaBrancaJ0(c):
	i = c + 1
	if 1 <= i <= 5:
		return [ladoCasa * i, ladoCasa * 6]
	elif 6 <= i <= 10:
		return [ladoCasa * 6, ladoCasa * (11-i)]
	elif 11 <= i <= 13:
		return [ladoCasa * (i - 5), 0]

def rotaciona(p, j):
	return [lambda c: c, lambda c: [15*ladoCasa - c[1], c[0]], lambda c: [15*ladoCasa - c[0], 15*ladoCasa - c[1]], lambda c: [c[1], 15*ladoCasa - c[0]]][j](p)

def rotacionase(p, j):
	return [x - ladoCasa//2 for x in rotaciona([x + ladoCasa//2 for x in p], j)]

def coordCasaComum(c):
	i = c - 1
	return rotacionase(coordCasaBrancaJ0(i % 13), i // 13)

def coordCasaRetaFinal(j):
	return [rotacionase([(i+1)*ladoCasa, 7*ladoCasa], j) for i in range(6)]

def desenhaCasas(cnv):
	desenhaCasasBrancas(cnv)
	desenhaCasasAbrigos(cnv)
	for j in range(4):
		desenhaCasasIniciais(cnv, j)
		desenhaCasaSaida(cnv, j)
		desenhaCasasRetaFinal(cnv, j)
		desenhaCasaFinal(cnv, j)
	
def desenhaPecasBarreiras(cnv, tabuleiro, j):
	for x, y in [coordCasaComum(b) for b in ludo.barreiras(tabuleiro, j)]:
		cnv.create_oval(x + 2, y + 2, x+38, y+38, fill=cores[j])
		cnv.create_oval(x + 5, y + 5, x+35, y+35, fill="black")
		desenhaPeca(cnv, x, y, cores[j])


def desenhaPeca(cnv, x, y, color):
	cnv.create_oval(x + 8, y + 8, x+32, y+32, fill=color)

def desenhaPecasIniciais(cnv, tabuleiro, j):
	qtdPecasIniciais = tabuleiro[j].count(0)
	for x, y in coordCasasIniciais(j)[:qtdPecasIniciais]:
		desenhaPeca(cnv, x, y, cores[j])

def desenhaPecasComunsERetaFinal(cnv, tabuleiro, j):
	for p in range(4):
		c = tabuleiro[j][p]
		if ludo.casa2Pecas(tabuleiro, c):
			continue
		if 1 <= c <= ludo.ultimaCasaBranca(0)+1:
			x, y = coordCasaComum(tabuleiro[j][p])
			desenhaPeca(cnv, x, y, cores[j])
		elif (ludo.ultimaCasaBranca(0)+1) < c < ludo.casaFinal:
			x, y = coordCasaRetaFinal(j)[c - ludo.ultimaCasaBranca(0)-2]
			desenhaPeca(cnv, x, y, cores[j])

def desenhaPecasAbrigos(cnv, tabuleiro):
	for abrigo in ludo.abrigos + [ludo.casaSaida(i) for i in range(4)]:
		if ludo.casa2Pecas(tabuleiro, abrigo):
			coresPecas = [cor for i, cor in enumerate(cores) if abrigo in tabuleiro[i]]
			x, y = coordCasaComum(abrigo)
			cnv.create_oval(x + 2, y + 2, x+38, y+38, fill=coresPecas[1])
			cnv.create_oval(x + 5, y + 5, x+35, y+35, fill="white")
			desenhaPeca(cnv, x, y, coresPecas[0])

def desenhaPecas(cnv, tabuleiro):
	desenhaPecasAbrigos(cnv, tabuleiro)
	for j in range(4):
		desenhaPecasIniciais(cnv, tabuleiro, j)
		desenhaPecasComunsERetaFinal(cnv, tabuleiro, j)
		desenhaPecasCasaFinal(cnv, tabuleiro, j)
		desenhaPecasBarreiras(cnv, tabuleiro, j)

def desenhaPecasCasaFinal(cnv, tabuleiro, j):
	x, y = coordCasaRetaFinal(0)[5]
	for i in range(tabuleiro[j].count(ludo.casaFinal)):
		dx, dy = rotacionase([3 * i + x, 3 * i + y], j)
		desenhaPeca(cnv, dx, dy, cores[j])
