 
saldo = 1000.00  # Define o saldo inicial como 1000.00

while True:  # Loop contínuo para manter o programa rodando até o usuário escolher sair
    print("\nCaixa Eletrônico")  # Exibe o título do menu do caixa eletrônico
    print("1 - Verificar Saldo")  # Opção para verificar o saldo
    print("2 - Depositar Dinheiro")  # Opção para depositar dinheiro
    print("3 - Sacar Dinheiro")  # Opção para sacar dinheiro
    print("4 - Sair")  # Opção para sair do programa

    opcao = input("Escolha uma Opção (1-4): ")  # Solicita que o usuário escolha uma opção

    if opcao == "1":  # Verifica se o usuário escolheu a opção de verificar saldo
        print(f"Seu saldo é: R$ {saldo:.2f}")  # Exibe o saldo atual com duas casas decimais

    elif opcao == "2":  # Verifica se o usuário escolheu a opção de depositar dinheiro
        deposito = float(input("Digite o valor do depósito: R$ "))  # Solicita o valor a ser depositado

        if deposito > 0:  # Verifica se o valor do depósito é positivo
            
            saldo += deposito  # Adiciona o valor depositado ao saldo
            print(f"Depósito de: R$ {deposito:.2f} realizado com sucesso")  # Confirmação de depósito

        else:  # Caso o valor do depósito seja inválido (menor ou igual a zero)
            print(f"Valor de depósito inválido")  # Exibe mensagem de erro

    elif opcao == "3":  # Verifica se o usuário escolheu a opção de sacar dinheiro
        saque = float(input("Digite o valor do saque: R$ "))  # Solicita o valor a ser sacado

        if saque > 0 and saque <= saldo:  # Verifica se o valor do saque é positivo e se há saldo suficiente
            saldo -= saque  # Subtrai o valor sacado do saldo
            print(f"Saque de: R$ {saque:.2f} realizado com sucesso")  # Confirmação do saque

        else:  # Caso o valor seja inválido ou não haja saldo suficiente
            print(f"Valor do saque inválido ou saldo insuficiente")  # Exibe mensagem de erro

    elif opcao == "4":  # Verifica se o usuário escolheu a opção de sair
        print("Obrigado por utilizar nosso caixa eletrônico. Até mais!")  # Mensagem de despedida
        break  # Interrompe o loop, encerrando o programa

    else:  # Caso o usuário insira uma opção inválida
        print("Opção inválida. Tente novamente")  # Mensagem de erro para opção inválida
