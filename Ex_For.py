#ex tabuada

n = int(input("Digite um numero inteiro positivo para exibir a sua tabela: "))

for i in range (1,11):

    resultado = n * i
    print(f"{n} x {i} = {resultado}")
print("Fim da tabela de multiplicação.")

n = int(input("Digite um numero inteiro positivo: "))

soma_quadrados = 0

for i in range(1,n+1):
    quadrado = i**2
    print(f"quadrado de {i}: {quadrado}")
    soma_quadrados += quadrado

print(f"A sima dos quadrados dos numeros de 1 ate {n} é: {soma_quadrados} ")



