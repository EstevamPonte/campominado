import random, time, copy




class CampoMinado:
    
    def __init__(self, num_bomb):
        self.lista_bombas = []
        self.__gera_lista_bombas(num_bomb)

    def __gera_lista_bombas(self, num_bomb):
        
        while len(self.lista_bombas) < num_bomb:
            r = random.randint(0, 8)
            c = random.randint(0, 8)
            if (r,c) not in self.lista_bombas:
                self.lista_bombas.append((r,c))        

    def get_lista_bomb(self):
        return self.lista_bombas
        self.lista_bombas.clear()

    def l(self, r, c, b):
        return b[r][c]

    def updateValues(self, rn, c, b):
        #Linha de cima.
        if rn-1 > -1:
            r = b[rn-1]
            
            if c-1 > -1:
                if not r[c-1] == '*':
                    r[c-1] += 1

            if not r[c] == '*':
                r[c] += 1

            if 9 > c+1:
                if not r[c+1] == '*':
                    r[c+1] += 1

        #Mesma linha (A do meio).    
        r = b[rn]

        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1

        #Linha de baixo.
        if 9 > rn+1:
            r = b[rn+1]

            if c-1 > -1:
                if not r[c-1] == '*':
                    r[c-1] += 1

            if not r[c] == '*':
                r[c] += 1

            if 9 > c+1:
                if not r[c+1] == '*':
                    r[c+1] += 1
    
    def zeroProcedure(self, r, c, k, b):
        #Linha de cima
        if r-1 > -1:
            row = k[r-1]
            if c-1 > -1: row[c-1] = self.l(r-1, c-1, b)
            row[c] = self.l(r-1, c, b)
            if 9 > c+1: row[c+1] = self.l(r-1, c+1, b)

        #Mesma linha
        row = k[r]
        if c-1 > -1: row[c-1] = self.l(r, c-1, b)
        if 9 > c+1: row[c+1] = self.l(r, c+1, b)

        #Linha de baixo
        if 9 > r+1:
            row = k[r+1]
            if c-1 > -1: row[c-1] = self.l(r+1, c-1, b)
            row[c] = self.l(r+1, c, b)
            if 9 > c+1: row[c+1] = self.l(r+1, c+1, b)
    def checkZeros(self, k, b, r, c):
        oldGrid = copy.deepcopy(k)
        self.zeroProcedure(r, c, k, b)
        if oldGrid == k:
            return
        while True:
            oldGrid = copy.deepcopy(k)
            for x in range (9):
                for y in range (9):
                    if self.l(x, y, k) == 0:
                        self.zeroProcedure(x, y, k, b)
            if oldGrid == k:
                return
    
    