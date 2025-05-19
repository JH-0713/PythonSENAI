#1 encontrar quantos reais e litros de combustivel é necessario para a viagem

#2 quantos litros são gastados em quilometros na viagem
# quanto de combustivel o carro contem
# quilometro ja percorido da viagem

#3 indentificar quantos litros possui no carro para a transformar em quilometros para saber quantos km ele ainda ira percorrer
#somar com aquele que ja percorreu,subitrair pela viagem,dividindo por quantos quilometros o carro pode ir com sua autonomia
#multiplicar pelo preço do combustivel para saber o valor e exibir o resultado

viagem = 800#km
autonomia = 7#km/litro
tanque_carro = 10#litro
percorido1 = 90#km
preco_combustivel = 6.90#litros


percorido2 = autonomia * tanque_carro
percorido3 = percorido2 + percorido1
viagem_2 = viagem - percorido3
m1 = viagem_2 / autonomia
m2 = m1 * preco_combustivel

print("caminho que você ira percorrer com a quantidade de combustivel sera =",percorido3)
print("caminho que falta percorrer =", viagem_2)
print("ele vai gastar em litros =", round(m1, 2))
print("você gastara a quantidade R$=", round(m2, 2))



