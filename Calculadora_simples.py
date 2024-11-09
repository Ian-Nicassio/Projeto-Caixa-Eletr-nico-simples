#Incinia loop para manter o programa rodando até o usuário decidir sair
while True:
    
    #Mostra o menu de operações
    print("\nCalculadora Simples:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    
    #Receber a escolha do usuário
    escolha = input("Escolha uma operação: ")
    
    #Condição para sair do programa
    if escolha == "5":
        
        print("Até mais!")
        
        break
        
    #Receber os dois números para a operação
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Condição para Adição
    if escolha == "1":
        
        resultado = num1 + num2
        print("Resultado:", resultado)
        
    # Condição para subtração
    elif escolha == "2":
        
        resultado = num1 - num2
        print("Resultado:", resultado)
        
    # Condição para multiplicação
    elif escolha == "3":
        
        resultado = num1 * num2
        print("Resultado:", resultado)
        
    # Condição para divisão
    elif escolha == "4":
        
        #Verificar se o divisor é zero para evitar erro de divisão por zero
        if num2 != 0:
                        
            resultado = num1 / num2
            print("Resultado:", resultado)
            
        else:
            
            #Mensagem de erro para divisão por zero
            print("Erro: Divisão por zero.")