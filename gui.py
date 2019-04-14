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
        self.expressao = "teste"

    
    def init(self):
        #inicia o looping para o script seja executado
        #executa as funções para criar os widgets
        self.visor_design()
        self.botoes_num()
        mainloop()


    def visor_design(self):
        self.visor = Label(self.root, text=self.expressao+" "*10, bg="#291C2A", fg="#fff", width=97, height=5, anchor=E, font="Arial 12 bold")
        self.visor.pack()
        self.framebt = Frame(self.root, width=678, height=350)
        self.framebt.pack()


    def botoes_num(self):
        #cria o botoes dentro do FrameBt
        FONT="Arial 8 bold"
        #linha 1
        Button(self.framebt, text="%", width=10, borderwidth=0, height=2, font=FONT).grid(row=0, column=0)
        Button(self.framebt, text="√", width=10, borderwidth=0, height=2, font=FONT).grid(row=0, column=1)
        Button(self.framebt, text="AC", width=10, borderwidth=0, height=2, font=FONT).grid(row=0, column=2)
        Button(self.framebt, text="DEL", width=10, borderwidth=0, height=2, font=FONT).grid(row=0, column=3)
        #linha 2
        Button(self.framebt, text="+", width=10, borderwidth=0, height=2, font=FONT).grid(row=1, column=0)
        Button(self.framebt, text="7", width=10, borderwidth=0, height=2, font=FONT).grid(row=1, column=1)
        Button(self.framebt, text="8", width=10, borderwidth=0, height=2, font=FONT).grid(row=1, column=2)
        Button(self.framebt, text="9", width=10, borderwidth=0, height=2, font=FONT).grid(row=1, column=3)
        #linha 3
        Button(self.framebt, text="-", width=10, borderwidth=0, height=2, font=FONT).grid(row=2, column=0)
        Button(self.framebt, text="4", width=10, borderwidth=0, height=2, font=FONT).grid(row=2, column=1)
        Button(self.framebt, text="5", width=10, borderwidth=0, height=2, font=FONT).grid(row=2, column=2)
        Button(self.framebt, text="6", width=10, borderwidth=0, height=2, font=FONT).grid(row=2, column=3)
        #linha 4
        Button(self.framebt, text="x", width=10, borderwidth=0, height=2, font=FONT).grid(row=3, column=0)
        Button(self.framebt, text="1", width=10, borderwidth=0, height=2, font=FONT).grid(row=3, column=1)
        Button(self.framebt, text="2", width=10, borderwidth=0, height=2, font=FONT).grid(row=3, column=2)
        Button(self.framebt, text="3", width=10, borderwidth=0, height=2, font=FONT).grid(row=3, column=3)
        #linha 5
        Button(self.framebt, text="/", width=10, borderwidth=0, height=2, font=FONT).grid(row=4, column=0)
        Button(self.framebt, text=",", width=10, borderwidth=0, height=2, font=FONT).grid(row=4, column=1)
        Button(self.framebt, text="0", width=10, borderwidth=0, height=2, font=FONT).grid(row=4, column=2)
        Button(self.framebt, text="Ans", width=10, borderwidth=0, height=2, font=FONT).grid(row=4, column=3)


    def botoes_funcao(self):
        pass


#ambiente de teste

teste_classe = Gui()
teste_classe.init()