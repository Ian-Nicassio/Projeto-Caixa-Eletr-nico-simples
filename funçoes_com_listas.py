"""
Ultilidades e funções com listas 
    len(): retorna o numero de elemnetos na lista
    max(): retorna o maior valor 
    min(): retorna o menor valor
    sum(): retorna a soma dos elementos
"""


#exemplos praticos

#1. len(): retorna o numero de elemnetos na lista
numeros = [6,3,8,15,2,7,14]

tamanho = len(numeros)
print(f" o numero de elementos na lista é: {tamanho}")

#2. max(): retorna o maior valor 

maior_valor = max(numeros)
print(f" o maior valor na lista é: {maior_valor}")

#3. min(): retorna o menor valor

menor_valor = min(numeros)
print(f" o menor valor na lista é: {menor_valor}")

#4. sum(): retorna a soma dos elementos

soma_total = sum(numeros)
print(f" a soma dos elementos na lista é: {soma_total}")



# Ex pratico 

# compreender e aplicar funções uteis que interagem com listas python

#instruções

#dada a lista valores = [23,45,67,89,12,56,78,90,34,56], determine
#e imprima o numero de elementos na lista usando a função len():

valores = [23,45,67,89,12,56,78,90,34,56]
elementos = len(valores)
print(elementos)

#ainda ultilizando a lista de valores, encontre e imprima o maior e menor
#valor presente na lista usando a função max() e min():

maior_numero = max(valores)
print (maior_numero)

menor_numero = min(valores)
print (menor_numero)

#calcule e imprima a soma de todos os elementos na lista valopres
#usando a função sum():

soma_total1 = sum(valores)
print(soma_total1)

#crie uma lista pesos com os seguintes valores: 58.5, 63.2, 71.3, 69.4, 68.2
#calcule e imprima a média dos pesos usando as funções sum() e len():

pesos = [58.5, 63.2, 71.3, 69.4, 68.2]
media_pesos = sum(pesos) / len(pesos)
print(media_pesos)