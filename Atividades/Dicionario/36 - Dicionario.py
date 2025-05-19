
#criar
aluno = {
    "Nome": "João H.",
    "Idade": 16,
    "Altura": 1.95,
    "Matriculado": True
}

#adicionar
aluno["peso"] = 105


#adulterar

aluno["Idade"] = 17

#deletar

del aluno["peso"]

#verificar
'''
if "peso" in aluno:
    print("Peso")
else:
    print("Sem Peso")
'''

#exibir
#for chave,valor in aluno.items():
#    print(f"{chave}: {valor}")

#print(aluno)

sistema_1 = {
    "edição": "Windows 11 Education",
    "processador": "11th Gen Intel(R) Core(TM) i7-11390H @ 3.40GHz 2.92 GHz",
    "memoria RAM": "16 0GB",
    "tipo": "64bits (x64)",
    "versão": "22H2"
}
sistema_2 = {
    "edição": "Windows 10",
    "processador": "SoC (Sistema em um Chip)",
    "memoria RAM": "4 GB",
    "tipo": "64bits (x64)",
    "versão": "22h2"
}
sistema_3 = {
    "edição": "Windows 7",
    "processador": "1 GHz ou superior",
    "memoria RAM": "2 GB",
    "tipo": "64bits (x64)",
    "versão": "Windows 7 Home Basic"
}
print("")
print("Pc 1:")
for chave, valor in sistema_1.items():
    
    print(f"    {chave}: {valor}")
    print("")
print("")
print("Pc 2:")
for chave2, valor2 in sistema_2.items():
    
    print(f"    {chave2}: {valor2}")
    print("")
print("")
print("Pc 3:")
for chave3, valor3 in sistema_3.items():
    
    print(f"    {chave3}: {valor3}")
    print("")
    
#exibir um lista de Dicionarios
lista_sis = [sistema_1,sistema_2,sistema_3]
    #escolhendo os campos
for sistema_1 in lista_sis:
    print(f"{sistema_1['processador']}")
    print("")
    print("")
    #exibindo todos
for sistema_1 in lista_sis:
    for chave, valor in sistema_1.items():
        print(f"    {chave}: {valor}")
    print("")
    
    
    
    
    
    
    
