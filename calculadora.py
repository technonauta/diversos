
"""

Calculadora While


"""

while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador [+-*/:] ")

    numeros_validos = None #flag 01
    num_float_1 = 0
    num_float_2 = 0

    ###validando números

    try:
        num_float_1 = float(numero_1)
        num_float_2 = float(numero_2)
        numeros_validos = True

    except: #ma prática, mas por enqto passa
        numeros_validos = None
    
    if numeros_validos is None:
        print("Um ou ambos números digitados são inválidos.")
        continue #flag 01
    
    ###validando operadores

    operador_ok = "+-/*"

    if operador not in operador_ok:
        print("Operador inválido!")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    ### calculadora
    print("Realizando sua conta. Confira resultado abaixo:)")

    if operador == "+":
        print(f"{num_float_1} + {num_float_2}=", num_float_1+num_float_2)
    elif operador == "-":
        print(f"{num_float_1} - {num_float_2}=", num_float_1-num_float_2)
    elif operador == "*":
        print(f"{num_float_1} * {num_float_2}=", num_float_1*num_float_2)
    elif operador == "/":
        print(f"{num_float_1} / {num_float_2}=", num_float_1/num_float_2)
    else:
        print("Você não deveria estar vendo esta mensagem!")

    ### sair da calculadora
    sair = input("Quer sair? [s]im: ").lower().startswith("s")

    if sair is True:
        break