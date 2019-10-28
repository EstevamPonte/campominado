# ##############################
# ## MINESWEEPER by @ThomasS1 ##
# ## ======================== ##
# ## Want to know how to make ##
# ## this and games like it?  ##
# ## Read my tutorial:        ##
# ## https://repl.it/talk/learn/How-to-program-MineSweeper-in-Python-fully-explained-in-depth-tutorial/9397 ##
# ##############################

# import random, time, copy, replit

# print()
# print('Bem vindo ao Campo Minado', 'red')
# print('=============================', 'red')



# #Escolha do jogo.
# def reset():
#     print('''
# MENU PRINCIPAL
# =========

# -> Para instruções de como jogar, precione 'I'
# -> Para jogar, precione 'J'
# ''')

#     escolha = input('Digite aqui: ').upper()

#     if escolha == 'I':
#         replit.clear()

#         #Prints das instruções.
#         print(open('instructions.txt', 'r').read())

#         input('Precione [enter] quando estiver pronto para jogar. ')
        
#     elif escolha != 'J':
#         replit.clear()
#         reset()

#     #A solução da gade.
#     b = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

#     for n in range (0, 10):
#         posicaoBomba(b)

#     for r in range (0, 9):
#         for c in range (0, 9):
#             value = l(r, c, b)
#             if value == '*':
#                 updateValues(r, c, b)

#     #Coloca a variavel k em espaços em brancos, pq n é para saber o que tem nas grades.
#     k = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

#     printBoard(k)

#     #O tempo começa
#     startTime = time.time()

#     #O jogo começa
#     play(b, k, startTime)

# #Pega os valores da coordenadas das grades.
# #Regra de negocio.
# def l(r, c, b):
#     return b[r][c]

# #Coloca as bombas em lugares aleatorios.
# #Regra de negocio.
# def posicaoBomba(b):
#     r = random.randint(0, 8)
#     c = random.randint(0, 8)
#     #Verifica se exite uma bomba naquela posição, se n tiver, a bomba é colocada, se tiver, a função é chamada novamente.
#     currentRow = b[r]
#     if not currentRow[c] == '*':
#         currentRow[c] = '*'
#     else:
#         posicaoBomba(b)

# #Adiciona 1 ao quadrados que  tiverem bonbas ao redor.
# #Regra de negocio.
# def updateValues(rn, c, b):

#     #Linha de cima.
#     if rn-1 > -1:
#         r = b[rn-1]
        
#         if c-1 > -1:
#             if not r[c-1] == '*':
#                 r[c-1] += 1

#         if not r[c] == '*':
#             r[c] += 1

#         if 9 > c+1:
#             if not r[c+1] == '*':
#                 r[c+1] += 1

#     #Mesma linha (A do meio).    
#     r = b[rn]

#     if c-1 > -1:
#         if not r[c-1] == '*':
#             r[c-1] += 1

#     if 9 > c+1:
#         if not r[c+1] == '*':
#             r[c+1] += 1

#     #Linha de baixo.
#     if 9 > rn+1:
#         r = b[rn+1]

#         if c-1 > -1:
#             if not r[c-1] == '*':
#                 r[c-1] += 1

#         if not r[c] == '*':
#             r[c] += 1

#         if 9 > c+1:
#             if not r[c+1] == '*':
#                 r[c+1] += 1

# #Quando um 0 é encontrado, todos os quadrados ao redor sao abertos.
# #Regra de negocio.
# def zeroProcedure(r, c, k, b):

#     #Linha de cima
#     if r-1 > -1:
#         row = k[r-1]
#         if c-1 > -1: row[c-1] = l(r-1, c-1, b)
#         row[c] = l(r-1, c, b)
#         if 9 > c+1: row[c+1] = l(r-1, c+1, b)

#     #Mesma linha
#     row = k[r]
#     if c-1 > -1: row[c-1] = l(r, c-1, b)
#     if 9 > c+1: row[c+1] = l(r, c+1, b)

