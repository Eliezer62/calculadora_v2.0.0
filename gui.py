from tkinter import *


#GUI da calculadora
#Calculadora v2.0.0

class Gui():
    def __init__(self):
        #criando a janela, self.root recebe a classe Tk()
        #definindo o título da janela, seu tamanho, background
        self.root = Tk()
        self.root.title("Calculadora v2.0.0")
        self.root.geometry("678x425+400+100")
        self.root.resizable(0, 0)
        self.root.config(bg="#19171A")

    
    def init(self):
        #inicia o looping para o script seja executado
        mainloop()


#ambiente de teste

teste_classe = Gui()
teste_classe.init()