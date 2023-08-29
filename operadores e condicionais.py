num = int(input("Digite um número: "))
a = num-1
s = num+1
print("O antecessor do seu número é: ", a)
print("O sucessor do seu número é: ", s)


num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
oper = int(input("Escolha uma operação (1-soma, 2-subtração, 3-multiplicação ou 4-divisão): "))
if oper==1:
    soma=num1+num2
    print("A soma dos números escolhidos é: ", soma)
if oper==2:
    subt=num1-num2
    print("A subtração dos números escolhidos é: ", subt)
if oper==3:
    mult=num1*num2
    print("A multiplicação dos números escolhidos é: ", mult)
if oper==4:
    divi=num1/num2
    print("A divisão dos números escolhidos é: ", divi)


num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
if num1>num2:
    print(True)
else:
    print(False)


temp = float(input("Informe a temperatura de hoje em graus celsius: "))
tempf = (temp * 1.8) + 32
print("A temperatura de hoje, em Fahrenheit é: ", tempf)

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
