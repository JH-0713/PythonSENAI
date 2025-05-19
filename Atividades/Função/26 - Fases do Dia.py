from datetime import datetime

print("Digite seu Nome Abaixo e Descubra o Horario")
print("")

def calcular_horario(nome):
    hr = datetime.now().hour
    if hr >= 0 and hr <= 5:
        print("Boa madrugada",nome)
    elif hr > 5 and hr <= 12:
        print("Bom Dia",nome)
    elif hr > 12 and hr <= 19:
        print("boa tarde",nome)
    elif hr > 19 and hr < 24:
        print("Boa Noite",nome)
    else:
        print("o horario é de ate 24 horas,",nome,"!",sep="")
        
def definir_nome():
    nome = input("Nome: ")
    calcular_horario(nome)
#datetime.now().hour
definir_nome()

    
    
    
    
    