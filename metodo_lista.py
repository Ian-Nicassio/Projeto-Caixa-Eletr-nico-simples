'''
metodos de listas 
    sort(): ordena a lista em in-place
    reverse(): inverte as ordem dos elementos in-place
    count(): conta o numero de ocorrencias de um elemento 
    index(): retorna o indice da primeira ocorrencia de um elemento 
'''

#metodos de listas

numeros = [23,1,45,6,12]
frutas = ["banana", "maça", "banana", "cereja", "maça", "damasco"]

#1. sort(): ordena a lista em in-place:

#ordena os itens da lista em ordem crescente por padrão 
#para numero é ordem numerica e para strings por ordem alfabetica 
numeros.sort()
frutas.sort()
print(numeros) # saida [1, 6, 12, 23, 45]

print() #serve so para a qeubra de linha

print(frutas) #['banana', 'banana', 'cereja', 'damasco', 'maça', 'maça']

print()#serve so para a qeubra de linha

#do maior numero para o maior numero, usando o "sort" e o "reverse"
numeros.sort(reverse=True)
print(numeros) #saida [45, 23, 12, 6, 1]


#2. reverse(): inverte as ordem dos elementos in-place.

print("\n-----------\n")
#inverte a ordem 
numeros.reverse()
print(numeros)

#inverteu de "A" a "Z" para "Z" a "A"
frutas.reverse()
print(frutas)


#3. count(): conta o numero de ocorrencias de um elemento.

#conta quantas vezes aquele elemneto apareceu na lista
#no caspo a banana apareceu duas vezes na lista frutas
ocorrencias_banana = frutas.count("banana") 
print(ocorrencias_banana) #saida 2

#conta quantas vezes aquele elemneto apareceu na lista
#no caspo o numero 6 apareceu uma veze na lista frutas
ocorrencias_numero_6 = numeros.count(6)
print(ocorrencias_numero_6) #saida 1

#4.index(): retorna o indice da primeira ocorrencia de um elemento.

#retorna o indice da primeira ocorrencia do elemento da lista
#no caso a banana estava no indice 4
indice_banana = frutas.index("banana")
print(indice_banana) #saida 4

#retorna o indice da primeira ocorrencia do elemento da lista
#no caso o 23 estava no indice 3
indice_23 = numeros.index(23)
print(indice_23) #saida 3




#exercicio: metodos de lista

#instruções

    #1 crie uma lista chamada numeros contendo os valores:
    #23,11,89,34,11,56,78,90,23,45

numeros = [23,11,89,34,11,56,78,90,23,45]
print(numeros)

    #2 ordende a lista em ordem crescente usando o metodo sort()
    #e imprima o resultado

numeros.sort()
print(numeros)

    #3 use o metodo reverse() para inverter a ordem dos elementos 
    #da lista e imprima o resultado.

numeros.reverse()
print(numeros)

    #4 conte quantas vezes o numero 11 aparece na lista usando o 
    #metodo count() e imprima o resultado

ocorrencias_11 = numeros.count(11)
print(ocorrencias_11)

    #5 encontre o indice da primeira ocorencia do numero 78 
    #usando o metodo index() e imprima o resultado

indice_78 = numeros.index(78)
print(indice_78)

    #6 tente encontrar o indice do numero que nao esta na lista 
    #(por exemplo 100) e capture a exeção usando um bloco 
    #try-except para exibir uma mensagem amigavel


try:
    indice_100 = numeros.index(78)
    print(f"enconramos o numero na posição: {indice_100}")
except ValueError:
    print("erro nao existe o indice desse numero nessa lista")