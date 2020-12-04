from ludo import *
import des_canvas

def tNaoTemBarreira():
    tabuleiro = [
        [casaSaida(0), 3, 5, 7],
        [casaSaida(1), 0, 0, 0],
        [casaSaida(2), 0, 0, 0],
        [casaSaida(3), 0, 0, 0]
    ]

    expectedValue = []
    actualValue = barreiras(tabuleiro, 0)

    return expectedValue == actualValue

def tTemBarreira():
    tabuleiro = [
        [casaSaida(0), 2, 5, 5],
        [casaSaida(1), 0, 0, 0],
        [casaSaida(2), 0, 0, 0],
        [casaSaida(3), 0, 0, 0]
    ]

    expectedValue = [5]
    actualValue = barreiras(tabuleiro, 0)

    return expectedValue == actualValue

def tTemBarreiraOponente():
    tabuleiro = [
        [casaSaida(0), 3, 3, 4],
        [casaSaida(1), 6, 6, 7],
        [casaSaida(2), 8, 9, 8],
        [casaSaida(3), 11, 12, 13]
    ]

    expectedValue = [6, 8]
    actualValue = barreirasOponentes(tabuleiro, 0)

    return expectedValue == actualValue

def tTemAbrigoCheio():
    tabuleiro = [
        [casaSaida(0), 3, 3, 4],
        [casaSaida(1), 10, 6, 7],
        [casaSaida(2), 10, 9, 8],
        [casaSaida(3), 11, 12, 13]
    ]

    expectedValue = True
    actualValue = casa2Pecas(tabuleiro, 10)

    return expectedValue == actualValue
    
def tPecaAnda():
    jogo = {
    'jogadorVez': 0,
    'valorDado6': 0,
    'pecaAnterior6': 0,
    'naoMove6': False,
    'tabuleiro': [
        [casaSaida(0), 0, 0, 0],
        [casaSaida(1), 0, 0, 0],
        [casaSaida(2), 0, 0, 0],
        [casaSaida(3), 0, 0, 0]
    ]
}
    
    expectedValue = {
        'jogadorVez': 0,
        'valorDado6': 0,
        'pecaAnterior6': 0,
        'naoMove6': False,
        'tabuleiro': [
            [6, 0, 0, 0],
            [casaSaida(1), 0, 0, 0],
            [casaSaida(2), 0, 0, 0],
            [casaSaida(3), 0, 0, 0]
        ]
    }

    moverPeca(jogo, 0, 5, False)
    actualValue = jogo

    return expectedValue == actualValue

def tJogaOutraVez():
    jogo = {
        'jogadorVez': 1,
        'valorDado6': 0,
        'pecaAnterior6': 0,
        'naoMove6': False,
        'tabuleiro': [
            [4, 0, 0, 0],
            [17, 15, 0, 0],
            [casaSaida(2), 0, 0, 0],
            [casaSaida(3), 0, 0, 0]
        ]
    }
    
    expectedValue = {
        'jogadorVez': 0,
        'valorDado6': 1,
        'pecaAnterior6': 1,
        'naoMove6': False,
        'tabuleiro': [
            [4, 0, 0, 0],
            [17, 21, 0, 0],
            [casaSaida(2), 0, 0, 0],
            [casaSaida(3), 0, 0, 0]
        ]
    }

    moverPeca(jogo, 1, 6, True)
    actualValue = jogo
    return expectedValue == actualValue

def tVoltaCasaInicial():
    jogo = {
        'jogadorVez': 1,
        'valorDado6': 2,
        'pecaAnterior6': 0,
        'naoMove6': False,
        'tabuleiro': [
            [4, 0, 0, 0],
            [17, 15, 0, 0],
            [casaSaida(2), 0, 0, 0],
            [casaSaida(3), 0, 0, 0]
        ]
    }
    
    expectedValue = {
        'jogadorVez': 1,
        'valorDado6': 0,
        'pecaAnterior6': 0,
        'naoMove6': False,
        'tabuleiro': [
            [4, 0, 0, 0],
            [0, 15, 0, 0],
            [casaSaida(2), 0, 0, 0],
            [casaSaida(3), 0, 0, 0]
        ]
    }

    moverPeca(jogo, 1, 6, True)
    actualValue = jogo
    return expectedValue == actualValue
    
def tPrimeiraRodadaPodeMoverPecaCasaInicial():
    tabuleiro = [
        [casaSaida(0), 0, 0, 0],
        [casaSaida(1), 0, 0, 0],
        [casaSaida(2), 0, 0, 0],
        [casaSaida(3), 0, 0, 0]
    ]

    expectedValue = True
    actualValue = podeMoverPeca(tabuleiro, 0, 0, 2)
    
    return expectedValue == actualValue

