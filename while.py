#while ... enquanto
# lopping de repetição

numero = 1 
#continua o loop enquanto for menor que 5
while numero < 5:
    print(numero)
    #numero = numero + 1
    numero += 1

contador = 10
#continua o loop enquanto for maior que 10
while contador >= 1:
    print(contador)
    #decrementa
    #numero = numero - 1
    contador -= 1


contador = 10
#continua o loop enquanto for maior que 10
while contador >= 1:
    print(contador)
    #decrementa de 2 em 2 
    #numero = numero - 2
    contador -= 2


contador = 0
while contador < 10:
    print("numero: ", contador)
    contador += 1
else:
    print("numeros impressos com sucesso")
    

numero = 1
while numero < 100:
    print(numero)
  
    if numero == 5:
        break
    numero +=1
    

linha = 0
while linha < 3:
    coluna = 0
    while coluna < 3:
        print("linha:", linha, "- coluna:", coluna)
        coluna+= 1
    linha += 1
    
numero_inicial = 1
numero_final = int (input("digite um numero maior que 1: "))

while  numero_inicial <=  numero_final:
    print(numero_inicial)
    numero_inicial += 1
    
#pegar numeros pares entre 1 e o numero fornecido
numero = 1
max = int(input("digite um inteiro maior que 1:"))
print("numeros pares entre 1 e", max, ":")
while numero <= max:
    if numero % 2 == 0:
        print(numero, end=(" "))
    numero += 1

#ex crie um algoritimo que solicite ao usuario uma senha, e só sai do 
#looping do while quando for digitado a senha corretamente 

# Definindo a senha correta
senha_correta = "12345"

# Inicializando a variável para armazenar a senha do usuário
senha_usuario = input("digite sua senha: ")

# Loop que continua até que a senha correta seja digitada
while senha_usuario != senha_correta:
    print("senha incorreta, tente novamente")

    #solicita o usuario que coloque a senha correta
    senha_usuario = input("digite sua senha: ")
print("senha correta")

while True:
    usuario = input("digite 'sair' para encerrar: ")
    if usuario == 'sair':
        break

# Importa a biblioteca random para gerar números aleatórios
import random  
# Gera um número secreto aleatório entre 1 e 100
numero_secreto = random.randint(1, 100) 
# Inicializa o contador de tentativas como zero
tentativas = 0  
# Imprime o número secreto
print(numero_secreto)  
 # Inicia um loop infinito que só vai parar quando o usuário acertar o número
while True: 
    # Solicita ao usuário um palpite e converte para inteiro
    palpite = int(input("digite seu palpite: "))  
    # Incrementa o contador de tentativas
    tentativas += 1  
    # Verifica se o palpite do usuário é menor que o número secreto
    if palpite < numero_secreto:  
        # Informa que o número secreto é maior
        print("o numero secreto é maior, tente novamente")  
    # Verifica se o palpite do usuário é maior que o número secreto
    elif palpite > numero_secreto: 
        # Informa que o número secreto é menor
        print("o numero secreto é menor, tente novamente")  
    # Caso contrário, o usuário acertou o número secreto
    else:  
        # Informa que o usuário acertou e o número de tentativas
        print(f"parabens voce acertou o numero secreto {numero_secreto} em {tentativas} tentativas")  
        # Encerra o loop porque o usuário acertou
        break  


#ex crie um algoritimo que leia n numeros inteiros digitados 
#pelo usuario e so pare quando digitar 0
#no final imprima na tela a soma de todos os numeros digitados 

soma_numero_digitado = 0

numero = int(input("digite um numero ou 0 para sair: "))

while numero != 0:
    soma_numero_digitado += numero

    numero = int(input("digite um numero ou 0 para sair: "))
print("total: ", soma_numero_digitado)

# ex crie um algoritimo que leia numeros inteiros positivos digitados
# pelo usuario ate que o usuario digite um numero menor que 0
# no final imprima o maior numero digitado

    

#ex 4
maior_numero = - 1
numero_digitado = int(input("digite um numero inteiro e maior que 0: "))

while numero_digitado >= 0:
    if numero_digitado > maior_numero:
    
        maior_numero = numero_digitado
    numero_digitado = int(input("digite um numero inteiro e maior que 0: "))
print("maior numero: ", maior_numero)