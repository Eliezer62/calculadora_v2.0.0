from math import *
def constante(exp):
    #esta funcao substitui as funcoes em numeros para utilizar no calculo
    exp = exp
    if "π" in exp:
        exp = exp.replace("π", str(pi))

    if "e" in exp:
        exp = exp.replace("e", str(e))

    return exp
def resolve(expressao):
    try:
        expressao = expressao
        expressao = constante(expressao)
        valor = str(eval(expressao))
        return valor

    except Exception:
        print("erro")

