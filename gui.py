from tkinter import Tk, Label, Frame, E, Button, X, mainloop
#from tkinter import 


#GUI da calculadora
#Calculadora v2.0.0

class Gui():
    def __init__(self):
        #criando a janela, self.root recebe a classe Tk()
        #definindo o título da janela, seu tamanho, background
        self.root = Tk()
        self.root.title("Calculadora v2.0.0")
        self.root.geometry("678x300+400+100")
        self.root.resizable(0, 0)
        self.root.config(bg="#19171A")
        self.expressao = "teste"

    
    def init(self):
        #inicia o looping para o script seja executado
        #executa as funções para criar os widgets
        self.visor_design()
        self.botoes_num()
        self.botoes_funcao()
        mainloop()


    def visor_design(self):
        self.visor = Label(self.root, text=self.expressao+" "*10, bg="#291C2A", fg="#fff", width=97, height=5, anchor=E, font="Arial 12 bold")
        self.visor.pack()
        self.framebt = Frame(self.root, width=678, height=350)
        self.framebt.pack()
        #etiqueta da calculadora
        Label(self.root, text="@Buizzy - Eliezer de Almeida", bg="#19171A", fg="#FFF").pack(fill=X)


    def botoes_num(self):
        #cria o botoes dentro do FrameBt
        FONT="Arial 8 bold"
        BG = "#181818"
        FG = "#FFF"
        #linha 1
        Button(self.framebt, text="%", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=0, column=0)
        Button(self.framebt, text="√", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=0, column=1)
        Button(self.framebt, text="AC", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=0, column=2)
        Button(self.framebt, text="DEL", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=0, column=3)
        #linha 2
        Button(self.framebt, text="+", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=1, column=0)
        Button(self.framebt, text="7", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=1, column=1)
        Button(self.framebt, text="8", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=1, column=2)
        Button(self.framebt, text="9", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=1, column=3)
        #linha 3
        Button(self.framebt, text="-", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=2, column=0)
        Button(self.framebt, text="4", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=2, column=1)
        Button(self.framebt, text="5", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=2, column=2)
        Button(self.framebt, text="6", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=2, column=3)
        #linha 4
        Button(self.framebt, text="x", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=3, column=0)
        Button(self.framebt, text="1", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=3, column=1)
        Button(self.framebt, text="2", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=3, column=2)
        Button(self.framebt, text="3", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=3, column=3)
        #linha 5
        Button(self.framebt, text="/", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=0)
        Button(self.framebt, text=",", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=1)
        Button(self.framebt, text="0", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=2)
        Button(self.framebt, text="Ans", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=3)


    def botoes_funcao(self):
        #cria os botoes com as funções de cálculos
        FONT = "Arial 8 bold"
        BG = "#181818"
        FG = "#FFF"
        #linha 1
        Button(self.framebt, text="e", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=0, column=4)
        Button(self.framebt, text="π", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=0, column=5)
        Button(self.framebt, text="M", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=0, column=6)
        Button(self.framebt, text="M+", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=0, column=7)
        Button(self.framebt, text="M-", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=0, column=8)
        #linha 2
        Button(self.framebt, text="sin", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=1, column=4)
        Button(self.framebt, text="cos", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=1, column=5)
        Button(self.framebt, text="tan", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=1, column=6)
        Button(self.framebt, text="hyp", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=1, column=7)
        Button(self.framebt, text="n!", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=1, column=8)
        #linha 3
        Button(self.framebt, text="(", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=2, column=4)
        Button(self.framebt, text=")", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=2, column=5)
        Button(self.framebt, text="log", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=2, column=6)
        Button(self.framebt, text="^", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=2, column=7)
        Button(self.framebt, text="|x|", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=2, column=8)
        #linha 4
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=3, column=4)
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=3, column=5)
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=3, column=6)
        Button(self.framebt, text="Deg", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=3, column=7)
        Button(self.framebt, text="Rad", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=3, column=8)
        #linha 5
        Button(self.framebt, text="=", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=4)
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=5)
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=6)
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=7)
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=8)


#ambiente de teste

teste_classe = Gui()
teste_classe.init()