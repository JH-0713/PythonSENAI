print("cite suas 2 notas para calcular sua media de 0-100")

x1 = float(input("Nota 1: "))
x2 = float(input("Nota 2: "))

if x1 <= 0 and x1 >= 100 and x2 <= 0 and x2 >= 100:
    print("Erro os numeros são de 0 a 100")



    
calc1 = x1 + x2
calc2 = calc1 / 2


if calc2 > 0 and calc2 < 50:
    print("Reprovado",calc2)
elif calc2 >= 50 and calc2 < 70:
    print("Recuperação",calc2)
elif calc2 >= 70 and calc2 <= 100:
    print("Aprovado",calc2)
else:
    pass