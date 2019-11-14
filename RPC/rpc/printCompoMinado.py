import random, time, copy
import rpyc
from negocioCampoMinado import CampoMinado


class PrintCampoMinado:
    
    def __init__(self, num_bomb):
        config = {'allow_public_attrs': True}
        self.proxy = rpyc.connect('localhost', 18861, config=config)
        self.campo_minado = self.proxy.root
        self.campo_minado.criar_novo_jogo(num_bomb)

    def reset(self):
        print('''
        MENU PRINCIPAL
        =========

        -> Para instruções de como jogar, precione 'I'
        -> Para jogar, precione 'J'
        ''')

        escolha = input('Digite aqui: ').upper()

        if escolha == 'I':

            #Prints das instruções.
            print(open('instructions.txt', 'r').read())

            input('Precione [enter] quando estiver pronto para jogar. ')
            
        elif escolha != 'J':
            self.reset()
         
        self.campo_minado.reset()

        #Coloca a variavel k em espaços em brancos, pq n é para saber o que tem nas grades.
        resposta = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        self.printBoard(resposta)

        #O tempo começa
        startTime = time.time()

        #O jogo começa
        self.play(resposta, startTime)

    def marker(self, r, c, resposta):
        resposta[r][c] = '⚐'
        self.printBoard(resposta)

    def printBoard(self, qualquer):
        print('    A   B   C   D   E   F   G   H   I')
        print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
        for r in range (0, 9):
            print(r,'║',qualquer[r][0],'║',qualquer[r][1],'║',qualquer[r][2],'║',qualquer[r][3],'║',qualquer[r][4],'║',qualquer[r][5],'║',qualquer[r][6],'║',qualquer[r][7],'║',qualquer[r][8],'║')
            if not r == 8:
                print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
        print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')
    

    def choose(self, gabarito, resposta, startTime):
        #Variables 'n stuff.
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        #Loop em caso de valor invalido.
        while True:
            chosen = input('Escolha os quandrados usando as coordenadas (ex. E4) ou marque uma bomba (ex. mE4): ').lower()
            #Verifica se é um quadrado valido.
            if len(chosen) == 3 and chosen[0] == 'm' and chosen[1] in letters and chosen[2] in numbers:
                return (ord(chosen[0]))-97, int(chosen[1]), True
            elif len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers: return (ord(chosen[0]))-97, int(chosen[1]), False
            else: return self.choose(gabarito, resposta, startTime) 


    def valida_acerto_bomba(self, value, startTime):
        #Se voce acertar uma bomba, o jogo acaba.
        if value == '*':
            self.printBoard(self.campo_minado.get_b())
            print('Você perdeu!')
            #Printa o resultado do tempo.
            print('Tempo: ' + str(round(time.time() - startTime)) + 's')
            #Oferece para jogar de novo.
            playAgain = input('Quer jogar de novo? (S/N): ').lower()
            if playAgain == 's':
                self.reset()
            else:
                quit()

    def play(self, resposta, startTime):
        gabarito = self.campo_minado.get_b()
        
        #Jogador escolhe um quadrado.
        coluna, linha, marcador = self.choose(gabarito, resposta, startTime)
        while marcador:
            self.marker(linha, coluna, resposta)
            coluna, linha, marcador = self.choose(gabarito, resposta, startTime)
        


        #Pega o valor daquela localização.
        value = self.campo_minado.filtro(linha, coluna)
        # v = minado.l(r, c, b)

        #Se voce acertar uma bomba, o jogo acaba.
        self.valida_acerto_bomba(value, startTime)

        #Coloca um valor ja descoberto na grade.
        resposta[linha][coluna] = value

        #Executa checkZeros() se o valor for 0.
        # if value == 0:
            # self.checkZeros(resposta, linha, coluna)
        self.printBoard(resposta)
        
        #Verifica se voce ganhou.
        squaresLeft = 0
        for x in range (0, 9):
            row = resposta[x]
            squaresLeft += row.count(' ')
            squaresLeft += row.count('⚐')
        if squaresLeft == 10:
            self.printBoard(gabarito)
            print('Voce ganhou!')
            #Printa o resultado do tempo.
            print('Tempo: ' + str(round(time.time() - startTime)) + 's')
            #Oferece para jogar novamente.
            playAgain = input('Quer jogar de novo? (S/N): ')
            playAgain = playAgain.lower()
            if playAgain == 's':
                self.reset()
            else:
                quit()
        #Repete!
        self.play(resposta, startTime)

    def zeroProcedure(self, linha, coluna, resposta):
        #Linha de cima
        gabarito = self.campo_minado.get_b()
        if linha-1 > -1:
            row = resposta[linha-1]
            if coluna-1 > -1: row[coluna-1] = self.campo_minado.filtro(linha-1, coluna-1)
            row[coluna] = self.campo_minado.filtro(linha-1, coluna)
            if 9 > coluna+1: row[coluna+1] = self.campo_minado.filtro(linha-1, coluna+1)

        #Mesma linha
        row = resposta[linha]
        if coluna-1 > -1: row[coluna-1] = self.campo_minado.filtro(linha, coluna-1)
        if 9 > coluna+1: row[coluna+1] = self.campo_minado.filtro(linha, coluna+1)

        #Linha de baixo
        if 9 > linha+1:
            row = resposta[linha+1]
            if coluna-1 > -1: row[coluna-1] = self.campo_minado.filtro(linha+1, coluna-1)
            row[coluna] = self.campo_minado.filtro(linha+1, coluna)
            if 9 > coluna+1: row[coluna+1] = self.campo_minado.filtro(linha+1, coluna+1)

    def checkZeros(self, resposta, linha, coluna):
        oldGrid = copy.deepcopy(resposta)
        self.zeroProcedure(linha, coluna, resposta)
        if oldGrid == resposta:
            return
        while True:
            oldGrid = copy.deepcopy(resposta)
            for x in range (9):
                for y in range (9):
                    if self.campo_minado.filtro(x, y) == 0:
                        self.zeroProcedure(x, y, resposta)
            if oldGrid == resposta:
                return

if __name__ == '__main__':
    p = PrintCampoMinado(10)
    p.reset()