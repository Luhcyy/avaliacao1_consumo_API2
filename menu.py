from search import searchByName, searchById
from display import displaySearchData, displayAll, displayIdData
from clear import clearScreen
import json

def loadData(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def displayMenu ():
    while True:
        print('Boas-vindas ao catalago de animes!\n')
        print ('Escolha uma opção para começar: \n')
        print('1 - exibir todos os animes disponiveis\n')
        print('2 - buscar anime por nome\n')
        print('3 - buscar anime por ID\n')
        print('4 - Sair\n')
    
        op = input("Digite sua Escolha: \n")
        clearScreen()
        if op == '1':
            data = loadData('data.json')
            displayAll(data)
            input("Pressione Enter para voltar ao menu...\n")
            clearScreen()
        elif op == '2':
            searchTerm = input("Digite o nome do anime para buscar: ")
            data = searchByName(searchTerm)
            displaySearchData(data) 
            input("Pressione Enter para voltar ao menu...\n")
            clearScreen()
        elif op == '3':
            try:
                id = int(input("Digite o ID do Anime que deseja: \n"))
                clearScreen()
                data = searchById(id)
                displayIdData(data)
                input("Pressione Enter para voltar ao menu...\n")
                clearScreen()
            except  ValueError:
                print("ID inválido. Por favor, insira um número válido.")
        elif op == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
        
    
