print("digite sua idade e o ano atual para saber sua faixa etaria")
print("")
x1 = int(input("Ano de Nacimento: "))
print("")
x2 = int(input("Ano Atual: "))
print("")
calc1 = x2 - x1

if calc1 <= 10 and calc1 >= 0:
    print("Criança")
    print("")
    print("Idade =",calc1)
elif calc1 <= 17 and calc1 >= 11:
    print("Adolecente")
    print("")
    print("Idade =",calc1)
elif calc1 <= 59 and calc1 >=18:
    print("Adulto")
    print("")
    print("Idade =",calc1)
elif calc1 >= 60 and calc1 <= 100:
    print("Idoso")
    print("")
    print("Idade =",calc1)
else:
    print("Morreu")