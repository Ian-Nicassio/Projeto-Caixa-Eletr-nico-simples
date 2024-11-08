"""
Defunição de tuplas:
    tuplas são uma das estruturas de dados embutudas no python. São 
    similares as listas, mas são imutaveis, oque significa que uma vez
    definidas, os elementos não podem ser modificados
"""
"""
exemplo pratico:

suponha que voce esteja criando um sistema para uma biblioteca. Uma 
das tarefas é representar informações sobre um livro. Voce pode escolher 
tuplas para representar essas informações porque, uma vez que um livro
é adicionado ao sistema, certas informações sobre ele, como titulo
, autor, e ISBN, geralmente não mudam.
"""


livro = ("A arte da guerra", "Sun Tzu", "978-8572835080")

#Agora vamos tentar algumas operações:

#acessar informações:

titulo = livro[0] #acessa titulo do lrvro
print(titulo) #saida: A arte da guerra

autor = livro[1] #acessa autor do lrvro
print(autor) #saida: Sun Tzu

ISBN = livro[2] #acessa isbn do lrvro
print(ISBN) #saida: 978-8572835080

print()#deixar espaço em branco

#Criação de tuplas
    #como criar uma tupla usando parenteses: t = (1,2,3)
    #tupla com um unico elemento: t = (1,)
    #tupla sem parenteses: t = 1,2,3
    #uso da função tuple(): tuple([1,2,3])


#1. como criar uma tupla usando parenteses: t = (1,2,3)

destino1 = ("paris", "frança", 5)
print(destino1)

#2. tupla com um unico elemento: t = (1,)

destino_indefinido = ("Kyoto",)
print(destino_indefinido)

#3. tupla sem parenteses: t = 1,2,3

destino2 = "Roma", "Italia", 4
print(destino2)

#4. uso da função tuple(): tuple([1,2,3])

lista_deestino_EUA = ["nova york", "EUA", 7]
destino3 = tuple(lista_deestino_EUA)
print(destino3)



#Ex tuplas
#criar uma tupla usando parenteses de livro:

livro1 = ("Orgulho e Preconceito", "Jane Austen", 1813)
print(livro1)

#tupla com um unico elemento: so coloca o titulo do livro

livro_indefinido = ("O pequeno principe",)
print(livro_indefinido)

#tupla sem parenteses: 

livro2 = 1984, "George Orwell", 1949
print(livro2)

#uso da função tuple:

novo_livro = ["O senhor dos Aneis", "J.R.R. Tolkien", 1954]
livro3 = tuple(novo_livro)
print(livro3)