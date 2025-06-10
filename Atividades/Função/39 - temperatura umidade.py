def verificar(t1,h1,est1):
    print("")
    if est1 == 1:
        print("Inverno")
        print("")
        if t1 >= 20 and t1 <= 22 and h1 >= 40 and h1 <= 55:
            print("Temperatura: Adequada")
            print("Umidade: Adequada")
            t1 = True
            h1 = True
            return t1,h1
        
        elif t1 >= 20 and t1 <= 22 and h1 != 40 and h1 != 55:
            print("Temperatura: Adequada")
            print("Umidade: Desregulada")
            t1 = True
            h1 = False
            return t1,h1
        
        elif t1 != 20 and t1 != 22 and h1 >= 40 and h1 <= 55:
            print("Temperatura: Desregulada")
            print("Umidade: Adequada")
            t1 = False
            h1 = True
            return t1,h1
        
        else:
            print("Temperatura: Desregulada")
            print("Umidade: Desregulada")
            t1 = False
            h1 = False
            return t1, h1
        
    elif est1 == 2:
        print("Inverno")
        print("")
        if t1 >= 23 and t1 <= 26 and h1 >= 40 and h1 <= 65:
            print("Temperatura: Adequada")
            print("Umidade: Adequada")
            t1 = True
            h1 = True
            return t1,h1
        
        elif t1 >= 23 and t1 <= 26 and h1 != 40 and h1 != 65:
            print("Temperatura Adequada")
            print("Umidade Desregulada")
            t1 = True
            h1 = False
            return t1,h1
        
        elif t1 != 23 and t1 != 26 and h1 >= 40 and h1 <= 65:
            print("Temperatura: Desregulada")
            print("Umidade: Adequada")
            t1 = False
            h1 = True
            return t1,h1
        
        else:
            print("Temperatura Desregulada")
            print("Umidade Desregulada")
            t1 = False
            h1 = False
            return t1, h1
    else:
        pass
        

print("")
print("Descreva a Temperatura Ambiente:")
print("")
t1 = int(input("> "))
print("")
print("")
print("Descreva a Umidade:")
print("")
h1 = int(input("> "))
print("")
print("Descreva a Estação Atual:")
print("")
print("[1] Inverno")
print("[2] Verão")
print("")
est1 = int(input("> "))
print("")
print(verificar(t1,h1,est1))
        