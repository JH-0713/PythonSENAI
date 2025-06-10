import inputs

lista1 = []
      
def cadastrar():
    media_aluno = {
    "aluno": inputs.input_str("Aluno: "),
    "nota1": inputs.input_int("Nota 1: "),
    "nota2": inputs.input_int("Nota 2: "),
    "nota3": inputs.input_int("Nota 3: ")
}
    
    for aluno in lista1:
        if aluno["aluno"] == media_aluno["aluno"]:
            print("")
            print("Este NOME já está na lista")
            print("")
            print("Por favor ensira um NOME que não esta na lista:")
            print("")
            print("Precione [ENTER] para continuar:")
            input("-")
            print("")
            break
        else:
            lista1.append(media_aluno)
            print("")
            print("Aluno Cadastrado")
            print("")
            return media_aluno
    else:
        lista1.append(media_aluno)
        print("")
        print("Aluno Cadastrado")
        print("")
        return media_aluno
    
def calcular(n1,n2,n3):
    calc1 = n1 + n2 + n3
    calc2 = calc1 / 3
    return calc2
    

def verificar(media):
    for i in lista1:
        if media >= 7:
            c1 = "Aprovado"
            return c1
            
        elif media >= 5 and i["media"] <= 6.9:
            c1 = "Reculperação"
            return c1
            
        elif media <= 4.9:
            c1 = "Reprovado"
            return c1
        
def exibir_final(lista1):
    print("")
    print("Situação:")
    print("")
    for i in lista1:
        if i["situação"] == "Aprovado":
            print(f"{i['aluno']}: {i['media']} -> {i['situação']}")
            
        elif i["situação"] == "Reculperação":
            print(f"{i['aluno']}: {i['media']} -> {i['situação']}")
            
        elif i["situação"] == "Reprovado":
            print(f"{i['aluno']}: {i['media']} -> {i['situação']}")   
        else:
            print("Nao Calculado") 
        
        
while True:
    print("")
    print("[1] Cadastrar Aluno")
    print("[2] Calcular Media")
    print("[3] Verificar Situação")
    print("[4] Exibir Situação")
    print("")
    esc1 = inputs.input_int("> ")
    print("")
    if esc1 == 1:
        cadastrar()
    elif esc1 == 2:
        print("Media Calculada")
        for i in lista1:
            calculo1 = calcular(i["nota1"],i["nota2"],i["nota3"])
            i["media"] = calculo1
    elif esc1 == 3:
        print("Verificação Completa")
        for i in lista1:
            situa1 = verificar(i["media"])
            i["situação"] = situa1
    elif esc1 == 4:
        exibir_final(lista1)
        print("")
        print("Precione [ENTER] para continuar:")
        input("-")
        print("")
        print("")
        print("")
        print("")
