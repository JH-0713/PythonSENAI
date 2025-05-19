# 1º crie uma lista com cinco items


objetos = ["Cadeira","Lousa","Mesa","Relogio","Porta"]
print("")

# 2º adicionar um item na lista

objetos.append("Lapis")
print("")

# 3º Acessar o objeto na 2ª posição

x1 = objetos[1]
print(x1)
print("")

# 4º Remova um item da lista e exiba

x2 = len(objetos)
x3 = objetos.pop(5)

print(x3,"quantidade antes: ",x2)#removido
print("")

# 5º exibir o tamanho da lista

x4 = len(objetos)

print("Quantidade Nova =",x4)
print("")

# 6º mostre todos os items com o comando "for"

x5 = 0
for objeto in objetos:
    x5 += 1
    print(x5,"º ",objeto,sep="")
    print("")
    
# 7º verificar se a "Cadeira" esta na lista se sim remova-a, senão adicione

if "Cadeira" in objetos:
    objetos.remove("Cadeira")#removido
    print("Cadeira Removida")
    print("")
else:
    objetos.append("Cadeira")
    print("Cadeira Adicionada")
    print("")
    
# 8º deixar a lista em ordem alfabetica, exibir Antes e Depois

print("Antes:",objetos)
print("")
objetos.sort()
print("Depois:",objetos)
print("")

# 9º exibir o primeiro e ultimo valor da lista

x6 = len(objetos)
primeiro1 = objetos[1]
ultimo1 = x6 - 1
ultimo2 = objetos[ultimo1]
print("Primeiro:",primeiro1)
print("")
print("Ultimo:",ultimo2)
print("")

# 10º limpe toda a lista

objetos.clear()
print("Lista Apagada")

