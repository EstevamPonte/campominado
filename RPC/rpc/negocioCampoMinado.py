import random, time, copy

class CampoMinado:
    
    def __init__(self, num_bomb):
        self.num_bomb = num_bomb
        self.lista_bombas = []
        self.__gera_lista_bombas()
        self.inicializar()

    def __gera_lista_bombas(self):
        
        while len(self.lista_bombas) < self.num_bomb:
            linha = random.randint(0, 8)
            coluna = random.randint(0, 8)
            if (linha,coluna) not in self.lista_bombas:
                self.lista_bombas.append((linha,coluna))        

    def __get_lista_bomb(self):
        return self.lista_bombas
        self.lista_bombas.clear()

    def inicializar(self):

        self.__gera_lista_bombas()

        #A solução da grade.
        self.gabarito = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.__espalhar_bombas_gabarito()
        self.__calcular_bombas_posicao_gabarito()
        self.__print_gabarito()

    def __print_gabarito(self):
        for linha in self.gabarito:
            print(linha)

    def __espalhar_bombas_gabarito(self):
        for item in self.__get_lista_bomb():
            self.gabarito[item[0]][item[1]] = '*'

    def __calcular_bombas_posicao_gabarito(self):
        for linha in range (0, 9):
            for coluna in range (0, 9):
                value = self.filtro(linha, coluna)
                # value = l(r, c, b)
                if value == '*':
                    self.__updateValues(linha, coluna)

    def __updateValues(self, linha, coluna):
        #Linha de cima.
        if linha-1 > -1:
            r = self.gabarito[linha-1]
            
            if coluna-1 > -1:
                if not r[coluna-1] == '*':
                    r[coluna-1] += 1

            if not r[coluna] == '*':
                r[coluna] += 1

            if 9 > coluna+1:
                if not r[coluna+1] == '*':
                    r[coluna+1] += 1

        #Mesma linha (A do meio).    
        r = self.gabarito[linha]

        if coluna-1 > -1:
            if not r[coluna-1] == '*':
                r[coluna-1] += 1

        if 9 > coluna+1:
            if not r[coluna+1] == '*':
                r[coluna+1] += 1

        #Linha de baixo.
        if 9 > linha+1:
            r = self.gabarito[linha+1]

            if coluna-1 > -1:
                if not r[coluna-1] == '*':
                    r[coluna-1] += 1

            if not r[coluna] == '*':
                r[coluna] += 1

            if 9 > coluna+1:
                if not r[coluna+1] == '*':
                    r[coluna+1] += 1
    
    def filtro(self, linha, coluna):
        return self.gabarito[linha][coluna]
    
    
    