
class Jogao:
    def __init__(self):
        
        self.tabuleiro = [[0,0,0], [0,0,0], [0,0,0]]
        self.horizontal = []
        self.vertical = []
        self.diagonal = []
        self.empat = []
        self.termino = 0
        self.jogador = 1
        self.conta_jogadas = 0
        
    def recebe_jogada (self, linha, coluna):
        self.tabuleiro[linha][coluna] = self.jogador
        if self.jogador == 1:
            self.jogador = 10
        else:
            self.jogador = 1
        
        self.conta_jogadas += 1
            
    def verificar(self):
        for i in range(3):
            self.horizontal.append(self.tabuleiro[i][0] + self.tabuleiro[i][1] + self.tabuleiro[i][2])
            self.vertical.append(self.tabuleiro[0][i] + self.tabuleiro[1][i] + self.tabuleiro[2][i])
        self.diagonal.append(self.tabuleiro[0][0] + self.tabuleiro[1][1] + self.tabuleiro[2][2])    
        self.diagonal.append(self.tabuleiro[2][0] + self.tabuleiro[1][1] + self.tabuleiro[0][2])
        
        for i in self.horizontal:
            if i == 3 or i == 30:
                self.termino = 1
        for i in self.vertical:
            if i == 3 or i == 30:
                self.termino = 1
        for i in self.diagonal:
            if i == 3 or i == 30:
                self.termino = 1
        

        else:
            self.diagonal = []
            self.horizontal = []
            self.vertical = []
            
        for i in range(3):
            for j in range(3):
                self.empat.append(self.tabuleiro[i][j])
                
        
        
            

        