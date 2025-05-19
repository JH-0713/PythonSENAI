print("Cite um numero para efetuar a contagem regresiva")

x1 = int(input("Numero: "))
quant1 = 0
while True:
    x1 -= 1
    if x1 % 2 == 0:
        print(x1)
        quant1 += 1
    elif x1 <= 0:
        print("quantidade:",quant1)
        break