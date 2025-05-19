def input_int():
    while True:
        try:
            print("")
            input_int = int(input("Numero Inteiro: "))
            print("")
            print("")
            break
        except NameError:
            print("")
            print("ERRO:Digite um Numero Inteiro (-3 -2 -1 0 1 2 3)")
            print("")
        except ValueError:
            print("")
            print("ERRO:Digite um Numero Inteiro (-3 -2 -1 0 1 2 3)")
            print("")
input_int()
def input_float():
    while True:
        try:
            print("")
            input_Float = float(input("Digite Numero Sem Letra: "))
            print("")
            print("")
            break
        except NameError:
            print("")
            print("ERRO:Digite um Numero Sem Letras(-1 0 0.5 1 20)")
            print("")
        except ValueError:
            print("")
            print("ERRO:Digite um Numero Sem Letras(-1 0 0.5 1 20)")
            print("")
input_float()
def input_str():
    while True:
        print("")
        input_str = str(input("Digite uma Letra Sem Numero:"))
        print("")
        print("")
        if not input_str.isalpha():
            print("ERRO: Digite uma Letra (A B C (...) X Y Z)")
            print("")
        else:
            return input_str
            break
input_str()
        
        

        
        
        
        