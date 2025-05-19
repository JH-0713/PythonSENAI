print("Defina o valor dos Celsius para achar o Kelvin e Fahrenheit")

def calcular_fah(cel1):
    calc1 = cel1 * 1.8
    calc2 = calc1 + 32
    calc3 = cel1 + 273
    print("Valor do Kelvin: ",round(calc3),"K",sep='')
    print("")
    print("Valor do Fahrenheit: ",round(calc2),"ºF",sep='')

def exibir_fah():
    print("")
    cel1 = int(input("Defina o valor de Celsius: "))
    print("")
    calcular_fah(cel1)
    
exibir_fah()