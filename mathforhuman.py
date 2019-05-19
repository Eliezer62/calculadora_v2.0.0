from math import pi, e, factorial, sqrt
import math as mt
def constante(exp):
    #esta funcao substitui as funcoes em numeros para utilizar no calculo
    exp = exp
    if "π" in exp:
        exp = exp.replace("π", str(pi))

    if "e" in exp:
        exp = exp.replace("e", str(e))

    return exp


def fatorial(exp):
    exp = str(exp)
    while "!" in exp:
        #vai verificar a existencia de fatorial e repetir os processos para cada
        local = exp.find("!")
        #vai verificar o local da primeira fatorial
        lista_exp = list(exp)
        #transforma a exp em uma lista para ser modificada.
        lista_exp.pop(local)
        #vai apagar a fatorial
        c = 1 #define o contador
        value = "" #define a variável temporária que vai sofrer modificações
        while True:
            #aqui vai pegar os números e armazená-los em value para serem calculados
            try:
                #vai ser tratado erros como os de range
                if lista_exp[local-c].isnumeric() and local-c > -1:
                    #verifica se o elemento da lista é um número e se corresponde ao range da esquerda pra a direita
                    value += str(lista_exp[local-c]) #caso verdade ele é atribuido ao value para ser calculado a fatorial
                    lista_exp.pop(local-c) #o número é apagado para ser substituído depois pelo valor da fatorial
                    pos = local-c #é salvo a posição do último número para ser innserido nesse espaço
                    c += 1 #aqui soma o contador

                else:
                    break
                    #caso não seja um número ou esteja voltando a lista, ele encerra

            except Exception:
                #caso exista um erro, ele para a executação
                break

        value = value[::-1] #inversão do value
        lista_exp.insert(pos,str(factorial(float(value)))) #calcula e insere a fatorial do value
        exp = "".join(lista_exp) #atribui os resultados à expressão

    return exp #retorna a expressão já com os resultados calculados


def raiz(exp):
    #esta funcao resolve raizes
    exp = str(exp)
    while "√" in exp:
        #verifica a existencia de raizes e faz um looping para repetir o processo para cada raiz.
        local = exp.find("√")
        #vai verificar o local da primeira raiz
        lista_exp = list(exp)
        #transforma a exp em uma lista para ser modificada.
        lista_exp.pop(local)
        #vai apagar a raiz      
        value = "" #define a variável temporária que vai sofrer modificações
        #aqui detecta o fator de multiplicação
        c = 1 #cria o contador
        tmp = "" #cria a var tmp que vai conter o fator
        while True: #cria um looping para pegaar todos os números
            try:
                if lista_exp[local-c].isnumeric() and local-c > -1:#verifica se o item da lista é um número e sua posição
                    tmp += lista_exp[local-c] #atribui a tmp
                    lista_exp[local-c] = ""#aqui vai substituir o valor, mas não vai mudar as casas

                else:
                    break #para quando não é um número ou está voltando

            except Exception: #interrope caso haja um erro
                break

        #aqui verifica se tmp tem valor senão é atribuído 1 para multiplicar
        if tmp != "":
            tmp = float(tmp[::-1]) #inverte a var

        else:
            tmp = 1

        while True:
            #aqui vai pegar os números e armazená-los em value para serem calculados
            try:
                #vai ser tratado erros como os de range
                if lista_exp[local].isnumeric():
                    #verifica se o elemento da lista é um número e se corresponde ao range da esquerda pra a direita
                    value += str(lista_exp[local]) #caso verdade ele é atribuido ao value para ser calculado a fatorial
                    lista_exp.pop(local) #o número é apagado para ser substituído depois pelo valor da fatorial
                    pos = local #é salvo a posição do último número para ser innserido nesse espaço

                else:
                    break
                    #caso não seja um número ou esteja voltando a lista, ele encerra

            except Exception:
                #caso exista um erro, ele para a executação
                break

        value = sqrt(float(value))
        lista_exp.insert(pos,str(tmp*value)) #calcula e insere a fatorial do value
        exp = "".join(lista_exp) #atribui os resultados à expressão

    return exp #retorna a expressão já com os resultados calculados


#EXPRESSÕES TRIGONOMÉTRICAS

def sin(val):
    mode = globals()["mode"] #busca mode que foi definida em resolve()
    #verifica se está em graus, caso contrário, apenas calcula o seno
    if mode[5:8] == "Deg": 
        tmp = mt.sin(mt.radians(float(val))) #calcula o sin
        tmp = "{:.10f}".format(tmp) #arredonda o valor para melhor compreensão

    else:
        tmp = sin(val)
        tmp = f"{tmp:.10f}"

    return float(tmp) #retorna tmp em float para retirar o zeros das casas decimais.


def cos(val):
    mode = globals()["mode"] #busca mode que foi definida em resolve()
    #verifica se está em graus, caso contrário, apenas calcula o cosseno
    if mode[5:8] == "Deg": 
        tmp = mt.cos(mt.radians(float(val))) #calcula o cos
        tmp = "{:.10f}".format(tmp) #arredonda o valor para melhor compreensão

    else:
        tmp = cos(val)
        tmp = f"{tmp:.10f}"

    return float(tmp) #retorna tmp em float para retirar o zeros das casas decimais.


def tan(val):
    mode = globals()["mode"] #busca mode que foi definida em resolve()
    #verifica se está em graus, caso contrário, apenas calcula o cosseno
    if mode[5:8] == "Deg": 
        tmp = mt.tan(mt.radians(float(val))) #calcula o cos
        tmp = "{:.10f}".format(tmp) #arredonda o valor para melhor compreensão

    else:
        tmp = tan(val)
        tmp = f"{tmp:.10f}"

    return float(tmp) #retorna tmp em float para retirar o zeros das casas decimais.


def resolve(expressao, mode):
    #define mode como uma variável global para ser usada nas expressões trignométricas
    globals()["mode"] = mode
    mode = mode
    try:
        expressao = expressao
        expressao = constante(expressao)
        expressao = fatorial(expressao)
        expressao = raiz(expressao)
        valor = str(eval(expressao))
        return valor

    except Exception:
        print("erro")

