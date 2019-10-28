import random, time, copy
from negocioCampoMinado import CampoMinado


class PrintCampoMinado:
    
    def __init__(self, campo_minado):
        self.campo_minado = campo_minado

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

        #A solução da grade.
        b = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]


        for item in self.campo_minado.get_lista_bomb():
            b[item[0]][item[1]] = '*'

        for r in range (0, 9):
            for c in range (0, 9):
                value = self.campo_minado.l(r, c, b)
                # value = l(r, c, b)
                if value == '*':
                    self.campo_minado.updateValues(r, c, b)
                    # minado.updateValues(r, c, b)

        #Coloca a variavel k em espaços em brancos, pq n é para saber o que tem nas grades.
        k = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        self.printBoard(k)

        #O tempo começa
        startTime = time.time()

        #O jogo começa
        self.play(b, k, startTime)

    def marker(self, r, c, k):
        k[r][c] = '⚐'
        self.printBoard(k)

    def printBoard(self, b):
        print('    A   B   C   D   E   F   G   H   I')
        print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
        for r in range (0, 9):
            print(r,'║',self.campo_minado.l(r,0,b),'║',self.campo_minado.l(r,1,b),'║',self.campo_minado.l(r,2,b),'║',self.campo_minado.l(r,3,b),'║',self.campo_minado.l(r,4,b),'║',self.campo_minado.l(r,5,b),'║',self.campo_minado.l(r,6,b),'║',self.campo_minado.l(r,7,b),'║',self.campo_minado.l(r,8,b),'║')
            if not r == 8:
                print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
        print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')
    

    def choose(self, b, k, startTime):
        #Variables 'n stuff.
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        #Loop em caso de valor invalido.
        while True:
            chosen = input('Escolha os quandrados usando as coordenadas (ex. E4) ou marque uma bomba (ex. mE4): ').lower()
            #Verifica se é um quadrado valido.
            if len(chosen) == 3 and chosen[0] == 'm' and chosen[1] in letters and chosen[2] in numbers:
                c, r = (ord(chosen[1]))-97, int(chosen[2])
                self.marker(r, c, k)
                self.play(b, k, startTime)
                break
            elif len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers: return (ord(chosen[0]))-97, int(chosen[1])
            else: self.choose(b, k, startTime) 

    def play(self, b, k, startTime):
        #Jogador escolhe um quadrado.
        c, r = self.choose(b, k, startTime)
        # c, r = minado.choose(b, k, startTime)

        #Pega o valor daquela localização.
        v = self.campo_minado.l(r, c, b)
        # v = minado.l(r, c, b)

        #Se voce acretar uma bomba, o jogo acaba.
        if v == '*':
            self.printBoard(b)
            print('Você perdeu!')
            #Printa o resultado do tempo.
            print('Tempo: ' + str(round(time.time() - startTime)) + 's')
            #Oferece para jogar de novo.
            playAgain = input('Quer jogar de novo? (S/N): ').lower()
            if playAgain == 's':
                self.reset()
            else:
                quit()
        #Coloca um valor ja descoberto na grade.
        k[r][c] = v
        #Executa checkZeros() se o valor for 0.
        if v == 0:
            self.campo_minado.checkZeros(k, b, r, c)
        self.printBoard(k)
        #Verifica se voce ganhou.
        squaresLeft = 0
        for x in range (0, 9):
            row = k[x]
            squaresLeft += row.count(' ')
            squaresLeft += row.count('⚐')
        if squaresLeft == 10:
            self.printBoard(b)
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
        self.play(b, k, startTime)
        
if __name__ == '__main__':
    o = CampoMinado(10)
    p = PrintCampoMinado(o)
    p.reset()