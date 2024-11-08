#For é um laço de repetição
#for - para
#função range para imprimir os numeros inteiros de 1 a 10


for i in range (1,11):

    print(i)

# for - ultilizando com numeros

for i in range(10,0, -1):

    print(i)

# de 2 ate 12 com passo de 2
for i in range(2,12, 2):

    print(i)


soma = 0
for i in range (1,11,2):
    print(f"Numero impar atual: {i}")

    soma += i
print(f"\nA soma dos numeros impares de 1 a 10 é: {soma}")


resultado = 1
for numero in range(1,6):
   
    resultado *= numero
    print(f"multiplicando por {numero}, e o resultado parcial é: {resultado}")
print(f"o resultado final da multiplicação de 1 a 5 é: {resultado}")

soma = 0
n = int(input("digite um numero: "))
for i in range(1,n + 1):
    if i %2 == 0:
        print(f"numero: {i} + {soma} = {i + soma}")
        soma += i
print(f"a soma dos numeros pares de 1 ate {n} é {soma} ")