from tkinter import Tk, Label, Frame, E, Button, X, mainloop
#from tkinter import 
import mathforhuman as mh


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
        self.expressao = ""

    
    def init(self):
        #inicia o looping para o script seja executado
        #executa as funções para criar os widgets
        self.visor_design()
        self.botoes_num()
        self.botoes_funcao()
        mainloop()


    def visor_design(self):
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
        Button(self.framebt, text="%", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG, command=lambda:self.atribui_valor("%")).grid(row=0, column=0)
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
        Button(self.framebt, text=",", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG
        , command=lambda:self.atribui_valor(",")).grid(row=4, column=1)
        Button(self.framebt, text="0", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG
        , command=lambda:self.atribui_valor("0")).grid(row=4, column=2)
        Button(self.framebt, text="Ans", width=10, borderwidth=0, height=2, font=FONT, bg=BG, fg=FG).grid(row=4, column=3)


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
            if len(self.expressao) > 0:
                lista = list(self.expressao)
                lista.pop()
                self.expressao = "".join(lista)

        self.visor.config(text=self.expressao+" "*10)



    def memoria(self, bt):
        #pega o valor do visor e salva em um bloco de notas
        if bt == "m":
            memory = open("memory.txt", "r")
            self.expressao += memory.read()

        elif bt == "m+":
            memory = open("memory.txt", "w")
            memory.writelines(self.expressao)
            memory.close()

        else:
            memory = open("memory.txt", "w")
            memory.close()
        
        self.visor.config(text=self.expressao+" "*10)



    def resolver(self):
        resulta = str(mh.resolve(self.expressao))
        print(resulta)
        self.visor.config(text=resulta+" "*10)

    
#ambiente de teste

teste_classe = Gui()
teste_classe.init()