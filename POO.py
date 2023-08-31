'''questao 1'''
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    def saudacao(self):
        return f"olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}."
pessoa = Pessoa("John", 19, "engenheiro")
print(pessoa.saudacao())

'''questao 2'''
class ContaB:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def informacoes(self):
        return f"olá {self.titular}, seu saldo é: {self.saldo}"
    def deposito(self, dinheiro):
        self.saldo+=dinheiro
    def saque(self, valor):
        if valor>0:
            self.saldo -= valor
John = ContaB('john', 0)
John.deposito(110)
John.informacoes()
John.saque(50)
John.informacoes()

'''questao 3'''
class Carro:
    def __str__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.aceleracao = 0
def acelerar(self, infobonus):
    self.aceleracao += infobonus
    print(f"o carro atingiu {self.aceleracao}km/h")
automovel = Carro("HR-V","Honda",2018)
print(f"o modelo solicitado foi: {automovel.marca} {automovel.modelo} {automovel.ano}")
automovel.aceleracao(20)
automovel.aceleracao(10)

'''questao 4'''
class FormaG:
    def calcular_area(self, raio):
        return 3.14*(raio**2)
class Circulo(FormaG):
    pass
class Retangulo(FormaG):
    def calcular_area(self, base, altura):
        return base*altura
circulo = Circulo()
area = circulo.calcular_area(20)
print(area)
retangulo = Retangulo()
area = retangulo.calcular_area(5,10)
print(area)

'''questao 5'''
class Especie:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def som(self):
        pass
    def info(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Som: {self.som()}"

class Cachorro(Especie):
    def som(self):
        return "auau"
class Gato(Especie):
    def som(self):
        return "miau"

cachorro = Cachorro("Toby", 1)
gato = Gato("laranja", 4)

print(cachorro.info())
print(gato.info())
