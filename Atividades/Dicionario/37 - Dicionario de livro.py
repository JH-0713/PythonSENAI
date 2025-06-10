import inputs
print("")
print("Cadastro de Livro:")
quantl1 = []

def myfunção(e):
  return e['ISBN']

while True:
    print("")
    print("Etapas:")
    print("")
    print("[1º] Cadastrar 1 Livro")
    print("[2º] Exibir Livros")
    print("[3º] Exibir Quantidade de Livros")
    print("[4º] Exibir Titulo dos Livros")
    print("[5º] Buscar Livros por Autor")
    print("[6º] Buscar Livros por Categoria")
    print("[7º] Editar Livro")
    print("")
    esc1 = input("Escolha: ")
    print("")
    
    if esc1 == "1":
        livro1 = {
            "Titulo" : inputs.input_str("Titulo: "),
            "Autor" : inputs.input_str("Autor: "),
            "Categoria" : inputs.input_str("Categoria: "),
            "Ano de Publicação" : inputs.input_int("Ano de Publicação: "),
            "ISBN" : inputs.input_int("ISBN: ")
        }
        
        for livro in quantl1:
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
                quantl1.append(livro1)
                print("Livro Cadastrado")
                print("")
        else:
            quantl1.append(livro1)
            print("Livro Cadastrado")
            print("")
                
    elif esc1 == "2":
        quantl1.sort(key=myfunção)
        for livro in quantl1:
            for chave, valor in livro.items():
                print(f"    {chave}: {valor}")
            print("")
            
    elif esc1 == "3":
        x1 = len(quantl1)
        print("Quantidade de Livros:",x1)
        
    elif esc1 == "4":
        for livro in quantl1:
            print(f"{livro['Titulo']}")
            
    elif esc1 == "5":
        x2 = inputs.input_str("Autor: ")
        print("")
        print("Livros:")
        for livro in quantl1:
            for chave, valor in livro.items():
                if x2 == livro["Autor"]:
                    print(f"    {chave}: {valor}")
            print("")
            
    elif esc1 == "6":
        x3 = inputs.input_str("Categoria: ")
        print("")
        print("Livros:")
        for livro in quantl1:
            for chave, valor in livro.items():
                if x3 == livro["Categoria"]:
                    print(f"    {chave}: {valor}")
            print("")
    elif esc1 ==  "7":
        x4 = 0
        print("Digite o ISBN do Livro:")
        print("")
        for livro in quantl1:
            x4 += 1
            print("[",x4,"]",f" {livro['ISBN']} ",f"{livro['Titulo']}",sep="")
        print("")
        x5 = inputs.input_int("Escolha: ")
        print("")
        print("Editar:")
        for livro in quantl1:
            if x5 == livro["ISBN"]:
                livro["Titulo"] = inputs.input_str("Titulo: ")
                livro["Autor"] = inputs.input_str("Autor: ")
                livro["Categoria"] = inputs.input_str("Categoria: ")
                livro["Ano de Publicação"] = inputs.input_int("Ano de Publicação: ")
                    
                    
                    
                    

            

'''
print("Etapas:")
print("")
print("[1º] ISBN")
print("[3º] Titulo")
print("[4º] Autor")
print("[5º] Categoria")
print("[6º] Ano de Publicação")
print("")
'''

























