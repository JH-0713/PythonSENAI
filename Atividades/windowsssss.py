sistema_operacional1 = {
    "edição": "Windows 11 Education",
    "processador": "11th Gen Intel(R) Core(TM) i7-11390H @ 3.40GHz 2.92 GHz",
    "memoria RAM": "16 0GB",
    "tipo": "64bits (x64)",
    "versão": "22H2"
}
sistema_operacional2 = {
    "edição": "Windows 10",
    "processador": "SoC (Sistema em um Chip)",
    "memoria RAM": "4 GB",
    "tipo": "64bits (x64)",
    "versão": "22h2"
}
sistema_operacional3 = {
    "edição": "Windows 7",
    "processador": "1 GHz ou superior",
    "memoria RAM": "2 GB",
    "tipo": "64bits (x64)",
    "versão": "Windows 7 Home Basic"
}
print("")
print("Pc 1:")
for chave, valor in sistema_operacional1.items():
    
    print(f"    {chave}: {valor}")
    print("")
print("")
print("Pc 2:")
for chave2, valor2 in sistema_operacional2.items():
    
    print(f"    {chave2}: {valor2}")
    print("")
print("")
print("Pc 3:")
for chave3, valor3 in sistema_operacional3.items():
    
    print(f"    {chave3}: {valor3}")
    print("")