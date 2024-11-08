#for com strings 

lista = ["A","B","C","D","E"]
for item in lista:

    print(item)
   
    if item == "C":
        # para a lista no "C"
        break


frutas = ["maça", "banana", "laranja"]
for fruta in frutas:
    print(fruta)


numero  = int(input("Digite um numero: "))

for i in range(1,numero+1):
    print(i)


numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    if numero % 2 == 0:
        print(numero, "é par")
    else:
        print(numero,"é impar")

#sepera oque precisa comprar
lista_compra = ["maça", "banana", "cenoura", "leite"]
for item in lista_compra:
    print("Eu preciso comprar",item)

#decrecenta as estrelas
for i in range(5,0, - 1):
    print('*'*i)
     
#pegar as palavras com mais de 4 letras
lista_palavras = ["casa", "carro", "sol", "arvore"]   
for item in lista_palavras:
    if len (item) > 4:
        print(item)
  
    
        