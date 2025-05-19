'''
O jogo deve ter um título como se fosse uma página inicial mostrando ao
usuário que está dentro do jogo, depois uma instrução do que o usuário deve fazer
para jogar, use um intervalo de 0 a 100 para o jogo escolher um número para ser
adivinhado, a cada chute do usuário mostrar uma mensagem se o chute está maior
ou menor do que o número misterioso. Quando o usuário acertar o número
perguntar se deseja começar outra rodada ou sair.
'''
import random
numr1 = random.randint(0,100)
print("                                                    Jogo de Adivinhe o Numero")
print("                                                           [1 a 100]")
print("")
print("")
print("Clique em qualquer tecla para continuar:")
input("-")
print("")
print("")
print("")
print("")
print("Regras:")
print("")
print("1º a maquina escolheu um numero")
print("2º você tenta adivinhar o numero")
print("3º a maquina te dara dicas tipo mais perto e mais longe")
print("4º se voce acertar você ganha")
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
while True:
    print("")
    print("Digite um Numero para adivinhar")
    print("")
    num1 = int(input("Numero: "))
    print("")
    if num1 == numr1:
        print("Acertou")
        print("")
        print("")
        print("presione qualquer tecla")
        input("-")
        break
    elif num1 < numr1:
        print("")
        print("")
        print("Numero é maior que",num1)
        print("")
        print("")
    elif num1 > numr1:
        print("")
        print("")
        print("Numero Menor que",num1)
        print("")
        print("")
    else:
        pass
while True:
    numr2 = random.randint(0,100)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Deseja Sair ou Resetar o Jogo?")
    print("[1] Resetar")
    print("[2] Sair")
    print("")
    esc1 = input("Escolha: ")
    if esc1 == "resetar" or esc1 == "Resetar" or esc1 == "RESETAR" or esc1 == "1":
        while True:
            print("")
            print("Digite um Numero para adivinhar")
            print("")
            num1 = int(input("Numero: "))
            print("")
            if num1 == numr2:
                print("Acertou")
                print("")
                print("")
                print("presione qualquer tecla")
                input("-")
                break
            elif num1 < numr2:
                print("")
                print("")
                print("Numero é maior que",num1)
                print("")
                print("")
            elif num1 > numr2:
                print("")
                print("")
                print("Numero Menor que",num1)
                print("")
                print("")
            else:
                pass
    elif esc1 == "sair" or esc1 == "Sair" or esc1 == "SAIR" or esc1 == "2":
        print("Obrigado por Jogar volte quando quiser")
        break













