# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:01:31 2016

@author: Guilherme Moraes
"""

import tkinter as tk

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
        
        def botao(x, y):
            botao = tk.Button(self.window)
            botao.configure(command=lambda i=x, j=y: self.jogada(i,j))
            botao.configure(text=XO, font='Arial 72',)
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
        botao.configure(text=XO, font='Arial 72',fg=f)
        botao.grid(row=x, column=y, sticky="nsew")
        
        # LABEL É O SÍMBOLO OPOSTO AO DO JOGO
        if XO == "X":
            self.j = "O"
        else:
            self.j = "X"
        self.label.configure(text="Próxima jogada: {0}".format(self.j))
        
        self.i += 1
         

    def iniciar(self):
        self.window.mainloop()
    

app = Tabuleiro()
app.iniciar()























