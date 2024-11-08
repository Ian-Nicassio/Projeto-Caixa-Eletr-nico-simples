"""
Litas e strings
    Coversão de strings para listas: list(), split().
    Coversão de listas para strings: join().
"""


#Exemplo Pratico

#1. Coversão de strings para listas: list(), split().

#a) usando list():


#ao usae a função list() em uma string, cada caractere da string 
#sera um elemneto da lista resultante
s = "ola"
lista_s = list(s)
print(lista_s) #saida ['o', 'l', 'a']

#B) split():

#a função split() é usada para dividir uma string em uma lista com
#base em um delimitador especificado> Se nenhum delimitador for 
#especificado, ela dividira a strings nos espaços em brancos 
frase = "python é divertido"
palavras =  frase.split()
print(palavras) #saida ['python', 'é', 'divertido']

#colocamos um delimitador especifico "/" para separar os elementos 
data = "16/10/2024"
elementos_data = data.split("/")
print(elementos_data)



#2. Coversão de listas para strings: join().

print() #deixar linha em branco

#A função join() é usada para converter uma lista em uma string. ela une
#os elementos de uma lista em uma unica string com base em um  delimitador
#especificado
lista_palavras = ['python', 'é', 'incrivel']
print(lista_palavras)

frase_juntada = ' '.join(lista_palavras)
print(frase_juntada)

#especificamos o "/" para juntar os elementos da lista 
lista_data = ["12", "12", "2024"]
data_juntada = '/'.join(lista_data)
print(data_juntada)


#Ex: lista e srings 

#instruções:

#dada a string palavra "python", coverta para uma lista de 
#caracteres e imprima a lista resultante. use o metodo list().

palavra = "python"
lista_p = list(palavra)
print(lista_p)

#dada a frase = "aprendendo python é divertido!", divida-a em uma 
#lista de palavras e imprima a lista resultante. ultilize o metodo split()

frase = "aprendendo python é divertido!"
frase_separada = frase.split()
print(frase_separada)

#usando a lista do passo 2, junte as palavras para formar a frase original 
#novamente e imprima-a. usando o metodo join().

lista_de_palavras = ['aprendendo', 'python', 'é', 'divertido!']
frase_junta = ' '.join(lista_de_palavras)
print(frase_junta)

#dada a lista itens = ["maça", "banana", "cereja"], converta em uma 
#string onde cada item é separado por uma virgula e imrpima o resultado

itens = ["maça", "banana", "cereja"]
itens_virgula = ', '.join(itens)
print(itens_virgula)
