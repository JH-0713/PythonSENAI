print("Calculo de IMC")
print("Fórmula: peso(kg) / (altura * altura) em (m²)")
print()
peso1 = float(input("Defina o seu Peso = "))
print()
altura_1 = float(input("Defina a sua Altura = "))
print()

altura_2 = altura_1 * altura_1
calc1 = peso1 / altura_2
if calc1 <= 18.5:
    print(round(calc1,3),"= Baixo peso")
elif calc1 <= 24.9:
    print(round(calc1,3),"Peso Normal")
elif calc1 <= 29.9:
    print(round(calc1,3),"Sobrepeso")
elif calc1 <= 34.9:
    print(round(calc1,3),"Grau 1 de Obesidade")
elif calc1 <= 39.9:
    print(round(calc1,3),"Grau 2 de Obesidade")
elif calc1 >= 40:
    print(round(calc1,3),"Grau 3 de Obesidade")
else:
    print("Thais Carla")