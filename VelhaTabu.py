# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:01:31 2016

@author: Guilherme Moraes
"""

import tkinter as tk



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
        
        def botao(x, y):
            botao = tk.Button(self.window)
            botao.configure(command=lambda i=x, j=y: self.jogada(i,j))
            botao.configure(text='X', font='Arial 72')
            botao.grid(row=x, column=y, sticky="nsew")
            

            
        self.botoes = []
        for i in range(3):
            linha_botoes = []
            for j in range(3):
                linha_botoes.append(botao(i,j))
            self.botoes.append(linha_botoes)
            
        label = tk.Label(self.window)
        label.configure(text="Next player's turn: ")
        label.grid(row=3, column=0)
        

    def iniciar(self):
        self.window.mainloop()

#    def jogada(self, row, column):
        

app = Tabuleiro()
app.iniciar()






















