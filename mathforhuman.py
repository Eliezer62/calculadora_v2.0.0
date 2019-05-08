from math import pi, e, factorial, sqrt
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

        lista_exp.insert(pos,str(sqrt(float(value)))) #calcula e insere a fatorial do value
        exp = "".join(lista_exp) #atribui os resultados à expressão

    return exp #retorna a expressão já com os resultados calculados


def resolve(expressao, mode):
    try:
        expressao = expressao
        expressao = constante(expressao)
        expressao = fatorial(expressao)
        expressao = raiz(expressao)
        valor = str(eval(expressao))
        return valor

    except Exception:
        print("erro")