#     #Linha de baixo
#     if 9 > r+1:
#         row = k[r+1]
#         if c-1 > -1: row[c-1] = l(r+1, c-1, b)
#         row[c] = l(r+1, c, b)
#         if 9 > c+1: row[c+1] = l(r+1, c+1, b)

# #Verifica se os quadrados ao redor de cada zero estao abertas, se n estiver ele abre.
# #Regra de negocio.
# def checkZeros(k, b, r, c):
#     oldGrid = copy.deepcopy(k)
#     zeroProcedure(r, c, k, b)
#     if oldGrid == k:
#         return
#     while True:
#         oldGrid = copy.deepcopy(k)
#         for x in range (9):
#             for y in range (9):
#                 if l(x, y, k) == 0:
#                     zeroProcedure(x, y, k, b)
#         if oldGrid == k:
#             return

# #Coloca o marcador na localização indicada
# #Regra de negocio.
# def marker(r, c, k):
#     k[r][c] = '⚐'
#     printBoard(k)

# #Printa o quadro.
# def printBoard(b):
#     replit.clear()
#     print('    A   B   C   D   E   F   G   H   I')
#     print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
#     for r in range (0, 9):
#         print(r,'║',l(r,0,b),'║',l(r,1,b),'║',l(r,2,b),'║',l(r,3,b),'║',l(r,4,b),'║',l(r,5,b),'║',l(r,6,b),'║',l(r,7,b),'║',l(r,8,b),'║')
#         if not r == 8:
#             print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
#     print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')

# #O jogador escolhe uma coordenada.
# #Regra de negocio.
# def choose(b, k, startTime):
#     #Variables 'n stuff.
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
#     #Loop em caso de valor invalido.
#     while True:
#         chosen = input('Escolha os quandrados usando as coordenadas (ex. E4) ou marque uma bomba (ex. mE4): ').lower()
#         #Verifica se é um quadrado valido.
#         if len(chosen) == 3 and chosen[0] == 'm' and chosen[1] in letters and chosen[2] in numbers:
#             c, r = (ord(chosen[1]))-97, int(chosen[2])
#             marker(r, c, k)
#             play(b, k, startTime)
#             break
#         elif len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers: return (ord(chosen[0]))-97, int(chosen[1])
#         else: choose(b, k, startTime)    


# #A maioria da jogabilidade acontece aqui.
# def play(b, k, startTime):
#     #Jogador escolhe um quadrado.
#     c, r = choose(b, k, startTime)
#     #Pega o valor daquela localização.
#     v = l(r, c, b)
#     #Se voce acretar uma bomba, o jogo acaba.
#     if v == '*':
#         printBoard(b)
#         print('Você perdeu!')
#         #Printa o resultado do tempo.
#         print('Tempo: ' + str(round(time.time() - startTime)) + 's')
#         #Oferece para jogar de novo.
#         playAgain = input('Quer jogar de novo? (S/N): ').lower()
#         if playAgain == 's':
#             replit.clear()
#             reset()
#         else:
#             quit()
#     #Coloca um valor ja descoberto na grade.
#     k[r][c] = v
#     #Executa checkZeros() se o valor for 0.
#     if v == 0:
#         checkZeros(k, b, r, c)
#     printBoard(k)
#     #Verifica se voce ganhou.
#     squaresLeft = 0
#     for x in range (0, 9):
#         row = k[x]
#         squaresLeft += row.count(' ')
#         squaresLeft += row.count('⚐')
#     if squaresLeft == 10:
#         printBoard(b)
#         print('Voce ganhou!')
#         #Printa o resultado do tempo.
#         print('Tempo: ' + str(round(time.time() - startTime)) + 's')
#         #Oferece para jogar novamente.
#         playAgain = input('Quer jogar de novo? (S/N): ')
#         playAgain = playAgain.lower()
#         if playAgain == 's':
#             replit.clear()
#             reset()
#         else:
#             quit()
#     #Repete!
#     play(b, k, startTime)

# reset()