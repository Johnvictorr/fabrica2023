canetap = int(input("Informe quantas canetas pretas você pegou: "))
canetaa = int(input("Informe quantas canetas azuis você pegou: "))
if canetap>=1:
    vtotalp = canetap * 2.50
if canetaa>=1:
    vtotala = canetaa * 2
print("O valor total de canetas pretas é: ", {vtotalp})
print("O valor total de canetas azuis é: ", {vtotala})

def soma(vtotalp, vtotala):
    return vtotalp + vtotala

def subt(vtotalp, vtotala):
    return vtotalp - vtotala

def mult(vtotalp, vtotala):
    return vtotalp * vtotala
