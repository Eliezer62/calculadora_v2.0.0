def resolve(expressao):
    try:
        valor = str(eval(expressao))
        print(valor)

    except Exception:
        print("erro")

