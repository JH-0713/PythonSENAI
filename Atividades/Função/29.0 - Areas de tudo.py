def area_c(lado_1):
    pi = 3.14
    lado_2 = lado_1 * lado_1
    area_c1 = lado_2 * pi
    return area_c1
    
def area_q(lado_1):
    area_q1 = lado_1 * lado_1
    return area_q1

    
def area_r(lado_1,h1):
    area_r1 = lado_1 * h1
    return area_r1

def area_te(lado_1):
    tri_e1 = lado_1 * lado_1
    raiz_1 = 3**0.5
    tri_e2 = tri_e1 * raiz_1
    area_te1 = tri_e2 / 4
    return area_te1
    
def area_h(lado_1):
    tri_e1 = lado_1 * lado_1
    raiz_1 = 3**0.5
    tri_e2 = tri_e1 * raiz_1
    area_te1 = tri_e2 / 4
    area_h1 = 6 * area_te1
    return area_h1
def peri_c(lado_1):
    pi = 3.14
    pc1 = 2 * pi * lado_1
    return pc1

def peri_q(lado_1):
    pq1 = 4 * lado_1
    return pq1

def peri_r(b1,h1):
    pr1 = b1 + h1
    pr2 = pr1 * 2
    return pr2

def peri_te(lado_1):
    pte1 = lado_1 * 3
    return pte1

def peri_h(lado_1):
    ph1 = lado_1 * 6
    return ph1
    
def exibir_a():
    print("Defina dois numeros para efetuar contas basicas")
    print("")
    print("[1] Area do Circulo")
    print("[2] Area do Quadrado")
    print("[3] Area do Retangulo")
    print("[4] Area do Triangulo Equilatero")
    print("[5] Area do Hexagono")
    print("[6] Perimetro")
    print("")
    num1 = int(input("Numero de [1-6]: "))
    print("")
    if num1 == 1:
        lado_1 = int(input("Valor do Lado: "))
        print("")
        print("Area do Circulo:",area_c(lado_1))
        print("")
    elif num1 == 2:
        lado_1 = int(input("Valor do Lado: "))
        print("")
        print("Area do Quadrado:",area_q(lado_1))
        print("")
    elif num1 == 3:
        lado_1 = int(input("Valor do Lado: "))
        print("")
        h1 = int(input("Valor Altura: "))
        print("")
        print("Area do Retangulo:",area_r(lado_1,h1))
        print("")
    elif num1 == 4:
        lado_1 = int(input("Valor do Lado: "))
        print("")
        print("Area do Triangulo Equilatero:",area_te(lado_1))
        print("")
        print("Area do Hexagono:",area_h(lado_1))
        print("")
    elif num1 == 5:
        lado_1 = int(input("Valor do Lado: "))
        print("")
        print("Area do Hexagono:",area_h(lado_1))
        print("")
    elif num1 == 6:
        print("Defina dois numeros para efetuar contas basicas")
        print("")
        print("[1] Perimetro do Circulo")
        print("[2] Perimetro do Quadrado")
        print("[3] Perimetro do Retangulo")
        print("[4] Perimetro do Triangulo Equilatero")
        print("[5] Perimetro do Hexagono")
        print("")
        num2 = int(input("Numero de [1-5]: "))
        print("")
        if num2 == 1:
            lado_1 = int(input("Valor do Lado: "))
            print("")
            print("Perimetro do Circulo:",peri_c(lado_1))
            print("")
        elif num2 == 2:
            lado_1 = int(input("Valor do Lado: "))
            print("")
            print("Perimetro do Quadrado:",peri_q(lado_1))
            print("")
        elif num2 == 3:
            b1 = int(input("Valor Base: "))
            print("")
            h1 = int(input("Valor Altura: "))
            print("")
            print("Perimetro do Retangulo:",peri_r(b1,h1))
            print("")
        elif num2 == 4:
            lado_1 = int(input("Valor do Lado: "))
            print("")
            print("Perimetro do Triangulo Equilatero:",peri_te(lado_1))
            print("")
        elif num2 == 5:
            lado_a = int(input("Valor do Lado 'a': "))
            print("")
            lado_b = int(input("Valor do Lado 'b': "))
            print("")
            lado_c = int(input("Valor do Lado 'c': "))
            print("")
            print("Perimetro do Hexagono:",peri_h(lado_a,lado_b,lado_c))
            print("")
    else:
        pass
exibir_a()
