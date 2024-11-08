#funções
#input
#nome = input ("digite seu nome: \n")
#print ("\n O seu nome é: " + nome)
""""
nome = input ("digite seu nome: \n")
nota1 = float (input ("digite a nota 1: "))
nota2 = float (input ("digite a nota 2: "))

media = (nota1 + nota2) /2
print ("\n ianaluno", nome, "media", media)
"""
#execicio1 faça uma tabuada usando o input
'''
numero =int( input("digite um numero inteiro: "))
print (numero, "* 1 =", numero * 1) 
print (numero, "* 2 =", numero * 2) 
print (numero, "* 3 =", numero * 3) 
print (numero, "* 4 =", numero * 4) 
print (numero, "* 5 =", numero * 5) 
print (numero, "* 6 =", numero * 6) 
print (numero, "* 7 =", numero * 7) 
print (numero, "* 8 =", numero * 8) 
print (numero, "* 9 =", numero * 9) 
print (numero, "* 10 =", numero * 10) 
'''
'''
ex2 crie um algoritimo que solicite o ano do nascimento do usuario 
com base no ano e imorima a idade
'''
'''
ano_atual = 2024
ano_nascimento = int(input("digite sua data de nascimento :"))
print(ano_nascimento, "\nsua idade é:", ano_atual - ano_nascimento )

'''
#função import random
import random 
print (random.randrange(1,100))

#gerar um numero de ponto flutuante/float entre 0 e 1:
print(random.random())

#gerar um numero inteiro aleatorio entre dois valores (inclusive):
print (random.randint(10,20))#gera um njemro entre 10 e 20

#escolher aleatoriamente um elemento da lista
frutas = ["maça","banana","uva"]
print(random.choice(frutas))

#escolher aleatoriamente uma lista
numeros =  [1,2,3,4,5]
random.shuffle(numeros)
print(numeros)

#gerar um numero flutuante aleatorio em um intervalo especifico
print(random.uniform(5.5, 9.5))