def tPrimeiraRodadaPodeMoverPecaCasaSaida():
    tabuleiro = [
        [casaSaida(0), 0, 0, 0],
        [casaSaida(1), 0, 0, 0],
        [casaSaida(2), 0, 0, 0],
        [casaSaida(3), 0, 0, 0]
    ]

    expectedValue = True
    actualValue = podeMoverPeca(tabuleiro, 0, 0, 5)
    
    return expectedValue == actualValue
    
def tPodeMoverPecaCasaInicial():
    tabuleiro = [
        [2, 0, 0, 0],
        [casaSaida(1), 0, 0, 0],
        [casaSaida(2), 0, 0, 0],
        [casaSaida(3), 0, 0, 0]
    ]

    expectedValue = True
    actualValue = podeMoverPeca(tabuleiro, 0, 1, 5)
    
    return expectedValue == actualValue

def tCasaSaidaVazia():
    tabuleiro = [
        [2, 0, 0, 0],
        [casaSaida(1), 0, 0, 0],
        [casaSaida(2), 0, 0, 0],
        [casaSaida(3), 0, 0, 0]
    ]

    expectedValue = True
    actualValue = casaSaidaVazia(tabuleiro, 0)
    
    return expectedValue == actualValue
    
def tCasaInicialVazia():
    tabuleiro = [
        [2, 2, 1, 1],
        [casaSaida(1), 0, 0, 0],
        [casaSaida(2), 0, 0, 0],
        [casaSaida(3), 0, 0, 0]
    ]

    expectedValue = True
    actualValue = casaInicialVazia(tabuleiro, 0)
    
    return expectedValue == actualValue
    
def tPodeCairAbrigo():
    tabuleiro = [
        [10, 2, 1, 1],
        [8, 0, 0, 0],
        [casaSaida(2), 0, 0, 0],
        [casaSaida(3), 0, 0, 0]
    ]

    expectedValue = True
    actualValue = podeMoverPeca(tabuleiro, 1, 0, 2)
    return expectedValue == actualValue
    
def tImpedimentoAbrigo():
    tabuleiro = [
        [10, 2, 1, 1],
        [10, 0, 0, 0],
        [8, 0, 0, 0],
        [casaSaida(3), 0, 0, 0]
    ]
    expectedValue = False
    actualValue = podeMoverPeca(tabuleiro, 2, 0, 2)
    
    return expectedValue == actualValue    
    
def tCasaCheia():
    tabuleiro = [
        [10, 2, 3, 1],
        [10, 0, 0, 0],
        [8, 0, 0, 0],
        [casaSaida(3), 0, 0, 0]
    ]

    expectedValue = True
    actualValue = casa2Pecas(tabuleiro, 10)
    
    return expectedValue == actualValue 
    
def tCasaJogadorCasaComum1():

    expectedValue = 8
    actualValue = casaJogador(34, 2)
    
    return expectedValue == actualValue
    
def tCasaJogadorCasaComum2():

    expectedValue = 34
    actualValue = casaJogador(8, 2)
    
    return expectedValue == actualValue

def tCasaJogadorRetaFinal():

    expectedValue = 54
    actualValue = casaJogador(54, 2)
    
    return expectedValue == actualValue
    
def tCasaTabuleiroCasaComum1():

    expectedValue = 8
    actualValue = casaTabuleiro(34, 2)
    
    return expectedValue == actualValue 
    
def tCasaTabuleiroCasaComum2():

    expectedValue = 34
    actualValue = casaTabuleiro(8, 2)
    
    return expectedValue == actualValue    

def tCasaTabuleiroRetaFinal():

    expectedValue = 54
    actualValue = casaTabuleiro(545, 2)
    
    return expectedValue == actualValue 

#desenhaCasas(cnv),
#desenhaPecas(cnv, tabuleiro),
#desenhaCasasBrancas(cnv),
#desenhaCasasIniciais(cnv),
#desenhaRetaFinal(cnv),
#desenhaCasasSaida(cnv),
#desenhaCasaFinal(cnv),
#desenhaCasaAbrigos(cnv)
#njogo, carregar, salvar, cnv, cnvdado, raiz

def tMostraTelaInicial():
    tabuleiro = novoJogo()['tabuleiro']
    janela = des_canvas.constroiJanela()
    des_canvas.desenhaCasas(janela[3])
    des_canvas.desenhaPecas(janela[3], tabuleiro)
    des_canvas.desenhaJanela(janela)
    #des_canvas.TestaJanela(novoJogo()['tabuleiro'])

