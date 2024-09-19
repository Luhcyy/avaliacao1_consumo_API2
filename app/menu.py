from search import searchByName, searchById
from display import displaySearchData, displayIdData
from clear import clearScreen

def displayMenu ():
    
    while True:
        print('Boas-vindas ao catalogo de animes!\n')
        print ('Escolha uma opção para começar: \n')
        print('1 - buscar anime por nome\n')
        print('2 - buscar anime por ID\n')
        print('3 - Sair\n')
    
        op = input("Digite sua Escolha: \n")
        
        clearScreen()
           
        if op == '1':
            searchTerm = input("Digite o nome do anime para buscar: ")
            data = searchByName(searchTerm)
            displaySearchData(data) 
            input("Pressione Enter para voltar ao menu...\n")
            clearScreen()
        elif op == '2':
            try:
                id = int(input("Digite o ID do Anime que deseja: \n"))
                clearScreen()
                data = searchById(id)
                displayIdData(data)
                input("Pressione Enter para voltar ao menu...\n")
                clearScreen()
            except  ValueError:
                clearScreen()
                print("ID inválido. Por favor, insira um número válido.")
                input("Pressione Enter para voltar ao menu...\n")
                clearScreen()
        elif op == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 3.")
        
    
