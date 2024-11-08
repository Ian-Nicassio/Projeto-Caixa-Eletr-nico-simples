#Exercicio: calculadora simples com funções 

# Função que adiciona dois números
def adicionar(a, b):
    return a + b 

# Função que subtrai o segundo número do primeiro
def subtrair(a, b):
    return a - b 

# Função que multiplica dois números
def multiplicar(a, b):
    return a * b 

# Função que divide o primeiro número pelo segundo
def dividir(a, b):
    return a / b 

# Solicita ao usuário que insira o primeiro número e o converte para float
num1 = float(input("Digite o primeiro numero: "))

# Solicita ao usuário que insira o segundo número e o converte para float
num2 = float(input("Digite o segundo numero: "))

# Solicita ao usuário que escolha a operação desejada
operacao = input("Escolha uma operação (adicionar, subtrair, multiplicar e dividir): ")

# Verifica qual operação o usuário escolheu e chama a função correspondente
if operacao == "adicionar": 
    resultado = adicionar(num1, num2)  # Chama a função de adição

elif operacao == "subtrair": 
    resultado = subtrair(num1, num2)  # Chama a função de subtração

elif operacao == "multiplicar": 
    resultado = multiplicar(num1, num2)  # Chama a função de multiplicação

elif operacao == "dividir": 
    resultado = dividir(num1, num2)  # Chama a função de divisão

# Se o usuário digitar uma operação inválida, exibe uma mensagem de erro
else:  
    print("Operação invalida")

# Exibe o resultado da operação escolhida pelo usuário
print("Resultado: ", resultado)


# Função que cria outras funções com base na operação escolhida
def fabrica_de_funcoes(operacao):

    # Função interna para soma de vários números
    def soma(*args):
        return sum(args)  # Utiliza a função sum para somar todos os argumentos
    
    # Função interna para subtração de vários números
    def subtracao(*args):
        resultado = args[0]  # Inicia o resultado com o primeiro número

        # Subtrai os números subsequentes
        for num in args[1:]:
            resultado -= num

        return resultado
    
    # Função interna para multiplicação de vários números
    def multiplicacao(*args):
        resultado = 1  # Inicia o resultado com 1 (identidade da multiplicação)

        # Multiplica todos os números fornecidos
        for num in args:
            resultado *= num

        return resultado
    
    # Função interna para divisão de vários números
    def divisao(*args):
        resultado = args[0]  # Inicia o resultado com o primeiro número

        # Divide os números subsequentes, com verificação de divisão por zero
        for num in args[1:]:
            if num == 0:
                raise ValueError("Divisão por zero não é permitida")
            
            resultado /= num  # Realiza a divisão

        return resultado
    
    # Verifica qual operação foi solicitada e retorna a função correspondente
    if operacao == "soma":
        return soma
    
    elif operacao == "subtracao":
        return subtracao
    
    elif operacao == "multiplicacao":
        return multiplicacao
    
    elif operacao == "divisao":
        return divisao
    
    else:
        # Se a operação não for suportada, retorna uma função que avisa sobre isso
        def operacao_nao_suportada(*args):
            return "Operação não suportada"
        
        return operacao_nao_suportada
    
# Cria a função para soma
adicionar = fabrica_de_funcoes("soma")
print(adicionar(5, 3, 2, 9, 4, 7))  # Esperado: 30

# Cria a função para subtração
subtrair = fabrica_de_funcoes("subtracao")
print(subtrair(5, 3, 1))  # Esperado: 1

# Cria a função para multiplicação
multiplicar = fabrica_de_funcoes("multiplicacao")
print(multiplicar(5, 3, 3))  # Esperado: 45

# Cria a função para divisão
dividir = fabrica_de_funcoes("divisao")
print(dividir(10, 2, 1))  # Esperado: 5

# Testa uma operação inválida
operacao_invalida = fabrica_de_funcoes("modulo")
print(operacao_invalida(5, 3))  # Esperado: "Operação não suportada"

