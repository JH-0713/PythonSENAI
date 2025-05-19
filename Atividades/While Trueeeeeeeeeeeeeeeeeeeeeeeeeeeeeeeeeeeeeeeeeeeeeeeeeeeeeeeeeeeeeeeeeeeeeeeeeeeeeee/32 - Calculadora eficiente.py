
while True:
    print("")
    print("Escolha uma das alternativas Abaixo")
    print("")
    print("[1] Fatorial")
    print("[2] Quadrado")
    print("[3] Cubo")
    print("[4] Tabuada")
    print("[0] Sair")
    print("")
    x1 = int(input("Numero de [0-4]: "))
    print("")
    
    if x1 == 1:
        numero = int(input("Determine o Numero: "))
        resultado=1
        num2=1
        while num2 <= numero:
            resultado *= num2
            num2 += 1
        print(resultado)
        
    elif x1 == 2:
        num1 = int(input("Determine o Numero: "))
        print("")
        calc1 = pow(num1,2)
        print("Valor ao Quadrado =",calc1)
        
        
    elif x1 == 3:
        num1 = int(input("Determine o Numero: "))
        print("")
        calc1 = pow(num1,3)
        print("Valor ao Cubo =",calc1)
        
    elif x1 == 4:
        num1 = int(input("Determine o Numero: "))
        print("")
        print(num1,"x 1 =",num1 * 1)
        print(num1,"x 2 =",num1 * 2)
        print(num1,"x 3 =",num1 * 3)
        print(num1,"x 4 =",num1 * 4)
        print(num1,"x 5 =",num1 * 5)
        print(num1,"x 6 =",num1 * 6)
        print(num1,"x 7 =",num1 * 7)
        print(num1,"x 8 =",num1 * 8)
        print(num1,"x 9 =",num1 * 9)
        print(num1,"x 10 =",num1 * 10)
        
    elif x1 == 0:
        print("Tchau")
        break
    else:
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
