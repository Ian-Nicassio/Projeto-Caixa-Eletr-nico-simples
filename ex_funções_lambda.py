'''
ex para pegar todos os numeros impares da lista 
numeros = [2,5,8,10,12,15,18,20,23,25] e eleve ao quadrado os numeros
impares

'''

numeros = [2,5,8,10,12,15,18,20,23,25]

numeros_impares = list(filter(lambda x: x % 2 !=0, numeros ))

numeros_ao_quadrados = list(map(lambda x: x**2, numeros_impares))
print(numeros_impares)
print(numeros_ao_quadrados)