#introdução listas
#defininindo uma lista de notas de um aluno
notas_aluno = [85,90,78,32,88]
print(notas_aluno)

#type classifica o argumento de cada lista
numero = 5
print(type(numero)) #saida <class 'int'>

lista_de_mumeros = [5,10,15]
print(type(lista_de_mumeros)) #saida <class 'list'>

mensagem = "ola"
print(type(mensagem)) #saida <class 'str'>

lista_de_strings = ["ola", "mundo"]
print(type(lista_de_strings)) #saida <class 'list'>

lista = [1,2,3]

lista[0] = 100 #isso é valido
lista[1] = 50 #isso é valido
print(lista)

tupla = (1,2,3)
#tupla[0] = 100 #isso vai gerar um erro, pois tupla são imutaveis
print(tupla)



#criando lista

#criando lista de numeros
numeros = [10,20,30,40]
print(numeros)
#criando lista de str
frutas  = ["maça", "banana", "cereja"]
print(frutas)
#criando lista mista
mista = [10, "ola", 2.5, ["a", "b", True]]
print(mista)
#acessando elementos da lista, começa com o indice 0
frutas  = ["maça", "banana", "cereja", "damasco"]
print(frutas[0])
print(frutas[1])
print(frutas[2])

#pega sempre o ultimo elemento da lista
frutas  = ["maça", "banana", "cereja", "damasco"]
print(frutas[-1])
#pega o penultimo elemento
print(frutas[-2])

#ex criando lista

frutas  = ["maça", "banana", "cereja", "damasco", "figo"]
print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-2])


