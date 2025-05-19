msg1 = input("Digite uma mesagem: ")


peri1 = input("Digite qual periodo estamos(manha,tarde,noite): ")

sal1 = ""

if peri1 == "manha":
    sal1 = "Bom Dia"
    print(sal1,"Pessoal",msg1)
elif peri1 == "tarde":
    sal1 = "Boa Tarde"
    print(sal1,"Pessoal",msg1)
elif peri1 == "noite":
    sal1 = "Boa noite"
    print(sal1,"Pessoal",msg1)
else:
    print("Isso não é um Periodo")
    pass