def tMostraTelaAbrigo():
    tabuleiro = [
        [0, 10, 0, 0],
        [0, 10, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    janela = des_canvas.constroiJanela()
    des_canvas.desenhaCasas(janela[3])
    des_canvas.desenhaPecas(janela[3], tabuleiro)
    des_canvas.desenhaJanela(janela)

def tMostraTelaBarreira():
    tabuleiro = [
        [0, 3, 3, 0],
        [0, 10, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    janela = des_canvas.constroiJanela()
    des_canvas.desenhaCasas(janela[3])
    des_canvas.desenhaPecas(janela[3], tabuleiro)
    des_canvas.desenhaJanela(janela)

def tDesenhaCasasBrancas():
    janela = des_canvas.constroiJanela()
    des_canvas.desenhaCasasBrancas(janela[3])
    des_canvas.desenhaJanela(janela)

def tcoordCasasIniciais():
    return 'Jogador 1 '+str(des_canvas.coordCasasIniciais(0))

def tDesenhaCasasIniciais():
    janela = des_canvas.constroiJanela()
    des_canvas.desenhaCasasIniciais(janela[3])
    des_canvas.desenhaJanela(janela)

def tDesenhaCasasSaida():
    janela = des_canvas.constroiJanela()
    des_canvas.desenhaCasasSaida(janela[3])
    des_canvas.desenhaJanela(janela)

def tDesenhaCasaFinal():
    janela = des_canvas.constroiJanela()
    des_canvas.desenhaCasaFinal(janela[3])
    des_canvas.desenhaJanela(janela)

def tcoordCasasBrancas():
    return 'coordenadaCasa10'+str(des_canvas.coordCasaComum(10))

def tcoordRetaFinal():
    return 'Jogador 2 '+str(des_canvas.coordCasaRetaFinal(1))

def tDesenhaRetaFinal():
    janela = des_canvas.constroiJanela()
    des_canvas.desenhaCasasRetaFinal(janela[3])
    des_canvas.desenhaJanela(janela)

def tDesenhaPeca():
    janela = des_canvas.constroiJanela()
    des_canvas.desenhaPeca(janela[3], 0, 0, 'green')
    des_canvas.desenhaJanela(janela)
    
def tDesenhaPecasBarreiras():
    tabuleiro = [
        [0, 3, 3, 0],
        [0, 10, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    janela = des_canvas.constroiJanela()
    des_canvas.desenhaCasas(janela[3])
    des_canvas.desenhaPecasBarreiras(janela[3], tabuleiro)
    des_canvas.desenhaJanela(janela)

def tDesenhaPecasIniciais():
    tabuleiro = [
        [0, 3, 3, 0],
        [0, 10, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
    ]
    janela = des_canvas.constroiJanela()
    des_canvas.desenhaCasas(janela[3])
    des_canvas.desenhaPecasIniciais(janela[3], tabuleiro)
    des_canvas.desenhaJanela(janela)

def tDesenhaPecasComuns():
    tabuleiro = [
        [0, 3, 35, 0],
        [0, 10, 4, 0],
        [0, 2, 27, 0],
        [0, 42, 0, 0],
    ]
    janela = des_canvas.constroiJanela()
    des_canvas.desenhaCasas(janela[3])
    des_canvas.desenhaPecasComuns(janela[3], tabuleiro)
    des_canvas.desenhaJanela(janela)

for t in [tNaoTemBarreira, tTemBarreira, tTemBarreiraOponente, tTemAbrigoCheio, tPecaAnda, tJogaOutraVez,
tVoltaCasaInicial, tPrimeiraRodadaPodeMoverPecaCasaInicial, tPrimeiraRodadaPodeMoverPecaCasaSaida,
tPodeMoverPecaCasaInicial, tCasaSaidaVazia, tCasaInicialVazia, tPodeCairAbrigo, tImpedimentoAbrigo, tCasaCheia,
tCasaJogadorCasaComum1, tCasaJogadorCasaComum2, tCasaJogadorRetaFinal, tCasaTabuleiroCasaComum1,
tCasaTabuleiroCasaComum2, tCasaTabuleiroRetaFinal]:
    print(t.__name__, ':', t())

#InterfaceGrafica
for t in [tcoordCasasIniciais, tcoordCasasBrancas, tcoordRetaFinal, tMostraTelaInicial, tMostraTelaAbrigo, tMostraTelaBarreira, 
tDesenhaCasasBrancas, tDesenhaCasasIniciais, tDesenhaCasasSaida, tDesenhaCasaFinal, tDesenhaRetaFinal, tDesenhaPeca,
tDesenhaPecasBarreiras, tDesenhaPecasIniciais, tDesenhaPecasComuns]:
    print(t.__name__, ':', t())