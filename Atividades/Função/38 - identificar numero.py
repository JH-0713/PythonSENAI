def verificar(esc1):
    if esc1 == 1:
        print("Escolha Qualquer Numero:")
        print("")
        x1 = int(input(">"))
        print("")
        if x1 <= -1:
            x1 = False
            return x1
        elif x1 >= 0:
            x1 = True
            return x1
    elif esc1 == 2:
        print("Escolha Qualquer Numero:")
        print("")
        x1 = int(input(">"))
        print("")
        if x1 <= -1:
            x1 = True
            return x1
        elif x1 >= 0:
            x1 = False
            return x1
    else:
        pass
print("")
print("Escolha o Formato do seu Numero:")
print("[1] Positivo")
print("[2] Negativo")
print("")
esc1 = int(input(">"))
print("")
print(verificar(esc1))

            
