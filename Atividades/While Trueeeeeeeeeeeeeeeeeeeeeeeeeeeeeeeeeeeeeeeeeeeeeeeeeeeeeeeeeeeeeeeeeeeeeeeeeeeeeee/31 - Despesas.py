quant = 0
valores = 0

while True:
    print("Adicione um valor para calcular a despesa")
    print("")
    print("[0] Adicionar valor da despesas")
    print("[1] Ver a quantidade e valor de Despesas")
    print("[2] Sair")
    print("")
    x1 = input("Escolha o que fazer: ")
    print("")
    if x1 == "0":
        print("")
        valor1 = int(input("digite o valor da despesa: "))
        valores = valores + valor1
        print(valor1)
    elif x1 == "1":
        print("Valor total:",valores)
        print("")
        quant += 1
        print("quantidade: ",quant)
        print("")
    elif x1 == "2":
        print("Tchau")
        print("")
        break
    
    else:
        pass
