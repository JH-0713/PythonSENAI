def IMC(peso1,altura_1):
    altura_2 = altura_1 * altura_1
    Imc1 = peso1 / altura_2
    return Imc1
def valores_n():
    print("Sistema Imc:")
    print("")
    peso1 = float(input("Defina o seu Peso = "))
    print("")
    altura_1 = float(input("Defina a sua Altura = "))
    print("")
    print("")
    print("")
    print("Resultado:")
    input("-")
    print("Seu IMC: ",IMC(peso1,altura_1))
    if IMC(peso1,altura_1) <= 18.5:
        print("Baixo peso")
    elif IMC(peso1,altura_1) <= 24.9:
        print("Peso Normal")
    elif IMC(peso1,altura_1) <= 29.9:
        print("Sobrepeso")
    elif IMC(peso1,altura_1) <= 34.9:
        print("Grau 1 de Obesidade")
    elif IMC(peso1,altura_1) <= 39.9:
        print("Grau 2 de Obesidade")
    elif IMC(peso1,altura_1) >= 40:
        print("Grau 3 de Obesidade")
    else:
        print("THAYS CARLA")
valores_n()


