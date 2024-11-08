#este sinal serve para comentar um codigo para que o usuario saiba oque esse codigo faz 

"""
usando 3 aspas podemos comentar
varias linhas 
assim quando o cod for executado o script 
pula essas linhas 
"""
print("script executado com sucesso")

#criar variavel
#principais tipos de variaveis 

int = 42
print("inteiro:" ,int)

float = 42.0
print("Flutante:" ,float)

complex = 3 + 4j
print("complexo:" ,complex)

string = "hello word"
print("texto:", string)

list = [1,2,3]
print("lista:", list)

#nao muda
tuple = (1,2,3,4,5)
print("tupla:", tuple)

#coleção nao ordenada, nao se repete
set = {1,2,3}
print("conjuntos:", set)

dict = {"chave": "valor"}
print("dicionario:", dict)

bool = True
print("booleano:", bool)

bool = False
print("booleano:", bool)

Nenhum = None
print("NoneType (nome):", Nenhum)

#exemplo

nome = "ian"
idade = 20

print("nome:", nome)
print("idade:", idade)
print("nome:", nome , ", idade", idade)

#podemos obter o tipo da variavel usando a função type

nome = "ian"
idade = 20

print(type(nome))
print(type(idade))

var1, var2, var3, var4 = "texto 1", "texto 2", "texto 3", "texto 4"
print(var1)
print(var2)
print(var3)
print(var4) 

var1 = var2 = var3 = var4 = "ian"
print(var1)
print(var2)
print(var3)
print(var4) 

#descompactar valores
exemplo =  "texto 1", "texto 2", "texto 3", "texto 4"
var1, var2, var3, var4 = exemplo
print(var1)
print(var2)
print(var3)
print(var4) 

nome = "ian"
print("o nome dele é",nome)

#concatenação
nome = "ian"
sobrenome = "leandro"
print ("seu nome completo é " + nome + " " + sobrenome)

#exercicios de variaveis 
#1 declare uma variavel chamda "idade" e atribua o valor de 25 a ela.
idade = 25
#2 declare uma variavel chamada "nome" e atribua o valor joao a ela.
nome = "joao"
#3 declare uma variavel chamada "saldo" e atribua o valor 100.50  a ela.
saldo = 100.50
#4 crie uma variavel chamada "soma" e atribua a ela a soma das variaveis "idade" e "saldo".
soma = idade + saldo
#5 imprima na tela o valor da variavel "soma"
print("o valor da soma é ", soma)

#exercicios de variaveis em python
#1 crie uma variavel chamada "nota1" e atribua o valor 7.5 a ela.
nota1 = 7.5
print(nota1)
#2 crie uma variavel chamada "nota2" e atribua o valor 8.3 a ela.
nota2 = 8.3
print(nota2)
#3 crie uma variavel chamada "nota3" e atribua o valor 6.9 a ela.
nota3 = 6.9
print(nota3)
#4 caucule a media das tres notas e atribua o resultado a variavel chamada "media"
media = (nota1 + nota2 + nota3) / 3
#5 imprima na tela o valor da variavel "media" formatado com duas casas decimais.
print("a media das notas são:", format(media, ".2f"))

