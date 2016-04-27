import tkinter as tk
from VelhaJogo import *
from tkinter import messagebox


XO = ""

class Tabuleiro:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x330+500+200")
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=30, weight=1)
        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)       
        self.i = 1
        self.j = "X"
        self.p1 = 0
        self.p2 = 0
#        self.textp1 = "P1: {0}".format(self.p1), fg="blue"
#        self.textp2 = "P2: {0}".format(self.p2), fg="red"
        
         
            
        self.criar_botoes()
        
#        self.label2 = tk.Label(self.window)
#        self.label2.configure(text="{0} | {1}".format(self.textp1, self.textp2))
#        self.label2.grid(row=3, column=2)
        
    def criar_botoes(self):
        
        def botao(x, y):
            botao = tk.Button(self.window)
            botao.configure(command=lambda i=x, j=y: self.jogada(i,j))
            botao.configure(text=XO, font='Arial 72')
            botao.grid(row=x, column=y, sticky="nsew") 
        
        self.botoes = []
        for i in range(3):
            linha_botoes = []
            for j in range(3):
                linha_botoes.append(botao(i,j))
            self.botoes.append(linha_botoes)
                        
        self.label = tk.Label(self.window)
        self.label.configure(text="Próxima jogada: {0}".format(self.j))
        self.label.grid(row=3, column=0)
      
    
    def jogada(self, x, y):
        if self.i % 2 == 0:
            XO = "O"
            f = "red"
        else:
            XO = "X"
            f = "blue"
        botao = tk.Button(self.window)
        botao.configure(text=XO, font='Arial 72', fg=f)
        botao.grid(row=x, column=y, sticky="nsew")
        
        # LABEL É O SÍMBOLO OPOSTO AO DO JOGO
        if XO == "X":
            self.j = "O"
        else:
            self.j = "X"
        self.label.configure(text="Próxima jogada: {0}".format(self.j))
        
        self.i += 1
        
        J.recebe_jogada(x, y)
        
        J.verificar()
        
        if J.termino == 1:
            self.acabo()
            
        soma = 0
        for i in J.empat:
            soma += i
        if soma == 45:
            self.empate()
            
        if J.conta_jogadas == 9:
            self.empate()

        
        
        
    def acabo(self):
        
        if self.j == "X":
            self.j = "O"
        else:
            self.j = "X"
        
        if messagebox.askyesno(message="Acabooooooo! O jogador {0} Ganhou!\nDeseja reiniciar?".format(self.j)) == True:
            self.reiniciar()
        else:
            quit()
    
    def empate(self):
         
        if messagebox.askyesno(message="Empatou! Seus ruim!\nDeseja reiniciar?") == True:
            self.reiniciar()
        else:
            quit()
        
    def reiniciar(self):
        
        self.criar_botoes()

        J.tabuleiro = [[0,0,0], [0,0,0], [0,0,0]]
        
        J.diagonal = []
        J.horizontal = []
        J.vertical = []
        
        J.termino = 0
        
        J.conta_jogadas = 0
        
        self.i = 1
        self.j = "X"
        self.label.configure(text="Próxima jogada: {0}".format(self.j))
        
        

    def iniciar(self):
        self.window.mainloop()
    
J = Jogao()

app = Tabuleiro()
app.iniciar()