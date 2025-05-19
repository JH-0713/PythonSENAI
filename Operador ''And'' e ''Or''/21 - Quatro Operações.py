print("Solicite Uma operação matematica para efetuar uma conta de 2 numeros:")
print()
print("EXEMPLO: '+','-','*' ou '/' lembrete o simbolo '*' é multiplicação e '/' é divisão ")
print()
qw1 = input("Digite a operação matematica para utilizara estes numeros: ")
print()
print("Solicite dois numeros para efetuar a conta:")
print()
x1 = float(input("Numero 1º = "))
print()
x2 = float(input("Numero 2º = "))
print()


if qw1 == "SOMA" or qw1 == "Soma" or qw1 == "soma" or qw1 == "+":
    print()
    calc1 = x1 + x2
    print("A adição dos valores =",round(calc1,1))
elif qw1 == "SUBTRAÇAO" or qw1 == "Subtrçao" or qw1 == "subtraçao" or qw1 == "-":
    print()
    calc1 = x1 - x2
    print("A subtração dos valores =",round(calc1,1))
elif qw1 == "MULTIPLICAÇAO" or qw1 == "Multiplicaçao" or qw1 == "multiplicaçao" or qw1 == "*":
    print()
    calc1 = x1 * x2
    print("A multiplicação dos valores =",round(calc1,1))
elif qw1 == "DIVISAO" or qw1 == "Divisao" or qw1 == "divisao" or qw1 == "/":
    print()
    calc1 = x1 / x2
    print("A divisão dos valores =",round(calc1,1))
else:
    print("erro")