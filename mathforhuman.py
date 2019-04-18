def resolve(expressao):
    try:
        valor = str(eval(expressao))
        return valor

    except Exception:
        print("erro")

