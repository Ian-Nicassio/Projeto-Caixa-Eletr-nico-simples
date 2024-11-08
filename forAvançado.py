#For Nested Loops
#loop for dentro de um loop for 

#ex de loops alinhados 
for i in range (1,4):

    for j in range (1,4):

        print(i, "*" ,j, "=", i * j)


quadrados_impares = [x**2 for x in range(10) if x % 2 != 0]
print(quadrados_impares)

#compreensão de lista, pegando somente as consoantes da palavra
texto = "hello world"
consoantes = [char for char in texto if char.lower() not in 'aeiou']
print(consoantes)


numero = int(input("Digite um numero interiro e nao negativo: "))
if numero < 0:
    print("O numero precisa ser positivo.")
    
else:
    fatorial = 1

    for i in range (1, numero +1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial}")


# for criando um retangulo 

largura = 5 
altura  = 3

for i in range (altura):
    for j in range (largura):
        print("*", end= " ")
    print()

# for criando um triangulo 

altura = 5

for i in range(altura):
    espacos = altura - i - 1
    asteriscos = 2 * i +1 
    print(" " * espacos + "*" * asteriscos)