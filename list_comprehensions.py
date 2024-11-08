"""
list comprehensions 
uma maneira concisa de criar listas: [x**2 for x in range(10) if x%2 == 0]

list comprehensions sao uma das caracteristicas mais uteis e elegantes de python
"""

#1. ex basico 

quadrados = [x**2 for x in range (10)]
print(quadrados)

#ex basico tradicional
quadrados = []

for x in range(10):
    quadrados.append(x**2)
print(quadrados)

print()#so para deixar uma linha em branco no terminal

#2.ex tradicional
quadrados_pares= []

for x in range(10):

    if x %2 == 0:
        quadrados_pares.append(x**2)
    
print(quadrados_pares)

#ex list comprehensions
quadrados_pares = [x**2 for x in range (10) if x%2 == 0]
print(quadrados_pares)

print()#so para deixar uma linha em branco no terminal

#ex de combinação com duas listas.
#definindo duas listas 
a = [1,2,3,4]
b = [1,2,3,4]
#iniciando uma lista vazia 
combinacoes = []

#loop atraves de cada elemento em "a"
for x in a: 
    #loop atraves de cada elemento em "b"
    for y in b:
        #verificando se a soma de x e y é igual a 5
        if x + y == 5:
            #se for verdade adiciona a combinação ("x" e "y")
            combinacoes.append((x,y))
#imprimi na tela
print(combinacoes)

#mesmo ex de cima com lista comprehensions
a = [1,2,3,4]
b = [1,2,3,4]
combinacoes = [(x,y) for x in a for y in b if x + y == 5]
print(combinacoes)


#ex list comprehensions 

#instruções:

#1 use uma list comprehensions para criar uma lista dos dez primeiros
#numeros elevados ao cubo e imprima o resultado

cubo = [x**3 for x in range (10)]
print(cubo)

#2 use uma list comprehension para criar uma lista contendo todos os 
#numeros 1 a 20 que sao divisiveis por 3. imprima o resultado

numeros = [x for x in range (1,21) if x %3==0]
print(numeros)

#3 dada a lista palavras frutas = ["maça", "banana", "manga", "uva","abacaxi", "laranja"]
#use uma list comprehension para cirar uma lista que possuem mais 
#de 5 caracteres 

frutas = ["maça", "banana", "manga", "uva","abacaxi", "laranja"]
frutas_5 = [fruta for fruta in frutas  if len(fruta) > 5]
print(frutas_5)

#4 dada a lista notas = [89,92,56,78,45,34,90,99,65,76,80,82]
#use uma list comprehension para obter todas as notas acima de 75
# e imprima o resultado

notas = [89,92,56,78,45,34,90,99,65,76,80,82]
acima_75 = [notas for notas in notas if notas > 75]
print(acima_75)

