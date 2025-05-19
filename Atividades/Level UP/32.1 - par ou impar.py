'''
Após sair o resultado perguntar se deseja
começar outra rodada ou sair.
'''

import random

print("                                                 Bem Vindo ao Jogo de Par ou Impar com Bot")
print("")
print("")
print("Você Vs Bot")
print("")
print("Clique em qualquer tecla para continuar:")
input("-")
print("")
print("")
print("")
print("")
print("")
print("Regras:")
print("")
print("1º o limite de numeros é de 1 a 10")
print("2º escolha um numero par ou impar")
print("3º se o numero somado for o mesmo da sua escolha Você ganha")
print("4º é permitido somente numeros interos Exemplo:(-4,-3,-2,-1,0,1,2,3,4)")
print("")
print("")
print("Clique em qualquer tecla para continuar:")
input("-")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Par ou Impar?")
print("")
print("[1] Par")
print("[2] Impar")
print("")
esc1 = input("Escolha: ")
if esc1 == "par" or esc1 == "Par" or esc1 == "PAR" or esc1 == "1":
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Escolha um Numero")
    print("")
    num1 = int(input("Numero: "))
    numr1 = random.randint(0,10)
    calc1 = num1 + numr1
    calc2 = calc1
    print("")
    while True:
        calc1 -= 2
        if calc1 % 2 == 0:
            print(num1,"+",numr1,"=",calc2)
            print("")
            print("Jogador Ganhou")
            print("")
            print("Clique em qualquer tecla:")
            input("")
            break
        elif calc1 < 0:
            print(num1,"+",numr1,"=",calc2)
            print("")
            print("Bot Ganhou")
            print("")
            print("Clique em qualquer tecla:")
            input("")
            break
elif esc1 == "impar" or esc1 == "Impar" or esc1 == "IMPAR" or esc1 == "2":
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Escolha um Numero")
    print("")
    num1 = int(input("Numero: "))
    numr1 = random.randint(0,10)
    calc1 = num1 + numr1
    calc2 = calc1
    print("")
    while True:
        calc1 -= 2
        if calc1 % 2 == 0:
            print(num1,"+",numr1,"=",calc2)
            print("")
            print("Bot Ganhou")
            print("")
            print("Clique em qualquer tecla:")
            input("")
            break
        elif calc1 < 0:
            print(num1,"+",numr1,"=",calc2)
            print("")
            print("Jogador Ganhou")
            print("")
            print("Clique em qualquer tecla:")
            input("")
            break
while True:
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Dejesa Continuar:")
    print("[1] Continuar")
    print("[2] Sair")
    print("")
    esc2 = input("-")
    if esc2 == "continuar" or esc2 == "Continuar" or esc2 == "CONTINUAR" or esc2 == "1":
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("Par ou Impar?")
        print("")
        print("[1] Par")
        print("[2] Impar")
        print("")
        esc1 = input("Escolha: ")
        if esc1 == "par" or esc1 == "Par" or esc1 == "PAR" or esc1 == "1":
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("Escolha um Numero")
            print("")
            num1 = int(input("Numero: "))
            numr1 = random.randint(0,10)
            calc1 = num1 + numr1
            calc2 = calc1
            print("")
            while True:
                calc1 -= 2
                if calc1 % 2 == 0:
                    print(num1,"+",numr1,"=",calc2)
                    print("")
                    print("Jogador Ganhou")
                    print("")
                    print("Clique em qualquer tecla:")
                    input("")
                    break
                elif calc1 < 0:
                    print(num1,"+",numr1,"=",calc2)
                    print("")
                    print("Bot Ganhou")
                    print("")
                    print("Clique em qualquer tecla:")
                    input("")
                    break
        elif esc1 == "impar" or esc1 == "Impar" or esc1 == "IMPAR" or esc1 == "2":
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("Escolha um Numero")
            print("")
            num1 = int(input("Numero: "))
            numr1 = random.randint(0,10)
            calc1 = num1 + numr1
            calc2 = calc1
            print("")
            while True:
                calc1 -= 2
                if calc1 % 2 == 0:
                    print(num1,"+",numr1,"=",calc2)
                    print("")
                    print("Bot Ganhou")
                    print("")
                    print("Clique em qualquer tecla:")
                    input("")
                    break
                elif calc1 < 0:
                    print(num1,"+",numr1,"=",calc2)
                    print("")
                    print("Jogador Ganhou")
                    print("")
                    print("Clique em qualquer tecla:")
                    input("")
                    break

    elif esc2 == "sair" or esc2 == "Sair" or esc2 == "SAIR" or esc2 == "2":
        print("")
        print("Obrigado por jogar volte quando quiser")
        break
    


        
