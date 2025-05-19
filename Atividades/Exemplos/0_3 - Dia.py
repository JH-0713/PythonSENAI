from datetime import datetime

def calcular_idade(ano_nacimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nacimento
    return idade
    
    
def mostrar_idade(ano_nacimento):
    ano_atual = 2025
    idade = ano_atual - ano_nacimento
    print("voce tem",idade,"anos")
    
def definir_idade():
    ano = int(input("Digite seu ano de nacimento: "))
    calcular_idade(ano) 
   
definir_idade()