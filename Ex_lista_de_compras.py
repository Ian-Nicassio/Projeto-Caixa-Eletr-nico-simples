lista_compras = []

while True:

    print("\nMenu")
    print("1 - Adicionar itens a lista: ")
    print("2 - remover itens da lista: ")
    print("3 - Exibir lista de compras: ")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        item = input("Qual item deseja adicionar a lista: ")
        lista_compras.append(item)
        print("Item adicionado na lista")
    
    elif opcao == 2:
        if len(lista_compras) == 0:

            print("A lista de compras esta vazia.")
        else:
            item = input("Qual item deseja remover da lista: ")

            if item in lista_compras:

                lista_compras.remove(item)
                print("Item removido da lista")
            else:
                print("O item não esta na lista.")
        
    elif opcao == 3:
        print("Lista de compras")

        for item in lista_compras:

            print("- ", item)

    elif opcao == 4:  
        print("saindo...") 
        break  

    else:  
        print("Opção inválida. Tente novamente")  
    


        
 