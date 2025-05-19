print("Solicite seu ano de nascimento")
print()
x1 = float(input("Ano de Nascimento: "))
print()
x2 = float(input("Digite o ano Atual: "))
print()
calc1 = x2 - x1
if calc1 <= 17:
    print("Idade:",round(calc1))
    print("Menor de Idade")
elif calc1 >= 18:
    print("Idade:",round(calc1))
    print("Maior de Idade")
else:
    pass

