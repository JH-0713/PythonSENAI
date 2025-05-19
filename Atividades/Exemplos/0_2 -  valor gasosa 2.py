#1 custo para terminar de encher o tanque

#2 descobrir a quantidade de litros dentro do tanque
# descobrir o valor para encher o tanque

#3 subtraia o numero para saber o valor que sera pre enchido
# multiplique pelo valor da parte vazia do taque
# exibir resultado do custo


lit1 = int(input("qual o limite de litros do seu carro = "))
quant1 = int(input("quantos litros você tem = "))

cal1 = lit1 - quant1

quant2 = 5.80 * cal1

print("custo para encher o tanque é de =",quant2)
