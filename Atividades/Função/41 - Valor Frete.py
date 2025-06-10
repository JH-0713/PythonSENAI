def calcular(p1,dis1,taxa_f1):
    c1 = p1 * 0.5
    c2 = dis1 * 0.1
    valor = c1 + c2 + taxa_f1
    return valor

print("")
print("Defina o valor do Peso:")
print("")
p1 = int(input("> "))
print("")
print("")
print("Defina o valor da Distancia:")
print("")
dis1 = int(input("> "))
print("")
print("")
print("Defina o valor da Taxa Fixa:")
print("")
taxa_f1 = int(input("> "))
print("")
print("Valor Frete:",calcular(p1,dis1,taxa_f1))