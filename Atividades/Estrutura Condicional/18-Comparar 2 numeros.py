print("Cite dois numeros")
x1 = float(input("1ºNumero: "))
x2 = float(input("2ºNumero: "))

if x1 > x2:
    print("o Numero",round(x1),"é maior que",round(x2))
elif x1 < x2:
    print("o Numero",round(x2),"é maior que",round(x1))
elif x1 == x2:
    print("Os dois são iguais")
else:
    pass