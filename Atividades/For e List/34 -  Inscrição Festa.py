import inputs
print("                                                        Inscrições para a Festa de Arromba")
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
convids1 = []
x2 = 0
while True:
    print("")
    print("Selecione o que fazer:")
    print("")
    print("[1] Inscrever")
    print("[2] Exibir quantidade de Pessoas")
    print("[3] Consultar um nome")
    print("")
    esc1 = input("Escolha: ")
    print("")
    if esc1 == '1':
        x1 = input("Nome: ")
        print("")
        if x1 in convids1:
            print("")
            print("Este nome já está na lista")
            print("")
            print("Por favor ensira um nome que não esta nessa lista:")
            print("")
            for convidados in convids1:
                print(convidados)
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
            x1 = convids1.append(x1)
            convids1.sort()
            print("")
            print(convids1)
            print("")
            print("")
    elif esc1 == '2':
        x3 = len(convids1)
        print("Quantidade de convidados:",x3)
        print("")
        print("Nome dos Conviados em Ordem Alfabetica:")
        for convidados in convids1:
            print("")
            print(convidados)
            print("")
    elif esc1 == '3':
        print("")
        esc2 = input("Nome: ")
        print("")
        if esc2 in convids1:
            print("")
            print("Nome encontrado. Deseja removê-lo? (s/n)")
            print("")
            esc3 = input("Escolha: ")
            if esc3 == "s" or esc3 == "S" or esc3 == "sim" or esc3 == "Sim" or esc3 == "SIM":
                convids1.remove(esc2)
                print("Nome Deletado!")
            elif esc3 == "n" or esc3 == "N" or esc3 == "não" or esc3 == "Não" or esc3 == "NÃO" or esc3 == "nao" or esc3 == "Nao" or esc3 == "NAO":
                print("Nome Não Deletado")
        elif not esc2 in convids1:
            print("")
            print("Nome não encontrado. Deseja adicioná-lo? (s/n)")
            print("")
            esc3 = input("Escolha: ")
            if esc3 == "s" or esc3 == "S" or esc3 == "sim" or esc3 == "Sim" or esc3 == "SIM":
                convids1.append(esc2)
                print("Nome Adicionado")
            elif esc3 == "n" or esc3 == "N" or esc3 == "não" or esc3 == "Não" or esc3 == "NÃO" or esc3 == "nao" or esc3 == "Nao" or esc3 == "NAO":
                print("Nome Adicionado")
        else:
            pass



        
        




