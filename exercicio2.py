id = int(input("Informe a sua idade: "))

if id >=18:
    print("Você já pode tirar sua carteira de motorista.")
else:
    print("Você ainda não pode tirar sua carteira de motorista")


vel = float(input("Qual foi a velocidade do indivíduo? "))
if vel >= 80:
    multa = (vel-80) * 7
    print("Você recebeu uma multa de: ", multa)
else:
    print("O motorista não passou de 80km/h")


num1 = int(input("Escreva um número: "))
num2 = int(input("Escreva outro número: "))
num3 = int(input("Escreva mais um número: "))
maior = num1
if num2>num3 and num2>num1:
    maior = num2
if num3>num2 and num3> num1:
    maior = num3
menor = num1
if num2<num3 and num2<num1:
    menor = num2
if num3<num2 and num3<num1:
    menor = num3
print("O maior número é: ", {maior})
print("O menor número é: ", {menor})
    

canetap = int(input("Informe quantas canetas pretas você pegou: "))
canetaa = int(input("Informe quantas canetas azuis você pegou: "))
if canetap>=1:
    vtotalp = canetap * 2.50
if canetaa>=1:
    vtotala = canetaa * 2
print("O valor total de canetas pretas é: ", {vtotalp})
print("O valor total de canetas azuis é: ", {vtotala})


nome1 = str(input("Insira seu nome: "))
nome2 = str(input("Insira seu nome: "))
nome3 = str(input("Insira seu nome: "))
nome = str(input("Insira seu nome: "))
if nome1=="joao maia":
    print("oi eu sou joao maia")
if nome2=="joao abrantes":
    print("oi eu sou joao abrantes")
if nome3=="pedro":
    print("oi eu sou pedro")
if (nome):
    print("oi eu sou ", {nome})