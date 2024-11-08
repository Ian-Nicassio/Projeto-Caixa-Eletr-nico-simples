"""
lista aninhadas (listas de listas)
    criando e acessando listas dentro de listas 
    ultilizando loops aninhados para iterar sobre elas.

são basicamnete listas que tem outras listas como seus elementos
"""


#1. criando listas aninhadas  

#vamos considerar que queremos representar uma matriz 3x3:
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#2. acessando listas aninhadas

#para acessar um elemento especifico, precisa espeicificar dois indices:
#da lista externa e da lista interna

# por ex para acessar o numero 5:

#o primeiro indice [1] refere-se a segunda lista (no caso a segunda linha)
#[4,5,6] e o segundo indice [1] refere-se ao segundo elemento que é o 5
#no caso a coluna 2
elemento = matriz[1] [1]
print(elemento)

#3. ultilizando loops aninhados para iterar:

# loop externo: itera sobre cada linha da matriz
for linha in matriz:
    #loop interno: itera sobre cada coluna (ou elemento) dentro da linha atual
    for coluna in linha:

        print(coluna, end=' ')
    #para spara visivelmente as linhas da matriz ao imprimir
    print()


#4. ex pratico:

#queremos calcular a transposta dessa matriz
# a transposta de uma matriz é obtida trocando suas linhas por coluna

#inicializamos uma linha vazia chamada transposta 
transposta = []

#loop atraves de cada coluna da matriz original
for i in range(len(matriz[0])):

    #inicializa uma linha temporaria para construir uma linha matriz transposta
    linha_temporaria = []

    #loop atraves de cada linha da matriz original
    for j in range(len(matriz)):

        #adiciona o elemento da posição j,i (transposta) a linha temporaria
        linha_temporaria.append(matriz[j] [i])

    #adiciona a linha temporaria completa a matriz transposta
    transposta.append(linha_temporaria)

print(transposta)


#Ex listas aninhadas 

#crie uma matriz com os seguintes valores

# 1,2,3
# 4,5,6
# 7,8,9

#represente essa matriz como uma lista de listas 

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#1. acesse e imprima o valor localizado na segunda linha e terceira coluna
#(deve ser o numero 6)

elemento = matriz [1] [2]
print(elemento)

#2. ultilizando loops aninhados, calcule e imprima a soma de todos os 
#valores presentes na lista

soma = 0

for linha in matriz:

    for numero in linha:

        soma += numero

print(soma)

#3. usando loops aninhados imprima a matriz por linha, e cada elemento
#separado por uma tabulação (\t)

for linha in matriz:

    for numero in linha:
        print(numero, end="\t")
    print()

