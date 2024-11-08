
def soma (a, b):
    return a + b

resultado = soma(2,3)
print(resultado)

resultado = soma(10,3)
print(resultado)

resultado = soma(2,20)
print(resultado)

#criando uma função soma
def soma (a,b):
    return a + b
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

resultado = soma(numero1, numero2)
print(f"a soma é: {resultado}")

#parametros e argumentos em uma função
def saudaçao (nome):
    print("ola, " + nome + " bem vindo")

nome = "ian"

saudaçao(nome)


#argumentos Default e Non-Default
def exibir_informaçoes (nome, idade, cidade = "desconhecida"):
    print("Nome:", nome)
    print("Idade:", idade)
    print("Cidade:", cidade)
#valor sem default
exibir_informaçoes("joao", 25, "são paulo")
#valor com default
exibir_informaçoes("maria", 30)


#ex com print
#parametros e argumentos em uma função
def saudaçao (nome):
    print("ola, " + nome + " bem vindo ao nosso programa!")
saudaçao("ian")
#ex com return
#criando uma função soma
def soma (a,b):
    return a + b
resultado = soma(3,4)
print("o resultado da soma é:", resultado)


#varios argumentos *args com numeros 
def soma(*args):
    #funçao sum = soma
    resultado = sum(args)
    return resultado

total = soma (2,4,6,8,10)
print("a soma dos numeros é: ",total)

#
def estatistica (*args):
    return sum(args) / len(args), max (args), min(args)
numeros = list((map)(float, input("Digite uma sequencia de numeros separados por espaços: ").split()))
media, maior, menor = estatistica(*numeros)

print(f"media: {media}")
print(f"maior numero: {maior}")
print(f"menor numero: {menor}")

def exibir_informacoes(**kwargs):
    #função que exibe informaçoes pessoais
    for chave, valor in kwargs.items():
        print(chave + ": " + str(valor))

exibir_informacoes (nome="joao", idade=25, cidade="sao paulo", sexo = "masculino")