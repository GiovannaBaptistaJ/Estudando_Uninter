#CADASTRAR JOGOS

def start():
    print('CADASTRAR NOVO JOGO - 1')
    print('LISTAR JOGOS E SEUS CONSOLES - 2')
    print ('SAIR - 3')
    question = input('O que deseja fazer?')
    
    if question == '1': #CADASTRO DE NOVO ITEM
            nome = input('Escreva o nome do jogo que deseja cadastrar:')
            videogame = input('Qual videogame ele pertence?') 
            print(f'{cadastrar(nome, videogame)} ')
            start()

    elif question == '2': #LISTAGEM DE TUDO CADASTRADO
            listagem()
            start()
        
    elif question == '3': #ENCERRANDO O PROGRAMA
            print('Programa finalizado.')
        
    else:
            print('Erro! Digite um número entre 1, 2 ou 3!')
            start()

def cadastrar(palavra, console):
    x = palavra
    y = console

    arquivo = open('recursos/games.txt', 'a' )
    arquivo.write(x)
    arquivo.write(' - ')
    arquivo.write(y)
    arquivo.write(' \n')
    arquivo.close()

    return x, y

def listagem():
    arquivo = open('recursos/games.txt', 'r' )
    print(arquivo.read())
    arquivo.close()

start()

