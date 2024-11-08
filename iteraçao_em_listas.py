"""
iteração em listas
    usando o loop for.
    usando enumerate() para obter indice e valor ao iterar
"""



#exemplos praticos 

frutas = ["maça", "banana", "cereja", "damasco", "figo"]

for fruta in  frutas:

    print(fruta)

#função enumerate() retorna o tanto de indice quanto o valor ao iterar
#sobre uma lista
for indice, fruta in enumerate(frutas):

    print(f"fruta no indice {indice} e {fruta}")



#Ex: iteração em listas 

#instruções:

#dada a lista nomes = ["alice", "bruno", "clara", "daniel", "eduarda"]
#use em loop for para imprimir cada nome na lista.

nomes = ["alice", "bruno", "clara", "daniel", "eduarda"]
for nome in nomes:

    print(nome)

#ultilizando a mesma lista de nomes, imprima o  nome juntamente com a sua 
#posição, para isso use o enumerate():

for indice, nome in enumerate(nomes):
    print(f"o nome no indice {indice} e {nome}")

#dada a lista notas = [85,90,78,92,88], use a função enumerate() para
#imprimir o nome do aluno da lista nomes e a sua respectiva nota.
notas = [85,90,78,92,88]

for indice, nome in enumerate(nomes):
    print(f"o nome: {nome}, obteve nota: {notas[indice]}")
