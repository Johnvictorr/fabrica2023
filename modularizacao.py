import funcao

canetap = int(input("Informe quantas canetas pretas você pegou: "))
canetaa = int(input("Informe quantas canetas azuis você pegou: "))
if canetap>=1:
    vtotalp = canetap * 2.50
if canetaa>=1:
    vtotala = canetaa * 2
print("O valor total de canetas pretas é: ", {vtotalp})
print("O valor total de canetas azuis é: ", {vtotala})

print(funcao.mult(vtotalp, vtotala))