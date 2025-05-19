import inputs
print("                                                          Inscrições para a Reunião de Pais")
print("")
print("")
print("")
print("")
print("")
print("Precione qualquer tecla para continuar:")
input("-")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
nomes = 0
pais1 = []
pais_a1 = []
pais_p1 = []
while True:
    print("")
    print("Selecione o que fazer:")
    print("")
    print("[1] Nome dos Pais")
    print("[2] Quantidade De Pais")
    print("[3] Comfirmação de Presença")
    print("[4] Lista de Presença")
    print("")
    esc1 = inputs.input_int(("Digite um dos Numeros: "))
    print("")
    if esc1 == 1:
        x1 = inputs.input_str("Nome: ")
        print("")
        if x1 in pais1:
            print("")
            print("Este nome já está na lista")
            print("")
            print("")
            print("Precione qualquer tecla para continuar:")
            input("-")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
        else:
            x1 = pais1.append(x1)
            pais1.sort()
            print("")
            print("Nome adicione")
            print("")
    elif esc1 == 2:
        x3 = len(pais1)
        print("Quantidade de convidados:",x3)
        print("")
        print("Nome dos Conviados em Ordem Alfabetica:")
        for convidados in pais1:
            print("")
            print(convidados)
            print("")
    elif esc1 == 3:
        print("")
        print("Chamada digital:")
        print("[P] Presente")
        print("[A] Ausente")
        print("")
        print("Pais:")
        print("")
        for convidado in pais1:
            print(convidado)
            print("")
            esc2 = inputs.input_str("")
            print("")
            if esc2 == "p" or esc2 == "P" or esc2 == "presente" or esc2 == "Presente" or esc2 == "PRESENTE":
                print("Presente")
                print("")
                pais_p1.append(convidado)
            elif esc2 == "a" or esc2 == "A" or esc2 == "ausente" or esc2 == "Ausente" or esc2 == "AUSENCIA":
                print("Ausente")
                print("")
                pais_a1.append(convidado)
    elif esc1 == 4:
        print("Pais Presentes: ")
        for convidado in pais_p1:
            print("")
            print(convidado)
            print("")
        print("Pais Ausentes: ")
        for convidado in pais_a1:
            print("")
            print(convidado)
            print("")
        
        
        
            
        
    
    
    
    
    
    
    
    