def verificar(x1):
    if x1 >= 0:
        x1 = True
        print("Positivo")
        print("")
        return x1

    elif x1 <= -1:
        x1 = False
        print("Negativo")
        print("")
        return x1
    
print("")
print("Escolha Qualquer Numero:")
print("")
x1 = int(input("> "))
print("")
print(verificar(x1))
