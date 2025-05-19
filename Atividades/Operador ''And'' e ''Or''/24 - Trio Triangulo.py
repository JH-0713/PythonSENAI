print("Defina o valor de cada lado do Triangulo")
print("")

l1 = float(input("Lado 1: "))
print("")
l2 = float(input("Lado 2: "))
print("")
l3 = float(input("Lado 3: "))
print("")

if l1 == l2 and l1 == l3 and l2 == l3:
    print("Triangulo Equilátero")
    print("")
elif l1 != l2 and l1 == l3 or l1 == l2 and l1 != l3 or l2 == l3 and l2 != l1:
    print("Triangulo Isósceles")
    print("")
elif l1 != l2 and l2 != l3 and l1 != l3:
    print("Triangulo Escaleno")
    print("")