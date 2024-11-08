
#funções internas (built-in)
#funções que ja são imbutidas na linguagem python, não necessita importar

#funções internas (built-in)
#print(), len(), input(), e etc

#print

nome = "maria"
print("ola,", nome)

#len

lista = [1,2,3]
print(len(lista))

#input()

#nome = input("Digite seu nome: ")
#print("seu nome é,", nome)


#conversão de tipos

#convertendo para inteiro
numero_decimal = "7.9"
numero_inteiro = int(float(numero_decimal))

print(numero_inteiro) #saida 7

#float

numero_str = "5.6"

numero_float = float (numero_str)
print(numero_float)

#str()- converte um valor para string

numero = 123

numero_str = str(numero)
print(numero_str)

'''
recursão
 - funções que chamam a si mesmas
 - problemas classicos, como caulculo do fatorial
 - riscos e limitações de recursão em python

'''
#1. funções que chamam a si mesmas

def contar_regressivamente (n):
    #verifica se é maior que 0
    if n > 0:

        print(n)
        #chama a função regressivamente passando n-1 como argumento
        contar_regressivamente(n -1)
#chama a função contar_regressivamente com o valor inicial de 5
contar_regressivamente(5)

#2. problemas classicos, como caulculo do fatorial
#fatorial é a multiplicação de todos os numeros antecessores
#ex numero (5) 5 x 4 x 3 x 2 x 1 = 120
def fatorial (n):
    if n == 0:
        return 1
    else:
        return n * fatorial (n - 1)
    
print(fatorial(5))

#3. riscos e limitações de recursão em python
#risco por conta que ficaria numeros infinitos, nao rodar
def recursao_infinita(n):
    print(n)

    return recursao_infinita (n+1)

recursao_infinita(1)



#documentação e anotaçõres de funções
# docstrings 
#anotações de tipo (type hints)

#1. docstrings
#são usadas para documentra especificamente oque uma função faz

#ex

def somar (a,b):
    '''
    função que retorna a soma de dois numeros.
    retorna a soma dos dois argumento
    '''
    return a + b 
print(somar.__doc__)
print(somar(2,3))

#2. anotações de tipo (type hints)
#ex

def multiplicar (a: int, b: int) -> int:
    return a * b
print(multiplicar(4,5)) #saida 20

#o -> int indica que tem que ser inteiro os argumentos