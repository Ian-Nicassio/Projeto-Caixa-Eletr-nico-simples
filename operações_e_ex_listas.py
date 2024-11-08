'''
operações basicas com listas
    adicionar elementos: append(), insert()
    remover elementos: remove(), pop()
    concatenar listas; +, extend()
    repetir listas: *
    verificar se um item esta na lista: in
'''


#1.adicionar elementos: append(), insert()

#append()

#criei a lista sem a cereja
frutas =["maça", "banana"]
#append adiociona o item na lista 
frutas.append("cereja")
print (frutas)

#insert()

#criei a lista sem o abacate
frutas =["maça", "banana", "cereja"]
#insere um item numa posição especifica, no caso ai na primeira
frutas.insert(1, "abacate")
print (frutas)

#2.remover elementos: remove(), pop()

#remove()

#criei a lista com a banana e removi
frutas =["maça", "banana", "cereja"]
#remove o item da lista prlo nome do elemento selecionado, no caso a banana
frutas.remove("banana")
print(frutas)

#pop()
#criei a lista com a maça e removi
frutas =["maça", "banana", "cereja"]
#remove o item da lista pelo indice selecionado, no caso a maça
frutas.pop(0)
print(frutas)

#3. concatenar listas; +, extend()

#+ - une duas listas 

lista1 = [1,2,3]
lista2 = [4,5,6]
#o + juntou as duas listas atraves de uma variavel "uniao"
uniao = lista1 + lista2
#imprimi na tela a variavel que juntou as listas
print(uniao)

#extend()

lista1 = [1,2,3]
lista2 = [4,5,6]
#junta a lista que esta imprimida no print 
lista1.extend(lista2)
print(lista1)# saida [1, 2, 3, 4, 5, 6]

#4. repetir listas: *

# * 

# o * repete a lista quantas vezes for selecionado o nunero no "*"
repeticao = ["a", "b"] * 4
print(repeticao)

#5.verificar se um item esta na lista: in

#in

frutas =["maça", "banana", "cereja"]
#o "in" verifica se aquele item descrito no print esta na lista como "true" e "false"
print("banana" in frutas)
#uva nao esta na lista entao é "falso"
print("uva" in frutas)



#ex criar uma lista chamada animais e modifique a usando as operações de lista

#1 começe com uma lista vazia 

animais = []
print(animais)
#2 adicione os seguintes animais a lista usando o append():


animais.append("cachorro")
animais.append("passaro")
animais.append("gato")
print(animais)

#3 insira peixe na segunda posição da lista usando o insert()

animais.insert(1, "peixe")
print(animais)

#4 remova gato da lista usando remove():

animais.remove("gato")
print(animais)

#5 remova o ultimo elemento da lista com o pop e armazene em uma 
#variavel chamada animal_removido:
 
animal_removido = animais.pop() #vazio remove o ultimo item
print(animais)
print(animal_removido)

#6 crie uma segunda lista chamada novos_animais com os valores 
#"tartarugas" e "hamster"

novos_animais = ["tartaruga", "hamster"]
print(novos_animais)

#7 concatene as duas listas (animais e novos_animais)
#usando o operador "+" e armaze na variavel "todos_animais"

todos_animais = animais + novos_animais
print(todos_animais)

#8 duplique os elementos da lista todos_animais usando o operardor
# "*" e aramazene o resultado em animais_duplicados:
animais_duplicados = todos_animais * 2
print(animais_duplicados)

#9 verifique se "cachorro" esta na lista usando o metodo "in" e imprima
if "cachorro" in todos_animais:
    print("cachorro esta na lista")
else:
    print("cachorro nao esta na lista")