from tkinter import Tk, Label, Frame, E, Button, X, mainloop, W
#from tkinter import 
import mathforhuman as mh
from sys import platform


#GUI da calculadora
#Calculadora v2.0.0

class Gui():
    def __init__(self):
        #criando a janela, self.root recebe a classe Tk()
        #definindo o título da janela, seu tamanho, background
        self.root = Tk()
        self.root.title("Calculadora v2.0.0")
        #self.root.geometry("678x315+400+100") para windows
        self.root.geometry("770x320" if platform == "linux" else "678x315+400+100")
        self.root.resizable(0, 0)
        self.root.config(bg="#19171A")
        #self.root.iconbitmap("./files/favicon1.ico")
        self.expressao = ""
        self.ans = ""
        self.root.bind("<Return>", self.resolver)
        self.root.bind("<Key>", self.key_atribui)
        self.mode_text = " "*5+"Deg"

    
    def init(self):
        #inicia o looping para o script seja executado
        #executa as funções para criar os widgets
        self.visor_design()
        self.botoes_num()
        self.botoes_funcao()
        mainloop()


    def visor_design(self):
        self.mode = Label(self.root, text=self.mode_text,  fg="#fff", bg="#291C2A", width=97, height=1, anchor=W, font="Arial 8")
        self.mode.pack(fill=X)
        self.visor = Label(self.root, text=self.expressao+" "*10, bg="#291C2A", fg="#fff", width=97, height=5, anchor=E, font="Arial 12")
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
        Button(self.framebt, text="%", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("")).grid(row=0, column=0)
        Button(self.framebt, text="√", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("√")).grid(row=0, column=1)
        Button(self.framebt, text="AC", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.apagar("ac")).grid(row=0, column=2)
        Button(self.framebt, text="DEL", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.apagar("del")).grid(row=0, column=3)
        #linha 2
        Button(self.framebt, text="+", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("+")).grid(row=1, column=0)
        Button(self.framebt, text="7", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("7")).grid(row=1, column=1)
        Button(self.framebt, text="8", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("8")).grid(row=1, column=2)
        Button(self.framebt, text="9", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("9")).grid(row=1, column=3)
        #linha 3
        Button(self.framebt, text="-", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("-")).grid(row=2, column=0)
        Button(self.framebt, text="4", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("4")).grid(row=2, column=1)
        Button(self.framebt, text="5", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG
        , command=lambda:self.atribui_valor("5")).grid(row=2, column=2)
        Button(self.framebt, text="6", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("6")).grid(row=2, column=3)
        #linha 4
        Button(self.framebt, text="*", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("*")).grid(row=3, column=0)
        Button(self.framebt, text="1", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG
        , command=lambda:self.atribui_valor("1")).grid(row=3, column=1)
        Button(self.framebt, text="2", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("2")).grid(row=3, column=2)
        Button(self.framebt, text="3", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("3")).grid(row=3, column=3)
        #linha 5
        Button(self.framebt, text="/", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG
        , command=lambda:self.atribui_valor("/")).grid(row=4, column=0)
        Button(self.framebt, text=".", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG
        , command=lambda:self.atribui_valor(".")).grid(row=4, column=1)
        Button(self.framebt, text="0", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG
        , command=lambda:self.atribui_valor("0")).grid(row=4, column=2)
        Button(self.framebt, text="Ans", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.visor.config(text=self.expressao+self.ans+" "*10)).grid(row=4, column=3)


    def botoes_funcao(self):
        #cria os botoes com as funções de cálculos
        FONT = "Arial 8 bold"
        BG = "#181818"
        FG = "#FFF"
        #linha 1
        Button(self.framebt, text="e", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("e")).grid(row=0, column=4)
        Button(self.framebt, text="π", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("π")).grid(row=0, column=5)
        Button(self.framebt, text="M", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.memoria("m")).grid(row=0, column=6)
        Button(self.framebt, text="M+", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.memoria("m+")).grid(row=0, column=7)
        Button(self.framebt, text="M-", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.memoria("m-")).grid(row=0, column=8)
        #linha 2
        Button(self.framebt, text="sin", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("sin(")).grid(row=1, column=4)
        Button(self.framebt, text="cos", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("cos(")).grid(row=1, column=5)
        Button(self.framebt, text="tan", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("tan(")).grid(row=1, column=6)
        Button(self.framebt, text="hyp", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=1, column=7)
        Button(self.framebt, text="n!", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG,command=lambda:self.atribui_valor("!")).grid(row=1, column=8)
        #linha 3
        Button(self.framebt, text="(", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("(")).grid(row=2, column=4)
        Button(self.framebt, text=")", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor(")")).grid(row=2, column=5)
        Button(self.framebt, text="log", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=2, column=6)
        Button(self.framebt, text="^", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("^(")).grid(row=2, column=7)
        Button(self.framebt, text="|x|", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=2, column=8)
        #linha 4
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=3, column=4)
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=3, column=5)
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=3, column=6)
        Button(self.framebt, text="Deg", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.altera_mode("Deg")).grid(row=3, column=7)
        Button(self.framebt, text="Rad", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.altera_mode("Rad")).grid(row=3, column=8)
        #linha 5
        Button(self.framebt, text="=", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.resolver()).grid(row=4, column=4)
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=5)
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=6)
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=7)
        Button(self.framebt, text="empty", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=8)


    def atribui_valor(self, valor):
        #esta funcao é executada e atribui valor a self.expressao
        #também atualiza a label self.visor
        if len(self.expressao) < 41:
            self.expressao += str(valor)
            self.visor.config(text=self.expressao+" "*10)
        
        else:
            print("Limite atingido")


    def apagar(self, comando):
        #essa função apaga o valor do visor
        if comando == "ac":
            self.expressao = ""

        elif comando == "del":
            #aqui serve para apagar as funcoes
            a = self.expressao[-1:-5:-1]#pega os ultimos valores a fim de verificar se é uma funcao
            a = a[::-1]#desinverte os valores
            #verifica a existencia dos valores na string, para evitar que delete valores que nao sao funcoes
            #a partir daqui executa o algoritmo para deletar a funcao
            if a in "sin(cos(tan(" and len(self.expressao) > 0:
                b = list(self.expressao)
                for c in range(1, 5):
                    b.pop(-1)

                self.expressao = "".join(b)

            elif len(self.expressao) > 0:
                lista = list(self.expressao)
                lista.pop()
                self.expressao = "".join(lista)

        self.visor.config(text=self.expressao+" "*10)



    def memoria(self, bt):
        #pega o valor do visor e salva em um bloco de notas
        if bt == "m":
            memory = open(".\\files\\memory.txt", "r")
            self.expressao += memory.read()

        elif bt == "m+":
            memory = open("memory.txt", "w")
            memory.writelines(self.expressao)
            memory.close()

        else:
            memory = open("memory.txt", "w")
            memory.close()
        
        self.visor.config(text=self.expressao+" "*10)



    def resolver(self, event=""):
        resulta = str(mh.resolve(self.expressao, self.mode_text))
        self.ans = resulta
        self.expressao = resulta
        self.visor.config(text=self.expressao+" "*10)


    def key_atribui(self, event):
        #usando um bind ele pega o event  de uma key e verifica se é um número
        key = event.char
        if key in "1234567890":
            self.atribui_valor(key)

        elif event.keycode == 22:
            self.apagar("del")


    def altera_mode(self, event):
        #altera mode que contém informações como se é grau ou radianos
        if event == "Deg" or event == "Rad":
            self.mode_text = self.mode_text.replace(self.mode_text[5:8:1], event)

        self.mode.config(text=self.mode_text)

    
#ambiente de teste

teste_classe = Gui()
teste_classe.init()