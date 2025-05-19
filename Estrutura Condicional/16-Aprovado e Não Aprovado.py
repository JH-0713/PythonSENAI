print("Coloque suas duas notas aqui")
x1 =  float(input("1º Nota: "))
x2 =  float(input("2º Nota: "))

calc1 =  x1 + x2
calc2 = calc1 / 2

if calc2 >= 70:
    print("Nota: ",calc2)
    print("Aprovado")
elif calc2 <= 69:
    print("Nota: ",calc2)
    print("Reprovado")
else:
    pass