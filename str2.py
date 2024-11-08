#ultilizando o formatted strings
nome = "alice"
idade = 25
altura = 1.65

#ciando uma mensagem formatada usando o f-string
'''
mensagem = f"ola, meu nome é {nome}. tenho {idade} anos e minha altura é {altura:.2f} metros. "
print(mensagem)

#transformando em maiusculo
texto = "ola. mundo!"
texto_upper = texto.upper()
print(texto_upper)
#transformando em minusculo
texto_lower = texto.lower()
print(texto_lower)
#transforma a primeira letra em maiusculo
texto_capitalize = texto.capitalize()
print(texto_capitalize)
#conta quantas letras tem na palavra 
ocorrencias = texto.count("o")
print(ocorrencias)
#troca a palavra por outra
texto_substituido = texto.replace("mundo", "amigo")
print(texto_substituido)
'''

#Ex

#ex1 - crie uma variavel chamada "nome" e atribua a  ela o valor "maria"
nome = "maria"

#ex2 - crie uma variavel chamada sobrenome e atribua o valor "silva"
sobrenome = "silva"

#ex3 - crie uma variavel chamada idade e atribua a ela o valor 30
idade = 30

#ex4 - concatene as variaveis "nome" e "sobrenome" em uma nova variavel chamada "nome_completo"
nome_completo = nome + " " + sobrenome

#ex5 - imprima na tela o valor da variavel "nome_completo"
print(nome_completo)

#ex6 - crie uma variavel chamada mensagem que ultulize a função format para criar uma frase 
#personalizada com as variaveis "nome_completo" e "idade"
mensagem = (f"meu nome completo é {nome_completo}. tenho {idade} anos.")

#ex7 - imprima na tela a variavel chamada mensagem
print(mensagem) 

#ex8 - crie uma variavel chamada "frase" e atribua a ela a seguinte frase
# python é uma linguagem de programação poderosa e versatil
frase = (f"python é uma linguagem de programação poderosa e versatil") 

#ex9 - imprima na tela o tamaho da frase, ou seja a quantidade de caracteres
# presentes nela
tamanho_frase = len(frase)
print("tamanho da frase", tamanho_frase)

#ex10 - crie uma variavel chamada palavra e atribua a ela
# a primeira palavra da frase
palavra = frase.split() [0]
print(palavra)

#ex11 - converta a variavel "frase" para letras maisuculas e atribua o
#resultado a uma nova variavel chamada "frase_maiuscula"
frase_maiuscula = frase.upper ()
print(frase_maiuscula)

#ex12 - substitua a palavra poderosa por incrivel na variavel
#frase e atribua o resultado a uma nova variavel chamada frase_substituida
frase_substituida = frase.replace("poderosa", "incrivel")
print(frase_substituida)