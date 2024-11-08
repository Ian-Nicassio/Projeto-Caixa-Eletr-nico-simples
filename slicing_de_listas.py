"""
Slicing de listas 
    como acessar subconjuntos de listas: minha_lista[1:3]
    omissão de indices iniciais ou finais: minha_lista[:2], minhalista[2:]
    slicing com passos: minha_lista[::2]

o "slicing" (fatiamento) é uma maneira poderosa de acessar subconjuntos
de listas.
"""

#1. como acessar subconjuntos de listas: minha_lista[1:3]

minha_lista = [0,1,2,3,4,5,6,7,8,9]
#especifou o indice de inicio e fim, com o ":"
subconjunto = minha_lista[1:4]
print(subconjunto) # [1,2,3]


#2. omissão de indices iniciais ou finais: minha_lista[:2], minhalista[2:]

#pega todos elementos ate o indice 2
primeiros_elementos = minha_lista [:2]
print(primeiros_elementos) #saida [0, 1]

#pega todos elemnetos a partir do indice 2
ultimos_elementos = minha_lista [2:]
print(ultimos_elementos) #saida [2, 3, 4, 5, 6, 7, 8, 9]

#3. slicing com passos: minha_lista[::2]

#pega todos elemnetos dando um passe de 2 (pegando alternadamente)
elementos_alternados = minha_lista [::2]
print(elementos_alternados) #saida [0, 2, 4, 6, 8]

#combinamos isso com indices iniciais e finais
subconjunto_alternado = minha_lista [2:8:2]
print(subconjunto_alternado) #saida [2, 4, 6]



#ex slicing de listas 

# 1 crie uma lista chamada cores como os seguintes elementos:
#"vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom", "cinza"

cores = ["vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom", "cinza"]
print(cores)

#2 acesse imprima as cores "verdes" e "azul" ultilizando slicing

subconjuntos = cores [1:3]
print(subconjuntos)

#3 imprima as duas primeiras cores da lista ultilizando slicing

subconjuntos2 = cores [0:2]
print(subconjuntos2)

#4. imprima todas as cores a partir do amarelo usando slicing

subconjuntos3 = cores[3:]
print(subconjuntos3)

#5. imprima todas as cores em posições impares na lista 
#(ou seja "vermelho", "azul", "laranja", "marrom") usando slicing

subconjuntos4 = cores [::2]
print(subconjuntos4)

#6. inverta a ordem das cores na lista usando slicing e imprima o resultado

inverso = cores[::-1]
print(inverso)