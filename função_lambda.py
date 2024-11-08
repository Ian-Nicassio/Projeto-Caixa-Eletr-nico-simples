'''
Funções anonimas (lambda)
- definição e uso
- limitações em relação as funções regulares
'''
#exemplo pratico 1: definição e uso

#função regular para dobrar um numero

def dobrar(n):

    return n * 2

print("Função regular: ",dobrar(5)) #saida 10

#função lambda para dobrar um numero

dobrar_com_lambda = lambda n: n * 2

print("função lambda: ",dobrar_com_lambda(5)) #saida 10

#exemplo pratico 2: limitações
#Expressividade
#limitações em relação as funções regulares

def classificar_numero(n):

    if n < 0:
        return "negativo"
    
    elif n == 0:
        return"zero"
    
    else:
        return "positivo"

print(classificar_numero(4)) #positivo

#tentativa de função lambda para classificar numeros (menos clara):

classificar_numero_lambda = lambda n: "negativo" if n < 0  else ("zero" if n == 0 else "positivo")

print(classificar_numero_lambda(-2)) #negativo


#Nomeação anonima

#função lambda com sorted
#ex com sorted
#ordenar as tuplas pela idade
pessoas = [("joao", 35), ("maria", 25), ("ian", 20)]

pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])

print(pessoas_ordenadas)



#função lambda com filter

'''
filtramos uma lista para obter apenas numeros pares
usando a função filter() junto com a função lambda

problema:
dada uma lista de numeros, filtre-a para obter apenas os numeros pares
'''

#lista origial de numeros
numeros = [1,2,3,4,5,6,7,8,9,10]

#usando filter () e lambda para obter so numeros pares
numeros_pares = list(filter(lambda x: x% 2 == 0, numeros))

print(numeros_pares)


#ex de filtro de textos, que começa com a letra A

#lista original de nomes

nomes = ["alice", "boby", "ana", "charles", "alex", "tom"]
#ver qual começa com a letra a pelo indice 0, primeiro argumento da lista
nomes_com_a = list(filter(lambda nome: nome [0] == "a", nomes))

print(nomes_com_a)

#ex com so saidas alice na lista
nomes = ["alice", "boby", "ana", "charles", "alex", "tom", "alice"]

nomes_alice = list(filter(lambda nome: nome  == "alice", nomes))

print(nomes_alice) #saida ['alice', 'alice']


#função com map
#ultilizar map com lambda para elever numeros da lista ao quadrado

numeros = [1,2,3,4,5]
#elevando cada numero ao quadrado com map e lambda
numeros_ao_quadrados = list(map(lambda x: x**2, numeros))

print(numeros_ao_quadrados)


#função lambda com map, para transformar uma lista de palavras
#em uma lista que contem o comprimento de cada palavra

palavras = ["maça", "banana", "arroz", "abacate"]
#pegar os comprimentos de cada palavra
comprimentos = list(map(lambda palavra: len(palavra), palavras))

print(comprimentos)
