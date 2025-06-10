import inputs

lista1 = []
           
def cadastrar():
    media_aluno = {
    "aluno": inputs.input_str("Aluno: "),
    "nota1": inputs.input_int("Nota 1: "),
    "nota2": inputs.input_int("Nota 2: "),
    "nota3": inputs.input_int("Nota 3: "),
    "media": 0,
}
    
    for aluno in lista1:
        if aluno["aluno"] == media_aluno["aluno"]:
            print("")
            print("Este NOME já está na lista")
            print("")
            print("Por favor ensira um NOME que não esta na lista:")
            print("")
            print("Precione qualquer tecla para continuar:")
            input("-")
            print("")
            break
        else:
            lista1.append(media_aluno)
            print("")
            print("Aluno Cadastrado")
            print("")
            
            media_aluno["media"] = calcular(media_aluno["nota1"] , media_aluno["nota2"] ,media_aluno["nota3"])
            print("Media Calculada")
            print("")
            
            media_aluno["situacao"] = verificar(media_aluno["media"])
            print("Situação Armazenada")
            print("")
            
            return media_aluno
    else:
        lista1.append(media_aluno)
        print("")
        print("Aluno Cadastrado")
        print("")
        
        media_aluno["media"] = calcular(media_aluno["nota1"],media_aluno["nota2"], media_aluno["nota3"])
        print("Media Calculada")
        
        media_aluno["situacao"] = verificar(media_aluno["media"])
        print("Situação Armazenada")
        
        return media_aluno
    
def exibir_final(lista1):
    print("")
    print("Situação:")
    print("")
    for i in lista1:
        if i['situacao'] == "Aprovado":
            print(f"{i['aluno']}: {i['situacao']}")
            
        elif i['situacao'] == "Reculperação":
            print(f"{i['aluno']}: {i['situacao']}")
            
        elif i['situacao'] == "Reprovado":
            print(f"{i['aluno']}: {i['situacao']}")   
        else:
            print("Nao Calculado")
            
def calcular(n1,n2,n3):
    calc1 = n1 + n2 + n3
    calc2 = calc1 / 3
    return calc2

def verificar(media):
    for i in lista1:
        print("")
        if media >= 7:
            c1 = "Aprovado"
            return c1
            
        elif media >= 5 and i["media"] <= 6.9:
            c1 = "Reculperação"
            return c1
            
        elif media <= 4.9:
            c1 = "Reprovado"
            return c1
        
        
while True:
    print("")
    print(lista1)
    print("")
    print("")
    print("[1] Cadastrar Aluno")
    print("[2] Verificar Alunos")
    print("")
    esc1 = inputs.input_int("> ")
    print("")
    if esc1 == 1:
        cadastrar()
    elif esc1 == 2:
        exibir_final(lista1)


